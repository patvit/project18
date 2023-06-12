import unittest
from unittest.mock import patch
from main import command_p, uniq_geo, channel_stat, ya_test

def multiplication_int(a, b):

    return a * b

def multiplication_string(line, n):
    return line * n

class TestSomething(unittest.TestCase):
    def setUp(self):
       print("method setUp")

    def tearDown(self):
        print("method tearDown")

    def test_numbers_3_4(self):
        self.assertEqual(multiplication_int(3, 4), 12)

    def test_strings_a_3(self):
        self.assertEqual(multiplication_string('a', 3), 'aaa')

    def test_command_p(self):
        res = command_p('11-2')
        expected = 'Документ с номером ', '11-2', ' принадлежит ', 'Геннадий Покемонов'
        self.assertEqual(res, expected)

    def test_uniq_geo(self):
        res = uniq_geo()
        expected = True
        self.assertEqual(res, expected)

    def test_channel_stats(self):
        res = channel_stat()
        expected = 'yandex'
        self.assertEqual(res, expected)

    def test_ya_test(self):
        res = ya_test()
        expected = 201
        self.assertEqual(res, expected)

if __name__ == '__main__':
    unittest.main()
