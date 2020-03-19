from unittest import TestCase

from sand_box.exception_fun import another_convert


class Test(TestCase):
    def test_another_convert(self):
        self.assertFalse(2, another_convert(-2))
