from tkinter import Y
from player import Player
player = Player()

class Game:
    def __init__(self) -> None:
        self.player_one = "Player One"
        self.player_two = "Player Two"
        self.game_type = ["Human vs. Human", "Human vs. AI"]
        self.game_round = ["1","2","3"]
        self.winner = True

    def select_gesture(self):
        print("Select 0 for Rock")
        print("Select 1 for Paper")
        print("Select 2 for Scissors")
        print("Select 3 for Lizard")
        print("Select 4 for Spock")

        gesture_pick = input("Player 1 please select a gesture: ")
        if gesture_pick == "0":
            player_one = player.gestures[0]
        elif gesture_pick == "1":
            player_one = player.gestures[1]
        elif gesture_pick == "2":
            player_one = player.gestures[2]
        elif gesture_pick == "3":
            player_one = player.gestures[3]
        elif gesture_pick == "4":
            player_one = player.gestures[4]
        print(f'Player one has selected {player_one}!')

        print(player.number_of_players)
        if player.number_of_players == "1":
            gesture_pick = player.choose_random_gesture(player.gestures)
            player_two = gesture_pick
            print(f'Player two has selected {player_two}!')
        else:
            gesture_pick = input("Player 2 please select a gesture: ")
            if gesture_pick == "0":
                player_two = player.gestures[0]
            elif gesture_pick == "1":
                player_two = player.gestures[1]
            elif gesture_pick == "2":
                player_two = player.gestures[2]
            elif gesture_pick == "3":
                player_two = player.gestures[3]
            elif gesture_pick == "4":
                player_two = player.gestures[4]

            print(f'Player two has selected {player_two}!')

        if player_one == "Rock" and player_two == "Paper":
            self.winner = False
        elif player_one == "Rock" and player_two == "Scissors":
            self.winner = True
        elif player_one == "Rock" and player_two == "Lizard":
            self.winner = True
        elif player_one == "Rock" and player_two == "Spock":
            self.winner = False
        elif player_one == "Paper" and player_two == "Rock":
            self.winner = True
        elif player_one == "Paper" and player_two == "Scissors":
            self.winner = False
        elif player_one == "Paper" and player_two == "Lizard":
            self.winner = False
        elif player_one == "Paper" and player_two == "Spock":
            self.winner = True
        elif player_one == "Scissors" and player_two == "Rock":
            self.winner = False
        elif player_one == "Scissors" and player_two == "Paper":
            self.winner = True
        elif player_one == "Scissors" and player_two == "Lizard":
            self.winner = True
        elif player_one == "Scissors" and player_two == "Spock":
            self.winner = False
        elif player_one == "Lizard" and player_two == "Rock":
            self.winner = False
        elif player_one == "Lizard" and player_two == "Paper":
            self.winner = True
        elif player_one == "Lizard" and player_two == "Scissors":
            self.winner = False
        elif player_one == "Lizard" and player_two == "Spock":
            self.winner = True   
        elif player_one == "Spock" and player_two == "Rock":
            self.winner = True
        elif player_one == "Spock" and player_two == "Paper":
            self.winner = False
        elif player_one == "Spock" and player_two == "Scissors":
            self.winner = True
        elif player_one == "Spock" and player_two == "Lizard":
            self.winner = False 
        else:
            print("The game ends in a tie")
    
    def run_human_vs_ai(self):
        self.select_gesture()
    
    def run_human_vs_human(self):
        self.select_gesture()

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
            
             

        # while player_one_win_count != (player_two_win_count-2) or player_one_win_count != (player_two_win_count+2):
        # run_game()    
        if self.winner == True:
            print('The winner is player 1')
                # player_one_win_count += 1
        else:
            print('The winner is player 2')
            # player_two_win_count += 1
        # round_number += 1  

    




