import unittest
from database import Database
from game import Game
from helpers import Textual, Mode

class TestDatabase(unittest.TestCase):
    
    def setUp(self):
        self.db = Database()
        self.game1 = Game()
        self.game2 = Game()
        self.game3 = Game()
        self.games = [self.game1, self.game2, self.game3]
    
    
    def test_name(self):
        uuids = [game._uuid for game in self.games]
        self.assertEqual(len(set(uuids)), len(uuids)) # unique uuid
        for game in self.games:
            self.assertEqual(game._rules, Textual.RULES.value)
            self.assertEqual(game._menu, Textual.MENU.value)
            self.assertIsNotNone(game._uuid)


    def test_mode(self):
        self.assertEqual(self.game1.mode, Mode.SOLO_EASY)
        self.game2.mode = Mode.SOLO_MERCILESS
        self.assertNotEqual(self.game1.mode, self.game2.mode)



        

if __name__ == '__main__':
    unittest.main()