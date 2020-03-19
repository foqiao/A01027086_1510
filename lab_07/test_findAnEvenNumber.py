from unittest import TestCase

from lab_07.exception import findAnEvenNumber


class Test(TestCase):
    def test_find_an_even_number(self):
        self.assertEqual(2, findAnEvenNumber([1, 2, 3]))
