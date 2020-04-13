from unittest import TestCase
from y2019.roundc.circuit_board import max_board
from random import randint


def generate_big_input(row, col):
    return [[randint(0, 1001) for j in range(col)] for i in range(row)]


class CircuitBoardTest(TestCase):

    def test_max_board_single_element(self):
        self.assertEqual(1, max_board([[3]], 3))

    def test_text_max_board_single_column(self):
        self.assertEqual(5, max_board([[5], [20], [1], [29], [30]], 0))

    def test_text_max_board_single_row(self):
        self.assertEqual(2, max_board([[3, 1, 3, 3]], 0))

    def test_text_max_board_zero_k(self):
        self.assertEqual(2, max_board([[4, 4, 5], [7, 6, 6]], 0))
        self.assertEqual(6, max_board([[2, 2, 4, 4, 20], [8, 3, 3, 3, 12], [6, 6, 3, 3, 3], [1, 6, 8, 6, 4]], 0))

    def test_text_max_board_small_k(self):
        self.assertEqual(4, max_board([[3, 1, 3, 3]], 2))
        self.assertEqual(3, max_board([[0, 5, 0], [8, 12, 3], [7, 10, 1]], 2))
        self.assertEqual(4, max_board([[20, 10, 20, 10], [10, 4, 5, 20], [20, 5, 4, 10], [10, 20, 10, 20]], 8))

    def test_max_board_big_input(self):
        self.assertTrue(max_board(generate_big_input(200, 200), 50) > 0)

