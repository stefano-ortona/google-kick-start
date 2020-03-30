from unittest import TestCase
from y2019.roundb.energy_stones import max_energy
from random import randint


def generate_big_input(n):
    return [[randint(1, 101), randint(1, 100001), randint(0, 100001)] for i in range(n)]

class TestEnergyStones(TestCase):

    def test_max_energy_zero_stones(self):
        self.assertEqual(0, max_energy([]))

    def test_max_energy_one_stone(self):
        self.assertEqual(30, max_energy([[5, 30, 1]]))

    def test_max_energy_two_stones(self):
        self.assertEqual(500, max_energy([[12, 300, 50], [5, 200, 0]]))

    def test_max_energy_three_stones_equal_loss(self):
        self.assertEqual(8, max_energy([[10, 4, 100], [10, 3, 100], [10, 8, 100]]))

    def test_max_energy_four_stones(self):
        self.assertEqual(105, max_energy([[20, 10, 1], [5, 30, 5], [100, 30, 1], [5, 80, 60]]))

    def test_max_energy_big_input(self):
        self.assertTrue(max_energy(generate_big_input(100)) > 0)
