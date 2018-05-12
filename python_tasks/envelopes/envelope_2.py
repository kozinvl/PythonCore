"""Envelope analysis

The program takes 2 arguments from different envelopes and returns
whether they can be nested. In order to calculating other envelopes
user has to give positive answer.

"""


class Envelope(object):
    def __init__(self, width: float, height: float) -> None:
        self.width = width
        self.height = height

    @staticmethod
    def is_validated(width, height) -> bool:
        """Validation of user arguments"""
        if not isinstance(width, float) and not isinstance(height, float):
            return False
        elif width <= 0 and height <= 0:
            return False
        else:
            return True

    def nested_or_not(self, second) -> str:
        if (self.width > second.width) and (self.height > second.height):
            return "second envelope can be nested"
        elif (second.width > self.width) and (second.height > self.height):
            return "second envelope can't be nested"
        else:
            return "Envelopes can't be nested"


def select_process():
    user_input = input("Do you want to continue or not? \nInput 'y' or 'yes' ")
    if user_input.lower() in ('y', 'yes'):
        return True
    else:
        return False


def get_arg(side):
    while True:
        try:
            value = float(input("Input " + side + " "))
            if value <= 0:
                raise ValueError
            else:
                return value
        except ValueError:
            print("Program has not been able to get valid argument! Try again")


def main():
    is_continue = True
    while is_continue:
        first_width = get_arg('width')
        first_height = get_arg('height')
        second_width = get_arg('width')
        second_height = get_arg('height')
        if Envelope.is_validated(first_height, first_height) \
                and Envelope.is_validated(second_width, second_height):
            first_envelope = Envelope(first_width, first_height)
            second_envelope = Envelope(second_width, second_height)
            print(first_envelope.nested_or_not(second_envelope))
        else:
            print("Instance hasn't been created. Enter correct arguments!")
        is_continue = select_process()


if __name__ == '__main__':
    main()
