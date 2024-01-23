import csv
import sys


def main():
    try:
        if len(sys.argv) < 3:
            sys.exit("Too few command-line arguments")
        elif len(sys.argv) == 3:
            if sys.argv[1].endswith(".csv") and sys.argv[2].endswith(".csv"):
                if sys.argv[1] == "before.csv" and sys.argv[2] == "after.csv":
                    with open(sys.argv[1]) as checking_file_1:
                        with open(sys.argv[2] , "w") as checking_file_2:
                            total(checking_file_1 , checking_file_2)
                else:
                    sys.exit("Could not read invalid_file.csv")
            else:
                sys.exit("Not a csv file")
        elif len(sys.argv) > 3:
            sys.exit("Too many command-line arguments")
    except FileNotFoundError:
        sys.exit("File does not exist")

def total(bef , aft):
    read = csv.DictReader(bef)
    f2 = csv.DictWriter(aft,fieldnames=["last","first","house"])
    f2.writeheader()
    for stu in read:
        last , first  = stu["name"].split(",")
        house = stu["house"]
        f2.writerow(
            {
            "last" : last,
            "first" : first,
            "house" : house,
            }
        )

if __name__ == "__main__":
    main()


