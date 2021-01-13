import os
import sys
from DTO import *

dbExist = os.path.isfile('moncafe.db')

if dbExist:
    os.remove('moncafe.db')

from Repository import repo


def insert_data(args):
    with open(args[1]) as inputFile:
        for line in inputFile:
            line = line.strip('\n')
            table = line[0]
            fields = line.split(', ')
            if table == 'E':
                repo.Employees.insert(Employee(fields[1], fields[2], fields[3], fields[4]))
            if table == 'S':
                repo.Suppliers.insert(Supplier(fields[1], fields[2], fields[3]))
            if table == 'P':
                repo.Products.insert(Product(fields[1], fields[2], fields[3], 0))
            if table == 'C':
                repo.Coffee_stands.insert(Coffee_stand(fields[1], fields[2], fields[3]))


def main(args):
    repo.create_tables()
    insert_data(args)


if __name__ == '__main__':
    main(sys.argv)
