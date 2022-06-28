from player import Player
import random

class Ai(Player):
    def __init__(self) -> None:
        super().__init__("name")
        self.ai_gesture = self.gestures

    def choose_random_gesture(self, list):
        random_item = random.choice(list)
        return random_item


        



    

    
        
