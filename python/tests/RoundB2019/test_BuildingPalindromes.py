from RoundB2019 import number_palindromes
from unittest import TestCase


class BuildingPalindromesTest(TestCase):

    def test_number_palindromes_empty_string(self):
        self.assertEqual(0, number_palindromes('', [[0, 3]]))

    def test_number_palindromes_two_single_questions(self):
        self.assertEqual(3, number_palindromes('ABCDEF', [[3, 3], [4, 4], [1, 1]]))
        self.assertEqual(3, number_palindromes('ABCDEF', [[3, 3], [4, 4], [1, 1], [10, 10], [0, 0], [2, 1]]))

    def test_number_palindromes_all_same_question(self):
        self.assertEqual(0, number_palindromes('XYZ', [[1, 3], [1, 3], [1, 3], [1, 3], [1, 3]]))

    def test_number_palindromes_generic_questions(self):
        self.assertEqual(3, number_palindromes('ABAACCA', [[3, 6], [4, 4], [2, 5], [6, 7], [3, 7]]))
