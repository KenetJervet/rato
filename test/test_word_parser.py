import unittest
from _parser._word import Word
from _parser._whitespace import WhiteSpace


class TestWordParser(unittest.TestCase):
    def setUp(self):
        pass

    def test_word_parser(self):
        string = "this is 0nly."
        word_parser = Word()
        res1 = word_parser.parse(string)
        self.assertTrue(res1.succeeded)
        res2 = WhiteSpace().parse(res1.remaining)
        res3 = word_parser.parse(res2.remaining)
        self.assertTrue(res3.succeeded)
        self.assertTrue(res3.recognized, 'is')
        res4 = WhiteSpace().parse(res3.remaining)
        res5 = word_parser.parse(res4.remaining)
        self.assertFalse(res5.succeeded)
