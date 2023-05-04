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

c.execute("""INSERT INTO store_deliver_to VALUES (101,20),
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
                                                (107,24)""") 

c.execute("""INSERT INTO locker VALUES (1004, 'Empty', 1743, 20),
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
                                        (1308, 'Empty', 2603, 23)""") 

c.execute("""INSERT INTO customer VALUES (1,'Mohammed Alhaddad', 966500010007, 'malhaddad@gmail.com'),
                                        (2,'Yousef Mishkhas', 966580688210, 'y3ou12@hotmail.com'),
                                        (3,'Hatem Alharbi', 966555411384, 'hatim999@Yahoo.com')""") 

c.execute("""INSERT INTO shipment VALUES (100001, 'Pending', '2023/05/10, 13:00', '2023/04/29, 11:00', 3),
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
                                        (100016, 'Ready For Collection', '2023/05/01, 14:20', '2023/05/01, 13:19', 2)""") 

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