import sys
sys.path.append('C:/Users/youse/Desktop/tkinter')

import sqlite3
import unittest
import utils

DB_PATH = 'C:/Users/youse/Desktop/tkinter/Database/pickbox.db'

class Test_Utils(unittest.TestCase):

    def setUp(self):
        self.conn = sqlite3.connect(DB_PATH)
        self.c= self.conn.cursor()

    def tearDown(self):
        self.conn.close()

    def test_cancel(self):

        # result = utils.cancel_shipment(shipment_id)
        # expected = False
        # self.assertEqual(result, expected)

        result = utils.is_valid_customer(966555411384)
        expected = True
        self.assertEqual(result, expected)

        result = utils.is_valid_customer(966555411383)
        expected = False
        self.assertEqual(result, expected)

        result = utils.is_valid_customer("966580688210")
        expected = True
        self.assertEqual(result, expected)

        result = utils.is_valid_customer("youssef")
        expected = False
        self.assertEqual(result, expected)

    def test_merge(self):
        
        result = utils.is_valid_driver("iHerb_South_Jeddah@pickbox","###")
        expected = True
        self.assertEqual(result, expected)

        result = utils.is_valid_driver("iHerb_North_Jeddah@pickbox","yousef")
        expected = False
        self.assertEqual(result, expected)

        result = utils.is_valid_driver("iHerb_North_Jeddah","###")
        expected = False
        self.assertEqual(result, expected)

        result = utils.is_valid_driver(966580688210,"###")
        expected = False
        self.assertEqual(result, expected)

    def test_update_locker(self):
        
        result = utils.is_valid_driver("iHerb_South_Jeddah@pickbox","###")
        expected = True
        self.assertEqual(result, expected)

        result = utils.is_valid_driver("iHerb_North_Jeddah@pickbox","yousef")
        expected = False
        self.assertEqual(result, expected)

        result = utils.is_valid_driver("iHerb_North_Jeddah","###")
        expected = False
        self.assertEqual(result, expected)

        result = utils.is_valid_driver(966580688210,"###")
        expected = False
        self.assertEqual(result, expected)
            
    def test_update_status(self):
        
        result = utils.is_valid_driver("iHerb_South_Jeddah@pickbox","###")
        expected = True
        self.assertEqual(result, expected)

        result = utils.is_valid_driver("iHerb_North_Jeddah@pickbox","yousef")
        expected = False
        self.assertEqual(result, expected)

        result = utils.is_valid_driver("iHerb_North_Jeddah","###")
        expected = False
        self.assertEqual(result, expected)

        result = utils.is_valid_driver(966580688210,"###")
        expected = False
        self.assertEqual(result, expected)
        
if __name__ == '__main__':
    unittest.main()