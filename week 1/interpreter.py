x1, o, x2 = input("Expression: ").strip().split(" ")
x1 = float(x1)
x2 = float(x2)

match o :
    case "+":
       answer = x1 + x2
    case "-":
        answer = x1 - x2
    case "*":
        answer = x1 * x2
    case "/":
        answer = x1 / x2
print(f"{answer:.1f}")



