
def main():
    while True:
        try:
            fu = input("Fraction: ").strip()
            print(gauge(convert(fu)))
            break
        except (ZeroDivisionError, ValueError):
            pass

def convert(fraction):
        try:
            fraction = fraction.split("/")
            fraction[0] = int(fraction[0])
            fraction[1] = int(fraction[1])
            if fraction[0] <= fraction[1]:
                 return round(fraction[0] / fraction[1]  * 100)
            elif fraction[1] == 0:
                 raise ZeroDivisionError
            else:
                 raise ValueError
        except (ZeroDivisionError, ValueError):
            pass


def gauge(percentage):
     if percentage <= 1:
          return "E"
     elif percentage >= 99:
          return "F"
     else:
          return f"{percentage}%"



if __name__ == "__main__":
    main()
#python fuel.py
