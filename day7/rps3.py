import sys
import random
from enum import Enum

def play_rps():
        class RPS(Enum):
         ROCK = 1
         PAPER = 2
         SCISSORS = 3

        

    
        playerchoice = input("\nEnter...\n1 for Rock, \n2 For paper, or \n3 for Scissors:\n\n")
        print(playerchoice)

        if playerchoice not in ["1","2","3"]:
               print("You must enter 1,2 or 3.")
               return play_rps()

        player = int(playerchoice)

    
        computerchoice = random.choice("123")
        computer = int(computerchoice)
        # print("\nYou chose " + str(RPS(player)).replace('RPS.', '') + "." )
            #print("python chose " + str(RPS(computer)).replace('RPS.', '') + ".\n")
        print("\nYou chose " + playerchoice + ".")
        print("Python chose " + computerchoice + ".\n")
        if player == 1 and computer == 3:
                print("you Win 🎉")
        elif player == 2 and computer == 1:
                print("you win 🎉")
        elif player == 3 and computer == 2:
                print("you win 🎉")
        elif player == computer:
                print("tie 😱")
        else:
                print("🐍 python wins")

        print("\nPlay again?")
        while True:
               
            playagain = input("\nPlay again? \nY for Yes  or\n to Quit \n")
            if playagain.lower() not in ["y", "q"]:
                   continue
            else:
                   break
        if playagain.lower() == "y":
                   return play_rps()
        else:
                print("\nthank you for playing! 🎉🎉")
                sys.exit(" thank you and goodbye.")


play_rps()

    

