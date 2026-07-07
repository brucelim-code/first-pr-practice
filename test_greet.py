import unittest

from greet import greet


class TestGreet(unittest.TestCase):
    def test_greet_with_name(self):
        self.assertEqual(greet("Bruce"), "Hello, Bruce!")

    def test_greet_with_empty_name(self):
        self.assertEqual(greet(""), "Hello, !")


if __name__ == "__main__":
    unittest.main()
