from unittest import TestCase
from y2014.rounda.segment_display import next_digit


class TestSegmentDisplay(TestCase):

    def test_next_digit_one_digit(self):
        self.assertEqual("1110000", next_digit(["1111111"]))

    def test_next_digit_one_error(self):
        self.assertEqual(None, next_digit(["0000000", "0001010"]))

    def test_next_digit(self):
        self.assertEqual("0100011", next_digit(["0100000", "0000111", "0000011"]))
        self.assertEqual("0010011", next_digit(["1011011", "1011111", "1010000", "1011111", "1011011"]))
        self.assertEqual("0000100", next_digit(["0000000", "0000000", "0000000", "0000100", "0000000"]))

