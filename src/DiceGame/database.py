import pickle
import random
from game import Game
from winner import Winner
from helpers import Data_Path as PATH, CODE_NAMES
import time
import os
os.chdir(os.path.dirname(os.path.realpath(__file__)))

class Database:
    
    def __init__(self):
        self._games: dict[str : Game] # paused games
        self._winners = self._load_data(PATH.WINNERS)
        self._highscore = self._generate_highscore()



    @property
    def highscore(self) -> list:
        return self._highscore
    
    
    
    ## PUBLIC METHODS
    def load_game(self, code: str) -> Game:
        game = self._games.pop(code, None)
        if game != None: self._store_data(self._games, PATH.GAMES)
        return game
    
    
    def store_game(self, game: Game) -> str:
        used_codes = self._games.keys()
        while code := random.choice(CODE_NAMES) not in used_codes:
            break
        self._games[code] = game
        self._store_data(self._games, PATH.GAMES)
        return code
    
    
    def add_winner(self, winner: Winner):
        self._winners.append(winner)
        self._store_data(self._winners, PATH.WINNERS)
        self._update_highscore()
        
    
    
    ## PRIVATE METHODS
    def _update_highscore(self):
        self._highscore = self._generate_highscore()
        pass
        
    def _load_data(self, p: PATH):
        file = open(p.value, 'rb')
        data = pickle.load(file)
        file.close()
        return data
    
    
    def _store_data(self, data, p: PATH):
        file = open(p.value, 'wb')
        pickle.dump(data, file)
        file.close()


    def _generate_highscore(self) -> list:
        data = [win.data for win in self._winners]
        data.sort(key=lambda win: win[0])
        collection = []
        name = data[0][1]
        pts = data[0][2]
        streak = 1
        for _, win in enumerate(data, 1):
            victor = win[1]
            score = win[2]
            if victor == name:
                pts += score
                streak += 1
            else:
                collection.append([name, streak, pts])
                name = victor
                pts = score
                streak = 1
        collection.sort(key=lambda row: (-row[1], -row[2]))
        return collection


    def _load_dummy_winners(self) -> list[Winner]:
        dummies = []
        size = 10
        people = ['Erick', 'Robert', 'Jennifer', 'Ciara', 'CPU']
        for _ in range(size):
            winner = random.choice(people)
            points = random.randint(100, 105)
            stamp = random.randint(20000, 50000)
            dummies.append(Winner(winner, points, stamp))
        return dummies
    
