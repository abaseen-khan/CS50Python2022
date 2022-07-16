def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    return check_is_capital(s) and check_length(s) and starts_with_letters(s)


def check_is_capital(s):
    return True if s.isupper() else False


def check_length(s):
    return True if 2 <= len(s) <= 6 else False


def starts_with_letters(s):
    return True if s[0:2].isalpha() else False


def only_alphanumeric(s):
    return True if s.isalnum() else False


# TODO create function that checks for letters in the middle of the string
# TODO create function that checks if the first appearance of a digit is 0
# https://cs50.harvard.edu/python/2022/psets/2/plates/

main()
