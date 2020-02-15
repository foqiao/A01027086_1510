import unittest
from syllable import syllable
from a2.DnD import roll_dice, generate_name, create_character, choose_inventory


class TestCase(unittest.TestCase):
    def test_roll_dice(self):
        self.assertEqual(roll_dice(2, 5), 10)

    def test_generate_name(self):
        self.assertIn("ab", generate_name(syllable))
        self.assertIn("ae", generate_name(syllable))
        self.assertIn("bq", generate_name(syllable))

    def test_create_character(self):
        self.assertEqual('Elf Orc', create_character(1, 2))
        self.assertFalse('Wu Wu', create_character(11, 12))

    def test_choose_inventory(self):
        self.assertIn('Special Curse', choose_inventory())

    def test_combat_round(self):
        self.assertEqual()