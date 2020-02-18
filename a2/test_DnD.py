import unittest
from syllable import syllable
from a2.DnD import roll_dice, generate_name, create_character, choose_inventory, purchased_items


class TestCase(unittest.TestCase):
    def test_roll_dice(self):
        self.assertEqual(roll_dice(2, 5), 10)

    def test_generate_name(self):
        self.assertTrue("ab", generate_name(syllable))
        self.assertTrue("ae", generate_name(syllable))
        self.assertTrue("bq", generate_name(syllable))

    def test_create_character(self):
        self.assertEqual('Elf Orc', create_character(1, 2))
        self.assertFalse('Wu Wu', create_character(11, 12))

    def test_choose_inventory(self):
        self.assertIn('Special Curse', choose_inventory())

    def test_combat_round(self):
        player_roll = 6
        second_player_roll = 6
        monster_roll = 4

        monster = {
            "health": range(100, 0, -1),
            "weapon": None
        }

        picked_second_character = {
            "health": range(100, 0, -1),
            "weapon": purchased_items
        }

        self.assertEqual(player_roll, second_player_roll, monster_roll, monster["health"] - 1)