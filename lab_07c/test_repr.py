from unittest import TestCase

from lab_07c.country import Country


class TestCountry(TestCase):
    def __str__(self):
        super(TestCountry, self).__str__()
        Canada = Country(self, 37590000, 9985000)
        self.assertEqual(self, Canada.__repr__(self))