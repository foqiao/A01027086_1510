from unittest import TestCase

from lab_05.sparse_vector import sparse_dot_product


class Test(TestCase):
    def test_sparse_dot_product(self):
        vector1 = {'length': 5, 0: 6, 3: 9}
        vector2 = {'length': 5, 0: 8, 3: 3}
        result = {'length': 5, 0: 48, 3: 27}
        self.assertTrue(result, sparse_dot_product(vector1, vector2))