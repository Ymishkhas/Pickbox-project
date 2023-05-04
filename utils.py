import atexit
import sqlite3
from datetime import datetime

DB_PATH = 'C:/Users/youse/Desktop/tkinter/Database/pickbox.db'
conn = sqlite3.connect(DB_PATH)
c = conn.cursor()

# Main Functions
def is_valid_customer(phone):
    # Check the database for a customer record by his number
    record = c.execute("select * from customer where phone= ?", (phone,)).fetchall()

    return record != []

def get_shipment(shipment_id):
    # Get the shipment details from the database
    return c.execute("""SELECT shipment_id, 
                                status, 
                                latestUpdate,
                                deliveryTime,
                                store_name,
                                pickbox_id,
                                locker_id,
                                phone
                        FROM customerView WHERE shipment_id = ?""", (shipment_id,)).fetchall()

def get_shipments(phone):
    # Get the all shipment under a phone number from the database
    return c.execute("""SELECT shipment_id, 
                                status, 
                                latestUpdate,
                                deliveryTime,
                                store_name,
                                pickbox_id,
                                locker_id,
                                phone
                        FROM customerView WHERE phone = ?""", (phone,)).fetchall()

def cancel_shipment(shipment_id):
    # Update the shipment status to Cancelled, the latestUpdate to the moment date from the database
    c.execute("UPDATE shipment SET status = 'Cancelled', latestUpdate = ? WHERE shipment_id = ?", (getCurrentTime(), shipment_id,))
    conn.commit()

def update_locker(locker_id, shipment_id):
    # Update the locker_id in a shipment from the database
    c.execute("UPDATE shipment_belongs_to SET locker_id = ? WHERE shipment_id = ?",(locker_id, shipment_id))
    conn.commit()

def is_valid_driver(username,password):
    # Check the database for a driver account along with his correct password
    record =  c.execute("select * from driver where username = ? and password = ?", (username,password,)).fetchall()

    return record != []

def get_driver_store_info(username):
    # Get the driver's region and store name from the database
    return c.execute("select region, store_name from online_store, driver where driver.username = ? and driver.store_id = online_store.store_id", (username,)).fetchall()

def get_driver_orders(username):
    # Get the driver's orders from the database
    return c.execute("""SELECT 
                            customerView.shipment_id, 
                            customerView.status, 
                            customerView.deliveryTime, 
                            customerView.pickbox_id,
                            customerView.locker_id
                        FROM
                            customerView, 
                            driver, 
                            pickbox,
                            online_store
                        WHERE 
                            customerView.store_name = online_store.store_name AND
                            driver.store_id = online_store.store_id AND
                            pickbox.pickbox_id = customerView.pickbox_id AND
                            driver.username = ? AND
                            pickbox.region = driver.region;""", (username,)).fetchall()

def update_shipment_status(shipment_id, prev_status):
    # Update the status in a shipment for a new status got from the database and return the new status

    new_status = prev_status
    if prev_status == "Pending":
        new_status = "Out For Delivery"
    elif prev_status == "Out For Delivery":
        new_status = "Ready For Collection"
                
    c.execute("UPDATE shipment SET status = ?, latestUpdate = ? WHERE shipment_id = ?", (new_status, getCurrentTime(), shipment_id,))
    conn.commit()

    return new_status

# Helper Functions
def getCurrentTime():
    # Return a formatted string of the current date and time

    # datetime object containing current date and time
    now = datetime.now()

    formatted_string = now.strftime("%Y/%m/%d, %H:%M")
    
    return formatted_string

def compareOrderTime(str_d1, str_d2):
    # Compares the delivery time of 2 shipments and returns the difference in hours    

    # convert string to date object
    d1 = datetime.strptime(str_d1, "%Y/%m/%d, %H:%M")
    d2 = datetime.strptime(str_d2, "%Y/%m/%d, %H:%M")

    # Calculate the difference between the two datetimes in hours
    diff_hours = abs((d2 - d1).total_seconds() / 3600)
    
    return diff_hours

def restore_shipment_status_latest_update(shipment_id, prev_status, prev_latest_update):
    
    c.execute("UPDATE shipment SET status = ?, latestUpdate = ? WHERE shipment_id = ?", (prev_status, prev_latest_update, shipment_id,))
    conn.commit()

def restore_shipment_locker_id(shipment_id, prev_locker_id):
    
    c.execute("UPDATE shipment_belongs_to SET locker_id = ? WHERE shipment_id = ?",(prev_locker_id, shipment_id))
    conn.commit()

def cleanup():
    # code to run when the program is closing
    print("\nProgram is closing...DB files are saving and closing")
    conn.commit()
    conn.close()

atexit.register(cleanup)