import sys
import random
from enum import Enum

def rps(name='PlayerOne'):
    game_count = 0
    player_wins = 0
    python_wins = 0

    def play_rps():
            nonlocal player_wins
            nonlocal python_wins
            nonlocal name
            class RPS(Enum):
                ROCK = 1
                PAPER = 2
                SCISSORS = 3
        
            playerchoice = input(f"\n {name}, Enter...\n1 for Rock, \n2 For paper, or \n3 for Scissors:\n\n")
            print(playerchoice)

            if playerchoice not in ["1","2","3"]:
                print(f" {name}, please enter 1,2 or 3.")
                return play_rps()

            player = int(playerchoice)

            computerchoice = random.choice("123")

            computer = int(computerchoice)
        
            print(f"\n{name} chose {str(RPS(player)).replace('RPS.', '').title()}.")
            print(f"Python chose {str(RPS(computer)).replace('RPS.', '').title()}." )

            def decide_winner(player, computer):
                nonlocal player_wins
                nonlocal python_wins
                nonlocal name
                if player == 1 and computer == 3:
                        player_wins += 1
                        return f"{name} you Win 🎉!"
                elif player == 2 and computer == 1:
                        player_wins += 1
                        return f"{name} win 🎉!"
                elif player == 3 and computer == 2:
                        player_wins +=  1
                        return f"{name} win 🎉!"
                elif player == computer:
                        return"tie 😱!"
                else:
                        python_wins += 1
                        return"🐍 python wins!"
            game_result = decide_winner(player, computer)
            print(game_result)
            nonlocal game_count 
            game_count += 1
            print(
                  f"\nGame count: {game_count}"
                  )
            print(
                  f"\n{name} have won: {player_wins} times"
                  )
            print(
                  f"\nPython have won: {python_wins} times"
                  )
            
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
                    if __name__ == "__main__":
                     sys.exit(" thank you and goodbye.")
                    else:
                        return
    

            return play_rps



if __name__ == "__main__":
   import argparse
   parser = argparse.ArgumentParser(
         description="Provides a personalized gaming experience."
   )
   parser.add_argument(
         "-n", "--name", metavar="name",
         required=True, help="the name of the person playing the game"
   )
   args = parser.parse_args()
   rock_paper_scissors = rps(args.name)
   rock_paper_scissors()
      