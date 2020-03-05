from unittest import TestCase
from midterm_review.review_questions import apples_vs_boxes, num_of_boxes, num_of_apples, multiple_if_statement, \
    user_age1


class Test(TestCase):

    def test_apples_vs_boxes(self):
        self.assertTrue(num_of_boxes + 1, apples_vs_boxes(num_of_boxes, num_of_apples))
        self.assertTrue(num_of_boxes - 1, apples_vs_boxes(num_of_boxes, num_of_apples))

    def test_multiple_if_statement(self):
        self.assertTrue('You are old enough to drive.', multiple_if_statement(user_age1))