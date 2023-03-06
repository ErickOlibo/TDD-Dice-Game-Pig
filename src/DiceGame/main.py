""" Main for running the Dice Game Pig
    This contains the main program entry point
"""

import sys
from game import Game
from helpers import *
from database import Database
from gui import GUI


def main():

    while True:

        # 1 - Start an instance of Game
        game = Game()
        db = Database()
        # 2 - Get the choice of the user at Start Up menu
        start_choice = game.show_startup_menu()
        print(start_choice)
        game.menu_transition()
        if start_choice in Start_Up.EXIT.value: break 
        
        # 3 - Deal with the Choice
        if start_choice == Start_Up.NEW_GAME.value:
            new_game_choice = game.show_new_game_menu()
            if new_game_choice in New_Game.BACK.value:
                game.menu_transition()
                continue
            
            if new_game_choice == New_Game.DUEL.value:
                game.set_duel_players()
            
            if new_game_choice == New_Game.EASY.value:
                game.set_solo_player(Mode.SOLO_EASY)
            
            if new_game_choice == New_Game.MEDIUM.value:
                game.set_solo_player(Mode.SOLO_MEDIUM)
                game.play()
            
            if new_game_choice == New_Game.HARD.value:
                game.set_solo_player(Mode.SOLO_HARD)
                game.play()
                
            
            if new_game_choice == New_Game.MERCILESS.value:
                game.set_solo_player(Mode.SOLO_MERCILESS)
                game.play()
            
            # Play the Game
            game.play()
                
        if start_choice == '2':
            # From database
            resume_game(game)
            
        
        if start_choice == '3':
            # from database
            scores = db.get_highscore()
            game.show_highscore(scores)
            game.press_any_keys_to_continue()
            pass
            
        
        if start_choice == '4':
            game.display_rules()
            game.press_any_keys_to_continue()
            

def new_game(game: Game):
    
    print('New Game')

def resume_game(game: Game):
    print('Resume Game')





if __name__ == "__main__":
    main()