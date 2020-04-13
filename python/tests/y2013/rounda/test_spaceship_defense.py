from unittest import TestCase
from y2013.rounda.spaceship_defense import shortest_path


class TestSpaceshipDefense(TestCase):

    def test_min_path_no_edges(self):
        self.assertEqual(-1, shortest_path(1, 2, ["None", "g1", "t3", "t3"], {}, 3))
        self.assertEqual(0, shortest_path(3, 2, ["None", "g1", "t3", "t3"], {}, 3))

    def test_min_path_one_hop(self):
        self.assertEqual(217, shortest_path(1, 2, ["None", "g1", "t3", "t3"], [[1, 2, 217], [3, 2, 567],
                                                                               [1, 1, 21]], 3))
        self.assertEqual(0, shortest_path(3, 2, ["None", "g1", "t3", "t3"], [[1, 2, 217], [3, 2, 567], [1, 1, 21]], 3))

    def test_min_path(self):
        self.assertEqual(-1, shortest_path(2, 1, ["None", "g1", "t3", "t3"], [[1, 2, 217], [3, 2, 567], [1, 1, 21]], 3))
        self.assertEqual(0, shortest_path(2, 3, ["None", "g1", "t3", "t3"], [[1, 2, 217], [3, 2, 567], [1, 1, 21]], 3))
        self.assertEqual(-1, shortest_path(1, 2, ["None", "ca", "bl", "bl", "8z"], [], 4))
        self.assertEqual(0, shortest_path(2, 3, ["None", "ca", "bl", "bl", "8z"], [], 4))
        self.assertEqual(0, shortest_path(1, 1, ["None", "ca", "bl", "bl", "8z"], [], 4))
        colors = ["None", "re", "b7", "ye", "gr", "0l", "0l", "ye", "b7"]
        adj_matrix = [[4, 1, 19], [2, 4, 21], [2, 5, 317], [4, 5, 34], [4, 7, 3], [4, 8, 265], [8, 6, 71]]
        self.assertEqual(3, shortest_path(4, 3, colors, adj_matrix, 8))
        self.assertEqual(55, shortest_path(2, 6, colors, adj_matrix, 8))
        self.assertEqual(-1, shortest_path(1, 4, colors, adj_matrix, 8))





