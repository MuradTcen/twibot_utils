#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest
import sys
sys.path.append('../twitterbot_utils/')
from Tweet import Tweet


class MyListTest(unittest.TestCase):

    def test_digits(self):
        res = Tweet(7).text
        self.assertEqual(bool(res), False)

    def test_bool(self):
        res = Tweet(False).text
        self.assertEqual(bool(res), False)

    def test_str(self):
        res = Tweet('test.').text
        self.assertEqual(bool(res), True)

    def test_gt_lt_special_symbols(self):
        res = Tweet('Test &gt; &lt;.').text
        self.assertEqual(res, 'Test > <.')

    def test_screen_names(self):
        res = Tweet('@name test @name test @name').text
        self.assertEqual(res, 'test test')

    def test_length(self):
        res = Tweet('123456789012345678901234567890 \
        	1234567890123456789012345678901234567890 \
        	1234567890123456789012345678901234567890 \
        	1234567890123456789012345678901234567890').text
        self.assertEqual(bool(res), False)
if __name__ == '__main__':
    unittest.main()
