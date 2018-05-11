import unittest
from python_tasks.chess_board.chess import Chess


class TestChess(unittest.TestCase):

    def test_is_validated_first(self):
        test_chess = Chess.is_validated(11, 11)
        self.assertTrue(test_chess)

    def test_is_validated_second(self):
        self.assertFalse(Chess.is_validated(-5, 0))


if __name__ == '__main__':
    TestChess()
