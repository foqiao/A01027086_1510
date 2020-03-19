from unittest import TestCase

from sand_box.exception_fun import convert


class Test(TestCase):
    def test_convert(self):
        self.assertEqual(5, convert(value='5'))
