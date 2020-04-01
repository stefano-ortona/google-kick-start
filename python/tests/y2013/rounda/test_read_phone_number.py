from unittest import TestCase
from y2013.rounda.read_phone_number import read_number


class TestReadPhoneNumber(TestCase):

    def test_read_number_one_digit(self):
        self.assertEqual('four', read_number([4], [1]))

    def test_read_number_one_part(self):
        self.assertEqual('four double two', read_number([4, 2, 2], [3]))

    def test_read_number_five_digits(self):
        self.assertEqual('one triple two three', read_number([1, 2, 2, 2, 3], [4, 1]))
        self.assertEqual('one two double two three', read_number([1, 2, 2, 2, 3], [2, 3]))

    def test_read_number_eleven_digits(self):
        self.assertEqual('one five zero one double two three three triple four',
                         read_number([1, 5, 0, 1, 2, 2, 3, 3, 4, 4, 4], [3, 4, 4]))
        self.assertEqual('one five zero one double two double three triple four',
                         read_number([1, 5, 0, 1, 2, 2, 3, 3, 4, 4, 4], [3, 3, 5]))

    def test_read_number_twenty_digits(self):
        self.assertEqual('decuple five nonuple six six',
                         read_number([5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6], [10, 9, 1]))
        self.assertEqual('decuple five decuple six',
                         read_number([5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6], [20]))
        self.assertEqual('quadruple five sextuple five quadruple six sextuple six',
                         read_number([5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6], [4, 10, 6]))






