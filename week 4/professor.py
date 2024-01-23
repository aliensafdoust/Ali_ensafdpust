import random

level_list = {
    1: [0, 9],
    2: [10, 99],
    3: [100, 999],
}


def main():
    input_level = get_level()
    Question = generate_integer(input_level)
    score = 0

    for qu in Question:
        try:
            x, y = qu.strip().split("+")
            trying = 0
            while True:
                answer = int(input(f"{qu} = "))
                if trying == 2:
                    print(f"EEE\n{qu} = {int(x) + int(y)}")
                    break
                elif int(x) + int(y) != answer:
                    print("EEE")
                    trying += 1
                else:
                    score += 1
                    break
        except ValueError:
            pass

    print(f"Score: {score}")


def get_level():
    while True:
        try:
            number = int(input("Level: ").strip())
            if number >= 1 and number <= 3:
                return number
        except ValueError:
            pass


def generate_integer(level):
    calculat = []

    x_lower = level_list[level][0]
    y_higger = level_list[level][1]

    for _ in range(0, 10):
        calculat.append(
            f"{random.randint(x_lower, y_higger)} + {random.randint(x_lower, y_higger)}"
        )

    return calculat


if __name__ == "__main__":
    main()
