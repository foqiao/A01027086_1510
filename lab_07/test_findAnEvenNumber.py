from unittest import TestCase

from lab_07.exception import findAnEvenNumber


class Test(TestCase):
    def test_find_an_even_number(self):
        with self.assertRaises(ValueError):
            findAnEvenNumber([1, 3, 5, 7])