from inventory_report.inventory.inventory import Inventory
import sys


def main():

    try:
        path = sys.argv[1]
        report_type = sys.argv[2]
        data = Inventory().import_data(path, report_type)
        print(data, end="")
    except IndexError:
        print("Verifique os argumentos", file=sys.stderr)
