from unittest import TestCase

from lab_07c.country import Country


class TestCountry(TestCase):
    def test_is_larger(self):
        Canada = Country("Canada", 37590000, 9985000)
        Denmark = Country("Denmark", 5603000, 42933)
        self.assertEqual(True, Canada.is_larger(Denmark))
