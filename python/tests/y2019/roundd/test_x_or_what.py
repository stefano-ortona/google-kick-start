from unittest import TestCase
from y2019.roundd.x_or_what import max_interval


class TestXOrWhat(TestCase):

    def test_max_interval_no_insertion(self):
        self.assertEqual('', max_interval([1, 2, 3, 4], []))

    def test_max_interval_one_insertion(self):
        self.assertEqual('3', max_interval([1, 2, 3, 4], [[0, 8]]))
        self.assertEqual('3', max_interval([5, 2, 3, 4], [[0, 8]]))
        self.assertEqual('4', max_interval([5, 2, 3, 4], [[0, 17]]))
        self.assertEqual('4', max_interval([32, 2, 3, 4], [[0, 17]]))
        self.assertEqual('4', max_interval([14, 1, 15, 20, 26], [[4, 26]]))

    def test_max_interval_three_insertions(self):
        self.assertEqual('4 3 4', max_interval([10, 21, 3, 7], [[1, 13], [0, 32], [2, 22]]))




