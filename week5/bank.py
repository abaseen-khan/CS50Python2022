def main():
    greeting = input("Greeting: ")
    print(value(greeting))


def value(greeting):
    greeting = greeting.capitalize()
    if greeting.startswith("Hello"):
        return "$0"
    elif greeting.startswith("H"):
        return "$20"
    else:
        return "$100"


if __name__ == '__main__':
    main()

