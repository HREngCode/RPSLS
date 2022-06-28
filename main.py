#Rock Paper Scissors Lizard Spock
import time
from game import Game
game_item = Game()

def opening_welcome():
    print("Welcome to Rock Paper Scissors Lizard Spock")
    # time.sleep(1)
    print("Each match will be the best of three games")
    # time.sleep(1)
    print("Use the number keys to make your selection")
    # time.sleep(1)
    print(" ")
    # time.sleep(1)

def print_rules():
    print("The rules are as follows:")
    # time.sleep(1)
    print("Scissors cut Paper")
    # time.sleep(1)
    print("Paper covers Rock")
    # time.sleep(1)
    print("Rock crushes Lizard")
    # time.sleep(1)
    print("Lizard poisons Spock")
    # time.sleep(1)
    print("Spock smashes Scissors")
    # time.sleep(1)
    print("Scissors decapitates Lizard")
    # time.sleep(1)
    print("Lizard eats Paper")
    # time.sleep(1)
    print("Paper disproves Spock")
    # time.sleep(1)
    print("Spock vaporizes Rock")
    # time.sleep(1)
    print("Rock crushes Scissors")



def run_opening():
    opening_welcome()
    print_rules()
    game_item.enter_number_of_players()
    game_item.start_round()

#Start to the program 
play_game_question = input("Would you like to play Rock Paper Scissors Lizard Spock? y/n ")
if play_game_question == "y":
    run_opening()
else:
    print("Sorry to hear that. Let's play again later.")
