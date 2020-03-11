from unittest import TestCase

from lab_06.maze import board


class Test(TestCase):
    def test_board(self):
        self.assertEqual(None, board())
