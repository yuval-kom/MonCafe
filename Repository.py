from DAO import _Employees, _Suppliers, _Products, _Coffee_stands, _Activities
import sqlite3
import atexit


class Employees_report:
    def __init__(self, name, salary, working_location, total_sales_income):
        self.name = name
        self.salary = salary
        self.working_location = working_location
        self.total_sales_income = total_sales_income


class Activities_report:
    def __init__(self, date, description, quantity, employee_name, supplier_name):
        self.date = date
        self.description = description
        self.quantity = quantity
        self.employee_name = employee_name
        self.supplier_name = supplier_name


class _Repository:
    def __init__(self):
        self._conn = sqlite3.connect('moncafe.db')
        self.Employees = _Employees(self._conn)
        self.Suppliers = _Suppliers(self._conn)
        self.Products = _Products(self._conn)
        self.Coffee_stands = _Coffee_stands(self._conn)
        self.Activities = _Activities(self._conn)

    def _close(self):
        self._conn.commit()
        self._conn.close()

    def create_tables(self):
        self._conn.executescript(""" CREATE TABLE Coffee_stands(id INTEGER PRIMARY KEY,
                                                                location TEXT NOT NULL,
                                                                 number_of_employees INTEGER
                                      );
                                    CREATE TABLE Employees(id INTEGER PRIMARY KEY,
                                                  name TEXT NOT NULL,
                                                  salary REAL NOT NULL,
                                                  coffee_stand INTEGER,
                                                  FOREIGN KEY(coffee_stand) REFERENCES Coffee_stands(id)
                                      );
                                      CREATE TABLE Suppliers(id INTEGER PRIMARY KEY,
                                                   name TEXT NOT NULL,
                                                   contact_information TEXT
                                      );
                                      CREATE TABLE Products(id INTEGER PRIMARY KEY,
                                                    description TEXT NOT NULL,
                                                    price REAL NOT NULL,
                                                    quantity INTEGER NOT NULL
                                      );
                                      CREATE TABLE Activities(product_id INTEGER,
                                                    quantity INTEGER NOT NULL,
                                                    activator_id INTEGER NOT NULL,
                                                    date DATE NOT NULL,
                                                    FOREIGN KEY(product_id) REFERENCES Products(id)
                                      );""")

    def get_employees_report(self):
        all = self._conn.execute("""
                                SELECT emp.name, emp.salary, Coffee_stands.location, SUM((-1)*(Activities.quantity)*Products.price)
                                FROM Employees emp
                                JOIN Coffee_stands ON emp.coffee_stand = Coffee_stands.id
                                LEFT OUTER JOIN Activities ON emp.id = Activities.activator_id AND Activities.quantity < 0
                                LEFT OUTER JOIN Products ON Activities.product_id = Products.id GROUP BY emp.id
                                ORDER BY emp.name""").fetchall()
        return [Employees_report(*row) for row in all]

    def get_activities_report(self):
        all = self._conn.execute("""
            SELECT act.date, Products.description, act.quantity, Employees.name, Suppliers.name FROM Activities act
            JOIN Products ON act.product_id = Products.id
            LEFT JOIN Employees ON act.activator_id = Employees.id
            LEFT JOIN Suppliers ON act.activator_id = Suppliers.id
            ORDER BY act.date""").fetchall()
        return [Activities_report(*row) for row in all]


repo = _Repository()
atexit.register(repo._close)
