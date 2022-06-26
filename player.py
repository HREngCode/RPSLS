import random
import time
class Player:
    def __init__(self,):
        self.name = "name"
        self.gestures = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]
        self.score = 0
        self.number_of_players = 0

    def choose_random_gesture(self, list):
        random_item = random.choice(list)
        return random_item

    def select_gesture(self):
        print("Select 0 for Rock")
        print("Select 1 for Paper")
        print("Select 2 for Scissors")
        print("Select 3 for Lizard")
        print("Select 4 for Spock")
        
        gesture_pick = input("Player 1 please select a gesture: ")
        if gesture_pick == "0":
            player_one = self.gestures[0]
        elif gesture_pick == "1":
            player_one = self.gestures[1]
        elif gesture_pick == "2":
            player_one = self.gestures[2]
        elif gesture_pick == "3":
            player_one = self.gestures[3]
        elif gesture_pick == "4":
            player_one = self.gestures[4]
        print(f'Player one has selected {player_one}!')

        if self.number_of_players == "1":
            gesture_pick = self.choose_random_gesture(self.gestures)
            player_two = gesture_pick
            time.sleep(1)
            print(f'Player two has selected {player_two}!')
        else:
            gesture_pick = input("Player 2 please select a gesture: ")
            if gesture_pick == "0":
                player_two = self.gestures[0]
            elif gesture_pick == "1":
                player_two = self.gestures[1]
            elif gesture_pick == "2":
                player_two = self.gestures[2]
            elif gesture_pick == "3":
                player_two = self.gestures[3]
            elif gesture_pick == "4":
                player_two = self.gestures[4]
            time.sleep(1)
            print(f'Player two has selected {player_two}!')

    def add_to_score(self):
        self.score += 1

    # player_one = " "
    # player_two = " "
    # gesture = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]
    # gesture_pick = 0
    # round_number = 0
    # number_of_players = 0
    # winner = True
    # player_one_win_count = 0
    # player_two_win_count = 0
    # print(gesture[0])