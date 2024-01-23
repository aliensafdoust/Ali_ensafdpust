def main():
    time = str(input("What time is it? ")).strip()

    food_time = convert(time)

    if food_time >= 7 and food_time <= 8 :
        print("breakfast time")
    elif food_time >= 12  and food_time <= 13 :
        print("lunch time")
    elif food_time >= 18 and food_time <= 19 :
        print("dinner time")

def convert(time):
    c = 0.0
    if time.rfind("a.m.") != -1:
        time =time.replace("a.m.","")
    elif time.rfind("p.m.") != -1:
        time = time.replace("p.m.","")
        c = 12.0

    ho , min =  time.split(":")
    result = float(ho)+ c +(float(min) / 60)
    return result


if __name__ == "__main__":
    main()