vowels = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']


def main():
	user_input = input("Input: ")
	print("Output:", shorten(user_input))


def shorten(word) -> str:
	for letter in word:
		if letter in vowels:
			word = word.replace(letter, '')
	return word


if __name__ == '__main__':
	main()
