import random
import tkinter as tk
from tkinter import ttk
import tkinter
from tkinter import messagebox
from tkinter import *
import customtkinter
import tkinter.ttk as ttk
import utils as utils

# GLOBAL VARIABLES
generatedPIN = 0
generatedPIN_phone = 0

def main():
    # Create root window
    root = customtkinter.CTk()
    root.geometry("700x400")
    root.title("PickBox")
    root.resizable(False,False)

    # Page(1) widgets, CUSTOMER PAGE
    welcome_label = customtkinter.CTkLabel(root, text="Welcome to Pick Box!", font=("Arial", 24))
    welcome_label.pack()
    welcome_label.place(relx=0.5, rely=0.2, anchor=tkinter.CENTER)

    choose_label = customtkinter.CTkLabel(root, text="Choose what suits you", font=("Arial", 16))
    choose_label.pack()
    choose_label.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)

    phone_button = customtkinter.CTkButton(root, text="Phone Number", command=lambda: phone_number_page(root))
    phone_button.pack()
    phone_button.place(relx=0.385, rely=0.5, anchor=tkinter.CENTER)

    shipment_button = customtkinter.CTkButton(root, text="Shipment ID", command=lambda: shipment_id_page(root))
    shipment_button.pack()
    shipment_button.place(relx=0.65, rely=0.5, anchor=tkinter.CENTER)

    # Page(2) widgets, DRIVER PAGE
    driver_login_frame = customtkinter.CTkFrame(root)
    driver_login_frame.pack(fill="both", expand=True)

    welcome_driver_label = customtkinter.CTkLabel(driver_login_frame, text="Welcome to Pick Box!", font=("Arial", 24))
    welcome_driver_label.pack()
    welcome_driver_label.place(relx=0.5, rely=0.2, anchor=tkinter.CENTER)

    login_label = customtkinter.CTkLabel(driver_login_frame, text="Enter your username and password to show all your orders", font=("Arial", 16))
    login_label.pack()
    login_label.place(relx=0.5, rely=0.35, anchor=tkinter.CENTER)

    # Username entry box
    username_entry = customtkinter.CTkEntry(driver_login_frame, width=220, placeholder_text="Username")
    username_entry.pack()
    username_entry.place(relx=0.5, rely=0.45, anchor=tkinter.CENTER)

    # Password entry box
    password_entry = customtkinter.CTkEntry(driver_login_frame, width=220, placeholder_text="Password", show="*")
    password_entry.pack()
    password_entry.place(relx=0.5, rely=0.55, anchor=tkinter.CENTER)

    # Login button
    login_button = customtkinter.CTkButton(driver_login_frame, text="Log In", fg_color="red", hover_color="dark red", command=lambda: (driver_login_frame.pack_forget(), driver_shipments(root, username_entry.get(), password_entry.get())))
    login_button.pack()
    login_button.place(relx=0.5, rely=0.65, anchor=tkinter.CENTER)
    driver_login_frame.pack_forget()


    # Toggle button to switch between customer page and driver page
    toggle_button = customtkinter.CTkButton(root, text=">", font=("Arial", 12), width=2, height=50,
                                            command=lambda: driver_login_frame.pack(side="right", fill="both", expand=True) if driver_login_frame.winfo_ismapped() == 0 else driver_login_frame.pack_forget())
    toggle_button.pack()
    toggle_button.place(relx=0.99, rely=0.01, anchor=tkinter.NE)

    root.mainloop()
    print("Successful running!")

# A page for the phone number option in the main root
def phone_number_page(root):
    # Create phone number page
    phone_number_frame = customtkinter.CTkFrame(root)
    phone_number_frame.pack(fill="both", expand=True)

    # Create login label
    login_label = customtkinter.CTkLabel(phone_number_frame, text="Enter your phone number to show all your orders ", font=("Arial", 16))
    login_label.pack()
    login_label.place(relx=0.5, rely=0.2, anchor=tkinter.CENTER)

    # Phone number entry box
    def allowed_phone_entry(new_value):
        return new_value.isdigit() or new_value == ""
    phone_number = customtkinter.CTkEntry(master=phone_number_frame, width=220, validate="key", validatecommand=(phone_number_frame.register(allowed_phone_entry), "%P"))
    phone_number.pack()
    phone_number.place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)

    # Create Send pin button
    checkButton=  customtkinter.CTkButton(phone_number_frame, text= "Send PIN", command=lambda: generatePIN(phone_number.get()))
    checkButton.pack()
    checkButton.place(relx=0.8, rely=0.3, anchor=tkinter.CENTER)

    # PIN entry box
    pin_number = customtkinter.CTkEntry(master=phone_number_frame, width=220, placeholder_text="PIN",)
    pin_number.pack()
    pin_number.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    # Show orders invokation button
    show = customtkinter.CTkButton(phone_number_frame, text="Show Orders", command=lambda: show_shipments(phone_number_frame, phone_number.get(), pin_number.get()))
    show.pack()
    show.place(relx=0.5, rely=0.6, anchor=tkinter.CENTER)

    # Create refresh page button
    def refresh():
        phone_number_frame.destroy()
        phone_number_page(root)
    refresh_button = customtkinter.CTkButton(phone_number_frame, text="Refresh", command=refresh)
    refresh_button.pack()
    refresh_button.place(relx=0.9, rely=0.05, anchor=tkinter.CENTER)

    # Create back to main page button
    back_button = customtkinter.CTkButton(phone_number_frame, text="Back to Main Page", command=phone_number_frame.destroy)
    back_button.pack()
    back_button.place(relx=0.5, rely=0.8, anchor=tkinter.CENTER)

    phone_number_frame.mainloop()

# A page for the shipment number option in the main root
def shipment_id_page(root):
    # Create shipment id page
    shipment_id_frame = customtkinter.CTkFrame(root)
    shipment_id_frame.pack(fill="both", expand=True)

    # Create search shipment label
    enter_label = customtkinter.CTkLabel(shipment_id_frame, text="Enter your Shipment ID to show your shipment status ", font=("Arial", 16))
    enter_label.pack()
    enter_label.place(relx=0.5, rely=0.2, anchor=tkinter.CENTER)

    # Shipment number entry box
    def validate_shipment_id(new_value):
        return new_value.isdigit() or new_value == ""
    shipID = customtkinter.CTkEntry(master=shipment_id_frame, width=220, placeholder_text="", validate="key", validatecommand=(shipment_id_frame.register(validate_shipment_id), "%P"))
    shipID.pack()
    shipID.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    # Show order invokation button
    show = customtkinter.CTkButton(shipment_id_frame, text="Show Order", command=lambda:show_shipment(shipID.get(), shipment_id_frame))
    show.pack()
    show.place(relx=0.8, rely=0.5, anchor=tkinter.CENTER)

    # Create refresh page button
    def refresh():
        shipment_id_frame.destroy()
        shipment_id_page(root)
    refresh_button = customtkinter.CTkButton(shipment_id_frame, text="Refresh", command=refresh)
    refresh_button.pack()
    refresh_button.place(relx=0.9, rely=0.2, anchor=tkinter.CENTER)

    # Create back to main page button
    back_button = customtkinter.CTkButton(shipment_id_frame, text="Back to Main Page", command=shipment_id_frame.destroy)
    back_button.pack()
    back_button.place(relx=0.5, rely=0.8, anchor=tkinter.CENTER)

    shipment_id_frame.mainloop()

# Used in phone_number_page, recieves a number and searches the DB for matching rows using a query
# Basically display all orders that have the same phone number
def show_shipments(phone_number_frame, phone, pin):

    global generatedPIN
    global generatedPIN_phone

    # Checks if customer entered correct pin
    if str(generatedPIN) != pin or str(generatedPIN_phone) != phone:
        messagebox.showerror("Error", "Wrong PIN number, try sending a new PIN number")

    else:

        orders = utils.get_shipments(phone)

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
        treeview["columns"] = ("select", "shipment_id", "status", "latest_update","delivery_time", "storename", "pickboxid", "locker_id", "phone")
        treeview.column("#0", width=0, stretch=tk.NO)
        treeview.column("select", anchor=tk.CENTER, width=0, minwidth=0)
        treeview.column("shipment_id", anchor=tk.CENTER, width=60)
        treeview.column("status", anchor=tk.CENTER, width=120)
        treeview.column("latest_update", anchor=tk.CENTER, width=120)
        treeview.column("delivery_time", anchor=tk.CENTER, width=120)
        treeview.column("storename", anchor=tk.CENTER, width=80)
        treeview.column("pickboxid", anchor=tk.CENTER, width=50)
        treeview.column("locker_id", anchor=tk.CENTER, width=45)
        treeview.column("phone", anchor=tk.CENTER, width=0, minwidth=0)
        # treeview.column("email", anchor=tk.CENTER, width=120)
        
        # Set up the headings of the columns
        treeview.heading("#0", text="", anchor=tk.W)
        treeview.heading("select", text="", anchor=tk.CENTER)
        treeview.heading("shipment_id", text="Shipment", anchor=tk.CENTER)
        treeview.heading("status", text="Status", anchor=tk.CENTER)
        treeview.heading("latest_update", text="Latest Update", anchor=tk.CENTER)
        treeview.heading("delivery_time", text="Delivery Time", anchor=tk.CENTER)
        treeview.heading("storename", text="Store Name", anchor=tk.CENTER)
        treeview.heading("pickboxid", text="PickBox", anchor=tk.CENTER)
        treeview.heading("locker_id", text="Locker", anchor=tk.CENTER)
        treeview.heading("phone", text="", anchor=tk.CENTER)
        # treeview.heading("email", text="Email", anchor=tk.CENTER)

        # Insert the orders into the treeview
        row_count = 0
        for oneorder in orders:
            treeview.insert("", row_count, text="", values=(False, *oneorder))
            row_count += 1
        
        # Delete selected orders when the delete button is clicked
        delete_button = customtkinter.CTkButton(phone_number_frame, text="Cancel Orders", command=lambda: cancel_selected_shipments(treeview))
        delete_button.pack()
        delete_button.place(relx= 0.25, rely= 0.6)        

        # Merge selected orders when the delete merge is clicked
        merge_button = customtkinter.CTkButton(phone_number_frame, text="Merge Orders", command=lambda: merge_selected_shipments(treeview))
        merge_button.pack()
        merge_button.place(relx= 0.55, rely= 0.6)    

        # Create back to main page button
        back_button = customtkinter.CTkButton(phone_number_frame, text="Back to Main Page", command=phone_number_frame.destroy)
        back_button.pack()
        back_button.place(relx=0.5, rely=0.8, anchor=tkinter.CENTER)

# Used inside show shipments function, when an operation happen(cancel or merge) it update the page with the latest changes
def refresh_shipments(treeview, phone):

    # Get orders from database for the entered phone number
    orders = utils.get_shipments(phone)
    
    # Clear the existing treeview
    treeview.delete(*treeview.get_children())

    # Insert the latest orders into the treeview
    row_count = 0
    for oneorder in orders:
        treeview.insert("", row_count, text="", values=(False, *oneorder))
        row_count += 1

# Used in shipment_id_page, Recieves a shipment number and searches the DB for matching row using a query
# Basically display the order that have the same shipment
def show_shipment(shipment_id, shipment_id_frame):
    
    order = utils.get_shipment(shipment_id)

    if not order:
        # No order found for the given shipment ID
        messagebox.showerror("Error", f"Shipment {shipment_id} dose not exist.")
        return None

    for widget in shipment_id_frame.winfo_children():
        widget.destroy()

    # Create a frame to show the order
    order_frame = tk.Frame(shipment_id_frame)
    order_frame.pack()

    # Create a treeview to show the orders
    treeview = ttk.Treeview(order_frame)
    treeview.pack()

    # Set up the columns of the treeview
    treeview["columns"] = ("shipment_id", "status", "latest_update", "delivery_time", "storename", "pickboxid", "locker_id", "phone")
    treeview.column("#0", width=0, stretch=tk.NO)
    treeview.column("shipment_id", anchor=tk.CENTER, width=60)
    treeview.column("status", anchor=tk.CENTER, width=120)
    treeview.column("latest_update", anchor=tk.CENTER, width=120)
    treeview.column("delivery_time", anchor=tk.CENTER, width=120)
    treeview.column("storename", anchor=tk.CENTER, width=80)
    treeview.column("pickboxid", anchor=tk.CENTER, width=50)
    treeview.column("locker_id", anchor=tk.CENTER, width=45)
    treeview.column("phone", anchor=tk.CENTER, width=0, minwidth=0)
    # treeview.column("email", anchor=tk.CENTER, width=120)
        
    # Set up the headings of the columns
    treeview.heading("#0", text="", anchor=tk.W)
    treeview.heading("shipment_id", text="Shipment", anchor=tk.CENTER)
    treeview.heading("status", text="Status", anchor=tk.CENTER)
    treeview.heading("latest_update", text="Latest Update", anchor=tk.CENTER)
    treeview.heading("delivery_time", text="Delivery Time", anchor=tk.CENTER)
    treeview.heading("storename", text="Store Name", anchor=tk.CENTER)
    treeview.heading("pickboxid", text="PickBox", anchor=tk.CENTER)
    treeview.heading("locker_id", text="Locker", anchor=tk.CENTER)
    treeview.heading("phone", text="", anchor=tk.CENTER)   

    row_count = 0
    for oneorder in order:
        treeview.insert("", row_count, text="", values=oneorder)
        row_count += 1
    
    # If the status "Pending" then a cancel button will appear
    status = order[0][1]
    if status == "Pending":
        # Delete selected orders when the delete button is clicked
        delete_button = customtkinter.CTkButton(shipment_id_frame, text="Cancel Order", 
                                                command=lambda: (utils.cancel_shipment(shipment_id), shipment_id_frame.destroy(), messagebox.showinfo("Success", f"Shipment {shipment_id} has been cancelled.")))
        delete_button.pack()
        delete_button.place(relx= 0.4, rely= 0.65)  

    # Create back to main page button
    back_button = customtkinter.CTkButton(shipment_id_frame, text="Back to Main Page", command=shipment_id_frame.destroy)
    back_button.pack()
    back_button.place(relx=0.5, rely=0.8, anchor=tkinter.CENTER)

# A page for the driver show shipments in the driver login page
def driver_shipments(root, username, password):

    # Check username and password in the DB
    if not utils.is_valid_driver(username,password):
        messagebox.showerror("Error", "the entered username/password is incorrect.")
        return
                
    # Create driver shipments page
    order_page_frame = customtkinter.CTkFrame(root)
    order_page_frame.pack(fill="both", expand=True)

    # Create a label to display the driver
    driver_info = utils.get_driver_store_info(username)
    driver_label = customtkinter.CTkLabel(order_page_frame, text=f"Welcome {driver_info[0][0]} of {driver_info[0][1]}", font=("Arial", 18))
    driver_label.pack(side=tkinter.TOP, pady=10)

    # Get assigned shipments from the database
    orders = utils.get_driver_orders(username)

    # Create a treeview to show the orders
    treeview = ttk.Treeview(order_page_frame)
    treeview.pack()

    # Set up the columns of the treeview
    treeview["columns"] = ("select", "shipment_id", "status", "latest_update", "delivery_time", "pickboxid", "locker_id")
    treeview.column("#0", width=0, stretch=tk.NO)
    treeview.column("select", anchor=tk.CENTER, width=0, minwidth=0)
    treeview.column("shipment_id", anchor=tk.CENTER, width=80)
    treeview.column("status", anchor=tk.CENTER, width=120)
    treeview.column("latest_update", anchor=tk.CENTER, width=120)
    treeview.column("delivery_time", anchor=tk.CENTER, width=120)
    treeview.column("pickboxid", anchor=tk.CENTER, width=90)
    treeview.column("locker_id", anchor=tk.CENTER, width=90)
    
    # Set up the headings of the columns
    treeview.heading("#0", text="", anchor=tk.W)
    treeview.heading("select", text="", anchor=tk.CENTER)
    treeview.heading("shipment_id", text="Shipment ID", anchor=tk.CENTER)
    treeview.heading("status", text="Status", anchor=tk.CENTER)
    treeview.heading("latest_update", text="Latest Update", anchor=tk.CENTER)
    treeview.heading("delivery_time", text="Delivery Time", anchor=tk.CENTER)
    treeview.heading("pickboxid", text="PickBox ID", anchor=tk.CENTER)
    treeview.heading("locker_id", text="Locker ID", anchor=tk.CENTER)

    row_count = 0
    for oneorder in orders:
        treeview.insert("", row_count, text="", values=("", *oneorder))
        row_count += 1

    # A method refreshes the page with latest updates, called when a driver press the update button
    def refresh():
        order_page_frame.pack_forget()
        driver_shipments(root, username, password)

    # Create a button to update the status of selected shipments
    update_button = customtkinter.CTkButton(order_page_frame, text="Update Selected Shipments", fg_color="red", hover_color="dark red", command=lambda: (update_selected_shipments(treeview), refresh()))
    update_button.pack()
    update_button.place(relx=0.5, rely=0.8, anchor=tkinter.CENTER)

    # Create back to main page button
    back_button = customtkinter.CTkButton(order_page_frame, text="Back to Main Page", fg_color="red", hover_color="dark red", command= order_page_frame.destroy)
    back_button.pack()
    back_button.place(relx=0.5, rely=0.9, anchor=tkinter.CENTER)

    order_page_frame.mainloop()

# Iterate over the selected shipments and runs checks to see if the shipment can be updates, if so then it updates based on provious status
def update_selected_shipments(treeview):
        # Get the selected items from the treeview
        selected_items = treeview.selection()

        # Update the status of each selected shipment
        for item in selected_items:
            # Get the shipment ID and previous status from the item dictionary
            shipment_id = treeview.item(item, "values")[1]
            prev_status = treeview.item(item, "values")[2]

            if prev_status != "Pending" and prev_status != "Out For Delivery":
                messagebox.showerror("Failure", f"You cannot update a {prev_status} shipment")
            else:
                # Update the status of the shipment
                new_status = utils.update_shipment_status(shipment_id, prev_status)
                messagebox.showinfo("Success", f"Shipment {shipment_id} has been updated to {new_status}.")

# Iterate over the selected shipments and runs checks to see if the shipment can be merged, if so then it merge
def merge_selected_shipments(treeview):
    """merge the selected orders"""
    
    # Get the valid selected shipments (not the ones with status Picked Up or Cancelled)
    valid_shipments = []
    itmes = treeview.selection()
    for item in itmes:

        values = treeview.item(item, "values")
        
        if values[2] == "Picked Up" or values[2] == "Cancelled":
            messagebox.showerror("Failure", f"Shipment {values[1]} is {values[2]} and cannot be merged.")
        else:
            valid_shipments.append(values)

        if values[2] == "Ready For Collection":
            locker_id = values[7]
    
    # Check that there are only two orders selected
    if len(valid_shipments) != 2:
        messagebox.showerror("Failure", "You must select only two valid shipments to merge.")
        return
    
    # Check that all selected orders have the same pickbox ID
    pickbox_ids = set([shipment[6] for shipment in valid_shipments])
    if len(pickbox_ids) > 1:
        messagebox.showerror("Failure", "shipments are in different pickboxs and cannot be merged.")
        return
    pickbox_ids = pickbox_ids.pop()

    # Check that all selected orders have the same locker ID (Already merged)
    locker_ids = set([shipment[7] for shipment in valid_shipments])
    if len(locker_ids) == 1:
        messagebox.showerror("Failure", "shipments already merged.")
        return
    locker_ids = locker_ids.pop()

    # Check that the delivry time difference between the selected orders is not greater than 12 hours
    start_date = valid_shipments[0][4]
    end_date = valid_shipments[-1][4]
    diff_hours = utils.compareOrderTime(start_date, end_date)
    if diff_hours > 12:
        messagebox.showerror("Failure", "The time difference of delivry Time between the selected orders is greater than 12 hours and cannot be merged.")
        return
    
    # if no shipment was already in a locker, pick a locker to merge orders at
    if 'locker_id' not in locals():
        locker_id = valid_shipments[0][7]

    # Update the database to merge the selected orders
    for order in valid_shipments:
        utils.update_locker(locker_id, order[1])

    
    # Show a success message and refresh the order display
    messagebox.showinfo("Success", "Orders merged successfully.")
    
    phone = valid_shipments[0][8]
    refresh_shipments(treeview, phone)

# Iterate over the selected shipments and runs checks to see if the shipment can be cancelled, if so it cancel it
def cancel_selected_shipments(treeview):
    """cancel the selected orders"""
    
    items = treeview.selection()
    for item in items:

        status = treeview.item(item, "values")[2]
        shipment_id = treeview.item(item, "values")[1]
        phone = treeview.item(item, "values")[8]
        
        if status == "Pending":
            utils.cancel_shipment(shipment_id)
            messagebox.showinfo("Success", f"Shipment {shipment_id} has been cancelled.")
        else:
            messagebox.showerror("Failure", f"Shipment {shipment_id} already {status} and cannot be cancelled.")
        
        # treeview.delete(shipment)
    refresh_shipments(treeview, phone)

# Used in the phone_number_page, checks if the entered phone is valid and generate a PIN code to be sent to the customer phone as a verification
def generatePIN(phone):
    
    global generatedPIN
    global generatedPIN_phone
  
    if utils.is_valid_customer(phone):
        generatedPIN = random.randint(1000,9999)
        print("PIN:", generatedPIN)
        messagebox.showinfo("SMS Message", f"OPT Code: {generatedPIN}\nReason: Login - App")
        generatedPIN_phone = phone
        # utils.send_opt(phone, generatedPIN)
        
    else:
        messagebox.showerror("Error", "No such registred phone in our system, double check your entered phone number")

if __name__ == '__main__':
    main()