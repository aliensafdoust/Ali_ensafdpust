import re


def main():
    print(count(input("Text: ")))


def count(s):
    txt = re.findall(r"^um\b|[ ]+um[.,? ]+", s , re.IGNORECASE)
    return len(txt)




if __name__ == "__main__":
    main()
