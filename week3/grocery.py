grocery_list = {}

print("Enter grocery list: (Press CTRL + Z to stop input)")

while True:
	try:
		item = input().upper().strip()
	except EOFError:
		print()
		break
	else:
		if item in grocery_list:
			grocery_list[item] += 1
		else:
			grocery_list[item] = 1


for grocery in sorted(grocery_list):
	print(f"{grocery_list[grocery]} {grocery}")