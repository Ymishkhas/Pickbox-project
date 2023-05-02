import random
import tkinter as tk
from tkinter import ttk
import tkinter
from tkinter import messagebox
from tkinter import *
import customtkinter
import sqlite3
import os
import re
from datetime import datetime
import tkinter.ttk as ttk
import atexit

# GLOBAL VARIABLES
DB_PATH = 'C:/Users/youse/Desktop/tkinter/pickbox.db'
generatedPIN = 0
generatedPIN_phone = 0

conn = sqlite3.connect(DB_PATH)
c = conn.cursor()

def cleanup():
    # code to run when the program is closing
    print("Program is closing...DB files are saving and closing")
    conn.commit()
    conn.close()

atexit.register(cleanup)

def merge_selected_orders(treeview):
    """merge the selected orders from the database"""
    
    # Get the selected orders (not the ones with status Picked Up or Cancelled)
    valid_shipments = []
    selected_shipments = treeview.selection()
    for item in selected_shipments:

        values = treeview.item(item, "values")
        
        if values[2] == "Picked Up" or values[2] == "Cancelled":
            messagebox.showerror("Error", f"Shipment {values[1]} is {values[2]} and cannot be merged.")
        else:
            valid_shipments.append(values)

        if values[2] == "Ready For Collection":
            locker_id = values[4]
    
    # Check that there are at least two orders selected
    if len(valid_shipments) < 2:
        messagebox.showerror("Error", "You must select at least two valid shipments to merge.")
        return
    
    # Check that all selected orders have the same pickbox ID
    pickbox_ids = set([shipment[5] for shipment in valid_shipments])
    if len(pickbox_ids) > 1:
        messagebox.showerror("Error", "shipments are in different pickboxs and cannot be merged.")
        return
    pickbox_ids = pickbox_ids.pop()

    # Check that all selected orders have the same locker ID (Already merged)
    locker_ids = set([shipment[4] for shipment in valid_shipments])
    if len(locker_ids) == 1:
        messagebox.showerror("Error", "shipments already merged.")
        return
    locker_ids = locker_ids.pop()

    # # Check that the time difference between the selected orders is not greater than 12 hours
    # start_date = valid_shipments[0][3]
    # end_date = valid_shipments[-1][3]
    # diff_hours = compareOrderTime(start_date, end_date)
    # if diff_hours > 12:
    #     messagebox.showerror("Error", "The time difference of orderTime between the selected orders is greater than 12 hours and cannot be merged.")
    #     return
    
    # if no shipment was already in a locker, pick a locker to merge orders at
    if 'locker_id' not in locals():
        locker_id = valid_shipments[0][4]

    # Update the database to merge the selected orders
    for order in valid_shipments:
        c.execute("UPDATE shipment_belongs_to SET locker_id = ? WHERE shipment_id = ?",(locker_id, order[1],))

    
    # Show a success message and refresh the order display
    messagebox.showinfo("Success", "Orders merged successfully.")
    
    phone = valid_shipments[0][8]
    refresh_orders(treeview, phone)

def cancel_order(shipment_id):
    """cancel the order from the database."""

    # Update the neccessary values for order to be cancelled
    c.execute("UPDATE shipment SET status = 'Cancelled', deliveryTime = ? WHERE shipment_id = ?", (getCurrentTime(), shipment_id,))
    

    # Dispaly Success msg for customer
    messagebox.showinfo("Success", f"Shipment {shipment_id} has been cancelled.")

def cancel_selected_orders(treeview):
    """cancel the selected orders from the database"""
    
    selected_items = treeview.selection()
    for item in selected_items:

        status = treeview.item(item, "values")[2]
        shipment_id = treeview.item(item, "values")[1]
        phone = treeview.item(item, "values")[8]
        
        if status == "Not Yet Dispatched":
            cancel_order(shipment_id)
        else:
            messagebox.showinfo("Failure", f"Shipment {shipment_id} already {status} and cannot be cancelled.")
        
        # treeview.delete(item)
    refresh_orders(treeview, phone)
        

#This method recieves a number and searches the DB for matching rows using a query with a condition of matching the number
#Basically display all orders that have the same phone number

def show_orders(Pnum, phone_number_frame, pin):

    global generatedPIN
    global generatedPIN_phone

    pin = pin.get()
    phone = Pnum.get()

    if str(generatedPIN) != pin or str(generatedPIN_phone) != phone:
        messagebox.showerror("Error", "Wrong PIN number, try sending a new PIN number")

    else:

        # Connect to database
        # conn = sqlite3.connect(DB_PATH)
        # c = conn.cursor()
        # Get orders from database for the entered phone number
        number = Pnum.get()
        
        orders = c.execute("SELECT * FROM customerView WHERE phone = ?", (phone,)).fetchall()
        
        
        # Close the database connection
        # conn.commit()
        # conn.close()

        # Clear the existing frame, if any
        for widget in phone_number_frame.winfo_children():
            widget.destroy()

        # Create a frame to show the orders
        orders_frame = tk.Frame(phone_number_frame)
        orders_frame.pack()

        # Create a treeview to show the orders
        treeview = ttk.Treeview(orders_frame)
        treeview.pack()

        # Set up the columns of the treeview
          # Set up the columns of the treeview
        # Set up the columns of the treeview
        treeview["columns"] = ("select", "shipment_id", "status", "delivery_time", "locker_id", "pickboxid", "email", "storename", "phone")
        treeview.column("#0", width=0, stretch=tk.NO)
        treeview.column("select", anchor=tk.CENTER, width=50)
        treeview.column("shipment_id", anchor=tk.CENTER, width=50)
        treeview.column("status", anchor=tk.CENTER, width=80)
        treeview.column("delivery_time", anchor=tk.CENTER, width=100)
        treeview.column("locker_id", anchor=tk.CENTER, width=40)
        treeview.column("pickboxid", anchor=tk.CENTER, width=40)
        treeview.column("email", anchor=tk.CENTER, width=120)
        treeview.column("storename", anchor=tk.CENTER, width=70)
        treeview.column("phone", anchor=tk.CENTER, width=80)
        # Set up the headings of the columns
        treeview.heading("#0", text="", anchor=tk.W)
        treeview.heading("select", text="", anchor=tk.CENTER)
        treeview.heading("shipment_id", text="Shipment ID", anchor=tk.CENTER)
        treeview.heading("status", text="Status", anchor=tk.CENTER)
        treeview.heading("delivery_time", text="Delivery Time", anchor=tk.CENTER)
        treeview.heading("locker_id", text="Locker ID", anchor=tk.CENTER)
        treeview.heading("pickboxid", text="PickBox ID", anchor=tk.CENTER)
        treeview.heading("email", text="Email", anchor=tk.CENTER)
        treeview.heading("storename", text="Store Name", anchor=tk.CENTER)
        treeview.heading("phone", text="Phone Number", anchor=tk.CENTER)

        # Insert the orders into the treeview
        row_count = 0
        for oneorder in orders:
            treeview.insert("", row_count, text="", values=(False, *oneorder))
            row_count += 1
        # Delete selected orders when the delete button is clicked
        delete_button = customtkinter.CTkButton(phone_number_frame, text="Cancel Selected Orders", command=lambda: cancel_selected_orders(treeview))
        delete_button.pack()
        delete_button.place(relx= 0.25, rely= 0.6)        

        merge_button = customtkinter.CTkButton(phone_number_frame, text="Merge Orders", command=lambda: merge_selected_orders(treeview))
        merge_button.pack()
        merge_button.place(relx= 0.55, rely= 0.6)    

        back_button = customtkinter.CTkButton(phone_number_frame, text="Back to Main Page", command=phone_number_frame.destroy)
        back_button.pack()
        back_button.place(relx=0.5, rely=0.8, anchor=tkinter.CENTER)
            

def refresh_orders(treeview, phone):

    # Connect to database
    # conn = sqlite3.connect(DB_PATH)
    # c = conn.cursor()
        
    # Get orders from database for the entered phone number
    orders = c.execute("SELECT * FROM customerView WHERE phone = ?", (phone,)).fetchall()
    
    # Close the database connection
    # conn.commit()
    # conn.close()

    # Clear the existing treeview
    treeview.delete(*treeview.get_children())

    # Insert the latest orders into the treeview
    row_count = 0
    for oneorder in orders:
        treeview.insert("", row_count, text="", values=(False, *oneorder))
        row_count += 1


def phone_number_page():
    # Create phone number page
    # Create shipment id page
    phone_number_frame = customtkinter.CTkFrame(root)
    phone_number_frame.pack(fill="both", expand=True)

    
    # phone_number_frame.title("Phone Number Page")
    # phone_number_frame.resizable(False, False)

    # create textboxes
    enter = customtkinter.CTkLabel(phone_number_frame, text="Enter your phone number to show all your orders ", font=("Arial", 16))
    enter.pack()
    enter.place(relx=0.5, rely=0.2, anchor=tkinter.CENTER)

    

    def validate_phone_number(new_value):
        return new_value.isdigit() or new_value == ""

    Pnum = customtkinter.CTkEntry(master=phone_number_frame, placeholder_text="966", width=220, validate="key", validatecommand=(phone_number_frame.register(validate_phone_number), "%P"))
    
    Pnum.pack()
    Pnum.place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)

 
    #create Send pin button
    checkButton=  customtkinter.CTkButton(phone_number_frame, text= "Send PIN", command=lambda: generatePIN(Pnum))
    checkButton.pack()
    checkButton.place(relx=0.8, rely=0.3, anchor=tkinter.CENTER)

    #Check PIN entry
    pin = customtkinter.CTkEntry(master=phone_number_frame, width=220, placeholder_text="PIN",)
    pin.pack()
    pin.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)


    
    #Show order invokation
    show = customtkinter.CTkButton(phone_number_frame, text="Show Orders", command=lambda: show_orders(Pnum, phone_number_frame,pin))
    show.pack()
    show.place(relx=0.5, rely=0.6, anchor=tkinter.CENTER)


    #


    
    def refresh():
        phone_number_frame.destroy()
        phone_number_page()

    refresh_button = customtkinter.CTkButton(phone_number_frame, text="Refresh", command=refresh)
    refresh_button.pack()
    refresh_button.place(relx=0.9, rely=0.05, anchor=tkinter.CENTER)

    back_button = customtkinter.CTkButton(phone_number_frame, text="Back to Main Page", command=phone_number_frame.destroy)
    back_button.pack()
    back_button.place(relx=0.5, rely=0.8, anchor=tkinter.CENTER)

    phone_number_frame.mainloop()

def generatePIN(phone):
    
    global generatedPIN
    global generatedPIN_phone

    # conn = sqlite3.connect(DB_PATH)
    # c = conn.cursor()
    #
    result = c.execute("select * from customer where phone= ?", (phone.get(),)).fetchall()
  
    if result != []:
        generatedPIN = random.randint(1000,9999)
        print("PIN:", generatedPIN)
        generatedPIN_phone = phone.get()
        
    else:
        messagebox.showerror("Error", "No such registred phone with that number in our system, double check your entered phone number")

def refresh_order(treeview, shipment_id):
        
    # Get orders from database for the entered phone number
    order = c.execute("SELECT * FROM customerView WHERE shipment_id = ?", (shipment_id,)).fetchall()
    
    # Close the database connection
    # conn.commit()
    # conn.close()

    # Clear the existing treeview
    treeview.delete(*treeview.get_children())

    # Insert the latest orders into the treeview
    row_count = 0
    for oneorder in order:
        treeview.insert("", row_count, text="", values=(False, *oneorder))
        row_count += 1


# creating connection from "show order" button in shipme
def show_order(shipID, shipment_id_frame):
    
    #connect to DB
    shipment_id = shipID.get()

    order = c.execute("SELECT * FROM customerView WHERE shipment_id = ?", (shipment_id,)).fetchall()

    print(order)

    #commit changes/save them

    if not order:
        # No order found for the given shipment ID
        messagebox.showinfo("Error", f"Shipment {shipment_id} dose not exist.")
        return None

    for widget in shipment_id_frame.winfo_children():
        widget.destroy()

    # Create a frame to show the orders
    order_frame = tk.Frame(shipment_id_frame)
    order_frame.pack()

    # Create a treeview to show the orders
    treeview = ttk.Treeview(order_frame)
    treeview.pack()

    treeview["columns"] = ("shipment_id", "status", "delivery_time", "locker_id", "pickboxid", "email","storename","phone")
    treeview.column("#0", width=0, stretch=tk.NO)
    treeview.column("shipment_id", anchor=tk.CENTER, width=60)
    treeview.column("status", anchor=tk.CENTER, width=80)
    treeview.column("delivery_time", anchor=tk.CENTER, width=100)
    treeview.column("locker_id", anchor=tk.CENTER, width=40)
    treeview.column("pickboxid", anchor=tk.CENTER, width=40)
    treeview.column("email", anchor=tk.CENTER, width=120)
    treeview.column("storename", anchor=tk.CENTER, width=100)
    treeview.column("phone", anchor=tk.CENTER, width=100)
    # Set up the headings of the columns
    treeview.heading("#0", text="", anchor=tk.W)
    treeview.heading("shipment_id", text="Shipment ID", anchor=tk.CENTER)
    treeview.heading("status", text="Status", anchor=tk.CENTER)
    treeview.heading("delivery_time", text="Delivery Time", anchor=tk.CENTER)
    treeview.heading("locker_id", text="Locker ID", anchor=tk.CENTER)
    treeview.heading("pickboxid", text="PickBox ID", anchor=tk.CENTER)
    treeview.heading("email", text="Email", anchor=tk.CENTER)
    treeview.heading("storename", text="Store Name", anchor=tk.CENTER)
    treeview.heading("phone", text="Phone Number", anchor=tk.CENTER)   

    row_count = 0
    for oneorder in order:
        treeview.insert("", row_count, text="", values=oneorder)
        row_count += 1

    status = order[0][1]
    if status == "Not Yet Dispatched":
        # Delete selected orders when the delete button is clicked
        delete_button = customtkinter.CTkButton(shipment_id_frame, text="Cancel Order", command=lambda: (cancel_order(shipment_id), shipment_id_frame.destroy()))
        delete_button.pack()
        delete_button.place(relx= 0.4, rely= 0.65)  

    back_button = customtkinter.CTkButton(shipment_id_frame, text="Back to Main Page", command=shipment_id_frame.destroy)
    back_button.pack()
    back_button.place(relx=0.5, rely=0.8, anchor=tkinter.CENTER)
    
    # delete_button = customtkinter.CTkButton(shipment_id_root, text="Delete Selected Orders", command=lambda: delete_selected_orders(treeview))
    # delete_button.pack()
    # delete_button.place(relx= 0.25, rely= 0.6) 


def shipment_id_page():
    # Create shipment id page
    shipment_id_frame = customtkinter.CTkFrame(root)
    shipment_id_frame.pack(fill="both", expand=True)

    # create textboxes
    enter = customtkinter.CTkLabel(shipment_id_frame, text="Enter your Shipment ID to show your shipment status ", font=("Arial", 16))
    enter.pack()
    enter.place(relx=0.5, rely=0.2, anchor=tkinter.CENTER)

    def validate_shipment_id(new_value):
        return new_value.isdigit() or new_value == ""

    shipID = customtkinter.CTkEntry(master=shipment_id_frame, width=220, placeholder_text="", validate="key", validatecommand=(shipment_id_frame.register(validate_shipment_id), "%P"))
    shipID.pack()
    shipID.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    show = customtkinter.CTkButton(shipment_id_frame, text="Show Order", command=lambda:show_order(shipID, shipment_id_frame))
    show.pack()
    show.place(relx=0.8, rely=0.5, anchor=tkinter.CENTER)

    def refresh():
        shipment_id_frame.destroy()
        shipment_id_page()

    refresh_button = customtkinter.CTkButton(shipment_id_frame, text="Refresh", command=refresh)
    refresh_button.pack()
    refresh_button.place(relx=0.9, rely=0.2, anchor=tkinter.CENTER)

    back_button = customtkinter.CTkButton(shipment_id_frame, text="Back to Main Page", command=shipment_id_frame.destroy)
    back_button.pack()
    back_button.place(relx=0.5, rely=0.8, anchor=tkinter.CENTER)

    shipment_id_frame.mainloop()







# Create root window
root = customtkinter.CTk()
root.geometry("700x400")
root.title("Modern Login")
root.resizable(False,False)



# First login page widgets
welcome_label = customtkinter.CTkLabel(root, text="Welcome to Pick Box!", font=("Arial", 24))
welcome_label.pack()
welcome_label.place(relx=0.5, rely=0.2, anchor=tkinter.CENTER)

choose_label = customtkinter.CTkLabel(root, text="Choose what suits you", font=("Arial", 16))
choose_label.pack()
choose_label.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)

phone_button = customtkinter.CTkButton(root, text="Phone Number", command=phone_number_page)
phone_button.pack()
phone_button.place(relx=0.385, rely=0.5, anchor=tkinter.CENTER)

shipment_button = customtkinter.CTkButton(root, text="Shipment ID", command=shipment_id_page)
shipment_button.pack()
shipment_button.place(relx=0.65, rely=0.5, anchor=tkinter.CENTER)



# Create a function to handle the Driver login button click
def Driverlogin():

    # Save the username and password entries
    username = username_entry.get()
    password = password_entry.get()

    # Check username and password in the DB
    result = c.execute("select * from driver where username = ? and password = ?", (username,password,)).fetchall()
    if result == []:
        messagebox.showerror("Error", "the entered username/password is incorrect.")
        return
                
    # Hide the second login frame
    second_login_frame.pack_forget()

    # Create a new page
    order_page_frame = customtkinter.CTkFrame(root)
    order_page_frame.pack(fill="both", expand=True)

    # Create a label to display the driver
    driver_info = c.execute("select region, store_name from online_store, driver where driver.username = ? and driver.store_id = online_store.store_id", (username,)).fetchall()
    driver_label = customtkinter.CTkLabel(order_page_frame, text=f"Welcome {driver_info[0][0]} of {driver_info[0][1]}", font=("Arial", 18))
    driver_label.pack(side=tkinter.TOP, pady=10)

    orders = c.execute("""SELECT 
                            customerView.shipment_id, 
                            customerView.status, 
                            customerView.deliveryTime, 
                            customerView.locker_id, 
                            customerView.pickbox_id
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

    # Create a treeview to show the orders
    treeview = ttk.Treeview(order_page_frame)
    treeview.pack()

    # Set up the columns of the treeview
    treeview["columns"] = ("select", "shipment_id", "status", "delivery_time", "locker_id", "pickboxid")
    treeview.column("#0", width=0, stretch=tk.NO)
    treeview.column("select", anchor=tk.CENTER, width=0)
    treeview.column("shipment_id", anchor=tk.CENTER, width=80)
    treeview.column("status", anchor=tk.CENTER, width=120)
    treeview.column("delivery_time", anchor=tk.CENTER, width=120)
    treeview.column("locker_id", anchor=tk.CENTER, width=90)
    treeview.column("pickboxid", anchor=tk.CENTER, width=90)

    # Set up the headings of the columns
    treeview.heading("#0", text="", anchor=tk.W)
    treeview.heading("select", text="", anchor=tk.CENTER)
    treeview.heading("shipment_id", text="Shipment ID", anchor=tk.CENTER)
    treeview.heading("status", text="Status", anchor=tk.CENTER)
    treeview.heading("delivery_time", text="Delivery Time", anchor=tk.CENTER)
    treeview.heading("locker_id", text="Locker ID", anchor=tk.CENTER)
    treeview.heading("pickboxid", text="PickBox ID", anchor=tk.CENTER)

    row_count = 0
    for oneorder in orders:
        treeview.insert("", row_count, text="", values=("", *oneorder))
        row_count += 1

    def update_status(shipment_id, prev_status):
    # Update the status of the shipment in the database based on its previous status
        
        new_status = prev_status
        if prev_status == "Not Yet Dispatched":
            new_status = "Out For Delivery"
        elif prev_status == "Out For Delivery":
            new_status = "Ready For Collection"
            
        c.execute("UPDATE shipment SET status = ? WHERE shipment_id = ?", (new_status, shipment_id,))
        messagebox.showinfo("Success", f"Shipment {shipment_id} has been updated to {new_status}.")

    def update_selected_shipments():
        # Get the selected items from the treeview
        selected_items = treeview.selection()

        # Update the status of each selected shipment
        for item in selected_items:
            # Get the shipment ID and previous status from the item dictionary
            shipment_id = treeview.item(item, "values")[1]
            prev_status = treeview.item(item, "values")[2]

            if prev_status != "Not Yet Dispatched" and prev_status != "Out For Delivery":
                messagebox.showerror("Error", f"You cannot update a {prev_status} shipment")
            else:
                # Update the status of the shipment
                update_status(shipment_id, prev_status)

        order_page_frame.pack_forget()
        Driverlogin()

        # # Refresh the treeview to show the updated status
        # refresh_treeview()

    # Create a button to update the status of selected shipments
    update_button = customtkinter.CTkButton(order_page_frame, text="Update Selected Shipments", fg_color="red", hover_color="dark red", command=update_selected_shipments)
    update_button.pack()
    update_button.place(relx=0.5, rely=0.8, anchor=tkinter.CENTER)

    

    # Create a button to go back to the second login page
    back_button = customtkinter.CTkButton(order_page_frame, text="Go Back", fg_color="red", hover_color="dark red", command=lambda: order_page_frame.pack_forget())
    back_button.pack()
    back_button.place(relx=0.5, rely=0.9, anchor=tkinter.CENTER)

# Second login page widgets
second_login_frame = customtkinter.CTkFrame(root)
second_login_frame.pack(fill="both", expand=True)

second_login_label = customtkinter.CTkLabel(second_login_frame, text="Welcome to Pick Box!", font=("Arial", 24))
second_login_label.pack()
second_login_label.place(relx=0.5, rely=0.2, anchor=tkinter.CENTER)

 # create textboxes
msg_label = customtkinter.CTkLabel(second_login_frame, text="Enter your username and password to show all your orders", font=("Arial", 16))
msg_label.pack()
msg_label.place(relx=0.5, rely=0.35, anchor=tkinter.CENTER)

# second_login_button = customtkinter.CTkButton(second_login_frame, text="Go Back", command=lambda: second_login_frame.pack_forget())
# second_login_button.pack()
# second_login_button.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

# Username entry box
username_entry = customtkinter.CTkEntry(second_login_frame, width=220, placeholder_text="Username")
username_entry.pack()
username_entry.place(relx=0.5, rely=0.45, anchor=tkinter.CENTER)

# Password entry box
password_entry = customtkinter.CTkEntry(second_login_frame, width=220, placeholder_text="Password", show="*")
password_entry.pack()
password_entry.place(relx=0.5, rely=0.55, anchor=tkinter.CENTER)

# Login button
login_button = customtkinter.CTkButton(second_login_frame, text="Log In", fg_color="red", hover_color="dark red", command=Driverlogin)
login_button.pack()
login_button.place(relx=0.5, rely=0.65, anchor=tkinter.CENTER)
# login_button.config(command=lambda: login_success(username_entry.get(), password_entry.get()))
second_login_frame.pack_forget()


# # Add a red button to the second login page
# red_button = customtkinter.CTkButton(second_login_frame, text="Red Button", fg_color="red", hover_color="#8B0000")
# red_button.pack()
# red_button.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

# Toggle button to switch between login pages
toggle_button = customtkinter.CTkButton(root, text=">", font=("Arial", 12), width=2, height=50,
                                        command=lambda: second_login_frame.pack(side="right", fill="both", expand=True) if second_login_frame.winfo_ismapped() == 0 else second_login_frame.pack_forget())
toggle_button.pack()
toggle_button.place(relx=0.99, rely=0.01, anchor=tkinter.NE)



def getCurrentTime():

    # datetime object containing current date and time
    now = datetime.now()

    formatted_string = now.strftime("%Y/%m/%d, %H:%M")
    
    return formatted_string


def compareOrderTime(str_d1, str_d2):

    # convert string to date object
    d1 = datetime.strptime(str_d1, "%Y/%m/%d, %H:%M")
    d2 = datetime.strptime(str_d2, "%Y/%m/%d, %H:%M")


    # Calculate the difference between the two datetimes in hours
    diff_hours = abs((d2 - d1).total_seconds() / 3600)
    
    return diff_hours

print("Successful running!")


root.mainloop()


