"""Fibonacci sequence

The program is calculating of fibonacci sequence in range from user arguments.
The range is specified by two arguments when the main class is called.
Numbers are separated by space.

"""
import sys


class Fibonacci:
    def __init__(self, start_sequence: int, finish_sequence: int) -> None:
        self.start_sequence = start_sequence
        self.finish_sequence = finish_sequence

    @staticmethod
    def is_validated(start_sequence: int, finish_sequence: int) -> bool:
        """Validation of user arguments"""
        if isinstance(start_sequence, int) and \
                isinstance(finish_sequence, int):
            if start_sequence >= 0 and finish_sequence > 0:
                return True
            else:
                return False
        else:
            return False

    def calculation_sequence(self):
        """Fibonacci sequence calculation and coincidence check"""
        fibonacci_equal = [self.start_sequence, self.finish_sequence]
        digit_start_count = 0
        next_count = 1
        fibonacci_sequence = []
        while digit_start_count <= self.finish_sequence:
            if digit_start_count >= self.start_sequence:
                fibonacci_sequence.append(digit_start_count)
            digit_start_count, next_count = \
                next_count, digit_start_count + next_count
        for digit in fibonacci_equal:
            if digit in fibonacci_sequence:
                print("Your number is the number of the "
                      "Fibonacci sequence ->", digit, end="\n")
        return fibonacci_sequence

    def __str__(self):
        """outputting info about sequence"""
        return "{} Numbers that are containing in the required " \
               "Fibonacci sequence".format(self.calculation_sequence())


def get_arg():
    if len(sys.argv) != 3 or not sys.argv[1].isdigit() \
            or not sys.argv[2].isdigit():
        print("The program hasn't been able to get valid arguments")
        quit()
    else:
        return [int(sys.argv[1]), int(sys.argv[2])]


def main():
    start_sequence = get_arg()[0]
    finish_sequence = get_arg()[1]
    if Fibonacci.is_validated(start_sequence, finish_sequence):
        fibonacci = Fibonacci(start_sequence, finish_sequence)
        print(fibonacci)
    else:
        print("Instance hasn't been created. Enter correct arguments!")


if __name__ == '__main__':
    main()
