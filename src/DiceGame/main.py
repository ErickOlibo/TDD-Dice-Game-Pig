""" Main for running the Dice Game Pig
    This contains the main program entry point
"""

import sys
from game import Game
from helpers import Mode


def main():
    flag = 2
    while True:
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
        # HIGHTLIGHT
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