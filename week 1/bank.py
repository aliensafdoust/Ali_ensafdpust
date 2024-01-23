txt = input("Greeting: ").strip().lower()

num = 100

if txt.startswith("hello"):
    num = 0
elif txt.startswith("h"):
    num = 20

print(f"${num}")
