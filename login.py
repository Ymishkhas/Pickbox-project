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

def show_orders(Pnum, phone_number_root):

    # Connect to database
    conn = sqlite3.connect('C:/Users/youse/Desktop/tkinter/pickbox.db')
    c = conn.cursor()
    # Get orders from database for the entered phone number
    number=Pnum.get()
    print(number)
    orders = c.execute(f"SELECT * FROM customerView WHERE phone = {number}")
    fetched= orders.fetchall()
    print(fetched)
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
    treeview["columns"] = ("shipment_id", "status", "delivery_time", "locker_id", "pickboxid","storename","phone")
    treeview.column("#0", width=0, stretch=tk.NO)
    treeview.column("shipment_id", anchor=tk.CENTER, width=60)
    treeview.column("status", anchor=tk.CENTER, width=80)
    treeview.column("delivery_time", anchor=tk.CENTER, width=100)
    treeview.column("locker_id", anchor=tk.CENTER, width=40)
    treeview.column("pickboxid", anchor=tk.CENTER, width=40)
    # treeview.column("email", anchor=tk.CENTER, width=120)
    # treeview.column("storeid", anchor=tk.CENTER, width=50)
    treeview.column("storename", anchor=tk.CENTER, width=100)
    treeview.column("phone", anchor=tk.CENTER, width=100)
    # Set up the headings of the columns
    treeview.heading("#0", text="", anchor=tk.W)
    treeview.heading("shipment_id", text="Shipment ID", anchor=tk.CENTER)
    treeview.heading("status", text="Status", anchor=tk.CENTER)
    treeview.heading("delivery_time", text="Delivery Time", anchor=tk.CENTER)
    treeview.heading("locker_id", text="Locker ID", anchor=tk.CENTER)
    treeview.heading("pickboxid", text="PickBox ID", anchor=tk.CENTER)
    # treeview.heading("email", text="Email", anchor=tk.CENTER)
    # treeview.heading("storeid", text="Store ID", anchor=tk.CENTER)
    treeview.heading("storename", text="Store Name", anchor=tk.CENTER)
    treeview.heading("phone", text="Phone Number", anchor=tk.CENTER)   
    # Insert the orders into the treeview
    for order in fetched:
        treeview.insert("", tk.END, text="", values=order)

 # Show the orders in a message box


def phone_number_page():
    # Create phone number page
    phone_number_root = customtkinter.CTk()
    phone_number_root.geometry("700x400")
    
    phone_number_root.title("Phone Number Page")
    phone_number_root.resizable(False, False)

    # create textboxes
    enter = customtkinter.CTkLabel(phone_number_root, text="Enter your phone number to show all your orders ", font=("Arial", 16))
    enter.pack()
    enter.place(relx=0.5, rely=0.1, anchor=tkinter.CENTER)

    def validate_phone_number(new_value):
        return new_value.isdigit() or new_value == ""

    Pnum = customtkinter.CTkEntry(master=phone_number_root, width=220, validate="key", validatecommand=(phone_number_root.register(validate_phone_number), "%P"))
   
    Pnum.pack()
    Pnum.place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)

    show = customtkinter.CTkButton(phone_number_root, text="Show Orders", command=lambda: show_orders(Pnum, phone_number_root))
    show.pack()
    show.place(relx=0.8, rely=0.3, anchor=tkinter.CENTER)

    
    def refresh():
        phone_number_root.destroy()
        phone_number_page()

    refresh_button = customtkinter.CTkButton(phone_number_root, text="Refresh", command=refresh)
    refresh_button.pack()
    refresh_button.place(relx=0.9, rely=0.9, anchor=tkinter.CENTER)

    back_button = customtkinter.CTkButton(phone_number_root, text="Back to Main Page", command=phone_number_root.destroy)
    back_button.pack()
    back_button.place(relx=0.5, rely=0.8, anchor=tkinter.CENTER)

    phone_number_root.mainloop()

def shipment_id_page():
    # Create shipment id page
    shipment_id_root = customtkinter.CTk()
    shipment_id_root.geometry("700x400")
    
    shipment_id_root.title("Shipment ID Page")
    shipment_id_root.resizable(False, False)

    # create textboxes
    enter = customtkinter.CTkLabel(shipment_id_root, text="Enter your Shipment ID to show your shipment status ", font=("Arial", 16))
    enter.pack()
    enter.place(relx=0.5, rely=0.1, anchor=tkinter.CENTER)

    def validate_shipment_id(new_value):
        return re.match(r'^[a-zA-Z0-9]*$', new_value) is not None or new_value == ""

    shipID = customtkinter.CTkEntry(master=shipment_id_root, width=220, placeholder_text="213156489714", validate="key", validatecommand=(shipment_id_root.register(validate_shipment_id), "%P"))
    shipID.pack()
    shipID.place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)

    show = customtkinter.CTkButton(shipment_id_root, text="Show Order")
    show.pack()
    show.place(relx=0.8, rely=0.3, anchor=tkinter.CENTER)

    def refresh():
        shipment_id_root.destroy()
        shipment_id_page()

    refresh_button = customtkinter.CTkButton(shipment_id_root, text="Refresh", command=refresh)
    refresh_button.pack()
    refresh_button.place(relx=0.9, rely=0.1, anchor=tkinter.CENTER)

    back_button = customtkinter.CTkButton(shipment_id_root, text="Back to Main Page", command=shipment_id_root.destroy)
    back_button.pack()
    back_button.place(relx=0.5, rely=0.8, anchor=tkinter.CENTER)

    shipment_id_root.mainloop()


# Create root window
root = customtkinter.CTk()
root.geometry("700x400")
root.title("Modern Login")
root.resizable(False,False)


# create textboxes
welcome_label = customtkinter.CTkLabel(root, text="Welcome to Pick Box!",  font=("Arial", 24))
welcome_label.pack()
welcome_label.place(relx=0.5, rely=0.2, anchor=tkinter.CENTER)

choose_label = customtkinter.CTkLabel(root, text="Choose what suits you",  font=("Arial", 16))
choose_label.pack()
choose_label.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)

phone_button = customtkinter.CTkButton(root, text="Phone Number", command=phone_number_page)
phone_button.pack()
phone_button.place(relx=0.3, rely=0.5, anchor=tkinter.CENTER)

shipment_button = customtkinter.CTkButton(root, text="Shipment ID", command=shipment_id_page)
shipment_button.pack()
shipment_button.place(relx=0.7, rely=0.5, anchor=tkinter.CENTER)


print("Successful running!")


root.mainloop()
