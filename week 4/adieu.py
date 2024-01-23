import sys
import inflect

names_list = []

while True:
    try:
        name = input("Name: ").strip()
        if name == "":
            print(f"Adieu, adieu, to {inflect.engine().join(names_list)}")
            sys.exit(0)
        names_list.append(name)
    except (EOFError, ValueError):
        print(
            f"\nAdieu, adieu, to {inflect.engine().join(names_list)}",
        )
        sys.exit(0)
