"""This module creates and maintains a database for the application."""
import pickle
import random
from game import Game
from winner import Winner
from player import Player
from helpers import Data_Path as PATH, CODE_NAMES, Mode
import os
os.chdir(os.path.dirname(os.path.realpath(__file__)))


class Database:

    def __init__(self):
        """Construct the necessary attributes for the database object."""
        self._games = self._load_data(PATH.GAMES)
        self._winners = self._load_data(PATH.WINNERS)
        self._highscore = self._generate_highscore()

    @property
    def highscore(self) -> list:
        return self._highscore

    def load_game(self, code: str) -> Game:
        game = self._games.pop(code, None)
        if game is not None:
            self._store_data(self._games, PATH.GAMES)
        return game

    def store_game(self, game: Game) -> str:
        used_codes = self._games.keys()
        while True:
            code = random.choice(CODE_NAMES)
            if code not in used_codes:
                break
        game.codename = code
        self._games[code] = game
        self._store_data(self._games, PATH.GAMES)
        return code

    def add_winner(self, winner: Winner):
        self._winners.append(winner)
        self._store_data(self._winners, PATH.WINNERS)
        self._update_highscore()

    def update_winner_name(self, old: str, new: str):
        winners = []
        for win in self._winners:
            [st, n, sc,] = win.data
            upd_win = Winner(new, sc, st) if n == old else win
            winners.append(upd_win)
        self._winners = winners
        self._store_data(self._winners, PATH.WINNERS)

    def _get_used_codenames(self) -> list[str]:
        return [game.codename for game in self._games]

    def _update_highscore(self):
        self._highscore = self._generate_highscore()

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

    def _display_some_info_on_database(self):
        print(f'Games Paused Size: {len(self._games.keys())}')
        print(f'Winners Size: {len(self._winners)}')
        print()
        print(self._games.keys())

        sada = self._games['Sada']
        print(f'{sada._p1.name} - {sada._p2.name}')

        for gm in self._games.values():
            print(f'{gm._codename} - {gm._p1.name} - {gm._p2.name}')

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

    def _load_dummy_games(self) -> dict[str: Game]:
        dummies = dict()
        size = 10
        people = ['Erick', 'Robert', 'Jennifer', 'Ciara', 'CPU']
        codenames = random.sample(CODE_NAMES, k=size)
        modes = [
            Mode.DUEL, Mode.SOLO_EASY,
            Mode.SOLO_MEDIUM, Mode.SOLO_MERCILESS
            ]
        for i in range(size):
            [p1, p2] = random.sample(people, k=2)
            mode = random.choice(modes)
            pep1 = Player(p1)
            pep2 = Player(p2)
            codename = codenames[i]
            game = Game()
            game.game_for_test(pep1, pep2, mode)
            game.codename = codename
            dummies[codename] = game
        return dummies
