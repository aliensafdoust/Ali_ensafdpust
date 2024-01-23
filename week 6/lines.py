import sys


import sys


def main():
    try:
        if len(sys.argv) < 2:
            sys.exit("Too few command-line arguments")
        elif len(sys.argv) == 2:
            if sys.argv[1].endswith(".py"):
                with open(sys.argv[1]) as check_file:
                    print(sum(check_file))
            else:
                sys.exit("Not a Python file")
        elif len(sys.argv) > 2:
            sys.exit("Too many command-line arguments")
    except FileNotFoundError:
        sys.exit("File does not exist")



def sum(file):
    total = file.readlines()
    t_line = 0
    f_line = 0
    for line in total:
        if (
            line.strip().startswith("#")
            or line.strip().startswith("\n")
            or line.isspace()
        ):
            f_line += 1
        t_line += 1
    return t_line - f_line


if __name__ == "__main__":
    main()
