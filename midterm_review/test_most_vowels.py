from unittest import TestCase

from midterm_review.most_vowels import most_vowels


class Test(TestCase):
    def test_most_vowels(self):
        string = "bob", "alice", "christopher"
        result = 3
        self.assertEqual(3, most_vowels(string))
