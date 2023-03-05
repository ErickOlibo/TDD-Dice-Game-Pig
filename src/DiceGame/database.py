import pickle
from game import Game


class Database:
    
    def __init__(self):
        self._games = self._load_games_db()
        self._highscore = None # array 
        self._paused_games = None
    

   
    def _load_games_db(self) -> list[Game]:
        # unpickle database
        
        # Update properties
        self._update_properties
        return []


    def _update_properties(self):
        pass
    

    def get_highscore(self) -> list:
        winners = [game.winner for game in self._games]
        return self._highscore
    
    
    def save_game(self, game: Game):
        # add game to list of games
        self._games.append(game)
        self._update_properties()
        # update
        
        pass
    
    
    
    
    def update_highscrore(self):
        pass
    
    def _generate_highscore(self):
        # get high score from list of finished games
        pass
    
    def _generate_used_codenames(self):
        pass