import sys
sys.path.append('C:/Users/youse/Desktop/tkinter')

import sqlite3
import unittest
import utils

DB_PATH = 'C:/Users/youse/Desktop/tkinter/Database/pickbox.db'

# These test works only if the database in its original form, if you made changes please delete pickbox.db and run creatingDB to get the original one
class Test_Fetch(unittest.TestCase):

    def setUp(self):
        self.conn = sqlite3.connect(DB_PATH)
        self.c= self.conn.cursor()

    def tearDown(self):
        self.conn.close()

    def test_get_shipment(self):

        result = utils.get_shipment(100016)
        expected = [(100016, 'Ready For Collection', '2023/05/01, 13:19', '2023/05/01, 14:20', 'Namshi', 22, 1245, 966580688210)]
        self.assertEqual(result, expected)

        result = utils.get_shipment(1000)
        expected = []
        self.assertEqual(result, expected)

    def test_get_shipments(self):
        
        result = utils.get_shipments(966580688210)
        expected = [(100013, 'Pending', '2023/05/20, 21:09', '2023/05/28, 21:30', 'Jarir', 22, 1246, 966580688210), 
                    (100014, 'Pending', '2023/05/25, 21:12', '2023/05/28, 21:20', 'Namshi', 21, 1243, 966580688210), 
                    (100016, 'Ready For Collection', '2023/05/01, 13:19', '2023/05/01, 14:20', 'Namshi', 22, 1245, 966580688210)]
        self.assertEqual(result, expected)

        result = utils.get_shipments(966541001226)
        expected = []
        self.assertEqual(result, expected)
        
    def test_get_driver_store_info(self):
        
        result = utils.get_driver_store_info("Namshi_JDN@pickbox")
        expected = [('North Jeddah', 'Namshi')]
        self.assertEqual(result, expected)

        result = utils.get_driver_store_info("Jarir_JDE@pickbox")
        expected = []
        self.assertEqual(result, expected)
              
    def test_get_driver_orders(self):

        result = utils.get_driver_orders("Namshi_JDN@pickbox")
        expected = [(100002, 'Pending', '2023/05/08, 12:34', '2023/05/12, 08:00', 23, 1305), 
                     (100014, 'Pending', '2023/05/25, 21:12', '2023/05/28, 21:20', 21, 1243), 
                     (100015, 'Out For Delivery', '2023/05/05, 19:10', '2023/05/05, 21:15', 22, 1244), 
                     (100016, 'Ready For Collection', '2023/05/01, 13:19', '2023/05/01, 14:20', 22, 1245)]
        self.assertEqual(result, expected)

        result = utils.get_driver_orders("Jarir_JDE@pickbox")
        expected = []
        self.assertEqual(result, expected)
            
if __name__ == '__main__':
    unittest.main()