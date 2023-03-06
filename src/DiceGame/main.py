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
        
        # 2 - Get the choice of the user at Start Up menu
        #print('\n')
        choice = game.show_startup_menu()
        if choice in ['e', 'E']: break 
        
        # 3 - Deal with the Choice
        if choice == '1':
            pass
        
        if choice == '2':
            pass
        
        if choice == '3':
            pass
        
        if choice == '4':
            game.display_rules()
            #print()
            game.press_any_keys_to_continue()
            #print()
            

def new_game():
    pass

def resume_game():
    pass

def show_highscore():
    pass




if __name__ == "__main__":
    main()