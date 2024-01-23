import datetime
import inflect

infl = inflect.engine()

def main():
    print(cacu(input("Date of Birth: ")))

def cacu(in_date):
    try:
        format = '%Y-%m-%d'
        user_input = datetime.datetime.strptime(in_date, format).date()
    except ValueError:
        return "Invalid date"


    today = datetime.date.today()
    interval = (today - user_input).days * 24 * 60
    return infl.number_to_words(interval, andword="").capitalize() + " minutes"



if __name__ == "__main__":
    main()
