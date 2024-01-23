def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    check = ""
    number_cheak = 0

    if s.isalnum() and len(s) <= 6 and len(s) >= 2:
        if s[0].isalpha() and s[1].isalpha():
            for char in s:
                if char.isalpha() and number_cheak == 0:
                    check += char
                elif char.isnumeric() and char != '0' and number_cheak == 0:
                    number_cheak += 1
                    check += char
                elif char.isnumeric() and number_cheak > 0:
                    number_cheak += 1
                    check += char
    if check == s:
        return True
    else:
        return False


main()
