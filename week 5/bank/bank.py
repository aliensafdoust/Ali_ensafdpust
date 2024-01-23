def main():
    greet = input("Greeting: ").strip()
    print(f"${value(greet)}")



def value(greeting):
    greeting = greeting.lower()
    num = 100

    if greeting.startswith("hello"):
        num = 0
    elif greeting.startswith("h"):
        num = 20
    return num

if __name__ == "__main__":
    main()
