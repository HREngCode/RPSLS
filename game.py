from ast import Return
import time
from player import Player
from human import Human
from ai import Ai


player_one = Player("Player One")
player_two = Player("Player Two")

class Game:
    def __init__(self):
        self.game_type = ["Human vs. Human", "Human vs. AI"]
        self.game_round = ["1","2","3"]
        self.winner = True
        self.number_of_wins = 0

    def display_options():
        print("Select 0 for Rock")
        print("Select 1 for Paper")
        print("Select 2 for Scissors")
        print("Select 3 for Lizard")
        print("Select 4 for Spock")

    def start_round(self):
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
        # self.display_options()
        gesture_pick = player_one.select_gesture()
        print(gesture_pick)
        gesture_pick = player_one.assign_gesture
        player_one.gesture_selected = gesture_pick
        print(f'Player one has selected {player_one.gesture_selected}')
        player_two = Ai()
        player_two.choose_random_gesture(player_two.gestures)
        gesture_pick = player_two.choose_random_gesture(player_two.gestures)
        player_two = gesture_pick
        print(f'Player two has selected {player_two}')
        self.start_round()
    
    def run_human_vs_human(self):
        # self.display_options()
        player_one.select_gesture()
        print(f'Player one has selected {player_one.gesture_selected}')
        player_two.select_gesture()
        print(f'Player two has selected {player_two.gesture_selected}!')
        self.start_round()


    def enter_number_of_players(self):
        self.number_of_players = input("How many players? 1 or 2: ")
        if self.number_of_players == "1":
            self.game_type[0]
            self.run_human_vs_ai()
        elif self.number_of_players == "2":
            self.game_type[1]
            self.run_human_vs_human()
        elif self.number_of_players != "1" and self.number_of_players != "2":
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

    




