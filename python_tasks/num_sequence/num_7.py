"""Num Sequence

Program is calculating a sequence of numbers which square is less or equal
than a given number from user.

"""
import sys


class NumSequence:
    def __init__(self, max_num: int) -> None:
        self.max_num = max_num

    @staticmethod
    def is_validated(max_num) -> bool:
        """Validation of user arguments"""
        if type(max_num) == int and \
                max_num > 0:
            return True
        else:
            return False

    def calculation_sequence(self) -> list:
        sequence_list = list()
        for i in range(1, self.max_num):
            if (i ** 2) <= self.max_num:
                sequence_list.append(i)
        return sequence_list

    def __str__(self):
        return "{}: Sequence to -> {} ".format(
            str(self.calculation_sequence()), self.max_num)


def get_arg():
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("The program hasn't been able to get valid arguments")
    else:
        return int(sys.argv[1])


def main():
    max_num = get_arg()
    if NumSequence.is_validated(max_num):
        num_sequence = NumSequence(max_num)
        print(num_sequence)
    else:
        print("Try again!")


if __name__ == '__main__':
    main()
