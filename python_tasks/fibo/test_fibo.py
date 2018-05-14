import unittest
from python_tasks.fibo.fibo_8 import Fibonacci


class TestFibonacci(unittest.TestCase):

    def test_is_validated_negative(self):
        test_fibonacci = Fibonacci.is_validated(5.0, 20.0)
        self.assertFalse(test_fibonacci)

    def test_is_validated_positive(self):
        test_fibonacci = Fibonacci.is_validated(0, 35)
        self.assertTrue(test_fibonacci)

    def test_list_fibonacci(self):
        test_list = [8, 13]
        instance_fibonacci = Fibonacci(6, 15).calculation_sequence()
        self.assertEqual(test_list, instance_fibonacci)


if __name__ == '__main__':
    TestFibonacci()
