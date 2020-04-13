from unittest import TestCase
from y2013.rounda.sorting import sort


class TestSorting(TestCase):

    def test_sorting_only_odd(self):
        self.assertEqual([1], sort([1]))
        self.assertEqual([1, 3, 11, 21], sort([21, 1, 3, 11]))

    def test_sorting_only_even(self):
        self.assertEqual([10], sort([10]))
        self.assertEqual([22, 12, 4, 2], sort([22, 2, 4, 12]))

    def test_sorting_odd_even(self):
        self.assertEqual([1, 4, 2, 3, 5], sort([5, 2, 4, 3, 1]))
        self.assertEqual([-5, 88, 11, 20, 2, -12, 87], sort([-5, -12, 87, 2, 88, 20, 11]))
