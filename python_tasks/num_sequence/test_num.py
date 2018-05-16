import unittest
from python_tasks.num_sequence.num_7 import NumSequence


class TestNum(unittest.TestCase):

    def test_is_validated_negative(self):
        num_negative = NumSequence.is_validated(-5)
        self.assertFalse(num_negative)

    def test_is_validate_positive(self):
        num_positive = NumSequence.is_validated(5)
        self.assertTrue(num_positive)

    def test_calc_num_sequence(self):
        sequence_list = [1, 2, 3, 4, 5]
        num_sequence = NumSequence(25).calculation_sequence()
        self.assertEqual(sequence_list, num_sequence)


if __name__ == '__main__':
    TestNum()
