import sys
import random
playerchoice = input('Enter...\n1 for Rock,\n2 for Paper,\n3 for Scissors: \n\n')
print(playerchoice)

player = int(playerchoice)

if player < 1 | player > 3:
    sys.exit("please choose 1, 2, or 3.")

computerchoice = random.choice("123")
computer = int(computerchoice)

print("")

print(" you choose " + str(player) +  "." )
print("python chose " + str(computer) + ".")
print()

if player == 1 and computer == 3:
    print("you win")
elif player == 2 and computer == 1:
    print("you win")
elif player == 3 and computer == 3:
    print("you win")
elif player == computer:
    print("tie")
else:
    print("python wins")