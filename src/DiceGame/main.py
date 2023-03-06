""" Main for running the Dice Game Pig
    This contains the main program entry point
"""

import sys
from game import Game
from helpers import Mode
from database import Database
from gui import GUI


def main():

    while True:

        # 1 - Start an instance of Game
        game = Game()
        db = Database()
        # 2 - Get the choice of the user at Start Up menu
        choice = game.show_startup_menu()
        if choice in ['e', 'E']: break 
        
        # 3 - Deal with the Choice
        if choice == '1':
            new_game(game)
            
        
        if choice == '2':
            # From database
            resume_game(game)
            
        
        if choice == '3':
            # from database
            scores = db.get_highscore()
            game.show_highscore(scores)
            game.press_any_keys_to_continue()
            pass
            
        
        if choice == '4':
            game.display_rules()
            game.press_any_keys_to_continue()
            

def new_game(game: Game):
    
    print('New Game')

def resume_game(game: Game):
    print('Resume Game')





if __name__ == "__main__":
    main()