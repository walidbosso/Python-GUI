#!/usr/bin/env python
# coding: utf-8

# 
# <hr>
# <div style="color:green;text-align:center; font-size:30px"> Pharmacy Management using Files </div><br>
# <div style="color:green;text-align:center; font-size:30px"> BOUSSOU Walid and KAIS Zakaria </div>
# <hr>

# # CRUD Operations:
# ## The choice of classes in our case were Client, Puchase, Product and Employee.
# 
# ### The methods implemented are:
# 
# > - Create
# > - Read_all & read
# > - Update
# > - Delete
# 
# ---
# 
# # Client:

# In[12]:


# CRUD operations for Client
class Client:
    file_path = "clients.txt"
    def __init__(self, client_id, first_name, last_name, number):
        self.id = client_id
        self.first_name = first_name
        self.last_name = last_name
        self.number = number

    @classmethod
    def create(cls, client):
        with open(cls.file_path, 'a') as file:
            file.write(f"{client.id},{client.first_name},{client.last_name},{client.number}\n")

    @classmethod
    def read_all(cls):
        clients = []
        with open(cls.file_path, 'r') as file:
            for line in file:
                data = line.strip().split(',')
                client = {'id': data[0], 'first_name': data[1], 'last_name': data[2], 'number': data[3]}
                clients.append(client)
        return clients
            
    @classmethod
    def read(cls, client_id):
        with open(cls.file_path, 'r') as file:
            for line in file:
                data = line.strip().split(',')
                if data[0] == client_id:
                    return {'id': data[0], 'first_name': data[1], 'last_name': data[2], 'number': data[3]}
            return None

    @classmethod
    def update(cls, client_id, new_data):
        data = []
        with open(cls.file_path, 'r') as file:
            for line in file:
                if line.startswith(client_id):
                    data.append(f"{new_data['id']},{new_data['first_name']},{new_data['last_name']},{new_data['number']}\n")
                else:
                    data.append(line)
        with open(cls.file_path, 'w') as file:
            file.writelines(data)

    @classmethod
    def delete(cls, client_id):
        data = []
        with open(cls.file_path, 'r') as file:
            for line in file:
                if not line.startswith(client_id):
                    data.append(line)
        with open(cls.file_path, 'w') as file:
            file.writelines(data)


# Demonstration:
# Creating a client
client = Client("1", "Walid", "Doe", "123456789")
Client.create(client)
client = Client("2", "Zak", "Doe", "123456789")
Client.create(client)
client = Client("3", "Hind", "Doe", "123456789")
Client.create(client)
client = Client("4", "Munir", "Doe", "123456789")
Client.create(client)

# Reading a client
result = Client.read("1")
print(result)

# Updating a client
new_data = {'id': '2', 'first_name': 'Johnny', 'last_name': 'Doey', 'number': '987654321'}
Client.update("2", new_data)

# Deleting a client
Client.delete("1")

# Reading all clients
result = Client.read_all()
print(result)




# ---
# 
# # CRUD Operations for Purchases
# 
# ---
# 

# In[14]:


# CRUD operations for Purchase
class Purchase:
    file_path = "purchases.txt"

    def __init__(self, purchase_id, client_id, product_id, employee_id, price, quantity, date):
        self.id = purchase_id
        self.client_id = client_id
        self.product_id = product_id
        self.employee_id = employee_id
        self.price = price
        self.quantity = quantity
        self.date = date

    @classmethod
    def create(cls, purchase):
        with open(cls.file_path, 'a') as file:
            file.write(f"{purchase.id},{purchase.client_id},{purchase.product_id},{purchase.employee_id},{purchase.price},{purchase.quantity},{purchase.date}\n")

    @classmethod
    def read_all(cls):
        purchases = []
        with open(cls.file_path, 'r') as file:
            for line in file:
                data = line.strip().split(',')
                purchase = {'id': data[0], 'client_id': data[1], 'product_id': data[2], 'employee_id': data[3], 'price': data[4], 'quantity': data[5], 'date': data[6]}
                purchases.append(purchase)
        return purchases

    @classmethod
    def read(cls, purchase_id):
        with open(cls.file_path, 'r') as file:
            for line in file:
                data = line.strip().split(',')
                if data[0] == purchase_id:
                    return {'id': data[0], 'client_id': data[1], 'product_id': data[2], 'employee_id': data[3], 'price': data[4], 'quantity': data[5], 'date': data[6]}
            return None

    @classmethod
    def update(cls, purchase_id, new_data):
        data = []
        with open(cls.file_path, 'r') as file:
            for line in file:
                if line.startswith(purchase_id):
                    data.append(f"{new_data['id']},{new_data['client_id']},{new_data['product_id']},{new_data['employee_id']},{new_data['price']},{new_data['quantity']},{new_data['date']}\n")
                else:
                    data.append(line)
        with open(cls.file_path, 'w') as file:
            file.writelines(data)

    @classmethod
    def delete(cls, purchase_id):
        data = []
        with open(cls.file_path, 'r') as file:
            for line in file:
                if not line.startswith(purchase_id):
                    data.append(line)
        with open(cls.file_path, 'w') as file:
            file.writelines(data)
            
# Example usage for Purchase class
from datetime import datetime

# Creating  purchase
for i in range(1,5):
    purchase = Purchase(i, "123", "456", "789", "100", "2", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    Purchase.create(purchase)

# Reading all purchases
all_purchases = Purchase.read_all()
print("All purchases:")
for purchase in all_purchases:
    print(purchase)

# Reading a specific purchase
purchase_id = "1"
result = Purchase.read(purchase_id)
print(f"Purchase with ID {purchase_id}:")
print(result)

# Updating a purchase
new_data = {'id': '2', 'client_id': '123', 'product_id': '789', 'employee_id': '999', 'price': '120', 'quantity': '20', 'date': datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
Purchase.update("2", new_data)

# Deleting a purchase
Purchase.delete("1")

# Reading all purchases
all_purchases = Purchase.read_all()
print("All purchases:")
for purchase in all_purchases:
    print(purchase)


# ---
# 
# # CRUD Operations for Product
# 
# ---

# In[15]:


# CRUD operations for Product
class Product:
    file_path = "products.txt"

    def __init__(self, product_id, name, description, price):
        self.id = product_id
        self.name = name
        self.description = description
        self.price = price

    @classmethod
    def create(cls, product):
        with open(cls.file_path, 'a') as file:
            file.write(f"{product.id},{product.name},{product.description},{product.price}\n")

    @classmethod
    def read_all(cls):
        products = []
        with open(cls.file_path, 'r') as file:
            for line in file:
                data = line.strip().split(',')
                product = {'id': data[0], 'name': data[1], 'description': data[2], 'price': data[3]}
                products.append(product)
        return products

    @classmethod
    def read(cls, product_id):
        with open(cls.file_path, 'r') as file:
            for line in file:
                data = line.strip().split(',')
                if data[0] == product_id:
                    return {'id': data[0], 'name': data[1], 'description': data[2], 'price': data[3]}
            return None

    @classmethod
    def update(cls, product_id, new_data):
        data = []
        with open(cls.file_path, 'r') as file:
            for line in file:
                if line.startswith(product_id):
                    data.append(f"{new_data['id']},{new_data['name']},{new_data['description']},{new_data['price']}\n")
                else:
                    data.append(line)
        with open(cls.file_path, 'w') as file:
            file.writelines(data)

    @classmethod
    def delete(cls, product_id):
        data = []
        with open(cls.file_path, 'r') as file:
            for line in file:
                if not line.startswith(product_id):
                    data.append(line)
        with open(cls.file_path, 'w') as file:
            file.writelines(data)

# Example usage for Pharmacy Product class
# Creating pharmacy products
for i in range (1,5):
    pharmacy_product = Product(i, "Aspirin", "Pain reliever", "5")
    Product.create(pharmacy_product)

# Reading all pharmacy products
all_pharmacy_products = Product.read_all()
print("All pharmacy products:")
for product in all_pharmacy_products:
    print(product)

# Reading a specific pharmacy product
product_id = "1"
result = Product.read(product_id)
print(f"Pharmacy product with ID {product_id}:")
print(result)

# Updating a pharmacy product
new_data = {'id': '2', 'name': 'Paracetamol', 'description': 'Fever and pain relief', 'price': '4'}
Product.update("2", new_data)

# Deleting a pharmacy product
Product.delete("1")

# Reading all pharmacy products
all_pharmacy_products = Product.read_all()
print("All pharmacy products after deleting:")
for product in all_pharmacy_products:
    print(product)


# ---
# 
# # CRUD Operations for Employee
# 
# ---

# In[16]:


# CRUD operations for Employee
class Employee:
    file_path = "employees.txt"

    def __init__(self, employee_id, name, salary, phone):
        self.id = employee_id
        self.name = name
        self.salary = salary
        self.phone = phone

    @classmethod
    def create(cls, employee):
        with open(cls.file_path, 'a') as file:
            file.write(f"{employee.id},{employee.name},{employee.salary},{employee.phone}\n")

    @classmethod
    def read_all(cls):
        employees = []
        with open(cls.file_path, 'r') as file:
            for line in file:
                data = line.strip().split(',')
                employee = {'id': data[0], 'name': data[1], 'salary': data[2], 'phone': data[3]}
                employees.append(employee)
        return employees

    @classmethod
    def read(cls, employee_id):
        with open(cls.file_path, 'r') as file:
            for line in file:
                data = line.strip().split(',')
                if data[0] == employee_id:
                    return {'id': data[0], 'name': data[1], 'salary': data[2], 'phone': data[3]}
            return None

    @classmethod
    def update(cls, employee_id, new_data):
        data = []
        with open(cls.file_path, 'r') as file:
            for line in file:
                if line.startswith(employee_id):
                    data.append(f"{new_data['id']},{new_data['name']},{new_data['salary']},{new_data['phone']}\n")
                else:
                    data.append(line)
        with open(cls.file_path, 'w') as file:
            file.writelines(data)

    @classmethod
    def delete(cls, employee_id):
        data = []
        with open(cls.file_path, 'r') as file:
            for line in file:
                if not line.startswith(employee_id):
                    data.append(line)
        with open(cls.file_path, 'w') as file:
            file.writelines(data)

# Example usage for Employee class
# Creating employees
for i in range(1,5):
    employee = Employee(i, "John Doe", "50000", "1234567890")
    Employee.create(employee)

# Reading all employees
all_employees = Employee.read_all()
print("All employees:")
for employee in all_employees:
    print(employee)

# Reading a specific employee
employee_id = "1"
result = Employee.read(employee_id)
print(f"Employee with ID {employee_id}:")
print(result)

# Updating an employee
new_data = {'id': '2', 'name': 'Jane Doe', 'salary': '60000', 'phone': '9876543210'}
Employee.update("2", new_data)

# Deleting an employee
Employee.delete("1")

# Reading all employees
all_employees = Employee.read_all()
print("All employees:")
for employee in all_employees:
    print(employee)


# <hr>
# <div style="color:green;text-align:center; font-size:30px"> Pharmacy Management using Files </div><br>
# <div style="color:green;text-align:center; font-size:30px"> BOUSSOU Walid and KAIS Zakaria </div>
# <hr>
