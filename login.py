import random
import tkinter as tk
from tkinter import ttk
import tkinter
from tkinter import messagebox
from PIL import ImageTk, Image
from tkinter import *
import customtkinter
import sqlite3
import os
import re

DB_PATH = 'D:/Downloads/tkinter2.0/pickbox.db'
generatedPIN = 0
generatedPIN_phone = 0
# creating connection from "show order" button in shipme
def show_order(shipID, shipment_id_root):
    #connect to DB
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    order = c.execute("SELECT * FROM customerView WHERE shipment_id = ?", (shipID.get(),)).fetchall()

    print(order)
    #commit changes/save them
    conn.commit()
    conn.close()

    for widget in shipment_id_root.winfo_children():
        widget.destroy()

    # Create a frame to show the orders
    order_frame = tk.Frame(shipment_id_root)
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
    
    delete_button = customtkinter.CTkButton(shipment_id_root, text="Delete Selected Orders", command=lambda: delete_selected_orders(treeview))
    delete_button.pack()
    delete_button.place(relx= 0.25, rely= 0.6) 

# Next Commit..
def merge_selected_orders(treeview):
    pass
#     # Get the selected orders
#     selected_orders = []
#     for item in treeview.get_children():
#         values = treeview.item(item, "values")
#         if values[0] == True:
#             selected_orders.append(values)
    
#     # Check that there are at least two orders selected
#     if len(selected_orders) < 2:
#         messagebox.showerror("Error", "You must select at least two orders to merge.")
#         return
    
#     # Check that all selected orders have the same locker ID
#     locker_ids = set([order[4] for order in selected_orders])
#     if len(locker_ids) > 1:
#         messagebox.showerror("Error", "All selected orders must have the same locker ID.")
#         return
#     locker_id = locker_ids.pop()
    
#     # Get the delivery time of the first order
#     delivery_time = selected_orders[0][3]
    
#     # Generate a new shipment ID for the merged order
#     new_shipment_id = generate_shipment_id()
    
#     # Update the database to merge the selected orders
#     conn = sqlite3.connect(DB_PATH)
#     c = conn.cursor()
#     for order in selected_orders:
#         c.execute("UPDATE orders SET shipment_id = ?, locker_id = ? WHERE shipment_id = ?",
#                   (new_shipment_id, locker_id, order[1]))
#     conn.commit()
#     conn.close()
    
#     # Show a success message and refresh the order display
#     messagebox.showinfo("Success", "Orders merged successfully.")
#     show_orders(Pnum, phone_number_root, pin)
#
def delete_order(order_id):
    """Deletes the order from the database."""
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    #check the variables names here
    c.execute("DELETE FROM shipment WHERE shipment_id = ?", (order_id,))
    conn.commit()
    conn.close()
    # check the variables names here also
    messagebox.showinfo("Success", f"Order {order_id} has been deleted.")


def delete_selected_orders(treeview):
    """Deletes the selected orders from the database."""
    selected_items = treeview.selection()
    for item in selected_items:
        order_id = treeview.item(item, "values")[0]
        delete_order(order_id)
        treeview.delete(item)

#This method recieves a number and searches the DB for matching rows using a query with a condition of matching the number
#Basically display all orders that have the same phone number

def show_orders(Pnum, phone_number_root, pin):

    global generatedPIN
    global generatedPIN_phone

    pin = pin.get()
    phone = Pnum.get()

    if str(generatedPIN) != pin or str(generatedPIN_phone) != phone:
        messagebox.showerror("Error", "Wrong PIN number, try sending a new PIN number")

    else:

        # Connect to database
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        # Get orders from database for the entered phone number
        number = Pnum.get()
        
        orders = c.execute("SELECT * FROM customerView WHERE phone = ?", (phone,)).fetchall()
        
        
        # Close the database connection
        conn.commit()
        conn.close()

        # Clear the existing frame, if any
        for widget in phone_number_root.winfo_children():
            widget.destroy()

        # Create a frame to show the orders
        orders_frame = tk.Frame(phone_number_root)
        orders_frame.pack()

        # Create a treeview to show the orders
        treeview = ttk.Treeview(orders_frame)
        treeview.pack()

        # Set up the columns of the treeview
        treeview["columns"] = ("select", "shipment_id", "status", "delivery_time", "locker_id", "pickboxid", "email", "storename", "phone")
        treeview.column("#0", width=0, stretch=tk.NO)
        treeview.column("select", anchor=tk.CENTER, width=50)
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
        delete_button = customtkinter.CTkButton(phone_number_root, text="Delete Selected Orders", command=lambda: delete_selected_orders(treeview))
        delete_button.pack()
        delete_button.place(relx= 0.25, rely= 0.6)        

        merge_button = customtkinter.CTkButton(phone_number_root, text="Merge Orders", command=lambda: merge_selected_orders(treeview))
        merge_button.pack()
        merge_button.place(relx= 0.55, rely= 0.6)    


            


def phone_number_page():
    # Create phone number page
    phone_number_root = customtkinter.CTk()
    phone_number_root.geometry("700x400")
    
    phone_number_root.title("Phone Number Page")
    phone_number_root.resizable(False, False)

    # create textboxes
    enter = customtkinter.CTkLabel(phone_number_root, text="Enter your phone number to show all your orders ", font=("Arial", 16))
    enter.pack()
    enter.place(relx=0.5, rely=0.2, anchor=tkinter.CENTER)

    

    def validate_phone_number(new_value):
        return new_value.isdigit() or new_value == ""

    Pnum = customtkinter.CTkEntry(master=phone_number_root, width=220, validate="key", validatecommand=(phone_number_root.register(validate_phone_number), "%P"))
    
    Pnum.pack()
    Pnum.place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)

 
    #create Send pin button
    checkButton=  customtkinter.CTkButton(phone_number_root, text= "Send PIN", command=lambda: generatePIN(Pnum))
    checkButton.pack()
    checkButton.place(relx=0.8, rely=0.3, anchor=tkinter.CENTER)

    #Check PIN entry
    pin = customtkinter.CTkEntry(master=phone_number_root, width=220)
    pin.pack()
    
    pin.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)


    
    #Show order invokation
    show = customtkinter.CTkButton(phone_number_root, text="Show Orders", command=lambda: show_orders(Pnum, phone_number_root,pin))
    show.pack()
    show.place(relx=0.5, rely=0.6, anchor=tkinter.CENTER)


    #


    
    def refresh():
        phone_number_root.destroy()
        phone_number_page()

    refresh_button = customtkinter.CTkButton(phone_number_root, text="Refresh", command=refresh)
    refresh_button.pack()
    refresh_button.place(relx=0.9, rely=0.05, anchor=tkinter.CENTER)

    back_button = customtkinter.CTkButton(phone_number_root, text="Back to Main Page", command=phone_number_root.destroy)
    back_button.pack()
    back_button.place(relx=0.5, rely=0.8, anchor=tkinter.CENTER)

    phone_number_root.mainloop()

def generatePIN(phone):
    
    global generatedPIN
    global generatedPIN_phone

    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    #
    result = c.execute("select * from customer where phone= ?", (phone.get(),)).fetchall()
  
    if result != []:
        generatedPIN = random.randint(1000,9999)
        print("PIN:", generatedPIN)
        generatedPIN_phone = phone.get()
        
    else:
        messagebox.showerror("Error", "No such registred phone with that number in our system, double check your entered phone number")
        
       
        
    
    



def shipment_id_page():
    # Create shipment id page
    shipment_id_root = customtkinter.CTk()
    shipment_id_root.geometry("700x400")
    
    shipment_id_root.title("Shipment ID Page")
    shipment_id_root.resizable(False, False)

    # create textboxes
    enter = customtkinter.CTkLabel(shipment_id_root, text="Enter your Shipment ID to show your shipment status ", font=("Arial", 16))
    enter.pack()
    enter.place(relx=0.5, rely=0.2, anchor=tkinter.CENTER)

    def validate_shipment_id(new_value):
        return re.match(r'^[a-zA-Z0-9]*$', new_value) is not None or new_value == ""

    shipID = customtkinter.CTkEntry(master=shipment_id_root, width=220, placeholder_text="", validate="key", validatecommand=(shipment_id_root.register(validate_shipment_id), "%P"))
    shipID.pack()
    shipID.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    show = customtkinter.CTkButton(shipment_id_root, text="Show Order", command=lambda:show_order(shipID, shipment_id_root))
    show.pack()
    show.place(relx=0.8, rely=0.5, anchor=tkinter.CENTER)

    def refresh():
        shipment_id_root.destroy()
        shipment_id_page()

    refresh_button = customtkinter.CTkButton(shipment_id_root, text="Refresh", command=refresh)
    refresh_button.pack()
    refresh_button.place(relx=0.9, rely=0.2, anchor=tkinter.CENTER)

    back_button = customtkinter.CTkButton(shipment_id_root, text="Back to Main Page", command=shipment_id_root.destroy)
    back_button.pack()
    back_button.place(relx=0.5, rely=0.8, anchor=tkinter.CENTER)

    shipment_id_root.mainloop()







  

# Create root window
root = customtkinter.CTk()
root.geometry("700x400")
root.title("Modern Login")
root.resizable(False,False)




welcome_label = customtkinter.CTkLabel(root, text="Welcome to Pick Box!",  font=("Arial", 24))
welcome_label.pack()
welcome_label.place(relx=0.5, rely=0.2, anchor=tkinter.CENTER)

choose_label = customtkinter.CTkLabel(root, text="Choose what suits you",  font=("Arial", 16))
choose_label.pack()
choose_label.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)

phone_button = customtkinter.CTkButton(root, text="Phone Number", command=phone_number_page)
phone_button.pack()
phone_button.place(relx=0.385, rely=0.5, anchor=tkinter.CENTER)

shipment_button = customtkinter.CTkButton(root, text="Shipment ID", command=shipment_id_page)
shipment_button.pack()
shipment_button.place(relx=0.65, rely=0.5, anchor=tkinter.CENTER)





print("Successful running!")


root.mainloop()
