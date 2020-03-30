from unittest import TestCase
from y2019.roundc.wiggle_walk import final_square


class TestWiggleWalk(TestCase):

    def test_final_square_empty_moves(self):
        self.assertEqual([1, 2], final_square(1, 2, 3, 6, ''))
        self.assertEqual([0, 0], final_square(0, 0, 10, 10, ''))

    def test_final_square_one_move(self):
        self.assertEqual([1, 3], final_square(1, 2, 3, 6, 'E'))
        self.assertEqual([2, 2], final_square(1, 2, 3, 6, 'S'))
        self.assertEqual([1, 1], final_square(1, 2, 3, 6, 'W'))
        self.assertEqual([0, 2], final_square(1, 2, 3, 6, 'N'))

    def test_final_square_generic_moves(self):
        self.assertEqual([2, 1], final_square(1, 2, 3, 6, 'EEWNS'))
        self.assertEqual([2, 2], final_square(0, 0, 3, 3, 'SESE'))
        self.assertEqual([2, 6], final_square(2, 3, 5, 8, 'NEESSWWNESE'))
