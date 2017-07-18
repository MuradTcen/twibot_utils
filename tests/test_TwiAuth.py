#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest
import sys
sys.path.append('../twitterbot_utils/')
from TwiAuth import TwiAuth

class MyListTest(unittest.TestCase):

    def test_setter_access_token_secre(self):
        auth = TwiAuth('a', 'b')
        self.assertEqual((auth.access_token, auth.access_secret), ('a', 'b'))

    def test_constructor_without_argv(self):
    	auth = TwiAuth()
    	self.assertEqual('access_token' and 'access_secret' in dir(auth),False)
if __name__ == '__main__':
    unittest.main()
