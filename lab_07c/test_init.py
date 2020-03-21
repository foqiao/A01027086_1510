from unittest import TestCase

from lab_07c.country import Country


class TestCountry(TestCase):
    def __init__(self, name):
        super(TestCountry, self).__init__(name)
        Canada = Country("Canada", 37590000, 9985000)
        self.assertEqual("Canada", Canada.name)