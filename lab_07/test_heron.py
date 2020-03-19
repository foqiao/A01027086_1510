from unittest import TestCase

from lab_07.exception import heron


class Test(TestCase):
    def test_heron(self):
        self.assertTrue(1.41666666666, heron(2))
