import pickle
import random
from game import Game
from winner import Winner

class Database:
    
    def __init__(self):
        # dummy list of winners for testing
        dummy_winners = []
        size = 500
        people = ['Erick', 'Robert', 'Jennifer', 'Ciara', 'CPU']
        for _ in range(size):
            couple = random.sample(people, k=2)
            points = random.randint(100, 105)
            stamp = random.randint(20000, 50000)
            dummy_winners.append(Winner(couple[0], couple[1], points, stamp))
        data = [win.data for win in dummy_winners]
        #print(data)
        data.sort(key=lambda win: win[0])
        collection = []
        name = data[0][1]
        pts = data[0][3]
        streak = 1
        for i, win in enumerate(data, 1):
            victor = win[1]
            score = win[3]
            if victor == name:
                pts += score
                streak += 1
            else:
                collection.append([name, streak, pts])
                name = victor
                pts = score
                streak = 1
            
        #[print(w) for w in collection]
        self._highscore = collection
        #[print(item) for item in data]
        #[print(win.data) for win in self._winners]

        # Unpickle database and set paused game & winners

        #self._paused_games = self._load_paused_games_db() # to change -> from pickle
        #self._winners = self._load_winners() # to change -> from pickle
        #self._highscore = None # array 
        #self._paused_games = None
    

   
    def _load_paused_games_db(self) -> list[Game]:
        # unpickle database
        
        # Update properties
        self._update_properties
        return []


    def _load_winners(self) -> list[Winner]:
        pass
    
    def add_winner(self, winner: Winner):
        self._winners.append(winner)
    

    def get_highscore(self) -> list:
        return self._highscore
    
    
    def save_paused_game(self, game: Game):
        self._paused_games.append(game)
        self._update_paused_game_database()

    
    def _update_paused_game_database(self):
        pass
    
    def get_saved_game(self, codename: str) -> Game:
        pass
    
    def update_highscrore(self):
        pass
    
    def _generate_highscore(self):
        # get high score from list of finished games
        pass
    
    def _generate_used_codenames(self):
        pass