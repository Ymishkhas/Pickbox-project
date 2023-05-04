import sys
sys.path.append('C:/Users/youse/Desktop/tkinter')

import sqlite3
import unittest
import utils

DB_PATH = 'C:/Users/youse/Desktop/tkinter/Database/pickbox.db'

class TestDB(unittest.TestCase):

    def setUp(self):
        self.conn = sqlite3.connect(DB_PATH)
        self.c= self.conn.cursor()

    def tearDown(self):
        self.conn.close()

    def test_tables(self):

        

        query = self.c.execute("select * from online_store")
        result = fetched= query.fetchall()
        expected = [(101, 'Jarir', '01:12:00:00'),
                    (102 , 'Al Nahdi', '00:06:00:00'),
                    (103 , 'Addidas','01:00:00:00'),
                    (104 , 'Saco', '01:00:00:00'),
                    (105 , 'Coffee Mood', '02:00:00:00'),
                    (106 , 'Namshi', '01:18:00:00'),
                    (107 , 'iHerb', '00:8:30:00'),
                    (108 , 'SesamBakery', '00:2:00:00'),
                    (109 , 'ArabiaOud', '00:18:00:00')]
        self.assertEqual(result, expected)

        query = self.c.execute("select * from driver")
        result= query.fetchall()
        expected = [(501, 'Jeddah', 'North Jeddah', 'Jarir_JDN@pickbox', 'Jarir', 101),
                    (502, 'Jeddah', 'North Jeddah', 'Namshi_JDN@pickbox', 'namshi', 106),
                    (503, 'Jeddah', 'North Jeddah', 'iHerb_JDN@pickbox', 'iherb', 107)]
        self.assertEqual(result, expected)

        query = self.c.execute("select * from pickbox")
        result= query.fetchall()
        expected = [(20, 'Active', 'Jeddah', 'North Jeddah', 'Taiba', 'R42V+8J'),
                    (21, 'Active', 'Jeddah', 'North Jeddah', 'Al Sawari', 'Q4W2+WC'),
                    (22, 'Active', 'Jeddah', 'North Jeddah', 'Al Yaqoot', 'Q3JR+VQ'),
                    (23, 'Active', 'Jeddah', 'North Jeddah', 'Al Zummard', 'Q3X6+82'),
                    (24, 'Active', 'Jeddah', 'North Jeddah', 'Al Lulu', 'Q39C+XM'),
                    (25, 'Down', 'Jeddah', 'North Jeddah', 'Al Firdous', 'Q4P9+FX')]
        self.assertEqual(result, expected)

        query = self.c.execute("select * from store_deliver_to")
        result= query.fetchall()
        expected = [(101,20),
                    (101,21),
                    (101,22),
                    (101,23),
                    (101,24),
                    (106,20),
                    (106,21),
                    (106,22),
                    (106,23),
                    (106,24),
                    (107,20),
                    (107,21),
                    (107,22),
                    (107,23),
                    (107,24)]
        self.assertEqual(result, expected)

        query = self.c.execute("select * from locker")
        result= query.fetchall()
        expected = [(1004, 'Empty', 1743, 20),
                    (1005, 'Occupied', 5582, 20),
                    (1006, 'Empty', 2783, 20),
                    (1007, 'Empty', 7899, 20),
                    (1130, 'Occupied', 7654, 21),
                    (1131, 'Empty', 4522, 21),
                    (1132, 'Empty', 2456, 21),
                    (1133, 'Occupied', 9369, 21),
                    (1243, 'Empty', 5448, 21),
                    (1244, 'Empty', 5677, 22),
                    (1245, 'Occupied', 1794, 22),
                    (1246, 'Empty', 1689, 22),
                    (1305, 'Empty', 8495, 23),
                    (1306, 'Occupied', 6685, 23),
                    (1307, 'Empty', 5719, 23),
                    (1308, 'Empty', 2603, 23)]
        self.assertEqual(result, expected)

        query = self.c.execute("select * from customer")
        result= query.fetchall()
        expected = [(1,'Mohammed Alhaddad', 966500010007, 'malhaddad@gmail.com'),
                    (2,'Yousef Mishkhas', 966580688210, 'y3ou12@hotmail.com'),
                    (3,'Hatem Alharbi', 966555411384, 'hatim999@Yahoo.com')]
        self.assertEqual(result, expected)

        query = self.c.execute("select * from shipment")
        result= query.fetchall()
        expected = [(100001, 'Pending', '2023/05/10, 13:00', '2023/04/29, 11:00', 3),
                    (100002, 'Pending', '2023/05/12, 08:00', '2023/05/08, 12:34', 3),
                    (100003, 'Out For Delivery', '2023/05/05, 10:00', '2023/05/05, 07:20', 3),
                    (100004, 'Ready For Collection', '2023/05/05, 19:00', '2023/05/05, 18:46', 3),
                    (100005, 'Ready For Collection', '2023/05/05, 07:30', '2023/05/05, 03:30', 3),
                    (100006, 'Picked Up', '2023/04/12, 19:45', '2023/04/12, 20:02', 3),
                    (100007, 'Pending', '2023/05/20, 13:00', '2023/05/18, 11:00', 1),
                    (100008, 'Pending', '2023/05/17, 08:00', '2023/05/14, 12:34', 1),
                    (100009, 'Out For Delivery', '2023/05/13, 10:00', '2023/05/13, 8:20', 1),
                    (100010, 'Ready For Collection', '2023/05/13, 19:00', '2023/05/13, 18:46', 1),
                    (100011, 'Ready For Collection', '2023/05/13, 08:30', '2023/05/13, 07:12', 1),
                    (100012, 'Picked Up', '2023/04/28, 19:45', '2023/04/28, 19:50', 1),
                    (100013, 'Pending', '2023/05/28, 21:30', '2023/05/20, 21:09', 2),
                    (100014, 'Pending', '2023/05/28, 21:20', '2023/05/25, 21:12', 2),
                    (100015, 'Out For Delivery', '2023/05/05, 21:15', '2023/05/05, 19:10', 3),
                    (100016, 'Ready For Collection', '2023/05/01, 14:20', '2023/05/01, 13:19', 2)]
        self.assertEqual(result, expected)

        query = self.c.execute("select * from shipment_belongs_to")
        result= query.fetchall()
        expected = [(100001,101, 1004),
                    (100002,106, 1305),
                    (100003,107, 1006),
                    (100004,105, 1005),
                    (100005,107, 1133),
                    (100006,102, 1132),
                    (100007,101, 1007),
                    (100008,106, 1207),
                    (100009,107, 1131),
                    (100010,107, 1130),
                    (100011,108, 1306),
                    (100012,103, 1307),
                    (100013,101, 1246),
                    (100014,106, 1243),
                    (100015,106, 1244),
                    (100016,106, 1245)]
        self.assertEqual(result, expected)

    def test_views(self):
        
        query = self.c.execute("select * from customerView")
        result= query.fetchall()
        expected = [(100001, 'Pending', '2023/04/29, 11:00', '2023/05/10, 13:00', 'Jarir', 20, 1004, 'hatim999@Yahoo.com', 966555411384), 
                    (100002, 'Pending', '2023/05/08, 12:34', '2023/05/12, 08:00', 'Namshi', 23, 1305, 'hatim999@Yahoo.com', 966555411384), 
                    (100003, 'Out For Delivery', '2023/05/05, 07:20', '2023/05/05, 10:00', 'iHerb', 20, 1006, 'hatim999@Yahoo.com', 966555411384), 
                    (100004, 'Ready For Collection', '2023/05/05, 18:46', '2023/05/05, 19:00', 'Coffee Mood', 20, 1005, 'hatim999@Yahoo.com', 966555411384), 
                    (100005, 'Ready For Collection', '2023/05/05, 03:30', '2023/05/05, 07:30', 'iHerb', 21, 1133, 'hatim999@Yahoo.com', 966555411384), 
                    (100006, 'Picked Up', '2023/04/12, 20:02', '2023/04/12, 19:45', 'Al Nahdi', 21, 1132, 'hatim999@Yahoo.com', 966555411384), 
                    (100007, 'Pending', '2023/05/18, 11:00', '2023/05/20, 13:00', 'Jarir', 20, 1007, 'malhaddad@gmail.com', 966500010007), 
                    (100009, 'Out For Delivery', '2023/05/13, 8:20', '2023/05/13, 10:00', 'iHerb', 21, 1131, 'malhaddad@gmail.com', 966500010007), 
                    (100010, 'Ready For Collection', '2023/05/13, 18:46', '2023/05/13, 19:00', 'iHerb', 21, 1130, 'malhaddad@gmail.com', 966500010007), 
                    (100011, 'Ready For Collection', '2023/05/13, 07:12', '2023/05/13, 08:30', 'SesamBakery', 23, 1306, 'malhaddad@gmail.com', 966500010007), 
                    (100012, 'Picked Up', '2023/04/28, 19:50', '2023/04/28, 19:45', 'Addidas', 23, 1307, 'malhaddad@gmail.com', 966500010007), 
                    (100013, 'Pending', '2023/05/20, 21:09', '2023/05/28, 21:30', 'Jarir', 22, 1246, 'y3ou12@hotmail.com', 966580688210), 
                    (100014, 'Pending', '2023/05/25, 21:12', '2023/05/28, 21:20', 'Namshi', 21, 1243, 'y3ou12@hotmail.com', 966580688210),
                    (100015, 'Out For Delivery', '2023/05/05, 19:10', '2023/05/05, 21:15', 'Namshi', 22, 1244, 'hatim999@Yahoo.com', 966555411384), 
                    (100016, 'Ready For Collection', '2023/05/01, 13:19', '2023/05/01, 14:20', 'Namshi', 22, 1245, 'y3ou12@hotmail.com', 966580688210)]
        self.assertEqual(result, expected)
        
if __name__ == '__main__':
    unittest.main()


# Brute force testing for developers


# #check the variables names here
# # newDeliveryTime = getCurrentTime()
# # print(type(newDeliveryTime))

# conn = sqlite3.connect(DB_PATH)
# c = conn.cursor()

# orders = c.execute("select * from customerView").fetchall()

# print(orders)

# conn.commit()
# conn.close()
