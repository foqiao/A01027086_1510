from unittest import TestCase

from lab_07.exception import heron


class Test(TestCase):
    def test_heron(self):
        with self.assertRaises(ZeroDivisionError):
            heron(0)