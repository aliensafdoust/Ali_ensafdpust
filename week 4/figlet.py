from random import choice
from pyfiglet import Figlet
import sys

figlet = Figlet()
font_list = figlet.getFonts()


if len(sys.argv) == 1:
    figlet.setFont(font=choice(font_list))
elif (
    len(sys.argv) == 3
    and str(sys.argv[1]) in ["-f", "--font"]
    and str(sys.argv[2]) in font_list
):
    figlet.setFont(font=str(sys.argv[2]))
else:
    sys.exit("Invalid usage")

txt = input("Input: ").strip()

print("Output: \n", figlet.renderText(txt))
