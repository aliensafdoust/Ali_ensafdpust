import sys
from PIL import Image, ImageOps

def main():
    try:
        if len(sys.argv) < 3:
            sys.exit("Too few command-line arguments")
        elif len(sys.argv) == 3:
            if sys.argv[2].endswith(".jpg") and sys.argv[1].endswith(".jpg"):
                if sys.argv[1] != sys.argv[2]:
                    image(sys.argv[1])
                else:
                    sys.exit("Input and output have different extensions")
            else:
                print("Invalid output")
                sys.exit(1)
        elif len(sys.argv) > 3:
            sys.exit("Too many command-line arguments")
    except FileNotFoundError:
        sys.exit("File does not exist")

def image(img):
    user_input = Image.open(img)
    shirt = Image.open("shirt.png")
    width = shirt.size
    user_input = ImageOps.fit(user_input, width)
    user_input.paste(shirt,shirt)
    user_input.save(sys.argv[2])




if __name__ == "__main__":
    main()
