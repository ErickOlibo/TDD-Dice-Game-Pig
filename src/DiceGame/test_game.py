import unittest
from game import Game
from database import Database
from helpers import Mode
from winner import Winner
from player import Player


class TestGame(unittest.TestCase):
    
    def setUp(self):
        self.db = Database()
        self.game = Game(self.db)
    
    
    def test_game(self):
        self.assertIsNotNone(Game(self.db))


    def test_mode(self):
        self.game.mode = Mode.DUEL
        self.assertNotEqual(self.game.mode, Mode.SOLO_EASY)
        
        with self.assertRaises(TypeError):
            self.game.mode = 'Mode.SOLO_EASY'
            self.assertIsInstance(self.game.mode, Game)
    
    
    def test_display_rules(self):
        pass
        
    def test_show_highscore(self):
        pass
    
    def test_show_startup_menu(self):
        pass
    
    def test_show_new_game_menu(self):
        
        pass
        
    
    def test__get_input_from_user(self):
        pass
    
    def test_menu_transition(self):
        pass
    
    def test_press_any_keys_to_continue(self):
        pass
    
    def test_set_duel_players(self):
        # self.game.set_duel_players()
        # self.assertEqual(len(self.game._participants), 2)
        # self.assertEqual(self.game._mode, Mode.DUEL)
        # self.assertIsInstance(self.game._participants[0], Player)
        pass
        
    

    
            
    


if __name__ == '__main__':
    unittest.main()