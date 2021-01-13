from DTO import *

class _Employees:
    def __init__(self, conn):
        self._conn = conn

    def insert(self, employee):
        self._conn.execute("INSERT INTO Employees (id, name,  salary, coffee_stand) VALUES (?, ?, ?, ?)",
                           [employee.id, employee.name, employee.salary, employee.coffee_stand])

    def find(self, employee_id):
        c = self._conn.cursor()
        c.execute("SELECT id, name, salary, coffee_stand FROM Employees WHERE id = ?", [employee_id])
        return Employee(*c.fetchone())

    def find_all(self):
        c = self._conn.cursor()
        all = c.execute("""
                SELECT emp.id, emp.name, emp.salary, emp.coffee_stand FROM Employees emp
                """).fetchall()
        return [Employee(*row) for row in all]


class _Suppliers:
    def __init__(self, conn):
        self._conn = conn

    def insert(self, supplier):
        self._conn.execute("INSERT INTO Suppliers (id, name, contact_information) VALUES (?, ?, ?)",
                           [supplier.id, supplier.name, supplier.contact_information])

    def find(self, supplier_id):
        c = self._conn.cursor()
        c.execute("SELECT id, name, contact_information FROM Suppliers WHERE id = ?", [supplier_id])
        return Supplier(*c.fetchone())

    def find_all(self):
        c = self._conn.cursor()
        all = c.execute("""
                SELECT sup.id, sup.name, sup.contact_information FROM Suppliers sup
                """).fetchall()
        return [Supplier(*row) for row in all]


class _Products:
    def __init__(self, conn):
        self._conn = conn

    def insert(self, product):
        self._conn.execute("INSERT INTO Products (id, description, price, quantity) VALUES (?, ?, ?, ?)",
                           [product.id, product.description, product.price, product.quantity])

    def find(self, product_id):
        c = self._conn.cursor()
        c.execute("SELECT id, description, price, quantity FROM Products WHERE id = ?", [product_id])
        return Product(*c.fetchone())

    def find_all(self):
        c = self._conn.cursor()
        all = c.execute("""
                SELECT prod.id, prod.description, prod.price, prod.quantity FROM Products prod
                """).fetchall()
        return [Product(*row) for row in all]

    def update(self, product):
        self._conn.execute("""
                  UPDATE Products SET quantity= (?) WHERE id=(?)
              """, [product.quantity, product.id])


class _Coffee_stands:
    def __init__(self, conn):
        self._conn = conn

    def insert(self, coffee_stand):
        self._conn.execute("INSERT INTO Coffee_stands (id, location, number_of_employees) VALUES (?, ?, ?)",
                           [coffee_stand.id, coffee_stand.location, coffee_stand.number_of_employees])

    def find(self, coffee_stand_id):
        c = self._conn.cursor()
        c.execute("SELECT id, location, number_of_employees FROM Coffee_stands WHERE id = ?", [coffee_stand_id])
        return Coffee_stand(*c.fetchone())

    def find_all(self):
        c = self._conn.cursor()
        all = c.execute("""
               SELECT cs.id, cs.location, cs.number_of_employees FROM Coffee_stands cs
                """).fetchall()
        return [Coffee_stand(*row) for row in all]


class _Activities:
    def __init__(self, conn):
        self._conn = conn

    def insert(self, activity):
        self._conn.execute("INSERT INTO Activities (product_id, quantity, activator_id, date) VALUES (?, ?, ?,?)",
                           [activity.product_id, activity.quantity, activity.activator_id, activity.date])

    def find(self, activator_id):
        c = self._conn.cursor()
        c.execute("SELECT product_id, quantity, activator_id, date FROM Activities WHERE activator_id = ?"
                  , [activator_id])
        return Activity(*c.fetchone())

    def find_all(self):
        c = self._conn.cursor()
        all = c.execute("""
                SELECT act.product_id, act.quantity, act.activator_id, act.date FROM Activities act
                ORDER BY act.date
                """).fetchall()
        return [Activity(*row) for row in all]
