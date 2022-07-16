vowels = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']

user_input = input("Input: ")

for letter in user_input:
    if letter in vowels:
        user_input = user_input.replace(letter, '')

print("Output:", user_input)
