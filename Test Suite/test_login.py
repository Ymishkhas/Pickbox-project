import sqlite3
import unittest
import methods

DB_PATH = 'C:/Users/youse/Desktop/tkinter/Database/pickbox.db'

class Test_Login(unittest.TestCase):

    def setUp(self):
        self.conn = sqlite3.connect(DB_PATH)
        self.c= self.conn.cursor()

    def tearDown(self):
        self.conn.close()

    def test_customer_login(self):

        result = methods.is_valid_customer(966541001226)
        expected = False
        self.assertEqual(result, expected)

        result = methods.is_valid_customer(966555411384)
        expected = True
        self.assertEqual(result, expected)

        result = methods.is_valid_customer(966555411383)
        expected = False
        self.assertEqual(result, expected)

        result = methods.is_valid_customer("966580688210")
        expected = True
        self.assertEqual(result, expected)

        result = methods.is_valid_customer("youssef")
        expected = False
        self.assertEqual(result, expected)

    def test_driver_login(self):
        
        result = methods.is_valid_driver("iHerb_South_Jeddah@pickbox","###")
        expected = True
        self.assertEqual(result, expected)

        result = methods.is_valid_driver("iHerb_North_Jeddah@pickbox","yousef")
        expected = False
        self.assertEqual(result, expected)

        result = methods.is_valid_driver("iHerb_North_Jeddah","###")
        expected = False
        self.assertEqual(result, expected)

        result = methods.is_valid_driver(966580688210,"###")
        expected = False
        self.assertEqual(result, expected)
        

if __name__ == '__main__':
    unittest.main()