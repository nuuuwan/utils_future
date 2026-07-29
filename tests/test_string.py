import unittest

from utils_future.misc.String import String


class TestStringShorten(unittest.TestCase):
    def s(self, text, max_len):
        return String(text).shorten(max_len)

    # --- guard conditions ---
    def test_negative_max_len_raises(self):
        with self.assertRaises(ValueError):
            self.s("hello", -1)

    def test_max_len_zero(self):
        self.assertEqual(self.s("hello", 0), "")

    def test_max_len_one(self):
        self.assertEqual(self.s("hello", 1), "h")

    def test_shorter_than_max_len_unchanged(self):
        self.assertEqual(self.s("hi", 10), "hi")

    def test_equal_to_max_len_unchanged(self):
        self.assertEqual(self.s("hello", 5), "hello")

    # --- multi-word ---
    def test_two_words_max_two(self):
        self.assertEqual(self.s("hello world", 2), "helloworld")

    def test_three_words_max_two(self):
        self.assertEqual(self.s("foo bar baz", 2), "foobar")

    def test_hyphenated_treated_as_multi_word(self):
        self.assertEqual(self.s("foo-bar", 2), "foobar")

    # --- single word (consonant abbreviation) ---
    def test_single_word_consonants(self):
        # "Hello" → h + consonants(l, l) → "Hll"
        self.assertEqual(self.s("Hello", 3), "Hll")

    def test_single_word_max_two(self):
        # "Hello" → h + first consonant (l) → "Hl"
        self.assertEqual(self.s("Hello", 2), "Hl")

    def test_single_word_all_vowels(self):
        # "aeiou" → first char + no consonants → "a"
        self.assertEqual(self.s("aeiou", 3), "a")


if __name__ == "__main__":
    unittest.main()
