import sqlite3


sqliteConnection = sqlite3.connect('pharmacy.db')
cursor = sqliteConnection.cursor()
print("Successfully Connected to SQLite")



class Client:
    def __init__(self, client_id, first_name, last_name, number):
        self.client_id = client_id
        self.first_name = first_name
        self.last_name = last_name
        self.number = number

class Product:
    def __init__(self, product_id, name, description, price, category):
        self.product_id = product_id
        self.name = name
        self.description = description
        self.price = price
        self.category = category

class Purchase:
    def __init__(self, purchase_id, customer_id, product_id, employee_id, price, quantity, date):
        self.purchase_id = purchase_id
        self.customer_id = customer_id
        self.product_id = product_id
        self.employee_id = employee_id
        self.price = price
        self.quantity = quantity
        self.date = date

class Employee:
    def __init__(self, employee_id, name, salary, phone):
        self.employee_id = employee_id
        self.name = name
        self.salary = salary
        self.phone = phone

# Client

def create_client(client):
    insert_query = "INSERT INTO client (client_id, first_name, last_name, number) VALUES (?, ?, ?, ?)"
    client_data = (client.client_id, client.first_name, client.last_name, client.number)
    cursor.execute(insert_query, client_data)
    sqliteConnection.commit()
    print("client created successfuly")


def delete_client(id):
    delete_query = "DELETE FROM client WHERE client_id = ?"
    cursor.execute(delete_query, (id,))
    sqliteConnection.commit()
    print("client deleted successfuly")


def show_all_clients():
    # Define the SQL query to select all clients
    select_query = "SELECT * FROM client"

   
    cursor.execute(select_query)

    # Fetch all client records
    clients = cursor.fetchall()

    if clients:
        for client in clients:
            client_id, first_name, last_name, number = client
            print(f"Client ID: {client_id}")
            print(f"First Name: {first_name}")
            print(f"Last Name: {last_name}")
            print(f"Phone Number: {number}")
            print("--------")
    else:
        print("No clients found in the database.")

def update_client(client):

    update_query = "UPDATE client SET first_name = ?, last_name = ?, number = ? WHERE client_id = ?"

    # Values to be updated in the database
    update_data = (client.first_name, client.last_name, client.number, client.client_id)

    cursor.execute(update_query, update_data)

    # Commit the changes to the database
    sqliteConnection.commit()

    print(f"Client with ID {client.client_id} has been updated successfully.")

'''
client1 = Client(1, "John", "Doe", "123-456-7890")
client2 = Client(2, "Jane", "Smith", "987-654-3210")
create_client(client1)
create_client(client2)

show_all_clients()
client2 = Client(2, "hamza", "Smith", "987-654-3210")

update_client(client2)
show_all_clients()


'''

#product


def create_product(product):
    insert_query =" INSERT INTO product (product_id, name, description, price, category) VALUES (?, ?, ?, ?, ?)"
    product_data = (product.product_id, product.name, product.description, product.price, product.category)
    cursor.execute(insert_query, product_data)
    sqliteConnection.commit()
    print("product created successfuly")


def delete_product(id):
    delete_query = "DELETE FROM product WHERE product_id = ?"
    cursor.execute(delete_query, (id,))
    sqliteConnection.commit()
    print("product deleted successfuly")

def show_all_products():
    select_query = "SELECT * FROM product"
    cursor.execute(select_query)
    products = cursor.fetchall()
    if products:
        for product in products:
            product_id, name, description, price, category = product
            print(f"Product ID: {product_id}")
            print(f"name: {name}")
            print(f"description: {description}")
            print(f"price: {price}")
            print(f"category: {category}")



            print("--------")
    else:
        print("No products found in the database.")

def update_product(product):
    update_query = "UPDATE product SET name = ?, description = ?, price = ?, category=? WHERE product_id = ?"

    # Values to be updated in the database
    update_data = (product.name, product.description, product.price, product.category,product.product_id)

    cursor.execute(update_query, update_data)

    # Commit the changes to the database
    sqliteConnection.commit()

    print(f"Product with ID {product.product_id} has been updated successfully.")

'''
product1 = Product(1, "Product A", "Description A", 19.99, "Category X")
product2 = Product(2, "Product B", "Description B", 29.99, "Category Y")
product3 = Product(3, "Product c", "Description c", 29.59, "Category z")

create_product(product1)
create_product(product2)
create_product(product3)

show_all_products()
delete_product(product3.product_id)
product2.price=0.5
update_product(product2)
show_all_products()
'''

#employee
#employee_id, name, salary, phone


def create_employee(employee):
    insert_query = "INSERT INTO employee (employee_id, name, salary, phone) VALUES (?, ?, ?, ?)"
    employee_data = (employee.employee_id, employee.name, employee.salary, employee.phone)
    cursor.execute(insert_query, employee_data)
    sqliteConnection.commit()
    print("employee created successfuly")


def delete_employee(id):
    delete_query = "DELETE FROM employee WHERE employee_id = ?"
    cursor.execute(delete_query, (id,))
    sqliteConnection.commit()
    print("employee deleted successfuly")


def show_all_employees():
    select_query = "SELECT * FROM employee"

   
    cursor.execute(select_query)

    # Fetch all client records
    employees = cursor.fetchall()

    if employees:
        for employee in employees:
            employee_id, name, salary, phone = employee
            print(f"employee ID: {employee_id}")
            print(f"Name: {name}")
            print(f"phone: {salary}")
            print(f"salary: {phone}")
            print("--------")
    else:
        print("No employees found in the database.")

def update_employee(employee):

    update_query = "UPDATE employee SET name = ?, salary = ?, phone = ? WHERE employee_id = ?"

    # Values to be updated in the database
    update_data = (employee.name, employee.salary, employee.phone, employee.employee_id)

    cursor.execute(update_query, update_data)

    # Commit the changes to the database
    sqliteConnection.commit()

    print(f"Employee with ID {employee.employee_id} has been updated successfully.")


'''
employee1 = Employee(1, "John Smith", 50000.00, "555-123-4567")
employee2 = Employee(2, "Jane Doe", 60000.00, "555-987-6543")
employee3 = Employee(3, "Jane zak", 7512.00, "5557-654543")




create_employee(employee1)
create_employee(employee2)
create_employee(employee3)


show_all_employees()
delete_employee(employee3.employee_id)
employee2.name="zakaria kais"
update_employee(employee2)
show_all_employees()

'''
# purchase 
#purchase_id, customer_id, product_id, employee_id, price, quantity, date
def create_purchase(purchase):
    insert_query = "INSERT INTO purchase (purchase_id, customer_id, product_id, employee_id, price, quantity, purchase_date) VALUES (?, ?, ?, ?, ?, ? , ?)"
    purchase_data = (purchase.purchase_id, purchase.customer_id, purchase.product_id, purchase.employee_id, purchase.price, purchase.quantity, purchase.date)
    cursor.execute(insert_query, purchase_data)
    sqliteConnection.commit()
    print("purchase created successfuly")

def delete_purchase(id):
    delete_query = "DELETE FROM purchase WHERE purchase_id = ?"
    cursor.execute(delete_query, (id,))
    sqliteConnection.commit()
    print("purchase deleted successfuly")

def show_all_purchases():
    select_query = "SELECT * FROM purchase"


    cursor.execute(select_query)

    # Fetch all client records
    purchases = cursor.fetchall()

    if purchases:
        for purchase in purchases:
            purchase_id, customer_id, product_id, employee_id, price, quantity, date = purchase
            print(f"purchase ID: {purchase_id}")
            print(f"customer ID: {customer_id}")
            print(f"product ID: {product_id}")
            print(f"employee ID: {employee_id}")
            print(f"price: {price}")
            print(f"quantity: {quantity}")
            print(f"date: {date}")

            
    else:
        print("No purchases found in the database.")


def update_purchase(purchase):

    update_query = "UPDATE purchase SET customer_id = ?, product_id = ? ,employee_id = ? , price=? ,quantity= ? ,purchase_date=? WHERE purchase_id = ?"

    # Values to be updated in the database
    update_data = (purchase.customer_id, purchase.product_id, purchase.employee_id, purchase.price, purchase.quantity, purchase.date ,purchase.purchase_id)

    cursor.execute(update_query, update_data)

    # Commit the changes to the database
    sqliteConnection.commit()

    print(f"purchase with ID {purchase.purchase_id} has been updated successfully.")



employee1 = Employee(1, "John Smith", 50000.00, "555-123-4567")
employee2 = Employee(2, "Jane Doe", 60000.00, "555-987-6543")
employee3 = Employee(3, "Jane zak", 7512.00, "5557-654543")

product1 = Product(1, "Product A", "Description A", 19.99, "Category X")
product2 = Product(2, "Product B", "Description B", 29.99, "Category Y")
product3 = Product(3, "Product c", "Description c", 29.59, "Category z")


client1 = Client(1, "John", "Doe", "123-456-7890")
client2 = Client(2, "Jane", "Smith", "987-654-3210")


purchase1 = Purchase(1, 1, 1, 1, 19.99, 2, "2023-10-15")
purchase2 = Purchase(2, 2, 2, 2, 29.99, 3, "2023-10-16")

create_purchase(purchase1)
create_purchase(purchase2)
purchase2.quantity=500
update_purchase(purchase2)
show_all_purchases()