def main():
    user_string = input()
    print(convert(user_string))


def convert(string: str) -> str:
    return string.replace(":)", "🙂").replace(":(", "🙁")


main()
