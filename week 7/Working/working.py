import re


def main():
    print(convert(input("Hours: ").strip()))


def convert(s):
    try:
        if time := re.search(r"(\d+):?(\d+)?[ ]+(AM|PM) (?:To|to|TO|tO) (\d+):?(\d+)?[ ]+(AM|PM)",s):
            time = time.groups()
            real_time = []
            for t in time:
                if t == None:
                    real_time.append("00")
                else:
                    real_time.append(t)
            if int(real_time[0]) > 12 or int(real_time[0]) < 0 or int(real_time[1]) > 59 or int(real_time[0]) < 0:
                raise ValueError
            if int(real_time[3]) > 12 or int(real_time[3]) < 0 or int(real_time[4]) > 59 or int(real_time[3]) < 0:
               raise ValueError

            # 24

            #PM
            if real_time[2] == "PM" and real_time[0] != '12':
               real_time[0] = int(real_time[0]) + 12
            if real_time[5] == "PM" and real_time[3] != '12':
                real_time[3] = int(real_time[3]) + 12
            #AM
            if real_time[2] == "AM" and real_time[0] == '12':
                real_time[0] = '00'
            if real_time[5] == "AM" and real_time[3] == '12':
                real_time[3] = '00'

            return f"{str(real_time[0]).zfill(2)}:{str(real_time[1]).zfill(2)} to {str(real_time[3]).zfill(2)}:{str(real_time[4]).zfill(2)}"
        else:
            raise ValueError
    except ValueError:
        raise ValueError


if __name__ == "__main__":
    main()
