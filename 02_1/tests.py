import unittest
from .solve import solve


class TestCase(unittest.TestCase):
    def test_1(self):
        self.assertEqual(solve([1, 0, 0, 0, 99]), [2, 0, 0, 0, 99])

    def test_2(self):
        self.assertEqual(solve([2, 3, 0, 3, 99]), [2, 3, 0, 6, 99])

    def test_3(self):
        self.assertEqual(solve([2, 4, 4, 5, 99, 0]), [2, 4, 4, 5, 99, 9801])

    def test_4(self):
        self.assertEqual(solve([1, 1, 1, 4, 99, 5, 6, 0, 99]), [30, 1, 1, 4, 2, 5, 6, 0, 99])


if __name__ == '__main__':
    unittest.main()
