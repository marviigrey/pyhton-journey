import random 
import sys


def guess_number(name='PlayerOne'):
    game_count = 0 
    player_wins = 0

    
    def play_guess_number():
       nonlocal name
       nonlocal player_wins

    playerChoice = input(
        f"\n {name} guess which number i am thinking of...1, 2 or 3\n\n"
        )

    if playerChoice not in ["1", "2", "3"]:
        print(f"{name}, please enter 1, 2 or 3")
        return play_guess_number()
    
   

    pythonChoice = random.choice("123")

    print(f"\n{name}, you chose {playerChoice}")
    print(f"\nI was thinking about the number {pythonChoice}")

    player = int(playerChoice)
    python = int(pythonChoice)

    def decide_winner(player, python):
        nonlocal player_wins
        nonlocal name
    
        if player == python:
            player_wins += 1

            return f"\n{name} guessed it right! i was thinking about {python}\n"
        
        else:
            return f"\nwrong!, i was thinking about {python}"
        
    game_result = decide_winner(player, python)
    print(game_result)

    
    game_count += 1

    print(f"\n Game count: {game_count}")
    print(f"\n{name}'s wins: {player_wins}")
    print(f"Your winning percentage: {player_wins/game_count:.2%}")
    print(f"\nPlay Again")
    
    while True:
        playAgain = input("\n\nY for yes or q to quit \n")
        if playAgain.lower() not in ["y","q"]:
            continue
        else:
            break
    if playAgain.lower() == "y":
        return play_guess_number()
    else:
        print("\n Thanks for playing")
        if __name__ == "__main__":
          sys.exit("goodbye!")
        else:
            return

    return play_guess_number

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(
        description="Providing a personalized gamin experience"
    )
    parser.add_argument(
        "-n", "--name", metavar="name",
        required=True, help="the name of the person playing"
    )

    args = parser.parse_args()
    guess_my_number = guess_number(args.name) 
    guess_my_number()