#Rock Paper Scissors Lizard Spock

from game import Game
game = Game()

def opening_welcome():
    print("Welcome to Rock Paper Scissors Lizard Spock")
    print("")
    print("Each match will be the best of three games")
    print("Use the number keys to make your selection")
    print(" ")
    print("Scissors cut Paper")
    print("Paper covers Rock")
    print("Rock crushes Lizard")
    print("Lizard poisons Spock")
    print("Spock smashes Scissors")
    print("Scissors decapitates Lizard")
    print("Lizard eats Paper")
    print("Paper disproves Spock")
    print("Spock vaporizes Rock")
    print("Rock crushes Scissors")
    game.enter_number_of_players()

def run_game():
    opening_welcome()

play_game_question = input("Would you like to play Rock Paper Scissors Lizard Spock? y/n ")
if play_game_question == "y":
    run_game()
else:
    print("Sorry to hear that. Let's play again later.")
