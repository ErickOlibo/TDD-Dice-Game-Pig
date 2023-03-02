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

    
    def test_display_rules(self):
        self.assertIsNone(self.game.display_rules())
        self.assertIsNotNone(self.game._rules)
        
    
    def test_start(self):
        with self.assertRaises(TypeError):
            self.game.start()
        
        self.game.mode = Mode.DUEL
        self.assertEqual(self.game.mode, Mode.DUEL)
    
    def test__start_menu(self):
        self.assertIsNone(self.game._start_menu())
        self.assertIsNotNone(self.game._menu)

    
    def test_mode(self):
        self.game.mode = Mode.DUEL
        self.assertNotEqual(self.game.mode, Mode.SOLO_EASY)
        
        with self.assertRaises(TypeError):
            self.game.mode = 'Mode.SOLO_EASY'
            self.assertIsInstance(self.game.mode, Game)


if __name__ == '__main__':
    unittest.main()