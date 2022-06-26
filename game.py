import time
from player import Player
from human import Human
from ai import Ai
player = Player()

class Game:
    def __init__(self):
        self.game_type = ["Human vs. Human", "Human vs. AI"]
        self.game_round = ["1","2","3"]
        self.winner = True
        self.number_of_wins = Player()
    
    def start_round(self):
        player_one = Player()
        player_two = Player()

        if player_one == "Rock" and (player_two == "Paper" or player_two == "Spock"):
            self.winner = False
        elif player_one == "Rock" and (player_two == "Scissors" or player_two == "Lizard"):
            self.winner = True
        elif player_one == "Paper" and (player_two == "Rock" or player_two == "Spock"):
            self.winner = True
        elif player_one == "Paper" and (player_two == "Scissors" or player_two == "Lizard"):
            self.winner = False
        elif player_one == "Scissors" and (player_two == "Rock" or player_two == "Spock"):
            self.winner = False
        elif player_one == "Scissors" and (player_two == "Paper" or player_two == "Lizard"):
            self.winner = True
        elif player_one == "Lizard" and (player_two == "Rock" or player_two == "Scissors"):
            self.winner = False
        elif player_one == "Lizard" and (player_two == "Paper" or player_two == "Spock"):
            self.winner = True
        elif player_one == "Spock" and (player_two == "Rock" or player_two == "Scissors"):
            self.winner = True
        elif player_one == "Spock" and (player_two == "Paper" or player_two == "Lizard"):
            self.winner = False
        else:
            print("The game ends in a tie")

    def run_human_vs_ai(self):
        player.select_gesture()
        self.start_round()
    
    def run_human_vs_human(self):
        player.gestures.select_gesture()
        self.start_round()

    def enter_number_of_players(self):
        print("How many players? 1 or 2")
        player.number_of_players = input(" ")
        if player.number_of_players == "1":
            self.run_human_vs_ai()
        elif player.number_of_players == "2":
            self.run_human_vs_human()
        elif player.number_of_players != "1" and player.number_of_players != "2":
            print("You must enter a valid number of players.")
            self.enter_number_of_players()


            
             

    # while number_of_wins != (player_two_win_count-2) or player_one_win_count != (player_two_win_count+2):
    #     run_game()    
    #     if self.winner == True:
    #         time.sleep(3)
    #         print('The winner is player 1')
    #             # player_one_win_count += 1
    #     else:
    #         time.sleep(3)
    #         print('The winner is player 2')
    #         # player_two_win_count += 1
    #     # round_number += 1  

    




