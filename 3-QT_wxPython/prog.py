import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QTableWidgetItem
import sqlite3

sqliteConnection = sqlite3.connect('pharmacy.db')
cursor = sqliteConnection.cursor()
print("Successfully Connected to SQLite")
# Function to create a Client instance


# client
# "
# ##########
# ########"


def client_window():
    EmployeeUI.hide()
    ProductUI.hide()
    PurchaseUI.hide()
    ClientUI.show()
    display_clients()


class Client:
    def __init__(self, client_id, first_name, last_name, number):
        self.client_id = client_id
        self.first_name = first_name
        self.last_name = last_name
        self.number = number


def display_clients():
    tableWidget = ClientUI.ClientsTable
    tableWidget.clearContents()
    tableWidget.setRowCount(0)
    cursor.execute("SELECT * FROM client")
    clients = cursor.fetchall()
    for row, client in enumerate(clients):
        client_id, first_name, last_name, number = client  # Unpack the tuple
        client_id_item = QTableWidgetItem(str(client_id))
        first_name_item = QTableWidgetItem(first_name)
        last_name_item = QTableWidgetItem(last_name)
        number_item = QTableWidgetItem(number)

        tableWidget.insertRow(row)
        tableWidget.setItem(row, 0, client_id_item)
        tableWidget.setItem(row, 1, first_name_item)
        tableWidget.setItem(row, 2, last_name_item)
        tableWidget.setItem(row, 3, number_item)


def edit_selected_client():
    tableWidget = ClientUI.ClientsTable
    selected_items = tableWidget.selectedItems()
    if selected_items:
        # Get the row of the first selected item
        selected_row = selected_items[0].row()
        print(selected_row)
        selected_values = []
        for column in range(4):  # Assuming you have 4 columns
            item = tableWidget.item(selected_row, column)
            selected_values.append(item.text())
        print(selected_values)

        ClientUI.client_Id.setText(str(selected_values[0]))
        ClientUI.client_firstName.setText(selected_values[1])
        ClientUI.client_lastname.setText(selected_values[2])
        ClientUI.client_number.setText(selected_values[3])


def createClient():
    client_id = ClientUI.client_Id.text()
    first_name = ClientUI.client_firstName.text()
    last_name = ClientUI.client_lastname.text()
    number = ClientUI.client_number.text()

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
    display_clients()


def delete_client():
    tableWidget = ClientUI.ClientsTable
    selected_item = tableWidget.selectedItems()
    if selected_item:
        selected_row = selected_item[0].row()

        item = tableWidget.item(selected_row, 0)
        client_id = item.text()

        cursor.execute("DELETE FROM client WHERE client_id=?", (client_id,))
        sqliteConnection.commit()
        display_clients()  # Refresh the Treeview after deletion


## Employee #######
##################
##################
##################
##################
##################

def employee_window():
    ClientUI.hide()
    PurchaseUI.hide()
    EmployeeUI.show()
    display_employees()
    EmployeeUI.createEmployee.clicked.connect(createEmployee)
    EmployeeUI.deleteEmployee.clicked.connect(delete_employee)
    EmployeeUI.editEmployee.clicked.connect(edit_selected_employee)


class Employee:
    def __init__(self, employee_id, name, salary, phone):
        self.employee_id = employee_id
        self.name = name
        self.salary = salary
        self.phone = phone


def display_employees():
    tableWidget = EmployeeUI.EmployeesTable
    tableWidget.clearContents()
    tableWidget.setRowCount(0)
    cursor.execute("SELECT * FROM employee")
    employees = cursor.fetchall()
    for row, employee in enumerate(employees):
        employee_id, name, salary, number = employee  # Unpack the tuple
        employee_id_item = QTableWidgetItem(str(employee_id))
        name_item = QTableWidgetItem(name)
        salary_item = QTableWidgetItem(str(salary))
        number_item = QTableWidgetItem(number)

        tableWidget.insertRow(row)
        tableWidget.setItem(row, 0, employee_id_item)
        tableWidget.setItem(row, 1, name_item)
        tableWidget.setItem(row, 2, salary_item)
        tableWidget.setItem(row, 3, number_item)


def createEmployee():

    employee_id = EmployeeUI.employee_id.text()
    employee_name = EmployeeUI.employee_fullName.text()
    employee_salary = EmployeeUI.employee_salary.text()
    employee_phone = EmployeeUI.employee_number.text()

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
    display_employees()


def delete_employee():
    tableWidget = EmployeeUI.EmployeesTable
    selected_item = tableWidget.selectedItems()
    if selected_item:
        selected_row = selected_item[0].row()

        item = tableWidget.item(selected_row, 0)
        employee_id = item.text()

        cursor.execute(
            "DELETE FROM employee WHERE employee_id=?", (employee_id,))
        sqliteConnection.commit()
        display_employees()


def edit_selected_employee():
    tableWidget = EmployeeUI.EmployeesTable
    selected_items = tableWidget.selectedItems()
    if selected_items:
        # Get the row of the first selected item
        selected_row = selected_items[0].row()
        selected_values = []
        for column in range(4):  # Assuming you have 4 columns
            item = tableWidget.item(selected_row, column)
            selected_values.append(item.text())

        EmployeeUI.employee_id.setText(str(selected_values[0]))
        EmployeeUI.employee_fullName.setText(selected_values[1])
        EmployeeUI.employee_salary.setText(str(selected_values[2]))
        EmployeeUI.employee_number.setText(selected_values[3])

##########
##########
## PRODUCT##
##########
##########


class Product:
    def __init__(self, product_id, name, description, price, category):
        self.product_id = product_id
        self.name = name
        self.description = description
        self.price = price
        self.category = category


def product_window():
    ClientUI.hide()
    EmployeeUI.hide()
    PurchaseUI.hide()
    ProductUI.show()
    display_products()


def display_products():
    tableWidget = ProductUI.productsTable
    tableWidget.clearContents()
    tableWidget.setRowCount(0)
    cursor.execute("SELECT * FROM product")
    products = cursor.fetchall()
    for row, product in enumerate(products):

        product_id, name, description, price, category = product  # Unpack the tuple
        product_id_item = QTableWidgetItem(str(product_id))
        name_item = QTableWidgetItem(name)
        description_item = QTableWidgetItem(description)
        price_item = QTableWidgetItem(str(price))
        category_item = QTableWidgetItem(category)

        tableWidget.insertRow(row)

        tableWidget.setItem(row, 0, product_id_item)
        tableWidget.setItem(row, 1, name_item)
        tableWidget.setItem(row, 2, description_item)
        tableWidget.setItem(row, 3, price_item)
        tableWidget.setItem(row, 4, category_item)


def createProduct():
    # product_id, name, description, price, category
    product_id = ProductUI.product_Id.text()
    name = ProductUI.product_name.text()
    description = ProductUI.product_description.text()
    price = ProductUI.product_price.text()
    category = ProductUI.product_category.text()

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
    display_products()


def edit_selected_product():
    tableWidget = ProductUI.productsTable
    selected_items = tableWidget.selectedItems()
    if selected_items:
        # Get the row of the first selected item
        selected_row = selected_items[0].row()
        selected_values = []
        for column in range(5):  # Assuming you have 4 columns
            item = tableWidget.item(selected_row, column)
            selected_values.append(item.text())
        ProductUI.product_Id.setText(str(selected_values[0]))
        ProductUI.product_name.setText(selected_values[1])
        ProductUI.product_description.setText(selected_values[2])
        ProductUI.product_price.setText(str(selected_values[3]))
        ProductUI.product_category.setText(selected_values[4])


def delete_product():
    tableWidget = ProductUI.productsTable
    selected_item = tableWidget.selectedItems()
    if selected_item:
        selected_row = selected_item[0].row()

        item = tableWidget.item(selected_row, 0)
        product_id = item.text()

        cursor.execute(
            "DELETE FROM product WHERE product_id=?", (product_id,))
        sqliteConnection.commit()
        display_products()


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


def purchase_window():
    ClientUI.hide()
    EmployeeUI.hide()
    ProductUI.hide()
    PurchaseUI.show()
    display_purchases()


def display_purchases():
    tableWidget = PurchaseUI.PurchasesTable
    tableWidget.clearContents()
    tableWidget.setRowCount(0)
    cursor.execute("SELECT * FROM purchase")
    purchases = cursor.fetchall()

    for row, purchase in enumerate(purchases):
        # purchase_id, customer_id, product_id, employee_id, price, quantity,date
        # Unpack the tuple

        purchase_id, customer_id, product_id, employee_id, price, quantity, date = purchase
        purchase_id_item = QTableWidgetItem(str(purchase_id))
        customer_id_item = QTableWidgetItem(str(customer_id))
        product_id_item = QTableWidgetItem(str(product_id))
        employee_id_item = QTableWidgetItem(str(employee_id))
        price_item = QTableWidgetItem(str(price))
        quantity_item = QTableWidgetItem(str(quantity))

        date_item = QTableWidgetItem(str(date))

        tableWidget.insertRow(row)

        tableWidget.setItem(row, 0, purchase_id_item)
        tableWidget.setItem(row, 1, customer_id_item)
        tableWidget.setItem(row, 2, product_id_item)
        tableWidget.setItem(row, 3, employee_id_item)
        tableWidget.setItem(row, 4, price_item)
        tableWidget.setItem(row, 5, quantity_item)


def createPurchase():
    # purchase_id, customer_id, product_id, employee_id, price, quantity,date
    purchase_id = PurchaseUI.purchase_Id.text()
    customer_id = PurchaseUI.purchase_customerId.text()
    product_id = PurchaseUI.purchase_productId.text()
    employee_id = PurchaseUI.purchase_employeeId.text()
    price = PurchaseUI.purchase_price.text()
    quantity = PurchaseUI.purchase_quantity.text()

    purchase = Purchase(purchase_id, customer_id, product_id,
                        employee_id, price, quantity, None)
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

    display_purchases()


def edit_selected_purchase():
    tableWidget = PurchaseUI.PurchasesTable
    selected_items = tableWidget.selectedItems()
    if selected_items:
        # Get the row of the first selected item
        selected_row = selected_items[0].row()
        selected_values = []
        for column in range(6):  # Assuming you have 4 columns
            item = tableWidget.item(selected_row, column)
            selected_values.append(item.text())

        PurchaseUI.purchase_Id.setText(str(selected_values[0]))
        PurchaseUI.purchase_customerId.setText(str(selected_values[1]))
        PurchaseUI.purchase_productId.setText(str(selected_values[2]))
        PurchaseUI.purchase_employeeId.setText(str(selected_values[3]))
        PurchaseUI.purchase_price.setText(str(selected_values[4]))
        PurchaseUI.purchase_quantity.setText(str(selected_values[5]))


def delete_purchase():
    tableWidget = PurchaseUI.PurchasesTable
    selected_item = tableWidget.selectedItems()
    if selected_item:
        selected_row = selected_item[0].row()

        item = tableWidget.item(selected_row, 0)
        purchase_id = item.text()

        cursor.execute(
            "DELETE FROM purchase WHERE purchase_id=?", (purchase_id,))
        sqliteConnection.commit()
        display_purchases()


App = QtWidgets.QApplication(sys.argv)
EmployeeUI = uic.loadUi("Employee_ui.ui")
EmployeeUI.createEmployee.clicked.connect(createEmployee)
EmployeeUI.deleteEmployee.clicked.connect(delete_employee)
EmployeeUI.editEmployee.clicked.connect(edit_selected_employee)

PurchaseUI = uic.loadUi("purchase_ui.ui")
PurchaseUI.createPurchase.clicked.connect(createPurchase)
PurchaseUI.deletePurchase.clicked.connect(delete_purchase)
PurchaseUI.editPurchase.clicked.connect(edit_selected_purchase)

ProductUI = uic.loadUi("product_ui.ui")
ProductUI.createProduct.clicked.connect(createProduct)
ProductUI.deleteProduct.clicked.connect(delete_product)
ProductUI.editProduct.clicked.connect(edit_selected_product)

ClientUI = uic.loadUi("client_ui.ui")
ClientUI.show()
ClientUI.createClient.clicked.connect(createClient)
ClientUI.editClient.clicked.connect(edit_selected_client)

ClientUI.deleteClient.clicked.connect(delete_client)


#

ClientUI.actionEmployee.triggered.connect(employee_window)

ClientUI.actionProduct.triggered.connect(product_window)

ClientUI.actionPurchase.triggered.connect(purchase_window)

#

EmployeeUI.actionClient.triggered.connect(client_window)

EmployeeUI.actionProduct.triggered.connect(product_window)

EmployeeUI.actionPurchase.triggered.connect(purchase_window)

#

PurchaseUI.actionClient.triggered.connect(client_window)

PurchaseUI.actionProduct.triggered.connect(product_window)

PurchaseUI.actionEmployee.triggered.connect(employee_window)

#


ProductUI.actionClient.triggered.connect(client_window)


ProductUI.actionEmployee.triggered.connect(employee_window)


ProductUI.actionPurchase.triggered.connect(purchase_window)


display_clients()
App.exec_()
sys.exit()
