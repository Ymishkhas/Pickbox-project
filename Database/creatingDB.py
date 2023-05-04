import sqlite3

DB_PATH = 'C:/Users/youse/Desktop/tkinter/Database/pickbox.db'

# create DB
conn = sqlite3.connect(DB_PATH)
#create cursor
c= conn.cursor()


# create tables
c.execute("""CREATE TABLE online_store (
                store_id integer,
                store_name text,
                Time_frame text,
                PRIMARY KEY (store_id)
            )""")

c.execute("""CREATE TABLE driver (
                driver_id integer,
                city text,
                region text,
                username text,
                password text,
                store_id integer,
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
                password integer,
                pickbox_id integer,
                PRIMARY KEY (locker_id),
                FOREIGN KEY (pickbox_id) REFERENCES pickbox(pickbox_id)
            )""")

c.execute("""CREATE TABLE customer (
                customer_id integer,
                customer_name text,
                phone integer,
                email text,
                PRIMARY KEY (customer_id)
            )""")

c.execute("""CREATE TABLE shipment (
                shipment_id integer,
                status text,
                deliveryTime text,
                latestUpdate text,
                customer_id integer,
                PRIMARY KEY (shipment_id)
                FOREIGN KEY (customer_id) REFERENCES customer(customer_id)
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
                    shipment.latestUpdate,
                    shipment.deliveryTime,
                    online_store.store_name, 
                    locker.pickbox_id,
                    shipment_belongs_to.locker_id,
                    customer.email,
                    customer.phone
                FROM 
                    shipment, 
                    shipment_belongs_to, 
                    online_store, 
                    locker, 
                    customer  
                WHERE 
                    shipment.shipment_id = shipment_belongs_to.shipment_id AND   
                    shipment.customer_id = customer.customer_id AND 
                    shipment_belongs_to.store_id = online_store.store_id AND 
                    shipment_belongs_to.locker_id = locker.locker_id
                """)


# #insert initial info
c.execute("""INSERT INTO online_store VALUES (101, 'Jarir', '01:12:00:00'),
                                            (102 , 'Al Nahdi', '00:06:00:00'),
                                            (103 , 'Addidas','01:00:00:00'),
                                            (104 , 'Saco', '01:00:00:00'),
                                            (105 , 'Coffee Mood', '02:00:00:00'),
                                            (106 , 'Namshi', '01:18:00:00'),
                                            (107 , 'iHerb', '00:8:30:00'),
                                            (108 , 'SesamBakery', '00:2:00:00'),
                                            (109 , 'ArabiaOud', '00:18:00:00')""") 

c.execute("""INSERT INTO driver VALUES (501, 'Jeddah', 'North Jeddah', 'Jarir_JDN@pickbox', 'Jarir', 101),
                                        (502, 'Jeddah', 'North Jeddah', 'Namshi_JDN@pickbox', 'namshi', 106),
                                        (503, 'Jeddah', 'North Jeddah', 'iHerb_JDN@pickbox', 'iherb', 107)""") 

c.execute("""INSERT INTO pickbox VALUES (20, 'Active', 'Jeddah', 'North Jeddah', 'Taiba', 'R42V+8J'),
                                        (21, 'Active', 'Jeddah', 'North Jeddah', 'Al Sawari', 'Q4W2+WC'),
                                        (22, 'Active', 'Jeddah', 'North Jeddah', 'Al Yaqoot', 'Q3JR+VQ'),
                                        (23, 'Active', 'Jeddah', 'North Jeddah', 'Al Zummard', 'Q3X6+82'),
                                        (24, 'Active', 'Jeddah', 'North Jeddah', 'Al Lulu', 'Q39C+XM'),
                                        (25, 'Down', 'Jeddah', 'North Jeddah', 'Al Firdous', 'Q4P9+FX')""") 

c.execute("""INSERT INTO store_deliver_to VALUES (107,20),
                                                (107,21),
                                                (107,22),
                                                (107,23),
                                                (107,24),
                                                (106,20),
                                                (106,21),
                                                (106,22),
                                                (106,23),
                                                (106,24),
                                                (101,20),
                                                (101,21),
                                                (101,22),
                                                (101,23),
                                                (101,24)""") 

c.execute("""INSERT INTO locker VALUES (1004, 'Empty', 1743, 20),
                                        (1005, 'Occupied', 5582, 20),
                                        (1006, 'Empty', 2783, 20),
                                        (1007, 'Empty', 7899, 20),
                                        (1130, 'Occupied', 7654, 21),
                                        (1131, 'Empty', 4522, 21),
                                        (1132, 'Occupied', 2456, 21),
                                        (1133, 'Occupied', 9369, 21),
                                        (1243, 'Occupied', 5448, 21),
                                        (1244, 'Empty', 5677, 22),
                                        (1245, 'Occupied', 1794, 22),
                                        (1246, 'Occupied', 1689, 22),
                                        (1305, 'Empty', 8495, 23),
                                        (1306, 'Occupied', 6685, 23),
                                        (1307, 'Empty', 5719, 23),
                                        (1308, 'Empty', 2603, 23)""") 

c.execute("""INSERT INTO customer VALUES (1,'Mohammed Alhaddad', 966500010007, 'malhaddad@gmail.com'),
                                        (2,'Yousef Mishkhas', 966580688210, 'y3ou12@hotmail.com'),
                                        (3,'Hatem Alharbi', 966555411384, 'hatim999@Yahoo.com')""") 

c.execute("""INSERT INTO shipment VALUES (100001, 'Pending', '2023/04/25, 13:00', '2023/04/24, 11:00', 3),
                                        (100002, 'Pending', '2023/09/03, 08:00', '2023/01/03, 12:34', 3),
                                        (100003, 'Out For Delivery', '2023/06/13, 10:00', '2023/06/13, 07:20', 3),
                                        (100004, 'Ready For Collection', '2023/09/03, 19:00', '2023/09/03, 18:46', 3),
                                        (100005, 'Ready For Collection', '2023/09/03, 21:30', '2023/09/07, 18:12', 3),
                                        (100006, 'Picked Up', '2023/09/12, 19:45', '2023/09/12, 20:02', 3),
                                        (100007, 'Pending', '2023/04/25, 13:00', '2023/04/25, 11:00', 1),
                                        (100008, 'Pending', '2023/09/03, 08:00', '2023/01/03, 12:34', 1),
                                        (100009, 'Out For Delivery', '2023/06/13, 10:00', '2023/06/13, 8:20', 1),
                                        (100010, 'Ready For Collection', '2023/09/03, 19:00', '2023/09/03, 18:46', 1),
                                        (100011, 'Ready For Collection', '2023/09/03, 21:30', '2023/09/07, 18:12', 1),
                                        (100012, 'Picked Up', '2023/09/12, 19:45', '2023/09/12, 19:50', 1),
                                        (100013, 'Pending', '2023/09/28, 21:30', '2023/09/27, 21:09', 2),
                                        (100014, 'Pending', '2023/09/28, 21:20', '2023/09/28, 21:12', 2),
                                        (100015, 'Out For Delivery', '2023/10/31, 21:15', '2023/10/31, 19:10', 3),
                                        (100016, 'Ready For Collection', '2023/12/01, 14:20', '2023/12/01, 13:19', 2)""") 

c.execute("""INSERT INTO shipment_belongs_to VALUES (100001,101, 1004),
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
                                                    (100016,106, 1245)""") 

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
