from unittest import TestCase

from lab_06.maze import make_board


class Test(TestCase):
    def test_make_board(self):
        board_size = {'length': 5, 'width': 5}
        self.assertEqual(board_size, make_board(5, 5))
