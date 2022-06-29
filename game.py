import time
from player import Player
from human import Human
from ai import Ai


class Game:
    def __init__(self):
        self.game_type = ["Human vs. Human", "Human vs. AI"]
        self.game_round = 0
        self.winner = True
        self.player_one = "None"
        self.player_two = "None"

    def run_game(self):
        self.opening_welcome()
        self.enter_number_of_players()

    def opening_welcome(self):
        print("Welcome to Rock Paper Scissors Lizard Spock")
        time.sleep(1)
        print("Each match will be the best of three games")
        time.sleep(1)
        print("Use the number keys to make your selection")
        time.sleep(1)
        print(" ")
        time.sleep(1)
        print("The rules are as follows:")
        time.sleep(1)
        print("Scissors cut Paper")
        time.sleep(1)
        print("Paper covers Rock")
        time.sleep(1)
        print("Rock crushes Lizard")
        time.sleep(1)
        print("Lizard poisons Spock")
        time.sleep(1)
        print("Spock smashes Scissors")
        time.sleep(1)
        print("Scissors decapitates Lizard")
        time.sleep(1)
        print("Lizard eats Paper")
        time.sleep(1)
        print("Paper disproves Spock")
        time.sleep(1)
        print("Spock vaporizes Rock")
        time.sleep(1)
        print("Rock crushes Scissors")

    def enter_number_of_players(self):
        time.sleep(1)
        self.number_of_players = input("Game Mode: Press 1 for Human vs. Ai, Press 2 for Human vs. Human: ")
        if self.number_of_players == "1":
            self.player_one = Human()
            self.player_one.name = "Player 1"
            self.player_two = Ai()
            self.player_two.name = "Player 2"
            self.start_round()
        elif self.number_of_players == "2":
            self.player_one = Human()
            self.player_one.name = "Player 1"
            self.player_two = Human()
            self.player_two.name = "Player 2"
            self.start_round()
        elif self.number_of_players != "1" and self.number_of_players != "2":
            print("You must enter a valid number of players.")
            self.enter_number_of_players()

    def start_round(self):
        while self.player_one.score < 2 and self.player_two.score < 2:
            self.game_round += 1
            time.sleep(1)
            print(f'Start Round {self.game_round}')
            self.player_one.choose_gesture()
            self.player_two.choose_gesture()
            if self.player_one.chosen_gesture == self.player_two.chosen_gesture:
                time.sleep(1)
                print("The game is a tie. Start again.")
            elif self.player_one == "Rock" and (self.player_two == "Scissors" or self.player_two == "Lizard"):
                self.winner = True
                self.player_one.add_to_score()
            elif self.player_one == "Paper" and (self.player_two == "Rock" or self.player_two == "Spock"):
                self.winner = True
                self.player_one.add_to_score()
            elif self.player_one == "Scissors" and (self.player_two == "Paper" or self.player_two == "Lizard"):
                self.winner = True
                self.player_one.add_to_score()
            elif self.player_one == "Lizard" and (self.player_two  == "Paper" or self.player_two == "Spock"):
                self.winner = True
                self.player_one.add_to_score()
            elif self.player_one == "Spock" and (self.player_two == "Rock" or self.player_two == "Scissors"):
                self.winner = True
                self.player_one.add_to_score()
            else:
                self.winner = False
                self.player_two.add_to_score()

        time.sleep(1)
        print(f'{self.player_one.score} wins for Player 1')
        time.sleep(1)
        print(f'{self.player_two.score} wins for Player 2')
        self.run_winner()

    def run_winner(self):
            if self.player_one.score > self.player_one.score:
                time.sleep(1)
                print("Player 1 is the winner")
            else:
                time.sleep(1)
                print("Player 2 is the winner")
            
            
            



    


            
             

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

    




