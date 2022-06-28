#Calling Random funciton
import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.gestures = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]
        self.score = 0
        self.number_of_players = 0
        self.gesture_selected = 0

    

    def select_gesture(self):
        self.gesture_selected = input(f'{self.name} please select a gesture: ')    

    def assign_gesture(self):
        gesture_pick = "0"
        if gesture_pick == "0":
            self.gesture_selected = self.gestures[0]
        elif gesture_pick == "1":
            self.gesture_selected= self.gestures[1]
        elif gesture_pick == "2":
            self.gesture_selected= self.gestures[2]
        elif gesture_pick == "3":
            self.gesture_selected = self.gestures[3]
        elif gesture_pick == "4":
            self.gesture_selected = self.gestures[4]
        else:
            print("please select a proper number")
        self.assign_gesture()



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