greeting = input("Greeting: ")
greeting = greeting.capitalize()

if greeting.startswith("Hello"):
    print("$0")
elif greeting.startswith("H"):
    print("$20")
else:
    print("$100")
