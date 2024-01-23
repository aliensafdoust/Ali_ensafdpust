import requests
import sys

def main():
    try:
        re = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").json()
        how_many = getarg()
        result = re["bpi"]["USD"]["rate_float"] * how_many
        print(f"${result:,.4f}")

    except requests.RequestException:
     sys.exit("Can not connect")


def getarg():
    try:
        if len(sys.argv) > 2:
            sys.exit("Missing command-line argument  ")
        elif not float(sys.argv[1]):
            sys.exit("Command-line argument is not a number")
        else:
            return float(sys.argv[1])

    except ValueError:
        sys.exit("Command-line argument is not a number")

if __name__ == "__main__":
    main()

