from fpdf import FPDF


def main():
    user_name = input("Name: ").strip()

    page = FPDF(orientation="portrait", unit="mm", format="A4")
    page.add_page()


    page.set_font("helvetica", "B", 40)
    page.cell(200, 50, "CS50 Shirtificate", align="C")

    page.image("shirtificate.png", x=10, y=65, w=190, h=190)


    page.set_text_color(255,255,255)
    page.set_xy(10, 70)
    page.cell(200, 150, user_name +" took CS50", align="C")

    page.output('shirtificate.pdf')


if __name__ == "__main__":
    main()
