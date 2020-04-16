from unittest import TestCase
from y2013.roundb.dragon_maze import shortest_path


class TestDragonMaze(TestCase):

    def test_shortest_path_same_start_end(self):
        self.assertEqual(10, shortest_path([0, 0], [0, 0], [[10, -1]]))

    def test_shortest_path_no_path(self):
        self.assertEqual(-1, shortest_path([0, 0], [1, 1], [[10, -1], [-1, 20]]))
        self.assertEqual(-1, shortest_path([0, 2], [1, 0], [[2, -1, 5], [3, -1, 6]]))

    def test_shortest_four_by_four(self):
        self.assertEqual(7, shortest_path([0, 2], [3, 2], [[-1, 1, 1, 2], [1, 1, 1, 1], [2, -1, -1, 1], [1, 1, 1, 1]]))
        self.assertEqual(9, shortest_path([0, 2], [3, 1], [[-1, 1, 1, 2], [1, 1, 1, 1], [3, -1, -1, 1], [1, 1, 1, 1]]))
