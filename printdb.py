from Repository import repo


def print_db():
    table = repo.Activities.find_all()
    print("Activities")
    for row in table:
        t = (row.product_id, row.quantity, row.activator_id, row.date)
        print(t)

    table = repo.Coffee_stands.find_all()
    print("Coffee stands")
    for row in table:
        t = (row.id, row.location, row.number_of_employees)
        print(t)

    table = repo.Employees.find_all()
    print("Employees")
    for row in table:
        t = (row.id, row.name, row.salary, row.coffee_stand)
        print(t)

    table = repo.Products.find_all()
    print("Products")
    for row in table:
        t = (row.id, row.description, row.price, row.quantity)
        print(t)

    table = repo.Suppliers.find_all()
    print("Suppliers")
    for row in table:
        t = (row.id, row.name, row.contact_information)
        print(t)

    employees_report()
    activities()


def employees_report():
    table = repo.get_employees_report()
    print("\nEmployees report")
    for row in table:
        if row.total_sales_income is None:
            row.total_sales_income = 0

        print("{} {} {} {}".format(row.name, row.salary, row.working_location, row.total_sales_income))


def activities():
    table = repo.get_activities_report()
    if table.__len__() > 0:
        print("\nActivities")
        for row in table:
            t = (row.date, row.description, row.quantity, row.employee_name, row.supplier_name)
            print(t)


def main():
    print_db()


if __name__ == '__main__':
    main()
