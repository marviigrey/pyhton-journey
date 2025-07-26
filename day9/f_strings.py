#Different format
person = "Dave"

coins = 3

print("\n" + person + " has " + str(coins) + " coins left")

message = "\n%s has %s coins left. " % (person, coins) #formatting string.
print(message)
message = "\n{} has {} coins left. ".format(person, coins) #formatting string.
print(message)
message = "\n{0} has {1} coins left. ".format(person, coins) #formatting string.
print(message)
message = "\n{person} has {coins} coins left. ".format(
    person=person, coins=coins
    ) #formatting string.
print(message)

player = {'person': 'dave', 'coins': 5}
message = "\n{person} has {coins} coins left. ".format(**player) #formatting string.
print(message)

#f-strings! This is the way

message = f"\n{person} has {coins} coins left."
print(message)

message = f"\n{person} has {2 * 5} coins left."
print(message)

message = f"\n{person.lower()} has {2 * 5} coins left."
print(message)

message = f"\n{player['person']} has {player['coins']} coins left."
print(message)

#When using f-string, you can pass formatting options as well.

num = 10
print(f"\n2.25 times {num} is {2.25 * num:.2f}\n")

for num in range(1,11):
    print(f"2.25 times {num} is {2.25 * num:.2f}")

for num in range(1,11):
    print(f"{num} divided  by 4.52 is {num / 4.52:.2%}")