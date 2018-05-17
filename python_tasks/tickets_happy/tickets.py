"""Happy tickets

The program is calculating happy tickets with 2 ways.
One of them sums up the right and left parts of the ticket with an equal amount
another sums up even numbers of the tickets is equal to the sum of odd figures.
Program works only with 2 algorithm(Moskow and Piter algorithm).
After inputting arguments will be shown the number of tickets
counted with one of the ways.

"""
import sys


class Ticket:
    def __init__(self, file_name: str) -> None:
        self.file_name = file_name

    def check_algorithm(self, tickets_list):
        """determination of the calculation method"""
        test_file = open(self.file_name)
        for string in test_file:
            if string.startswith("Moskow"):
                print(self.moscow_count(tickets_list))
            elif string.startswith("Piter"):
                print(self.petersburg_count(tickets_list))
            else:
                print("Algorithm has not been found")
                quit()

    @staticmethod
    def tickets_create() -> list():
        """filling with tickets number in range from
        000000 to 999999"""
        tickets_list = [str(i).rjust(6, '0') for i in range(0, 999999)]
        return tickets_list

    def moscow_count(self, tickets_list):
        happy_tickets_count = 1
        for digit in tickets_list:
            sum_left = int(digit[0]) + int(digit[1]) + int(digit[2])
            sum_right = int(digit[3]) + int(digit[4]) + int(digit[5])
            if sum_left == sum_right:
                happy_tickets_count = happy_tickets_count + 1
        return happy_tickets_count

    def petersburg_count(self, tickets_list):
        happy_tickets_count = 1
        for digit in tickets_list:
            sum_even = int(digit[0]) + int(digit[2]) + int(digit[4])
            sum_odd = int(digit[1]) + int(digit[3]) + int(digit[5])
            if sum_even == sum_odd:
                happy_tickets_count = happy_tickets_count + 1
        return happy_tickets_count


def main():
    try:
        if len(sys.argv) == 2 and open(sys.argv[1], mode='r'):
            ticket = Ticket(sys.argv[1])
            tickets_list = ticket.tickets_create()
            ticket.check_algorithm(tickets_list)
        else:
            print("The program hasn't been able to get valid arguments")
    except FileNotFoundError:
        print("File has not been found. Try again!")


if __name__ == '__main__':
    main()
