""" Main for running the Dice Game Pig
    This contains the main program entry point
"""

import sys
from game import Game
from helpers import *
from database import Database
from gui import GUI
import time


def main():

    game = Game()
    game.training_game()
    
    # A GAME PLAYED gives you a Winner object or a codename for Database
    while True:
        break
        # 1 - Start an instance of Game
        game = Game()
        db = Database()
        
        # 2 - Get the option from the user for the Start Up menu
        start_choice = game.show_menu('START UP', Start_Up.MENU)
        
        # 3 - Handle Chosen Option
        game.menu_transition()
        if start_choice == Start_Up.EXIT: 
            break 
        
        if start_choice == Start_Up.NEW_GAME:
            new_game_choice = game.show_menu('NEW GAME MODE', Mode.MENU)
            if new_game_choice == Mode.BACK:
                game.menu_transition()
                continue
            
            if new_game_choice == Mode.DUEL:
                game.set_duel_players()
            
            solo_mode = [mode for mode in Mode if mode not in [Mode.DUEL, Mode.BACK]]
            if new_game_choice in solo_mode:
                game.set_solo_player(new_game_choice)

            # START THE NEW GAME
            game.play()
                
        if start_choice == Start_Up.RESUME_GAME:
            codename = game.request_codename_from_user()
            # RESTART A SUPENDED GAME
            game.play(codename)
        
        
        if start_choice == Start_Up.HIGH_SCORE:
            scores = db.get_highscore()
            game.show_highscore(scores)
            game.press_any_keys_to_continue()


        if start_choice == Start_Up.RULES:
            game.display_rules()
            game.press_any_keys_to_continue()
            


def new_game(game: Game):
    print('New Game')


def resume_game(game: Game):
    print('Resume Game')





if __name__ == "__main__":
    main()