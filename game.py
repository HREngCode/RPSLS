# 10 Commits
# Dev properly incorporate inheritance
# Player(parent), Human(child), AI, child
# enters correctly
# Store gesture options in a list
# Demo
# Correct player to win given round
# Best of 3
# Single Player or Multi Player
class Game:
    def __init__(self) -> None:
        self.gesture = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]
        self.game_type = ["Human vs. Human", "Human vs. AI"]
        self.game_round = ["1","2","3"]

    def opening_welcome(self):
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

    def enter_number_of_players(self):
        print("How many players? 1, 2, or 3 for something different")
        number_of_players = input(" ")




