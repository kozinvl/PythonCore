"""Printing a Chess Board

Program 'ChessBoard'
If you enter width and height arguments display will show chess
board with preset parameter.

"""
import sys


class Chess:
    def __init__(self, height: int, width: int) -> None:
        self.height = height
        self.width = width

    @staticmethod
    def is_validated(height, width) -> bool:
        """Validation of user arguments"""
        if isinstance(height, int) and isinstance(width, int) \
                and height > 0 and width > 0:
            return True
        else:
            return False

    def draw_chess_board(self):
        for i in range(self.height):
            if i % 2 != 0:
                print(" ", end='')
            for j in range(self.width):
                print("* ", end='')
            print()


def get_arg():
    arguments = []
    if len(sys.argv) != 3 or not sys.argv[1].isdigit() or \
            not sys.argv[2].isdigit():
        print("Please, input valid height and width values")
        quit()
    else:
        arguments.append(int(sys.argv[1]))
        arguments.append(int(sys.argv[2]))
        return arguments


def main():
    user_arg = get_arg()
    height_chess = (user_arg[0])
    width_chess = (user_arg[1])
    if Chess.is_validated(height_chess, width_chess):
        new_chess = Chess(height_chess, width_chess)
        new_chess.draw_chess_board()
    else:
        print("Invalid data has been entered")
        quit()


if __name__ == '__main__':
    main()
