def main():
	user_input = input("Fraction: ")
	converted = convert(user_input)
	print(f"{converted}%")


# def convert(fraction):
	# numerator, denominator = fraction.split('/')
	# try:
	# 	numerator = int(numerator)
	# 	denominator = int(denominator)
	# except ValueError:
	# 	exit("Values aren't integers")
	#
	# try:
	# 	if numerator > denominator:
	# 		raise ValueError
	# 	result = int((numerator / denominator) * 100)
	# except ValueError:
	# 	exit("Numerator can't be greater than denominator")
	# except ZeroDivisionError:
	# 	exit("Can't divide by zero")
	# else:
	# 	return result
	# TODO redo the entire function block above because it's shit and doesn't work


# def gauge(percentage):


if __name__ == '__main__':
	main()
