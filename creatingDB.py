import sqlite3

# create DB
conn = sqlite3.connect('C:/Users/youse/Desktop/tkinter/pickbox.db')
#create cursor
c= conn.cursor()

# create table

c.execute("""CREATE TABLE shipments (
                shipid integer primary key,
                status text,
                deliveryTime text,
                lockerid integer,
                pickboxid integer,
                email text,
                storeid integer,
                storename text,
                phone integer
            )""") 

#insert initial info
c.execute("""INSERT INTO shipments VALUES (100001, 'Shipped', '2023-04-25, 11:00 AM', 1123, 1001, 'yaseer@gmail.com', 301, 'Guerlain', 966555411384),
                                        (100002, 'Picked Up', '2023-01-2, 12:34 PM', 1124, 1001, 'Jacob@hotmail.com', 302, 'Al-Nahdi', 966555411384),
                                        (100003, 'Cancelled', '2023-06-13, 8:20 AM', 1120, 1003, 'YousefXX@Yahoo.com', 304, 'Addidas',966580688210),
                                        (100004, 'Out For Delivery', '2023-09-3, 6:46 PM', 1122, 1001, 'Hegazi@gmail.com', 305, 'Puma', 966580688210),
                                        (100005, 'Out For Delivery', '2023-09-7, 6:20 PM', 1121, 1003, 'mohammed@gmail.com', 306, 'Coffee Mood', 966580688210),
                                        (100006, 'Picked Up', '2023-09-12, 7:02 PM', 1127, 1001, 'Based@gmail.com', 301, 'Guerlain', 966555411384),
                                        (100007, 'Picked Up', '2023-09-28, 9:09 AM', 1120, 1004, 'amjad26@gmail.com', 308, 'Tom Ford', 966507095266),
                                        (100008, 'Picked Up', '2023-09-28, 9:12 AM', 1121, 1004, 'amjad26@gmail.com', 309, 'iHerb', 966507095266),
                                        (100009, 'Picked Up', '2023-10-31, 9:12 AM', 1120, 1002, 'GordonsUncle@gmail.com', 309, 'iHerb', 966552495419),
                                        (100012, 'Picked Up', '2023-10-31, 9:15 AM', 1120, 1002, 'GordonsUncle@gmail.com', 310, 'SesamBakery', 966552495419),
                                        (100010, 'Shipped', '2023-12-1, 1:19 PM', 1122, 1002, 'GordonsUncle@gmail.com', 311, 'ArabiaOud', 966552495419),
                                        (100011, 'Picked Up', '2023-01-6, 1:19 PM', 1120, 1009, 'Yaseen1423@gmail.com', 312, 'Macdonalds', 966554587433)""")


conn.commit()
conn.close()

print("Created Database successfully")