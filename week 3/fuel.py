while True:
    try:
        fu = input("Fraction: ").strip()
        fun = fu.split("/")
        fun[0] = int(fun[0])
        fun[1] = int(fun[1])
    except (ZeroDivisionError, ValueError):
        pass
    else:
        if fun[0] <= fun[1]:
            break
if fun[0] / fun[1] <= 0.1:
    print("E")
elif fun[0] / fun[1] < 0.80:
    print(f"{round((fun[0] / fun[1]) * 100)}%")
elif fun[0] / fun[1] >= 0.90:
    print("F")
