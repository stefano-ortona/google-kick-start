from unittest import TestCase
from y2013.roundb.ignore_comments import parse_comments

class TestIgnoreComments(TestCase):

    def test_parse_comments_no_recursion(self):
        self.assertEqual("/* file header */", parse_comments("//*no recursion*/* file header */"))

    def test_parse_comments_nested(self):
        self.assertEqual("Hello  world", parse_comments("Hello /* a comment /* a comment inside comment */ inside /* "
                                                        "another comment inside comment */ string */ world"))

    def test_parse_comments_nested(self):
        f = open("test_program_input", "r")
        s_input = f.read()
        f.close()
        f = open("test_program_output", "r")
        s_output = f.read()
        f.close()
        self.assertEqual(s_output, parse_comments(s_input))
