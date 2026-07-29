import unittest

from utils_future.misc.Int import Int


class TestIntHumanize(unittest.TestCase):
    def h(self, value):
        return Int(value).humanize

    # --- small values (no suffix) ---
    def test_zero(self):
        self.assertEqual(self.h(0), "0")

    def test_below_thousand(self):
        self.assertEqual(self.h(999), "999")
        self.assertEqual(self.h(1), "1")

    # --- thousands (K) ---
    def test_1k_single_decimal(self):
        self.assertEqual(self.h(1_234), "1.2K")

    def test_1k_rounds_up(self):
        self.assertEqual(self.h(9_876), "9.9K")

    def test_10k_no_decimal(self):
        self.assertEqual(self.h(12_345), "12K")

    def test_100k_rounds_
    to_tens(self):
        self.assertEqual(self.h(123_456), "120K")

    # --- millions (M) ---
    def test_1m_single_decimal(self):
        self.assertEqual(self.h(1_234_567), "1.2M")

    def test_10m_no_decimal(self):
        self.assertEqual(self.h(12_345_678), "12M")

    def test_100m_rounds_to_tens(self):
        self.assertEqual(self.h(123_456_789), "120M")

    # --- billions (B) ---
    def test_1b(self):
        self.assertEqual(self.h(1_499_000_000), "1.5B")
        self.assertEqual(self.h(1_449_000_000), "1.4B")

    # --- negative values ---
    def test_negative_small(self):
        self.assertEqual(self.h(-999), "-999")

    def test_negative_thousands(self):
        self.assertEqual(self.h(-1_234), "-1.2K")

    def test_negative_millions(self):
        self.assertEqual(self.h(-1_234_567), "-1.2M")


if __name__ == "__main__":
    unittest.main()
