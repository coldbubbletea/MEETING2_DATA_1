import unittest
from types import SimpleNamespace
from unittest.mock import patch

from lingua import Language
from skill_languages_gt100 import classify_prose, prose_only


ENGLISH = (
    "Review the project requirements before making changes. "
    "Run the existing tests and explain the results to the user. "
    "Read the documentation carefully and verify that the implementation works correctly. "
)
CHINESE = (
    "\u5728\u4fee\u6539\u4ee3\u7801\u4e4b\u524d\uff0c\u8bf7\u5148\u9605\u8bfb\u9879\u76ee\u6587\u6863\u5e76\u786e\u8ba4\u7528\u6237\u7684\u9700\u6c42\u3002"
    "\u5b8c\u6210\u4fee\u6539\u4ee5\u540e\uff0c\u8fd0\u884c\u73b0\u6709\u6d4b\u8bd5\u5e76\u68c0\u67e5\u5b9e\u73b0\u662f\u5426\u6b63\u786e\u3002"
    "\u5411\u7528\u6237\u8bf4\u660e\u9a8c\u8bc1\u7ed3\u679c\uff0c\u5982\u679c\u51fa\u73b0\u9519\u8bef\u5219\u5148\u6392\u67e5\u539f\u56e0\u3002"
)


class LanguageTests(unittest.TestCase):
    def test_english(self):
        self.assertEqual(classify_prose(ENGLISH)[0], "english")

    def test_chinese_with_technical_names(self):
        self.assertEqual(classify_prose(CHINESE + " Python API GitHub")[0], "chinese")

    def test_technical_names_are_not_english_instructions(self):
        text = CHINESE * 3 + " Path A brainstorm context7 design.md plan-first delivery-gate API GitHub Python"
        self.assertEqual(classify_prose(text)[0], "chinese")

    def test_mixed(self):
        self.assertEqual(classify_prose(ENGLISH + "\n\n" + CHINESE * 2)[0], "mixed")

    def test_other_language(self):
        text = (
            "Antes de modificar el proyecto, revise los requisitos del usuario y lea la documentaci\u00f3n. "
            "Ejecute las pruebas existentes y compruebe que todos los cambios funcionan correctamente. "
        )
        self.assertEqual(classify_prose(text)[0], "other")

    def test_japanese_is_not_chinese(self):
        text = (
            "\u30d7\u30ed\u30b8\u30a7\u30af\u30c8\u3092\u5909\u66f4\u3059\u308b\u524d\u306b\u3001\u5229\u7528\u8005\u306e\u8981\u4ef6\u3092\u78ba\u8a8d\u3057\u3066\u304f\u3060\u3055\u3044\u3002"
            "\u6587\u66f8\u3092\u8aad\u3093\u3067\u304b\u3089\u5b9f\u88c5\u3092\u9032\u3081\u3001\u65e2\u5b58\u306e\u30c6\u30b9\u30c8\u3092\u5b9f\u884c\u3057\u307e\u3059\u3002"
            "\u554f\u984c\u304c\u898b\u3064\u304b\u3063\u305f\u5834\u5408\u306f\u539f\u56e0\u3092\u8abf\u3079\u3001\u7d50\u679c\u3092\u8aac\u660e\u3057\u3066\u304f\u3060\u3055\u3044\u3002"
        )
        self.assertEqual(classify_prose(text)[0], "other")

    def test_mixed_thresholds(self):
        for english, chinese, expected in ((160, 40, "mixed"), (161, 39, "english"), (165, 41, "english")):
            english_text = "the and to " * (english // 8) + "x" * (english % 8)
            boundary = len(english_text)
            text = english_text + "\u4e2d" * chinese
            fake = SimpleNamespace(
                detect_multiple_languages_of=lambda _: [
                    SimpleNamespace(start_index=0, end_index=boundary, language=Language.ENGLISH),
                    SimpleNamespace(start_index=boundary, end_index=len(text), language=Language.CHINESE),
                ],
                detect_language_of=lambda _: Language.ENGLISH,
            )
            classify_prose.cache_clear()
            with patch("skill_languages_gt100.detector", return_value=fake):
                self.assertEqual(classify_prose(text)[0], expected)
        classify_prose.cache_clear()

    def test_short_or_code_only(self):
        for text in ("", "Python API", "```python\nprint('English')\n```"):
            self.assertEqual(classify_prose(prose_only(text))[0], "unknown")

    def test_excludes_metadata_code_urls_and_paths(self):
        text = (
            "---\nname: example\ndescription: metadata\n---\n"
            "```python\nprint('code')\n```\n"
            "~~~sh\nprintf code\n~~~\n"
            "[Read the guide](https://example.com/guide) and use `some_api()`.\n"
            "    indented_code()\n"
            "See src/components/widget.ts and https://example.com.\n"
        )
        prose = prose_only(text)
        self.assertIn("Read the guide", prose)
        for excluded in ("metadata", "print", "printf", "some_api", "indented_code", "https://", "widget.ts"):
            self.assertNotIn(excluded, prose)

    def test_chinese_code_does_not_make_english_prose_mixed(self):
        text = ENGLISH + "\n```text\n" + CHINESE * 5 + "\n```"
        self.assertEqual(classify_prose(prose_only(text))[0], "english")


if __name__ == "__main__":
    unittest.main()
