txt = str(input("camelCase: ")).strip()
result = ""

for upper in txt:
    if upper.isupper():
        result = result + "_" + upper.lower()
    else:
        result += upper
print(f"snake_case: {result}")
