due = 50
accepted = [5, 10, 25]

while due > 0:
    print("Amount Due:", due)
    insert = int(input("Insert Coin: "))
    if insert in accepted:
        due = due - insert

print("Change Owed:", abs(due))
