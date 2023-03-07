import unittest
from database import Database
from game import Game
from winner import Winner
import random
from helpers import Textual, Mode
import time

class TestDatabase(unittest.TestCase):
    
    def setUp(self):
        self.db = Database()
        self.game1 = Game()
        self.game2 = Game()
        self.game3 = Game()
        self.games = [self.game1, self.game2, self.game3]
    
    
    def test_database(self):
        self.assertIsNotNone(self.db)
        self.assertIsInstance(self.db._games, dict)
        self.assertIsInstance(self.db._winners, list)
        self.assertIsInstance(self.db.highscore, list)
    
    def test_load_game(self):
        self.assertIsNone(self.db.load_game('XXXX'))
    
    def test_store_game(self):
        code = self.db.store_game(self.game1)
        self.assertEqual(len(code), 4)
        game = self.db.load_game(code)
        self.assertEqual(self.game1, game)
    
    
    def test_add_winner(self):
        pep = random.choice(['Erick', 'Robert', 'Jennifer', 'Ciara', 'CPU'])
        pts = random.randint(100, 105)
        win = Winner(pep, pts)
        numb1 = len(self.db._winners)
        self.db.add_winner(win)
        numb2 = len(self.db._winners)
        self.assertEqual(numb1 +1, numb2)
    

    def test_update_winner_name(self):
        pass
        
    def test__get_used_codenames(self):
        pass
    
    def test__update_highscore(self):
        pass
    
    def test__load_data(self):
        pass
    
    def test__store_data(self):
        pass
    
    def test__generate_highscore(self):
        pass


        

if __name__ == '__main__':
    unittest.main()