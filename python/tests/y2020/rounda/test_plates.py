from unittest import TestCase
from y2020.rounda import pick_plates
from random import randint


def generate_big_input(row, col):
    stack = [[randint(0, 100) for i in range(col)] for j in range(row)]
    return stack


class Test(TestCase):

    def test_pick_plates_empty_stack(self):
        self.assertEqual(pick_plates([[]], 2), 0)

    def test_pick_plates_one_element_stack(self):
        self.assertEqual(pick_plates([[20]], 2), 20)

    def test_pick_plates_one_element_stack(self):
        self.assertEqual(pick_plates([[20]], 2), 20)

    def test_pick_plates_no_capacity(self):
        self.assertEqual(pick_plates([[20, 40, 50]], 0), 0)

    def test_pick_plates_two_stacks(self):
        self.assertEqual(pick_plates([[10, 10, 100, 30], [80, 50, 10, 50]], 5), 250)

    def test_pick_plates_three_stacks(self):
        self.assertEqual(pick_plates([[80, 80], [15, 50], [20, 10]], 3), 180)

    def test_pick_plates_big_input(self):
        for i in range(10):
            self.assertTrue(pick_plates(generate_big_input(50, 30), randint(0, 50*30)) > 0)

