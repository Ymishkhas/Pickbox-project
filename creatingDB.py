import sqlite3

# create DB
conn = sqlite3.connect('C:/Users/youse/Desktop/tkinter/pickbox.db')
#create cursor
c= conn.cursor()

# create tables
c.execute("""CREATE TABLE online_store (
                store_id integer,
                store_name text,
                Time_frame text,
                username text,
                password text,
                PRIMARY KEY (store_id)
            )""")

c.execute("""CREATE TABLE driver (
                driver_id integer,
                city text,
                region text,
                username text,
                password text,
                store_id text,
                PRIMARY KEY (driver_id),
                FOREIGN KEY (store_id) REFERENCES online_store(store_id)
            )""")

c.execute("""CREATE TABLE pickbox (
                pickbox_id integer,
                status text,
                city text,
                region text,
                distrect text,
                plus_code text,
                PRIMARY KEY (pickbox_id)
            )""")

c.execute("""CREATE TABLE store_deliver_to (
                store_id integer,
                pickbox_id integer,
                PRIMARY KEY (store_id, pickbox_id)
            )""")

c.execute("""CREATE TABLE locker (
                locker_id integer,
                status text,
                type text,
                pickbox_id integer,
                PRIMARY KEY (locker_id),
                FOREIGN KEY (pickbox_id) REFERENCES pickbox(pickbox_id)
            )""")

c.execute("""CREATE TABLE unregistered_customer (
                customer_id integer,
                phone integer,
                PRIMARY KEY (customer_id)
            )""")

c.execute("""CREATE TABLE registered_customer (
                customer_id integer,
                first_name text,
                minit text,
                last_name text,
                email text,
                username text,
                password text,
                PRIMARY KEY (customer_id)
                FOREIGN KEY (customer_id) REFERENCES unregistered_customer(customer_id)
            )""")

c.execute("""CREATE TABLE shipment (
                shipment_id integer,
                status text,
                orderTime text,
                deliveryTime text,
                customer_id integer,
                PRIMARY KEY (shipment_id)
                FOREIGN KEY (customer_id) REFERENCES unregistered_customer(customer_id)
            )""")

c.execute("""CREATE TABLE shipment_belongs_to (
                shipment_id integer,
                store_id integer,
                locker_id integer,
                PRIMARY KEY (shipment_id)
                FOREIGN KEY (shipment_id) REFERENCES shipment(shipment_id)
                FOREIGN KEY (store_id) REFERENCES online_store(store_id)
                FOREIGN KEY (locker_id) REFERENCES locker(locker_id)
            )""")


# create views
c.execute("""CREATE VIEW customerView AS
                SELECT 
                    shipment.shipment_id, 
                    shipment.status, 
                    shipment.deliveryTime,
                    shipment_belongs_to.locker_id, 
                    locker.pickbox_id, 
                    online_store.store_name, 
                    unregistered_customer.phone
                FROM 
                    shipment, 
                    shipment_belongs_to, 
                    online_store, 
                    locker, 
                    unregistered_customer  
                WHERE 
                    shipment.shipment_id = shipment_belongs_to.shipment_id AND   
                    shipment.customer_id = unregistered_customer.customer_id AND 
                    shipment_belongs_to.store_id = online_store.store_id AND 
                    shipment_belongs_to.locker_id = locker.locker_id
                """)


# #insert initial info
c.execute("""INSERT INTO online_store VALUES (101, 'Guerlain', '01:12:00:00', 'Guerlain@pickbox', '###'),
                                            (102 , 'Al-Nahdi', '00:06:00:00', 'Al-Nahdi@pickbox', '###'),
                                            (103 , 'Addidas','01:00:00:00', 'Addidas@pickbox', '###'),
                                            (104 , 'Puma', '01:00:00:00', 'Puma@pickbox', '###'),
                                            (105 , 'Coffee Mood', '02:00:00:00', 'Coffee_Mood@pickbox', '###'),
                                            (106 , 'Tom Ford', '01:18:00:00', 'Tom_Ford@pickbox', '###'),
                                            (107 , 'iHerb', '00:8:30:00', 'iHerb@pickbox', '###'),
                                            (108 , 'SesamBakery', '00:2:00:00', 'SesamBakery@pickbox', '###'),
                                            (109 , 'ArabiaOud', '00:18:00:00', 'ArabiaOud@pickbox', '###')""") 

c.execute("""INSERT INTO driver VALUES (501, 'Jeddah', 'South Jeddah', 'iHerb_South_Jeddah@pickbox', '###', 107),
                                        (502, 'Jeddah', 'North Jeddah', 'iHerb_North_Jeddah@pickbox', '###', 107),
                                        (503, 'Jeddah', 'East Jeddah', 'iHerb_East_Jeddah@pickbox', '###', 107),
                                        (504, 'Jeddah', 'West Jeddah', 'iHerb_West_Jeddah@pickbox', '###', 107),
                                        (505, 'Jeddah', 'Middle Jeddah', 'iHerb_Middle_Jeddah@pickbox', '###', 107)""") 

c.execute("""INSERT INTO pickbox VALUES (20, 'Active', 'Jeddah', 'North Jeddah', 'Taiba', 'R42V+8J'),
                                        (21, 'Active', 'Jeddah', 'North Jeddah', 'Al Sawari', 'Q4W2+WC'),
                                        (22, 'Active', 'Jeddah', 'North Jeddah', 'Al Yaqoot', 'Q3JR+VQ'),
                                        (23, 'Active', 'Jeddah', 'North Jeddah', 'Al Zummard', 'Q3X6+82'),
                                        (24, 'Active', 'Jeddah', 'North Jeddah', 'Al Lulu', 'Q39C+XM'),
                                        (25, 'Down', 'Jeddah', 'North Jeddah', 'Al Firdous', 'Q4P9+FX')""") 

c.execute("""INSERT INTO store_deliver_to VALUES (107,20),
                                                (107,21),
                                                (107,22),
                                                (107,25)""") 

c.execute("""INSERT INTO locker VALUES (1130, 'Empty', 'A', 22),
                                        (1131, 'Empty', 'A', 22),
                                        (1132, 'Occupied', 'A', 22),
                                        (1004, 'Occupied', 'B', 25),
                                        (1005, 'Occupied', 'B', 25),
                                        (1006, 'Occupied', 'B', 23),
                                        (1205, 'Occupied', 'A', 23),
                                        (1206, 'Occupied', 'A', 23),
                                        (1207, 'Empty', 'A', 23)""") 

c.execute("""INSERT INTO unregistered_customer VALUES (1,966555411384),
                                                    (2,966580688210),
                                                    (3,966507095266),
                                                    (4,966552495419),
                                                    (5,966554587433)""") 

c.execute("""INSERT INTO registered_customer VALUES (1,'yaseer', 'Ashraf', 'Alharbi', 'yaseer@gmail.com', 'yaseerAshraf' ,'###'),
                                                    (2,'Jacob', 'Hassan', 'Qiza', 'Jacob@hotmail.com', 'Jacob12' ,'###'),
                                                    (3,'Yousef', 'Ahmad', 'Sumaydee', 'YousefXX@Yahoo.com', 'YousefXX' ,'###'),
                                                    (4,'Gordon', 'Peter', 'Griffen', 'GordonsUncle@gmail.com', 'GordonsUncle' ,'###'),
                                                    (5,'amjad', 'Ali', 'Mubarak', 'amjad26@gmail.com', 'amjad26' ,'###')""") 

c.execute("""INSERT INTO shipment VALUES (100001, 'Shipped', '2023-04-25, 01:00 PM', '2023-04-25, 11:00 AM', 1),
                                        (100002, 'Picked Up', '2023-01-02, 01:00 PM', '2023-01-02, 12:34 PM', 1),
                                        (100003, 'Picked Up', '2023-06-13, 10:00 AM', '2023-06-13, 8:20 AM', 2),
                                        (100004, 'Cancelled', '2023-09-3, 7:00 PM', '2023-09-3, 6:46 PM', 2),
                                        (100005, 'Out For Delivery', '2023-09-7, 6:30 PM', null, 3),
                                        (100006, 'Picked Up', '2023-09-12, 7:45 PM', '2023-09-12, 7:02 PM', 4),
                                        (100007, 'Picked Up', '2023-09-28, 9:30 AM', '2023-09-28, 9:09 AM', 5),
                                        (100008, 'Picked Up', '2023-09-28, 9:20 AM', '2023-09-28, 9:12 AM', 1),
                                        (100009, 'Out For Delivery', '2023-10-31, 9:15 AM', null, 5),
                                        (100010, 'Shipped', '2023-12-1, 2:20 PM', '2023-12-1, 1:19 PM', 5),
                                        (100011, 'Shipped', '2023-01-6, 3:00 PM', '2023-01-6, 1:19 PM', 3)""") 

c.execute("""INSERT INTO shipment_belongs_to VALUES (100001,101, 1130),
                                                    (100002,105, 1004),
                                                    (100003,102, 1205),
                                                    (100004,103, 1005),
                                                    (100005,107, 1006),
                                                    (100006,106, 1206),
                                                    (100007,109, 1132),
                                                    (100008,109, 1133),
                                                    (100009,107, 1207),
                                                    (100010,107, 1130),
                                                    (100011,101, 1132)""") 

conn.commit()
conn.close()

print("Created Database successfully")















# c.execute("""CREATE TABLE shipments (
#                 shipid integer primary key,
#                 status text,
#                 deliveryTime text,
#                 lockerid integer,
#                 pickboxid integer,
#                 email text,
#                 storeid integer,
#                 storename text,
#                 phone integer
#             )""") 

# #insert initial info
# c.execute("""INSERT INTO shipments VALUES (100001, 'Shipped', '2023-04-25, 11:00 AM', 1123, 1001, 'yaseer@gmail.com', 301, 'Guerlain', 966555411384),
#                                         (100002, 'Picked Up', '2023-01-2, 12:34 PM', 1124, 1001, 'Jacob@hotmail.com', 302, 'Al-Nahdi', 966555411384),
#                                         (100003, 'Cancelled', '2023-06-13, 8:20 AM', 1120, 1003, 'YousefXX@Yahoo.com', 304, 'Addidas',966580688210),
#                                         (100004, 'Out For Delivery', '2023-09-3, 6:46 PM', 1122, 1001, 'Hegazi@gmail.com', 305, 'Puma', 966580688210),
#                                         (100005, 'Out For Delivery', '2023-09-7, 6:20 PM', 1121, 1003, 'mohammed@gmail.com', 306, 'Coffee Mood', 966580688210),
#                                         (100006, 'Picked Up', '2023-09-12, 7:02 PM', 1127, 1001, 'Based@gmail.com', 301, 'Guerlain', 966555411384),
#                                         (100007, 'Picked Up', '2023-09-28, 9:09 AM', 1120, 1004, 'amjad26@gmail.com', 308, 'Tom Ford', 966507095266),
#                                         (100008, 'Picked Up', '2023-09-28, 9:12 AM', 1121, 1004, 'amjad26@gmail.com', 309, 'iHerb', 966507095266),
#                                         (100009, 'Picked Up', '2023-10-31, 9:12 AM', 1120, 1002, 'GordonsUncle@gmail.com', 309, 'iHerb', 966552495419),
#                                         (100012, 'Picked Up', '2023-10-31, 9:15 AM', 1120, 1002, 'GordonsUncle@gmail.com', 310, 'SesamBakery', 966552495419),
#                                         (100010, 'Shipped', '2023-12-1, 1:19 PM', 1122, 1002, 'GordonsUncle@gmail.com', 311, 'ArabiaOud', 966552495419),
#                                         (100011, 'Picked Up', '2023-01-6, 1:19 PM', 1120, 1009, 'Yaseen1423@gmail.com', 312, 'Macdonalds', 966554587433)""") 
