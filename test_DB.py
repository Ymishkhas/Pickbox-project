import sqlite3
import unittest

class TestDB(unittest.TestCase):

    def test_tables(self):

        conn = sqlite3.connect('C:/Users/youse/Desktop/tkinter/pickbox.db')
        c= conn.cursor()

        query = c.execute("select * from online_store")
        result = fetched= query.fetchall()
        expected = [(101, 'Guerlain', '01:12:00:00', 'Guerlain@pickbox', '###'),
                    (102 , 'Al-Nahdi', '00:06:00:00', 'Al-Nahdi@pickbox', '###'),
                    (103 , 'Addidas','01:00:00:00', 'Addidas@pickbox', '###'),
                    (104 , 'Puma', '01:00:00:00', 'Puma@pickbox', '###'),
                    (105 , 'Coffee Mood', '02:00:00:00', 'Coffee_Mood@pickbox', '###'),
                    (106 , 'Tom Ford', '01:18:00:00', 'Tom_Ford@pickbox', '###'),
                    (107 , 'iHerb', '00:8:30:00', 'iHerb@pickbox', '###'),
                    (108 , 'SesamBakery', '00:2:00:00', 'SesamBakery@pickbox', '###'),
                    (109 , 'ArabiaOud', '00:18:00:00', 'ArabiaOud@pickbox', '###')]
        self.assertEqual(result, expected)

        query = c.execute("select * from driver")
        result= query.fetchall()
        expected = [(501, 'Jeddah', 'South Jeddah', 'iHerb_South_Jeddah@pickbox', '###', 107),
                    (502, 'Jeddah', 'North Jeddah', 'iHerb_North_Jeddah@pickbox', '###', 107),
                    (503, 'Jeddah', 'East Jeddah', 'iHerb_East_Jeddah@pickbox', '###', 107),
                    (504, 'Jeddah', 'West Jeddah', 'iHerb_West_Jeddah@pickbox', '###', 107),
                    (505, 'Jeddah', 'Middle Jeddah', 'iHerb_Middle_Jeddah@pickbox', '###', 107)]
        self.assertEqual(result, expected)

        query = c.execute("select * from pickbox")
        result= query.fetchall()
        expected = [(20, 'Active', 'Jeddah', 'North Jeddah', 'Taiba', 'R42V+8J'),
                    (21, 'Active', 'Jeddah', 'North Jeddah', 'Al Sawari', 'Q4W2+WC'),
                    (22, 'Active', 'Jeddah', 'North Jeddah', 'Al Yaqoot', 'Q3JR+VQ'),
                    (23, 'Active', 'Jeddah', 'North Jeddah', 'Al Zummard', 'Q3X6+82'),
                    (24, 'Active', 'Jeddah', 'North Jeddah', 'Al Lulu', 'Q39C+XM'),
                    (25, 'Down', 'Jeddah', 'North Jeddah', 'Al Firdous', 'Q4P9+FX')]
        self.assertEqual(result, expected)

        query = c.execute("select * from store_deliver_to")
        result= query.fetchall()
        expected = [(107,20),
                    (107,21),
                    (107,22),
                    (107,25)]
        self.assertEqual(result, expected)

        query = c.execute("select * from locker")
        result= query.fetchall()
        expected = [(1004, 'Empty', 'B', 25),
                    (1005, 'Occupied', 'B', 25),
                    (1006, 'Empty', 'B', 25),
                    (1130, 'Occupied', 'A', 22),
                    (1131, 'Empty', 'A', 22),
                    (1132, 'Occupied', 'A', 22),
                    (1205, 'Empty', 'A', 23),
                    (1206, 'Occupied', 'A', 23),
                    (1207, 'Empty', 'A', 23),
                    (1208, 'Empty', 'A', 23)]
        self.assertEqual(result, expected)

        query = c.execute("select * from customer")
        result= query.fetchall()
        expected = [(1,'yaseer Alharbi', 966555411384, 'yaseer@gmail.com'),
                    (2,'Jacob Qiza', 966580688210, 'Jacob@hotmail.com'),
                    (3,'Yousef Sumaydee', 966507095266, 'YousefXX@Yahoo.com'),
                    (4,'Gordon Griffen', 966552495419, 'GordonsUncle@gmail.com'),
                    (5,'amjad Mubarak', 966554587433, 'amjad26@gmail.com')]
        self.assertEqual(result, expected)

        query = c.execute("select * from shipment")
        result= query.fetchall()
        expected = [(100001, 'Shipped', '2023-04-25, 01:00 PM', '2023-04-25, 11:00 AM', 1),
                    (100002, 'Picked Up', '2023-01-02, 01:00 PM', '2023-01-02, 12:34 PM', 1),
                    (100003, 'Picked Up', '2023-06-13, 10:00 AM', '2023-06-13, 8:20 AM', 2),
                    (100004, 'Cancelled', '2023-09-3, 7:00 PM', '2023-09-3, 6:46 PM', 2),
                    (100005, 'Out For Delivery', '2023-09-7, 6:30 PM', None, 3),
                    (100006, 'Picked Up', '2023-09-12, 7:45 PM', '2023-09-12, 7:02 PM', 4),
                    (100007, 'Picked Up', '2023-09-28, 9:30 AM', '2023-09-28, 9:09 AM', 5),
                    (100008, 'Picked Up', '2023-09-28, 9:20 AM', '2023-09-28, 9:12 AM', 1),
                    (100009, 'Out For Delivery', '2023-10-31, 9:15 AM', None, 5),
                    (100010, 'Shipped', '2023-12-1, 2:20 PM', '2023-12-1, 1:19 PM', 5),
                    (100011, 'Shipped', '2023-01-6, 3:00 PM', '2023-01-6, 1:19 PM', 3)]
        self.assertEqual(result, expected)

        query = c.execute("select * from shipment_belongs_to")
        result= query.fetchall()
        expected = [(100001,101, 1130),
                    (100002,105, 1004),
                    (100003,102, 1205),
                    (100004,103, 1005),
                    (100005,107, 1006),
                    (100006,106, 1206),
                    (100007,109, 1132),
                    (100008,109, 1207),
                    (100009,107, 1207),
                    (100010,107, 1130),
                    (100011,101, 1132)]
        self.assertEqual(result, expected)

        conn.close()

    def test_views(self):

        conn = sqlite3.connect('C:/Users/youse/Desktop/tkinter/pickbox.db')
        c= conn.cursor()
        
        query = c.execute("select * from customerView")
        result= query.fetchall()
        expected = [(100001, 'Shipped', '2023-04-25, 11:00 AM', 1130, 22, 'yaseer@gmail.com', 'Guerlain', 966555411384), 
                    (100002, 'Picked Up', '2023-01-02, 12:34 PM', 1004, 25, 'yaseer@gmail.com', 'Coffee Mood', 966555411384), 
                    (100003, 'Picked Up', '2023-06-13, 8:20 AM', 1205, 23, 'Jacob@hotmail.com', 'Al-Nahdi', 966580688210), 
                    (100004, 'Cancelled', '2023-09-3, 6:46 PM', 1005, 25, 'Jacob@hotmail.com', 'Addidas', 966580688210), 
                    (100005, 'Out For Delivery', None, 1006, 25, 'YousefXX@Yahoo.com', 'iHerb', 966507095266), 
                    (100006, 'Picked Up', '2023-09-12, 7:02 PM', 1206, 23, 'GordonsUncle@gmail.com', 'Tom Ford', 966552495419), 
                    (100007, 'Picked Up', '2023-09-28, 9:09 AM', 1132, 22, 'amjad26@gmail.com', 'ArabiaOud', 966554587433), 
                    (100008, 'Picked Up', '2023-09-28, 9:12 AM', 1207, 23, 'yaseer@gmail.com', 'ArabiaOud', 966555411384), 
                    (100009, 'Out For Delivery', None, 1207, 23, 'amjad26@gmail.com', 'iHerb', 966554587433), 
                    (100010, 'Shipped', '2023-12-1, 1:19 PM', 1130, 22, 'amjad26@gmail.com', 'iHerb', 966554587433), 
                    (100011, 'Shipped', '2023-01-6, 1:19 PM', 1132, 22, 'YousefXX@Yahoo.com', 'Guerlain', 966507095266)]
        self.assertEqual(result, expected)

        conn.close()
        

if __name__ == '__main__':
    unittest.main()