# from django.test import TestCase
from unittest import TestCase

# Create your tests here.
def sum_int(a, b):
    return a + b


class TestSum(TestCase):
    def test_sum(self):
        self.assertEqual(sum_int(1, 2), 3)
