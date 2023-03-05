""" Main for running the Dice Game Pig
    This contains the main program entry point
"""

import sys
from game import Game
from helpers import Mode, Entry_Menu
from database import Database
from gui import GUI


def main():
    ### INITIALISATION  ONLY ONCE ###
    # A - Load Games from Database
    # B - Extract HighScore from Database
    db = Database()
    gui = GUI()
    games_dict = db.get_games()
    highscore = db.get_highscore()
    flag = 2
    
    while True:

        # 1 - Show the entry_menu (New Game - Resume Game)
        entry_choice = gui.display_entry_menu()

        # 2 - deal with the entry_choice for the right option
        if entry_choice == Entry_Menu.NEW.value:
            print('Choice is New Game')
        
        if entry_choice == Entry_Menu.RESUME.value:
            is_in_database = False
            while not is_in_database:
                game_code = input('Enter the Game Code (or B to go back):')
                if  game_code.lower == 'b':
                    
                # ask for the Game code to resume
                    break
            
            print('Choice is Resume Game')
        
        if entry_choice == Entry_Menu.EXIT.value:
            print('Choice is Exit Main')
        
        #   1 - New Game()
        #   2 - Resume Gane()
        # get the list of code and games from the database
        
        # start a new instance of game
        game = Game()
        
        # 
        # -> game.initiate_
        # game.show_menu()
        # START NEW GAME
        # 1 - duel  (2 players -> names)
        # 2 - solo Easy (1 player -> name)
        # 3 - solo medium
        # 4 - solo hard
        # 5 - solo merciless
        # RESUME GAME
        # 6 - restart (get game code [change name to code])
        # HIGHLIGHTS
        # 7 - Show Highscore
        
    # Show Menu of option
    # 1 - Resume a game --> ask name of the gamr
        #GUI <- SOLO EASY
        game.start(Mode.DUEL)
    # - Mode selection (type of game)
    # - Reload suspended Game
    # - Show Highscore
    
    # Select the Mode
    
    # Enter Players Details (depending of mode)
    
        if game.exit() == True:
            break





if __name__ == "__main__":
    main()