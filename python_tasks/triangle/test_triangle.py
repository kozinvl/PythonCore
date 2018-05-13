import unittest
from python_tasks.triangle.triangle_sort import Triangle


class TestTriangle(unittest.TestCase):

    def test_is_validated_negative(self):
        test_tr_negative = Triangle.is_validated(-9, 2, 0)
        self.assertFalse(test_tr_negative)

    def test_is_validated_positive(self):
        test_tr_positive = Triangle.is_validated(6, 7, 8)
        self.assertTrue(test_tr_positive)

    def test_calc_square(self):
        test_tr_square = 21.218
        triangle = Triangle("Vas", 7, 7, 7).calc_square()
        self.assertEqual(test_tr_square, triangle)


if __name__ == '__main__':
    TestTriangle()
