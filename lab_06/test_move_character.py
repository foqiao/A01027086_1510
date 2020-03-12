from unittest import TestCase

from lab_06.maze import move_character


class Test(TestCase):
    def test_move_character(self):
        character = {'x': 'str', 'y': 'str'}
        direction = 'str'
        self.assertFalse(character, move_character(character, direction))
        self.assertTrue(direction, move_character(character, direction))