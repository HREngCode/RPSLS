#Calling Random funciton
import random
import time

class Player:
    def __init__(self):
        self.name = ""
        self.gestures = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]
        self.chosen_gesture = ""
        self.score = 0
        self.number_of_players = 0

    def choose_gesture(self):
        self.chosen_gesture = random.choice(self.gestures)
        print(f'{self.name} has chosen {self.chosen_gesture}')

    
    def add_to_score(self):
        self.score += 1


