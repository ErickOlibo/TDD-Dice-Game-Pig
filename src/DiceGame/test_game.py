from unittest.mock import patch
import unittest
from game import Game
from brain import Brain
from dice import Dice
from database import Database
from helpers import Mode, Start_Up, Settings, Turn
from winner import Winner
from player import Player


class TestGame(unittest.TestCase):
    
    def setUp(self):
        self.db = Database()
        self.game = Game(self.db)
        self.game._p1 = Player('Erick')
        self.game._p2 = Player('CPU', Brain(), Dice(Mode.SOLO_MERCILESS))
        self.game._hand = self.game._p2
    
    
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
        self.assertIsInstance(g._is_cpu_hand(), bool)
        g._p2.add_points_to_score(34)
        [g._p2.roll_dice() for _ in range(4)]
        resp = g._cpu_chosing()
        self.assertIn(resp, [Turn.HOLD, Turn.ROLL])
        

    def test_messages(self):
        g = self.game
        self.assertTrue('any key' in g._intro_message())
        self.assertTrue('any key' in g._loss_message())
        self.assertTrue('HOLD' in g._roll_or_hold_message())
        self.assertTrue('10 points' in g._hold_message(10))
        resp = g._we_have_winner_message()
        self.assertTrue('THE WINNER IS' in resp)
        
    def test_game_for_test(self):
        p1 = Player('Erick')
        p2 = Player('Robert')
        mode = Mode.DUEL
        self.game.game_for_test(p1, p2, mode)
        self.assertEqual(self.game.mode, mode)

    @patch('game.input', return_value='')
    def test_hold_roll_win(self, input):
        g = self.game
        resp = g._hold_for_win()
        self.assertEqual(resp, None)
        
        resp = g._choose_hold()
        self.assertEqual(resp, None)
        
        resp = g._rolled_one()
        self.assertIsInstance(resp, Turn)
        
        resp = g._play_new_solo_game()
        self.assertEqual(resp, None)

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