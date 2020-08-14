#!/usr/bin/env python3


import unittest

from validations import validate_user

class TestValidateUser(unittest.TestCase):
    def test_valid(self):
        self.assertEqual(validate_user("validuser",3), True)
    
    def test_too_short(self):
        self.assertEqual(validate_user("short",10), False)

    def test_invalid_chars(self):
        self.assertEqual(validate_user("invalid_chars",3), False)

    def test_invalid_minlen(self):
        ## assertRaises   expected error , thing to call, parameters
        self.assertRaises(ValueError, validate_user, "user", -1)
    
    

unittest.main()
