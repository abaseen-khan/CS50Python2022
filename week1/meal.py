def main():
    time = input("What time is it? ")
    time = convert(time)
    if 7 <= time <= 8:
        print("breakfast time")
    if 12 <= time <= 13:
        print("lunch time")
    if 18 <= time <= 19:
        print("dinner time")


def convert(time) -> float:
    digits, period = time.split(" ")
    hour, minutes = digits.split(':')
    hour = int(hour)
    if period == "p.m.":
        hour += 12
    minutes = int(minutes)
    minutes = float(minutes / 60)
    return hour + minutes


if __name__ == '__main__':
    main()
