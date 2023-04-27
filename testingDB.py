import sqlite3

# create DB
conn = sqlite3.connect('C:/Users/youse/Desktop/tkinter/pickbox.db')
#create cursor
c= conn.cursor()

# order = c.execute("""
#                 SELECT 
#                     shipment.shipment_id, 
#                     shipment.status, 
#                     shipment.deliveryTime,
#                     shipment_belongs_to.locker_id,
#                     locker.pickbox_id,
#                     online_store.store_name,
#                     unregistered_customer.phone
#                 FROM 
#                     shipment, 
#                     unregistered_customer,
#                     shipment_belongs_to,
#                     online_store,
#                     locker,
#                     pickbox
#                 WHERE 
#                     shipment.customer_id = unregistered_customer.customer_id AND
#                     shipment.shipment_id = shipment_belongs_to.shipment_id AND
#                     shipment_belongs_to.locker_id = locker.locker_id AND 
#                     shipment_belongs_to.store_id = online_store.store_id
#                 """)
# fetched= order.fetchall()
# print(fetched)




print("TESTS")
print('============================================================')

# order = c.execute("select * from online_store")
# fetched= order.fetchall()
# print(fetched)

# order = c.execute("select * from pickbox")
# fetched= order.fetchall()
# print(fetched)

# order = c.execute("select * from driver")
# fetched= order.fetchall()
# print(fetched)

# order = c.execute("select * from store_deliver_to")
# fetched= order.fetchall()
# print(fetched)

# order = c.execute("select * from locker")
# fetched= order.fetchall()
# print(fetched)

# order = c.execute("select * from unregistered_customer")
# fetched= order.fetchall()
# print(fetched)

# order = c.execute("select * from registered_customer")
# fetched= order.fetchall()
# print(fetched)

# order = c.execute("select * from shipment")
# fetched= order.fetchall()
# print(fetched)

# order = c.execute("select * from shipment_belongs_to")
# fetched= order.fetchall()
# print(fetched)

order = c.execute("select * from customerView")
fetched= order.fetchall()
print(fetched)

conn.close()