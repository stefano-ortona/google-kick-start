from unittest import TestCase
from y2020.roundb.roboth_path_decoding import final_square


class TestRobotPathDecoding(TestCase):

    def test_final_square_one_move(self):
        self.assertEqual([2, 1], final_square("E"))
        self.assertEqual([1000000000, 1], final_square("W"))
        self.assertEqual([1, 2], final_square("S"))
        self.assertEqual([1, 1000000000], final_square("N"))

    def test_final_square_no_nesting(self):
        self.assertEqual([4, 4], final_square("SSSEEE"))

    def test_final_square_with_nesting(self):
        self.assertEqual([3, 1], final_square("N3(S)N2(E)N"))
        self.assertEqual([3, 999999995], final_square("2(3(NW)2(W2(EE)W))"))
