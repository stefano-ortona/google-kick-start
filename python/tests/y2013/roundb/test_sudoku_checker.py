from unittest import TestCase
from y2013.roundb.sudoku_checker import check_sudoku


class TestSudokuChecker(TestCase):

    def test_check_sudoku_one_square(self):
        self.assertEqual(True, check_sudoku([[1]], 1))
        self.assertEqual(False, check_sudoku([[0]], 1))

    def test_check_sudoku_four_squares(self):
        self.assertEqual(False, check_sudoku([[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]], 2))
        self.assertEqual(False, check_sudoku([[100, 2, 3, 4], [3, 4, 1, 2], [1, 2, 3, 4], [1, 2, 3, 4]], 2))

    def test_check_sudoku_nine_squares(self):
        self.assertEqual(True, check_sudoku([[5, 3, 4, 6, 7, 8, 9, 1, 2],
                                             [6, 7, 2, 1, 9, 5, 3, 4, 8],
                                             [1, 9, 8, 3, 4, 2, 5, 6, 7],
                                             [8, 5, 9, 7, 6, 1, 4, 2, 3],
                                             [4, 2, 6, 8, 5, 3, 7, 9, 1],
                                             [7, 1, 3, 9, 2, 4, 8, 5, 6],
                                             [9, 6, 1, 5, 3, 7, 2, 8, 4],
                                             [2, 8, 7, 4, 1, 9, 6, 3, 5],
                                             [3, 4, 5, 2, 8, 6, 1, 7, 9]], 3))
        self.assertEqual(False, check_sudoku([[1, 2, 3, 4, 5, 6, 7, 8, 9],
                                             [1, 2, 3, 4, 5, 6, 7, 8, 9],
                                             [1, 2, 3, 4, 5, 6, 7, 8, 9],
                                             [1, 2, 3, 4, 5, 6, 7, 8, 9],
                                             [1, 2, 3, 4, 5, 6, 7, 8, 9],
                                             [1, 2, 3, 4, 5, 6, 7, 8, 9],
                                             [1, 2, 3, 4, 5, 6, 7, 8, 9],
                                             [1, 2, 3, 4, 5, 6, 7, 8, 9],
                                             [1, 2, 3, 4, 5, 6, 7, 8, 9]], 3))
        self.assertEqual(False, check_sudoku([[5, 3, 4, 6, 7, 8, 9, 1, 2],
                                             [6, 7, 2, 1, 9, 5, 3, 4, 8],
                                             [1, 9, 8, 3, 4, 2, 5, 6, 7],
                                             [8, 5, 9, 7, 6, 1, 4, 2, 3],
                                             [4, 2, 6, 8, 999, 3, 7, 9, 1],
                                             [7, 1, 3, 9, 2, 4, 8, 5, 6],
                                             [9, 6, 1, 5, 3, 7, 2, 8, 4],
                                             [2, 8, 7, 4, 1, 9, 6, 3, 5],
                                             [3, 4, 5, 2, 8, 6, 1, 7, 9]], 3))

