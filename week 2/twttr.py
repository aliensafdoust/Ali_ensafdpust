letters = ["a", "e", "i", "o", "u"]
txt = input("Input: ").strip()
result = ""

for letter in txt:
    if letter.lower() not in letters:
        result += letter


print(f"Output: {result}")
