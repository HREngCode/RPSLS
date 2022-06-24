#Rock Paper Scissors Lizard Spock

from game import Game

play_game_question = input("Would you like to play Rock Paper Scissors Lizard Spock? y/n ")
if play_game_question == "y":
    game = Game()
    game.run_game()

def run_game(self):
    game.opening_welcome()

game.enter_number_of_players()

print("Choose 0 for Rock")
print("Choose 1 for Paper")
print("Choose 2 for Scissors")
print("Choose 3 for Lizard")
print("Choose 4 for Spock")