# TODO very rough code, needs cleanup I think

def main():
	result = get_input()
	if result > 100:
		get_input()
	elif result >= 99:
		print("F")
	elif result <= 1:
		print("E")
	else:
		print(f"{result}%")


def get_input():
	while True:
		try:
			user_input = input("Fraction: ")
			numerator, denominator = user_input.split('/')
			numerator = int(numerator)
			denominator = int(denominator)
			result = int((numerator / denominator) * 100)
		except (ValueError, ZeroDivisionError):
			pass
		else:
			return result


main()
