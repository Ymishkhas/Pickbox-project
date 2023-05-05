import sys
sys.path.append('C:/Users/youse/Desktop/tkinter')

import sqlite3
import unittest
import utils

DB_PATH = 'C:/Users/youse/Desktop/tkinter/Database/pickbox.db'

class Test_Login(unittest.TestCase):

    def setUp(self):
        self.conn = sqlite3.connect(DB_PATH)
        self.c= self.conn.cursor()

    def tearDown(self):
        self.conn.close()

    def test_customer_login(self):

        result = utils.is_valid_customer(966541001226)
        expected = False
        self.assertEqual(result, expected)

        result = utils.is_valid_customer(966555411384)
        expected = True
        self.assertEqual(result, expected)

        result = utils.is_valid_customer("966580688210")
        expected = True
        self.assertEqual(result, expected)

    def test_driver_login(self):
        
        result = utils.is_valid_driver("Namshi_JDN@pickbox","namshi")
        expected = True
        self.assertEqual(result, expected)

        result = utils.is_valid_driver("Namshi_JDN@pickbox","yousef")
        expected = False
        self.assertEqual(result, expected)

        result = utils.is_valid_driver("iHerb_North_Jeddah","Jarir")
        expected = False
        self.assertEqual(result, expected)

        result = utils.is_valid_driver(966580688210,"###")
        expected = False
        self.assertEqual(result, expected)
        

if __name__ == '__main__':
    unittest.main()