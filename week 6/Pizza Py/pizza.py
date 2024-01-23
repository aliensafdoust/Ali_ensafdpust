import sys
import csv
from tabulate import tabulate


def main():
    try:
        if len(sys.argv) < 2:
            sys.exit("Too few command-line arguments")
        elif len(sys.argv) == 2:
            if sys.argv[1].endswith(".csv"):
                with open(sys.argv[1]) as checking_file:
                    print(pizza(checking_file))
            else:
                sys.exit("Not a Python file")
        elif len(sys.argv) > 2:
            sys.exit("Too many command-line arguments")
    except FileNotFoundError:
        sys.exit("File does not exist")
def pizza(file):
    file_table = csv.DictReader(file ,delimiter = ",")
    print(tabulate(file_table , headers="keys", tablefmt="grid"))

if __name__ == "__main__":
    main()
