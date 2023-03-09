from unittest.mock import patch
import unittest
from game import Game
from database import Database
from helpers import Mode, Start_Up, Settings
from winner import Winner
from player import Player


class TestGame(unittest.TestCase):
    
    def setUp(self):
        self.db = Database()
        self.game = Game(self.db)
    
    
    def test_game(self):
        g = self.game
        self.assertIsNotNone(Game(self.db))
        g.codename = 'JANE'
        self.assertEqual(g.codename, 'JANE')
        self.assertIsNone(g.display_rules())
        scores = [('One', 1, 102), ('Two', 2, 209), ('Three', 3, 315)]
        resp = g.show_highscore(scores)
        self.assertIsNone(resp)
        self.assertIsNone(g.menu_transition())
        g._p2 = Player('CPU')
        g._p1 = Player('Erick')
        #g._p2.name = 'CPU'
        self.assertIsNone(g.play())
        
        
        
    def test_game_for_test(self):
        p1 = Player('Erick')
        p2 = Player('Robert')
        mode = Mode.DUEL
        self.game.game_for_test(p1, p2, mode)
        self.assertEqual(self.game.mode, mode)

    # @patch('game.input', return_value='1')
    # def test_show_menu(self, input):
    #     g = self.game
    #     title = 'Title'
    #     input.side_effect = '1'
    #     mode = Mode.DUEL
    #     sup = Start_Up.NEW_GAME
    #     set = Settings.NAME
    #     resp_mode = g.show_menu(title, mode)
    #     self.assertIsInstance(resp_mode, Mode)
    #     resp_sup = g.show_menu(title, sup)
    #     self.assertIsInstance(resp_sup, Start_Up)
    #     resp_set = g.show_menu(title, set)
    #     self.assertIsInstance(resp_set, Settings)

    def test_mode(self):
        self.game.mode = Mode.DUEL
        self.assertNotEqual(self.game.mode, Mode.SOLO_EASY)
        
        with self.assertRaises(TypeError):
            self.game.mode = 'Mode.SOLO_EASY'
            self.assertIsInstance(self.game.mode, Game)





if __name__ == '__main__':
    unittest.main()