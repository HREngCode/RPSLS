from player import Player

class Human(Player):
    def __init__(self):
        super().__init__()
        self.human_player_one = Player("Player 1")
        self.human_player_two = Player("Player 2")
        self.human_gesture = self.gestures


        if self.number_of_players == "1":
            
            self.human_gesture = input("Player 1 please select a gesture: ")
        elif self.number_of_players == "2":

            print(f'Player one has selected {player_one}!')





        


    
        





