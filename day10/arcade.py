from guess_number import guess_number
from rps8 import rock_paper_scissors
import sys





def arcade(name="player"):
  welcome_back = False

  while True:
    if welcome_back == True:
      print(f"\n {name}, welcome back to the arcade menu.")


    playerChoice = input(f"\n welcome {name}! to grey_arcade.\npick 1 = 'rock paper and scissors'\n\n 2 = guess the 'number'\n x to exit!")
    if playerChoice not in ["1", "2", "x"]:
        print(f"\nplease select 1 2 or x")
        return arcade(name)
    
    welcome_back = True

    if playerChoice == "1":
       rps = rock_paper_scissors(name)
       rps()
    elif playerChoice =="2":
       guess = guess_my_number(name)
       guess()
    else:
       print("\n see you next time!\n")
       sys.exit("Bye {name}!")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(
      description="Provides a personalized gaming experience."
    )
    parser.add_argument(
      "-n", "--name", metavar="name",
      required=True, help="The name of the person playing the game."
    )
    args = parser.parse_args()
    arcadia = arcade(args.name)
    arcadia()

