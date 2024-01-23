letters = ["a", "e", "i", "o", "u"]


def main():
    txt = input("Input: ").strip()
    print(f"Output: {shorten(txt)}")


def shorten(word):
    result = ""
    for letter in word:
        if letter.lower() not in letters:
            result += letter
    return result


if __name__ == "__main__":
    main()
