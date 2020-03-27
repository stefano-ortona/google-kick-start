from unittest import TestCase
from RoundA2020 import min_difficulty


class TestWorkout(TestCase):
    def test_min_difficulty_empty_times(self):
        self.assertEqual(0, min_difficulty([], 5))

    def test_min_difficulty_no_times_difference(self):
        self.assertEqual(1, min_difficulty([1, 2, 3, 4, 5], 5))

    def test_min_difficulty_one_additional_training(self):
        self.assertEqual(3, min_difficulty([1, 2, 3, 4, 10], 1))
        self.assertEqual(10, min_difficulty([1, 2, 19, 20, 30], 1))

    def test_min_difficulty_two_additional_training(self):
        self.assertEqual(2, min_difficulty([10, 13, 15, 16, 17], 1))

    def test_min_difficulty_three_additional_training(self):
        self.assertEqual(1, min_difficulty([1, 2, 3, 4, 5, 6, 7, 10], 3))

    def test_min_difficulty_six_additional_training(self):
        self.assertEqual(3, min_difficulty([9, 10, 20, 26, 30], 6))
        self.assertEqual(16, min_difficulty([9, 10, 20, 26, 90], 6))


