from unittest import TestCase

from lab_07c.country import Country


class TestCountry(TestCase):
    def __str__(self):
        super(TestCountry, self).__str__()
        Canada = Country("Canada", 37590000, 9985000)
        result = "The population density is " + Canada.population + " and " + Canada.size
        self.assertEqual(result, Canada.__str__(self))