import tkinter as tk
import sqlite3
from tkinter import ttk

sqliteConnection = sqlite3.connect('pharmacy.db')
cursor = sqliteConnection.cursor()
print("Successfully Connected to SQLite")
# Function to create a Client instance


app = tk.Tk()
app.title("Client Creator")

Client_page = tk.Frame(app)
Product_page = tk.Frame(app)
Purchase_page = tk.Frame(app)
Employee_page = tk.Frame(app)


def show_page(page):
    if page == "client":
        Client_page.pack()
        Product_page.pack_forget()
        Purchase_page.pack_forget()
        Employee_page.pack_forget()
    elif page == "product":
        Client_page.pack_forget()
        Product_page.pack()
        Purchase_page.pack_forget()
        Employee_page.pack_forget()
    elif page == "purchase":
        Client_page.pack_forget()
        Product_page.pack_forget()
        Purchase_page.pack()
        Employee_page.pack_forget()
    elif page == "employee":
        Client_page.pack_forget()
        Product_page.pack_forget()
        Purchase_page.pack_forget()
        Employee_page.pack()


## Client page ##


class Client:
    def __init__(self, client_id, first_name, last_name, number):
        self.client_id = client_id
        self.first_name = first_name
        self.last_name = last_name
        self.number = number


def clear_client_entry_fields():
    client_id_entry.delete(0, 'end')
    first_name_entry.delete(0, 'end')
    last_name_entry.delete(0, 'end')
    number_entry.delete(0, 'end')


def create_client():
    client_id = client_id_entry.get()
    first_name = first_name_entry.get()
    last_name = last_name_entry.get()
    number = number_entry.get()

    # Create a Client instance
    client = Client(client_id, first_name, last_name, number)
    # Check if the client ID already exists in the database
    cursor.execute(
        "SELECT client_id FROM client WHERE client_id=?", (client_id,))
    existing_client = cursor.fetchone()

    if existing_client:
        update_query = "UPDATE client SET first_name = ?, last_name = ?, number = ? WHERE client_id = ?"

        # Values to be updated in the database
        update_data = (client.first_name, client.last_name,
                       client.number, client.client_id)

        cursor.execute(update_query, update_data)

        # Commit the changes to the database
        sqliteConnection.commit()

    else:
        insert_query = "INSERT INTO client (client_id, first_name, last_name, number) VALUES (?, ?, ?, ?)"
        client_data = (client.client_id, client.first_name,
                       client.last_name, client.number)
        cursor.execute(insert_query, client_data)
        sqliteConnection.commit()
        print("client created successfuly")
        # Display client details
        '''result_label.config(text=f"Client ID: {client.client_id}\n"
                                f"First Name: {client.first_name}\n"
                                f"Last Name: {client.last_name}\n"
                                f"Number: {client.number}")'''
    show_clients()


def show_clients():
    # Clear the current data in the Treeview
    for row in clients_treeview.get_children():
        clients_treeview.delete(row)

    # Fetch client data from the database
    cursor.execute("SELECT * FROM client")
    clients = cursor.fetchall()

    # Add client data to the Treeview
    for client in clients:
        clients_treeview.insert("", "end", values=client)


def delete_client():
    selected_item = clients_treeview.selection()
    if selected_item:
        client_id = clients_treeview.item(selected_item, 'values')[0]
        cursor.execute("DELETE FROM client WHERE client_id=?", (client_id,))
        sqliteConnection.commit()
        show_clients()  # Refresh the Treeview after deletion


def show_selected_client():
    clear_client_entry_fields()
    selected_item = clients_treeview.selection()
    if selected_item:
        client = clients_treeview.item(selected_item, 'values')
        client_id_entry.insert(0, client[0])
        first_name_entry.insert(0, client[1])
        last_name_entry.insert(0, client[2])
        number_entry.insert(0, client[3])


client_id_label = tk.Label(Client_page, text="Client ID:")
client_id_label.pack()
client_id_entry = tk.Entry(Client_page)
client_id_entry.pack()

first_name_label = tk.Label(Client_page, text="First Name:")
first_name_label.pack()
first_name_entry = tk.Entry(Client_page)
first_name_entry.pack()

last_name_label = tk.Label(Client_page, text="Last Name:")
last_name_label.pack()
last_name_entry = tk.Entry(Client_page)
last_name_entry.pack()

number_label = tk.Label(Client_page, text="Number:")
number_label.pack()
number_entry = tk.Entry(Client_page)
number_entry.pack()

create_button = tk.Button(
    Client_page, text="Create/Update Client", command=create_client)
create_button.pack()

result_label = tk.Label(Client_page, text="")
result_label.pack()

Edit_Client = tk.Button(Client_page, text="Edit Client",
                        command=show_selected_client)
Edit_Client.pack()
# Update the Treeview with client data
columns = ("Client ID", "First Name", "Last Name", "Number")
clients_treeview = ttk.Treeview(Client_page, columns=columns, show="headings")
for column in columns:
    clients_treeview.heading(column, text=column)
    clients_treeview.column(column, width=100)  # Adjust column width as needed
clients_treeview.pack()

# Create a button to fetch and display clients
fetch_button = tk.Button(
    Client_page, text="Fetch Clients", command=show_clients)
fetch_button.pack()

delete_button = tk.Button(
    Client_page, text="Delete Client", command=delete_client)
delete_button.pack()

# Fetch and display clients initially
show_clients()
Client_page.pack()

page_buttons_frame = tk.Frame(app)
page_buttons_frame.pack(side="bottom", padx=10, pady=10)
# button buttons
client_page_button = tk.Button(
    page_buttons_frame, text="Client", command=lambda: show_page('client'))
product_page_button = tk.Button(
    page_buttons_frame, text="Product", command=lambda: show_page('product'))
purchase_page_button = tk.Button(
    page_buttons_frame, text="Purchase", command=lambda: show_page('purchase'))
employee_page_button = tk.Button(
    page_buttons_frame, text="Employee", command=lambda: show_page('employee'))

client_page_button.pack(side="left")
product_page_button.pack(side="left")
purchase_page_button.pack(side="left")
employee_page_button.pack(side="left")


## Product #######
##################
##################
##################
##################
##################

class Product:
    def __init__(self, product_id, name, description, price, category):
        self.product_id = product_id
        self.name = name
        self.description = description
        self.price = price
        self.category = category


def clear_product_entry_fields():
    product_id_entry.delete(0, 'end')
    name_entry.delete(0, 'end')
    description_entry.delete(0, 'end')
    price_entry.delete(0, 'end')
    category_entry.delete(0, 'end')


def create_product():
    product_id = product_id_entry.get()
    name = name_entry.get()
    description = description_entry.get()
    price = price_entry.get()
    category = category_entry.get()

    product = Product(product_id, name, description, price, category)
    cursor.execute(
        "SELECT product_id FROM product WHERE product_id=?", (product_id,))
    existing_product = cursor.fetchone()

    if existing_product:
        update_query = "UPDATE product SET name = ?, description = ?, price = ?, category=? WHERE product_id = ?"

        # Values to be updated in the database
        update_data = (product.name, product.description,
                       product.price, product.category, product.product_id)

        cursor.execute(update_query, update_data)

        # Commit the changes to the database
        sqliteConnection.commit()

    else:
        insert_query = " INSERT INTO product (product_id, name, description, price, category) VALUES (?, ?, ?, ?, ?)"
        product_data = (product.product_id, product.name,
                        product.description, product.price, product.category)
        cursor.execute(insert_query, product_data)
        sqliteConnection.commit()

    show_products()


def show_products():
    for row in products_treeview.get_children():
        products_treeview.delete(row)

    cursor.execute("SELECT * FROM product")
    products = cursor.fetchall()

    for product in products:
        products_treeview.insert("", "end", values=product)


def delete_product():
    selected_item = products_treeview.selection()
    if selected_item:
        product_id = products_treeview.item(selected_item, 'values')[0]
        cursor.execute("DELETE FROM product WHERE product_id=?", (product_id,))
        sqliteConnection.commit()
        show_products()  # Refresh the Treeview after deletion


def show_selected_products():
    clear_product_entry_fields()
    selected_item = products_treeview.selection()
    if selected_item:
        product = products_treeview.item(selected_item, 'values')
        product_id_entry.insert(0, product[0])
        name_entry.insert(0, product[1])
        description_entry.insert(0, product[2])
        price_entry.insert(0, product[3])
        category_entry.insert(0, product[4])


product_id_label = tk.Label(Product_page, text="Product ID:")
product_id_label.pack()
product_id_entry = tk.Entry(Product_page)
product_id_entry.pack()

name_label = tk.Label(Product_page, text="Product name:")
name_label.pack()
name_entry = tk.Entry(Product_page)
name_entry.pack()

description_label = tk.Label(Product_page, text="Product description:")
description_label.pack()
description_entry = tk.Entry(Product_page)
description_entry.pack()

price_label = tk.Label(Product_page, text="Product price:")
price_label.pack()
price_entry = tk.Entry(Product_page)
price_entry.pack()

category_label = tk.Label(Product_page, text="Product category:")
category_label.pack()
category_entry = tk.Entry(Product_page)
category_entry.pack()


create_button_proudct = tk.Button(
    Product_page, text="Create/Update Proudct", command=create_product)
create_button_proudct.pack()

# result_label = tk.Label(Client_page, text="")
# result_label.pack()

Edit_Product = tk.Button(Product_page, text="Edit Product",
                         command=show_selected_products)
Edit_Product.pack()

products_columns = ("Product ID", "Name", "description", "price", "category")
products_treeview = ttk.Treeview(
    Product_page, columns=products_columns, show="headings")
for column in products_columns:
    products_treeview.heading(column, text=column)
    # Adjust column width as needed
    products_treeview.column(column, width=100)
products_treeview.pack()

fetch_products_button = tk.Button(
    Product_page, text="Fetch products", command=show_products)
fetch_products_button.pack()

delete_product_button = tk.Button(
    Product_page, text="Delete Product", command=delete_product)
delete_product_button.pack()


show_products()

## Employee #######
##################
##################
##################
##################
##################


class Employee:
    def __init__(self, employee_id, name, salary, phone):
        self.employee_id = employee_id
        self.name = name
        self.salary = salary
        self.phone = phone


def clear_employee_entry_fields():
    employee_id_entry.delete(0, 'end')
    employee_name_entry.delete(0, 'end')
    employee_salary_entry.delete(0, 'end')
    employee_phone_entry.delete(0, 'end')


def create_employee():
    employee_id = employee_id_entry.get()
    employee_name = employee_name_entry.get()
    employee_salary = employee_salary_entry.get()
    employee_phone = employee_phone_entry.get()

    employee = Employee(employee_id, employee_name,
                        employee_salary, employee_phone)
    cursor.execute(
        "SELECT employee_id FROM employee WHERE employee_id=?", (employee_id,))
    existing_employee = cursor.fetchone()

    if existing_employee:
        update_query = "UPDATE employee SET name = ?, salary = ?, phone = ? WHERE employee_id = ?"

        update_data = (employee.name, employee.salary,
                       employee.phone, employee.employee_id)

        cursor.execute(update_query, update_data)

        # Commit the changes to the database
        sqliteConnection.commit()

    else:

        insert_query = "INSERT INTO employee (employee_id, name, salary, phone) VALUES (?, ?, ?, ?)"
        employee_data = (employee.employee_id, employee.name,
                         employee.salary, employee.phone)
        cursor.execute(insert_query, employee_data)
        sqliteConnection.commit()

    show_employees()


def show_employees():
    for row in employee_treeview.get_children():
        employee_treeview.delete(row)

    cursor.execute("SELECT * FROM employee")
    employees = cursor.fetchall()

    for employee in employees:
        employee_treeview.insert("", "end", values=employee)


def delete_employee():
    selected_item = employee_treeview.selection()
    if selected_item:
        employee_id = employee_treeview.item(selected_item, 'values')[0]
        cursor.execute(
            "DELETE FROM employee WHERE employee_id=?", (employee_id,))
        sqliteConnection.commit()
    show_employees()  # Refresh the Treeview after deletion


def show_selected_employees():
    clear_employee_entry_fields()
    selected_item = employee_treeview.selection()
    if selected_item:
        employee = employee_treeview.item(selected_item, 'values')
        employee_id_entry.insert(0, employee[0])
        employee_name_entry.insert(0, employee[1])
        employee_salary_entry.insert(0, employee[2])
        employee_phone_entry.insert(0, employee[3])


employee_id_label = tk.Label(Employee_page, text="Employee ID:")
employee_id_label.pack()
employee_id_entry = tk.Entry(Employee_page)
employee_id_entry.pack()

employee_name_label = tk.Label(Employee_page, text="name:")
employee_name_label.pack()
employee_name_entry = tk.Entry(Employee_page)
employee_name_entry.pack()

employee_salary_label = tk.Label(Employee_page, text="salary:")
employee_salary_label.pack()
employee_salary_entry = tk.Entry(Employee_page)
employee_salary_entry.pack()

employee_phone_label = tk.Label(Employee_page, text="phone:")
employee_phone_label.pack()
employee_phone_entry = tk.Entry(Employee_page)
employee_phone_entry.pack()


create_button_employee = tk.Button(
    Employee_page, text="Create/Update Employee", command=create_employee)
create_button_employee.pack()


Edit_Employee = tk.Button(Employee_page, text="Edit Employee",
                          command=show_selected_employees)

Edit_Employee.pack()

employee_columns = ("Employee ID", "Name", "salary", "phone")

employee_treeview = ttk.Treeview(
    Employee_page, columns=employee_columns, show="headings")
for column in employee_columns:
    employee_treeview.heading(column, text=column)
    # Adjust column width as needed
    employee_treeview.column(column, width=100)
employee_treeview.pack()

fetch_employee_button = tk.Button(
    Employee_page, text="Fetch employee", command=show_employees)
fetch_employee_button.pack()

delete_employee_button = tk.Button(
    Employee_page, text="Delete employee", command=delete_employee)
delete_employee_button.pack()


show_employees()


## purchase #######
##################
##################
##################
##################
##################

class Purchase:
    def __init__(self, purchase_id, customer_id, product_id, employee_id, price, quantity, date):
        self.purchase_id = purchase_id
        self.customer_id = customer_id
        self.product_id = product_id
        self.employee_id = employee_id
        self.price = price
        self.quantity = quantity
        self.date = date


def clear_purchase_entry_fields():
    purchase_id_entry.delete(0, 'end')
    customer_id_purchase_entry.delete(0, 'end')
    product_id_purchase_entry.delete(0, 'end')
    employee_id_purchase_entry.delete(0, 'end')
    purchase_price_entry.delete(0, 'end')
    purchase_quantity_entry.delete(0, 'end')
    purchase_date_entry.delete(0, 'end')


def create_purchase():
    purchase_id = purchase_id_entry.get()
    customer_id = customer_id_purchase_entry.get()
    product_id = product_id_purchase_entry.get()
    employee_id = employee_id_purchase_entry.get()
    price = purchase_price_entry.get()
    quantity = purchase_quantity_entry.get()
    date = purchase_id_entry.get()

    purchase = Purchase(purchase_id, customer_id, product_id,
                        employee_id, price, quantity, date)
    cursor.execute(
        "SELECT purchase_id FROM purchase WHERE purchase_id=?", (purchase_id,))
    existing_purchase = cursor.fetchone()

    if existing_purchase:

        update_query = "UPDATE purchase SET customer_id = ?, product_id = ? ,employee_id = ? , price=? ,quantity= ? ,purchase_date=? WHERE purchase_id = ?"

        # Values to be updated in the database
        update_data = (purchase.customer_id, purchase.product_id, purchase.employee_id,
                       purchase.price, purchase.quantity, purchase.date, purchase.purchase_id)

        cursor.execute(update_query, update_data)

        # Commit the changes to the database
        sqliteConnection.commit()

    else:
        insert_query = "INSERT INTO purchase (purchase_id, customer_id, product_id, employee_id, price, quantity, purchase_date) VALUES (?, ?, ?, ?, ?, ? , ?)"
        purchase_data = (purchase.purchase_id, purchase.customer_id, purchase.product_id,
                         purchase.employee_id, purchase.price, purchase.quantity, purchase.date)
        cursor.execute(insert_query, purchase_data)

        sqliteConnection.commit()

    show_purchases()


def show_purchases():
    for row in purchases_treeview.get_children():
        purchases_treeview.delete(row)

    cursor.execute("SELECT * FROM purchase")
    purchases = cursor.fetchall()

    for purchase in purchases:
        purchases_treeview.insert("", "end", values=purchase)


def delete_purchase():
    selected_item = purchases_treeview.selection()
    if selected_item:
        purchase_id = purchases_treeview.item(selected_item, 'values')[0]
        cursor.execute(
            "DELETE FROM purchase WHERE purchase_id=?", (purchase_id,))
        sqliteConnection.commit()
        show_purchases()  # Refresh the Treeview after deletion


def show_selected_products():
    clear_product_entry_fields()
    selected_item = products_treeview.selection()
    if selected_item:
        product = products_treeview.item(selected_item, 'values')
        product_id_entry.insert(0, product[0])
        name_entry.insert(0, product[1])
        description_entry.insert(0, product[2])
        price_entry.insert(0, product[3])
        category_entry.insert(0, product[4])


purchase_id_label = tk.Label(Purchase_page, text="Purchase ID:")
purchase_id_label.pack()
purchase_id_entry = tk.Entry(Purchase_page)
purchase_id_entry.pack()


customer_id_purchase_label = tk.Label(Purchase_page, text="costumer ID:")
customer_id_purchase_label.pack()
customer_id_purchase_entry = tk.Entry(Purchase_page)
customer_id_purchase_entry.pack()

product_id_purchase_label = tk.Label(Purchase_page, text="purchase ID:")
product_id_purchase_label.pack()
product_id_purchase_entry = tk.Entry(Purchase_page)
product_id_purchase_entry.pack()

employee_id_purchase_label = tk.Label(Purchase_page, text="employee ID:")
employee_id_purchase_label.pack()
employee_id_purchase_entry = tk.Entry(Purchase_page)
employee_id_purchase_entry.pack()

purchase_price_label = tk.Label(Purchase_page, text="Pruchase price:")
purchase_price_label.pack()
purchase_price_entry = tk.Entry(Purchase_page)
purchase_price_entry.pack()

purchase_quantity_label = tk.Label(Purchase_page, text="Quantity:")
purchase_quantity_label.pack()
purchase_quantity_entry = tk.Entry(Purchase_page)
purchase_quantity_entry.pack()


purchase_date_label = tk.Label(Purchase_page, text="date:")
purchase_date_label.pack()
purchase_date_entry = tk.Entry(Purchase_page)
purchase_date_entry.pack()

create_button_purchase = tk.Button(
    Purchase_page, text="Create/Update Purchase", command=create_purchase)
create_button_purchase.pack()

# result_label = tk.Label(Client_page, text="")
# result_label.pack()

Edit_Product = tk.Button(Product_page, text="Edit Product",
                         command=show_selected_products)
Edit_Product.pack()

purchases_columns = ("purchase_id", "customer_id", "product_id",
                     "employee_id", "price", "quantity", "purchase_date")
purchases_treeview = ttk.Treeview(
    Purchase_page, columns=purchases_columns, show="headings")
for column in purchases_columns:
    purchases_treeview.heading(column, text=column)
    # Adjust column width as needed
    purchases_treeview.column(column, width=100)
purchases_treeview.pack()

fetch_pruchases_button = tk.Button(
    Purchase_page, text="Fetch purchases", command=show_purchases)
fetch_pruchases_button.pack()

delete_purchase_button = tk.Button(
    Purchase_page, text="Delete purchase", command=delete_purchase)
delete_purchase_button.pack()


show_purchases()


app.mainloop()
