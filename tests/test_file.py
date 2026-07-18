import unittest

from utils_future import Directory, File


class TestCase(unittest.TestCase):
    def test_read_write(self):
        file = File(Directory.get_temp("utils_future"), "test_file.txt")
        content = "Hello, World!"
        file.write(content)
        read_content = file.read()
        self.assertEqual(content, read_content)
