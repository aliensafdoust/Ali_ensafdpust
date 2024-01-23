import re

def main():
    print(parse(input("HTML: ").strip()))


def parse(s):

    if Addre := re.search(r'https?://(?:www\.)?\w+\.com\/embed\/(\w+)',s):
        return "https://youtu.be/" + Addre.group(1)
    else:
        None



if __name__ == "__main__":
    main()
