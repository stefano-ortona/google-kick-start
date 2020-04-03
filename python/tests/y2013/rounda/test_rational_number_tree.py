from unittest import TestCase
from y2013.rounda.rational_number_tree import NumberTree


class TestNumberTree(TestCase):

    def setUp(self):
        self.tree = NumberTree()


class TestFindNumberByIndex(TestNumberTree):

    def test_small_index(self):
        self.assertEqual([1, 1], self.tree.find_number_by_index(1))
        self.assertEqual([1, 2], self.tree.find_number_by_index(2))
        self.assertEqual([2, 1], self.tree.find_number_by_index(3))
        self.assertEqual([1, 3], self.tree.find_number_by_index(4))
        self.assertEqual([3, 2], self.tree.find_number_by_index(5))
        self.assertEqual([2, 3], self.tree.find_number_by_index(6))
        self.assertEqual([3, 1], self.tree.find_number_by_index(7))

    def test_big_index(self):
        self.assertEqual([8, 3], self.tree.find_number_by_index(27))
        self.assertEqual([3, 14], self.tree.find_number_by_index(80))
        self.assertEqual([14, 11], self.tree.find_number_by_index(81))
        self.assertEqual([46, 19], self.tree.find_number_by_index(435))
        self.assertEqual([65, 19], self.tree.find_number_by_index(871))
        self.assertEqual([64, 1], self.tree.find_number_by_index(pow(2, 64) - 1))


class TestFindIndexByNumber(TestNumberTree):

    def test_small_number(self):
        self.assertEqual(1, self.tree.find_index_by_number(1, 1))
        self.assertEqual(2, self.tree.find_index_by_number(1, 2))
        self.assertEqual(3, self.tree.find_index_by_number(2, 1))
        self.assertEqual(4, self.tree.find_index_by_number(1, 3))
        self.assertEqual(5, self.tree.find_index_by_number(3, 2))
        self.assertEqual(6, self.tree.find_index_by_number(2, 3))
        self.assertEqual(7, self.tree.find_index_by_number(3, 1))

    def test_big_number(self):
        self.assertEqual(27, self.tree.find_index_by_number(8, 3))
        self.assertEqual(80, self.tree.find_index_by_number(3, 14))
        self.assertEqual(81, self.tree.find_index_by_number(14, 11))
        self.assertEqual(435, self.tree.find_index_by_number(46, 19))
        self.assertEqual(871, self.tree.find_index_by_number(65, 19))
        self.assertTrue(pow(2, 64) - 1, self.tree.find_index_by_number(64, 1))




