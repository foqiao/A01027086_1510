from unittest import TestCase

from lab_05.sparse_vector import sparse_dot_product

"""
test second function of sparse_vector.py
"""
class Test(TestCase):
    def test_sparse_dot_product(self):
        vector_input1 = {1: 5, 0: 6, 3: 9, 4: 8}
        vector_input2 = {1: 5, 0: 8, 3: 3, 5: 3}
        result = {'length': 10, 'total': 0}
        self.assertTrue(result, sparse_dot_product(vector_input1, vector_input2))