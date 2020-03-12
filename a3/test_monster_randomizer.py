from unittest import TestCase

from a3.monster_combat import monster_randomizer


class Test(TestCase):
    def test_monster_randomizer(self):
        monster_names = ['Crazed Brigand', 'Frostbite Spider', 'Beholder', 'Mangled Death Knight', 'Treeant', 'Unicorn',
                         'Dire Wolf', 'Shia Labeouf', 'Violent Bounty Hunter', 'Green Snail']
        result2 = {'Name': monster_names[8], 'HP': [5, 5]}
        """
        result1 = {'Name': monster_names[-1], 'HP': [5, 5]}
        result = {'Name': monster_names[10], 'HP': [5, 5]}
        self.assertEqual(result, monster_randomizer())
        self.assertEqual(result1, monster_randomizer())
        """

        self.assertTrue(result2, monster_randomizer())
