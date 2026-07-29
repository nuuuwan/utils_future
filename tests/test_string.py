import unittest

from utils_future.misc.String import String


class TestCase(unittest.TestCase):
    def test_shorten(self):
        for s, max_len, expected in [
            ("Colombo Central", 100, "Colombo Central"),
            ("Colombo Central", 2, "CC"),
            ("Ja-Ela", 2, "JE"),
            ("Maharagama", 5, "Mhrgm"),
            ("Maharagama", 3, "Mhr"),
        ]:
            with self.subTest(s=s, max_len=max_len):
                self.assertEqual(String(s).shorten(max_len), expected)


if __name__ == "__main__":
    unittest.main()
