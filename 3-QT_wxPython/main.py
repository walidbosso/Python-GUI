
import wx
import wx.grid
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


class Employee:
    def __init__(self, employee_id, name, salary, phone):
        self.employee_id = employee_id
        self.name = name
        self.salary = salary
        self.phone = phone


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


# import wx.aui


# class MainFrame(wx.Frame):
#   def __init__(self):
#      super(MainFrame, self).__init__(None, title="Main Window", size=(800, 600))
#     self.panel = wx.Panel(self)
#
#       self.notebook = wx.Notebook(self.panel)
#      self.client_panel = ClientUI(self.notebook)
#     self.employee_panel = EmployeeUI(self.notebook)
#    self.product_panel = ProductUI(self.notebook)
#   self.purchase_panel = PurchaseUI(self.notebook)
#
#       self.notebook.AddPage(self.client_panel, "Client")
#      self.notebook.AddPage(self.employee_panel, "Employee")
#     self.notebook.AddPage(self.product_panel, "Product")
#    self.notebook.AddPage(self.purchase_panel, "Purchase")
#
#       sizer = wx.BoxSizer(wx.VERTICAL)
#      sizer.Add(self.notebook, 1, wx.EXPAND | wx.ALL, 5)
#
#       self.panel.SetSizer(sizer)
#      self.Show()


class ClientUI(wx.Frame):
    def __init__(self):
        super(ClientUI, self).__init__(None, title="Client Window", size=(1100, 700))
        self.panel = wx.Panel(self)
        self.ClientsTable = wx.grid.Grid(self.panel)
        self.ClientsTable.CreateGrid(0, 4)
        self.ClientsTable.SetColLabelValue(0, "Client ID")
        self.ClientsTable.SetColLabelValue(1, "First Name")
        self.ClientsTable.SetColLabelValue(2, "Last Name")
        self.ClientsTable.SetColLabelValue(3, "Number")

        self.client_Id = wx.TextCtrl(self.panel)
        self.client_firstName = wx.TextCtrl(self.panel)
        self.client_lastname = wx.TextCtrl(self.panel)
        self.number = wx.TextCtrl(self.panel)

        self.edit_button = wx.Button(self.panel, label="Select Row to Edit")
        self.edit_button.Bind(wx.EVT_BUTTON, self.edit_selected_client)

        self.create_button = wx.Button(self.panel, label="Create/Update Client")
        self.create_button.Bind(wx.EVT_BUTTON, self.createClient)

        self.delete_button = wx.Button(self.panel, label="Delete Client")
        self.delete_button.Bind(wx.EVT_BUTTON, self.delete_client)

        sizer = wx.BoxSizer(wx.VERTICAL)
        # self.show_clients_button = wx.Button(self.panel, label="Show Clients")
        # self.show_clients_button.Bind(wx.EVT_BUTTON, lambda event: self.display_clients())
        # sizer.Add(self.show_clients_button, 0, wx.EXPAND | wx.ALL, 5)
        sizer.Add(self.ClientsTable, 1, wx.EXPAND | wx.ALL, 5)
        sizer.Add(wx.StaticText(self.panel, label="Client ID:"), 0, wx.ALL, 5)
        sizer.Add(self.client_Id, 0, wx.EXPAND | wx.ALL, 5)
        sizer.Add(wx.StaticText(self.panel, label="First Name:"), 0, wx.ALL, 5)
        sizer.Add(self.client_firstName, 0, wx.EXPAND | wx.ALL, 5)
        sizer.Add(wx.StaticText(self.panel, label="Last Name:"), 0, wx.ALL, 5)
        sizer.Add(self.client_lastname, 0, wx.EXPAND | wx.ALL, 5)
        sizer.Add(wx.StaticText(self.panel, label="Number:"), 0, wx.ALL, 5)
        sizer.Add(self.number, 0, wx.EXPAND | wx.ALL, 5)
        sizer.Add(self.edit_button, 0, wx.EXPAND | wx.ALL, 5)
        sizer.Add(self.create_button, 0, wx.EXPAND | wx.ALL, 5)
        sizer.Add(self.delete_button, 0, wx.EXPAND | wx.ALL, 5)

        self.panel.SetSizer(sizer)
        # self.panel.SetSizerAndFit(sizer)
        self.Show()
        self.display_clients()

    def edit_selected_client(self, event):
        table = self.ClientsTable
        selected_rows = table.GetSelectedRows()

        if selected_rows:
            selected_row = selected_rows[0]
            client_id = table.GetCellValue(selected_row, 0)
            first_name = table.GetCellValue(selected_row, 1)
            last_name = table.GetCellValue(selected_row, 2)
            number = table.GetCellValue(selected_row, 3)

            self.client_Id.SetValue(client_id)
            self.client_firstName.SetValue(first_name)
            self.client_lastname.SetValue(last_name)
            self.number.SetValue(number)

            cursor.execute("UPDATE client SET first_name=?, last_name=?, number=? WHERE client_id=?",
                           (first_name, last_name, number, client_id))
            sqliteConnection.commit()

            self.display_clients()

    def createClient(self, event):
        client_id = self.client_Id.GetValue()
        first_name = self.client_firstName.GetValue()
        last_name = self.client_lastname.GetValue()
        number = self.number.GetValue()

        client = Client(client_id, first_name, last_name, number)

        cursor.execute("SELECT client_id FROM client WHERE client_id=?", (client_id,))
        existing_client = cursor.fetchone()

        if existing_client:
            update_query = "UPDATE client SET first_name = ?, last_name = ?, number = ? WHERE client_id = ?"
            update_data = (client.first_name, client.last_name, client.number, client.client_id)
            cursor.execute(update_query, update_data)
            sqliteConnection.commit()
        else:
            insert_query = "INSERT INTO client (client_id, first_name, last_name, number) VALUES (?, ?, ?, ?)"
            client_data = (client.client_id, client.first_name, client.last_name, client.number)
            cursor.execute(insert_query, client_data)
            sqliteConnection.commit()

        self.display_clients()

    def delete_client(self, event):
        table = self.ClientsTable
        selected_rows = table.GetSelectedRows()

        if selected_rows:
            for selected_row in reversed(selected_rows):
                client_id = table.GetCellValue(selected_row, 0)

                cursor.execute("DELETE FROM client WHERE client_id=?", (client_id,))
                sqliteConnection.commit()

            self.display_clients()

    def display_clients(self):
        table = self.ClientsTable
        if table.GetNumberRows() > 0:
            table.ClearGrid()
            table.DeleteRows(pos=0, numRows=table.GetNumberRows())

        cursor.execute("SELECT * FROM client")
        clients = cursor.fetchall()

        for row, client in enumerate(clients):
            client_id, first_name, last_name, number = client
            table.AppendRows()
            table.SetCellValue(row, 0, str(client_id))
            table.SetCellValue(row, 1, first_name)
            table.SetCellValue(row, 2, last_name)
            table.SetCellValue(row, 3, number)


class EmployeeUI(wx.Frame):
    def __init__(self):
        super(EmployeeUI, self).__init__(None, title="EmployeeUI Window", size=(1100, 700))
        self.panel = wx.Panel(self)
        self.EmployeesTable = wx.grid.Grid(self.panel)
        self.EmployeesTable.CreateGrid(0, 4)
        self.EmployeesTable.SetColLabelValue(0, "Employee ID")
        self.EmployeesTable.SetColLabelValue(1, "Name")
        self.EmployeesTable.SetColLabelValue(2, "Salary")
        self.EmployeesTable.SetColLabelValue(3, "Phone")

        self.employee_id = wx.TextCtrl(self.panel)
        self.employee_fullName = wx.TextCtrl(self.panel)
        self.employee_salary = wx.TextCtrl(self.panel)
        self.employee_number = wx.TextCtrl(self.panel)

        self.edit_button = wx.Button(self.panel, label="Select Employee Row you want to Edit")
        self.edit_button.Bind(wx.EVT_BUTTON, self.edit_selected_employee)

        self.create_button = wx.Button(self.panel, label="Create/Update Employee")
        self.create_button.Bind(wx.EVT_BUTTON, self.createEmployee)

        self.delete_button = wx.Button(self.panel, label="Delete Employee")
        self.delete_button.Bind(wx.EVT_BUTTON, self.delete_employee)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.EmployeesTable, 1, wx.EXPAND | wx.ALL, 5)
        sizer.Add(wx.StaticText(self.panel, label="Employee ID:"), 0, wx.ALL, 5)
        sizer.Add(self.employee_id, 0, wx.EXPAND | wx.ALL, 5)
        sizer.Add(wx.StaticText(self.panel, label="Full Name:"), 0, wx.ALL, 5)
        sizer.Add(self.employee_fullName, 0, wx.EXPAND | wx.ALL, 5)
        sizer.Add(wx.StaticText(self.panel, label="Salary:"), 0, wx.ALL, 5)
        sizer.Add(self.employee_salary, 0, wx.EXPAND | wx.ALL, 5)
        sizer.Add(wx.StaticText(self.panel, label="Phone:"), 0, wx.ALL, 5)
        sizer.Add(self.employee_number, 0, wx.EXPAND | wx.ALL, 5)
        sizer.Add(self.edit_button, 0, wx.EXPAND | wx.ALL, 5)
        sizer.Add(self.create_button, 0, wx.EXPAND | wx.ALL, 5)
        sizer.Add(self.delete_button, 0, wx.EXPAND | wx.ALL, 5)

        self.panel.SetSizer(sizer)
        self.Show()
        self.display_employees()

    def edit_selected_employee(self, event):
        table = self.EmployeesTable
        selected_rows = table.GetSelectedRows()

        if selected_rows:
            selected_row = selected_rows[0]
            employee_id = table.GetCellValue(selected_row, 0)
            name = table.GetCellValue(selected_row, 1)
            salary = table.GetCellValue(selected_row, 2)
            phone = table.GetCellValue(selected_row, 3)

            self.employee_id.SetValue(employee_id)
            self.employee_fullName.SetValue(name)
            self.employee_salary.SetValue(salary)
            self.employee_number.SetValue(phone)

            cursor.execute("UPDATE employee SET name=?, salary=?, phone=? WHERE employee_id=?",
                           (name, salary, phone, employee_id))
            sqliteConnection.commit()

            self.display_employees()

    def createEmployee(self, event):
        employee_id = self.employee_id.GetValue()
        employee_name = self.employee_fullName.GetValue()
        employee_salary = self.employee_salary.GetValue()
        employee_phone = self.employee_number.GetValue()

        employee = Employee(employee_id, employee_name, employee_salary, employee_phone)

        cursor.execute("SELECT employee_id FROM employee WHERE employee_id=?", (employee_id,))
        existing_employee = cursor.fetchone()

        if existing_employee:
            update_query = "UPDATE employee SET name = ?, salary = ?, phone = ? WHERE employee_id = ?"
            update_data = (employee.name, employee.salary, employee.phone, employee.employee_id)
            cursor.execute(update_query, update_data)
            sqliteConnection.commit()
        else:
            insert_query = "INSERT INTO employee (employee_id, name, salary, phone) VALUES (?, ?, ?, ?)"
            employee_data = (employee.employee_id, employee.name, employee.salary, employee.phone)
            cursor.execute(insert_query, employee_data)
            sqliteConnection.commit()

        self.display_employees()

    def delete_employee(self, event):
        table = self.EmployeesTable
        selected_rows = table.GetSelectedRows()

        if selected_rows:
            for selected_row in reversed(selected_rows):
                employee_id = table.GetCellValue(selected_row, 0)

                cursor.execute("DELETE FROM employee WHERE employee_id=?", (employee_id,))
                sqliteConnection.commit()

            self.display_employees()

    def display_employees(self):
        table = self.EmployeesTable
        if table.GetNumberRows() > 0:
            table.ClearGrid()
            table.DeleteRows(pos=0, numRows=table.GetNumberRows())

        cursor.execute("SELECT * FROM employee")
        employees = cursor.fetchall()

        for row, employee in enumerate(employees):
            employee_id, name, salary, number = employee
            table.AppendRows()
            table.SetCellValue(row, 0, str(employee_id))
            table.SetCellValue(row, 1, name)
            table.SetCellValue(row, 2, str(salary))
            table.SetCellValue(row, 3, number)


class ProductUI(wx.Frame):
    def __init__(self):
        super(ProductUI, self).__init__(None, title="ProductUI Window", size=(1100, 700))
        self.panel = wx.Panel(self)
        self.ProductsTable = wx.grid.Grid(self.panel)
        self.ProductsTable.CreateGrid(0, 5)
        self.ProductsTable.SetColLabelValue(0, "Product ID")
        self.ProductsTable.SetColLabelValue(1, "Name")
        self.ProductsTable.SetColLabelValue(2, "Description")
        self.ProductsTable.SetColLabelValue(3, "Price")
        self.ProductsTable.SetColLabelValue(4, "Category")

        self.product_id = wx.TextCtrl(self.panel)
        self.product_name = wx.TextCtrl(self.panel)
        self.product_description = wx.TextCtrl(self.panel)
        self.product_price = wx.TextCtrl(self.panel)
        self.product_category = wx.TextCtrl(self.panel)

        self.edit_button = wx.Button(self.panel, label="Select Product you want to edit")
        self.edit_button.Bind(wx.EVT_BUTTON, self.edit_selected_product)

        self.create_button = wx.Button(self.panel, label="Create/Update Product")
        self.create_button.Bind(wx.EVT_BUTTON, self.createProduct)

        self.delete_button = wx.Button(self.panel, label="Delete Product")
        self.delete_button.Bind(wx.EVT_BUTTON, self.delete_product)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.ProductsTable, 1, wx.EXPAND | wx.ALL, 5)
        sizer.Add(wx.StaticText(self.panel, label="Product ID:"), 0, wx.ALL, 5)
        sizer.Add(self.product_id, 0, wx.EXPAND | wx.ALL, 5)
        sizer.Add(wx.StaticText(self.panel, label="Name:"), 0, wx.ALL, 5)
        sizer.Add(self.product_name, 0, wx.EXPAND | wx.ALL, 5)
        sizer.Add(wx.StaticText(self.panel, label="Description:"), 0, wx.ALL, 5)
        sizer.Add(self.product_description, 0, wx.EXPAND | wx.ALL, 5)
        sizer.Add(wx.StaticText(self.panel, label="Price:"), 0, wx.ALL, 5)
        sizer.Add(self.product_price, 0, wx.EXPAND | wx.ALL, 5)
        sizer.Add(wx.StaticText(self.panel, label="Category:"), 0, wx.ALL, 5)
        sizer.Add(self.product_category, 0, wx.EXPAND | wx.ALL, 5)
        sizer.Add(self.edit_button, 0, wx.EXPAND | wx.ALL, 5)
        sizer.Add(self.create_button, 0, wx.EXPAND | wx.ALL, 5)
        sizer.Add(self.delete_button, 0, wx.EXPAND | wx.ALL, 5)

        self.panel.SetSizer(sizer)
        self.Show()
        self.display_products()

    def edit_selected_product(self, event):
        table = self.ProductsTable
        selected_rows = table.GetSelectedRows()

        if selected_rows:
            selected_row = selected_rows[0]
            product_id = table.GetCellValue(selected_row, 0)
            name = table.GetCellValue(selected_row, 1)
            description = table.GetCellValue(selected_row, 2)
            price = table.GetCellValue(selected_row, 3)
            category = table.GetCellValue(selected_row, 4)

            self.product_id.SetValue(product_id)
            self.product_name.SetValue(name)
            self.product_description.SetValue(description)
            self.product_price.SetValue(price)
            self.product_category.SetValue(category)

            cursor.execute("UPDATE product SET name=?, description=?, price=?, category=? WHERE product_id=?",
                           (name, description, price, category, product_id))
            sqliteConnection.commit()

            self.display_products()

    def createProduct(self, event):
        product_id = self.product_id.GetValue()
        product_name = self.product_name.GetValue()
        product_description = self.product_description.GetValue()
        product_price = self.product_price.GetValue()
        product_category = self.product_category.GetValue()

        product = Product(product_id, product_name, product_description, product_price, product_category)

        cursor.execute("SELECT product_id FROM product WHERE product_id=?", (product_id,))
        existing_product = cursor.fetchone()

        if existing_product:
            update_query = "UPDATE product SET name = ?, description = ?, price = ?, category = ? WHERE product_id = ?"
            update_data = (product.name, product.description, product.price, product.category, product.product_id)
            cursor.execute(update_query, update_data)
            sqliteConnection.commit()
        else:
            insert_query = "INSERT INTO product (product_id, name, description, price, category) VALUES (?, ?, ?, ?, ?)"
            product_data = (product.product_id, product.name, product.description, product.price, product.category)
            cursor.execute(insert_query, product_data)
            sqliteConnection.commit()

        self.display_products()

    def delete_product(self, event):
        table = self.ProductsTable
        selected_rows = table.GetSelectedRows()

        if selected_rows:
            for selected_row in reversed(selected_rows):
                product_id = table.GetCellValue(selected_row, 0)

                cursor.execute("DELETE FROM product WHERE product_id=?", (product_id,))
                sqliteConnection.commit()

            self.display_products()

    def display_products(self):
        table = self.ProductsTable
        if table.GetNumberRows() > 0:
            table.ClearGrid()
            table.DeleteRows(pos=0, numRows=table.GetNumberRows())

        cursor.execute("SELECT * FROM product")
        products = cursor.fetchall()

        for row, product in enumerate(products):
            product_id, name, description, price, category = product
            table.AppendRows()
            table.SetCellValue(row, 0, str(product_id))
            table.SetCellValue(row, 1, name)
            table.SetCellValue(row, 2, description)
            table.SetCellValue(row, 3, str(price))
            table.SetCellValue(row, 4, category)


class PurchaseUI(wx.Frame):
    def __init__(self):
        super(PurchaseUI, self).__init__(None, title="PurchaseUI Window", size=(1100, 700))
        self.panel = wx.Panel(self)
        self.PurchasesTable = wx.grid.Grid(self.panel)
        self.PurchasesTable.CreateGrid(0, 7)
        self.PurchasesTable.SetColLabelValue(0, "Purchase ID")
        self.PurchasesTable.SetColLabelValue(1, "Customer ID")
        self.PurchasesTable.SetColLabelValue(2, "Product ID")
        self.PurchasesTable.SetColLabelValue(3, "Employee ID")
        self.PurchasesTable.SetColLabelValue(4, "Price")
        self.PurchasesTable.SetColLabelValue(5, "Quantity")
        self.PurchasesTable.SetColLabelValue(6, "Date")

        self.purchase_id = wx.TextCtrl(self.panel)
        self.customer_id = wx.TextCtrl(self.panel)
        self.product_id = wx.TextCtrl(self.panel)
        self.employee_id = wx.TextCtrl(self.panel)
        self.purchase_price = wx.TextCtrl(self.panel)
        self.purchase_quantity = wx.TextCtrl(self.panel)
        self.purchase_date = wx.TextCtrl(self.panel)

        self.edit_button = wx.Button(self.panel, label="Select Purchase Row you want to Edit")
        self.edit_button.Bind(wx.EVT_BUTTON, self.edit_selected_purchase)

        self.create_button = wx.Button(self.panel, label="Create/Update Purchase")
        self.create_button.Bind(wx.EVT_BUTTON, self.createPurchase)

        self.delete_button = wx.Button(self.panel, label="Delete Purchase")
        self.delete_button.Bind(wx.EVT_BUTTON, self.delete_purchase)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.PurchasesTable, 1, wx.EXPAND | wx.ALL, 5)
        sizer.Add(wx.StaticText(self.panel, label="Purchase ID:"), 0, wx.ALL, 5)
        sizer.Add(self.purchase_id, 0, wx.EXPAND | wx.ALL, 5)
        sizer.Add(wx.StaticText(self.panel, label="Customer ID:"), 0, wx.ALL, 5)
        sizer.Add(self.customer_id, 0, wx.EXPAND | wx.ALL, 5)
        sizer.Add(wx.StaticText(self.panel, label="Product ID:"), 0, wx.ALL, 5)
        sizer.Add(self.product_id, 0, wx.EXPAND | wx.ALL, 5)
        sizer.Add(wx.StaticText(self.panel, label="Employee ID:"), 0, wx.ALL, 5)
        sizer.Add(self.employee_id, 0, wx.EXPAND | wx.ALL, 5)
        sizer.Add(wx.StaticText(self.panel, label="Price:"), 0, wx.ALL, 5)
        sizer.Add(self.purchase_price, 0, wx.EXPAND | wx.ALL, 5)
        sizer.Add(wx.StaticText(self.panel, label="Quantity:"), 0, wx.ALL, 5)
        sizer.Add(self.purchase_quantity, 0, wx.EXPAND | wx.ALL, 5)
        sizer.Add(wx.StaticText(self.panel, label="Date:"), 0, wx.ALL, 5)
        sizer.Add(self.purchase_date, 0, wx.EXPAND | wx.ALL, 5)
        sizer.Add(self.edit_button, 0, wx.EXPAND | wx.ALL, 5)
        sizer.Add(self.create_button, 0, wx.EXPAND | wx.ALL, 5)
        sizer.Add(self.delete_button, 0, wx.EXPAND | wx.ALL, 5)

        self.panel.SetSizer(sizer)
        self.Show()
        self.display_purchases()

    def edit_selected_purchase(self, event):
        table = self.PurchasesTable
        selected_rows = table.GetSelectedRows()

        if selected_rows:
            selected_row = selected_rows[0]
            purchase_id = table.GetCellValue(selected_row, 0)
            customer_id = table.GetCellValue(selected_row, 1)
            product_id = table.GetCellValue(selected_row, 2)
            employee_id = table.GetCellValue(selected_row, 3)
            price = table.GetCellValue(selected_row, 4)
            quantity = table.GetCellValue(selected_row, 5)
            date = table.GetCellValue(selected_row, 6)

            self.purchase_id.SetValue(purchase_id)
            self.customer_id.SetValue(customer_id)
            self.product_id.SetValue(product_id)
            self.employee_id.SetValue(employee_id)
            self.purchase_price.SetValue(price)
            self.purchase_quantity.SetValue(quantity)
            self.purchase_date.SetValue(date)

            cursor.execute(
                "UPDATE purchase SET customer_id=?, product_id=?, employee_id=?, price=?, quantity=?, purchase_date=? WHERE purchase_id=?",
                (customer_id, product_id, employee_id, price, quantity, date, purchase_id))
            sqliteConnection.commit()

            self.display_purchases()

    def createPurchase(self, event):
        purchase_id = self.purchase_id.GetValue()
        customer_id = self.customer_id.GetValue()
        product_id = self.product_id.GetValue()
        employee_id = self.employee_id.GetValue()
        purchase_price = self.purchase_price.GetValue()
        purchase_quantity = self.purchase_quantity.GetValue()
        purchase_date = self.purchase_date.GetValue()

        purchase = Purchase(
            purchase_id, customer_id, product_id, employee_id, purchase_price, purchase_quantity, purchase_date
        )

        cursor.execute("SELECT purchase_id FROM purchase WHERE purchase_id=?", (purchase_id,))
        existing_purchase = cursor.fetchone()

        if existing_purchase:
            update_query = "UPDATE purchase SET customer_id = ?, product_id = ?, employee_id = ?, " \
                           "price = ?, quantity = ?, purchase_date = ? WHERE purchase_id = ?"
            update_data = (
                purchase.customer_id, purchase.product_id, purchase.employee_id,
                purchase.price, purchase.quantity, purchase.date, purchase.purchase_id
            )
            cursor.execute(update_query, update_data)
            sqliteConnection.commit()
        else:
            insert_query = "INSERT INTO purchase (purchase_id, customer_id, product_id, employee_id, " \
                           "price, quantity, purchase_date) VALUES (?, ?, ?, ?, ?, ?, ?)"
            purchase_data = (
                purchase.purchase_id, purchase.customer_id, purchase.product_id,
                purchase.employee_id, purchase.price, purchase.quantity, purchase.date
            )
            cursor.execute(insert_query, purchase_data)
            sqliteConnection.commit()

        self.display_purchases()

    def delete_purchase(self, event):
        table = self.PurchasesTable
        selected_rows = table.GetSelectedRows()

        if selected_rows:
            for selected_row in reversed(selected_rows):
                purchase_id = table.GetCellValue(selected_row, 0)

                cursor.execute("DELETE FROM purchase WHERE purchase_id=?", (purchase_id,))
                sqliteConnection.commit()

            self.display_purchases()

    def display_purchases(self):
        table = self.PurchasesTable
        if table.GetNumberRows() > 0:
            table.ClearGrid()
            table.DeleteRows(pos=0, numRows=table.GetNumberRows())

        cursor.execute("SELECT * FROM purchase")
        purchases = cursor.fetchall()

        for row, purchase in enumerate(purchases):
            purchase_id, customer_id, product_id, employee_id, price, quantity, date = purchase
            table.AppendRows()
            table.SetCellValue(row, 0, str(purchase_id))
            table.SetCellValue(row, 1, str(customer_id))
            table.SetCellValue(row, 2, str(product_id))
            table.SetCellValue(row, 3, str(employee_id))
            table.SetCellValue(row, 4, str(price))
            table.SetCellValue(row, 5, str(quantity))
            table.SetCellValue(row, 6, str(date))


if __name__ == "__main__":
    app = wx.App(False)
    client_frame = ClientUI()
    employee_frame = EmployeeUI()
    product_frame = ProductUI()
    purchase_frame = PurchaseUI()

    # main_frame = MainFrame()
    app.MainLoop()