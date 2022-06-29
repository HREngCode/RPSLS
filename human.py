from player import Player
import time

class Human(Player):
    def __init__(self):
        super().__init__()
        self.name = "human player"


    def choose_gesture(self):
        print("Select 0 for Rock")
        print("Select 1 for Paper")
        print("Select 2 for Scissors")
        print("Select 3 for Lizard")
        print("Select 4 for Spock")

        user_choice = int(input("Select a gesture: "))
        if user_choice > 4:
            time.sleep(1)
            print("Please enter a valid answer")
            self.choose_gesture()
        else:
            self.chosen_gesture = self.gestures[user_choice]
            time.sleep(1)
            print(f'{self.name} has chosen {self.chosen_gesture}')





        


    
        





