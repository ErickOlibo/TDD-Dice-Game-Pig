import unittest
from game import Game
from helpers import Mode

class TestGame(unittest.TestCase):
    
    def setUp(self):
        self.game = Game()
    
    
    def test_game(self):
        self.assertIsNotNone(Game())
        
    
    def test_name(self):
        self.game.name = 'Heros game'
        self.assertIsNot(self.game.name, 'Monday')
        
        with self.assertRaises(TypeError):
            self.game.name = 12
            self.assertNotIsInstance(self.game.name, int)
    
    def test_get_menu(self):
        self.assertIsNotNone(self.game.get_menu())
        self.assertIsInstance(self.game.get_menu(), str)
    
    def test_get_rules(self):
        self.assertIsNotNone(self.game.get_rules())
        self.assertIsInstance(self.game.get_rules(), str)
        
    
    def test_mode(self):
        self.game.mode = Mode.BATTLE
        self.assertNotEqual(self.game.mode, Mode.SOLO)
        
        with self.assertRaises(TypeError):
            self.game.mode = 'Mode.SOLO'
            self.assertIsInstance(self.game.mode, Game)


if __name__ == '__main__':
    unittest.main()