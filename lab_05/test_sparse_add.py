from unittest import TestCase

from lab_05.sparse_vector import sparse_add

"""
test first function of sparse_vector.py
"""
class Test(TestCase):
    def test_sparse_add(self):
        vector_input1 = {1: 5, 0: 6, 3: 9, 4: 8}
        vector_input2 = {1: 5, 0: 8, 3: 3, 5: 3}
        result = {1: 10, 0: 24, 3: 36}
        self.assertTrue(result, sparse_add(vector_input1, vector_input2))