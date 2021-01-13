import sys
import printdb
from DTO import *
from Repository import repo


def insert_activities(args):
    with open(args[1]) as inputFile:
        for line in inputFile:
            fields = line.split(", ")
            if fields.__len__() > 1:
                activity_quantity = int(fields[1])
                product = repo.Products.find(fields[0])

                if product.quantity >= -activity_quantity:
                    repo.Activities.insert(Activity(*fields))
                    product.quantity = product.quantity + activity_quantity
                    repo.Products.update(product)

    printdb.print_db()


def main(args):
    insert_activities(args)


if __name__ == '__main__':
    main(sys.argv)
