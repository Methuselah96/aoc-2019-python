import unittest
from .solve import solve_single


class TestCase(unittest.TestCase):
    def test_14(self):
        self.assertEqual(solve_single(14), 2)

    def test_1969(self):
        self.assertEqual(solve_single(1969), 966)

    def test_100756(self):
        self.assertEqual(solve_single(100756), 50346)


if __name__ == '__main__':
    unittest.main()
