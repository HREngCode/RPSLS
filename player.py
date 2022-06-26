import random
class Player:
    def __init__(self):
        self.name = "name"
        self.gestures = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]
        self.score = 0
        self.number_of_players = 0

    def choose_random_gesture(self, list):
        random_item = random.choice(list)
        return random_item

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