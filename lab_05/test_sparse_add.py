from unittest import TestCase

from lab_05.sparse_vector import sparse_add


class Test(TestCase):
    def test_sparse_add(self):
        vector1 = {'length': 5, 0: 6, 3: 9}
        vector2 = {'length': 5, 0: 8, 3: 3}
        result = {'length': 5, 0: 14, 3: 12}
        self.assertTrue(result, sparse_add(vector1, vector2))