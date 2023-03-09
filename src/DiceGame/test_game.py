"""This module test game using unittest."""
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
    """Test classes and methods using UnitTest."""

    def setUp(self):
        """Test set up method using UnitTest."""
        self.db = Database()
        self.game = Game(self.db)
        self.game._p1 = Player('Erick')
        self.game._p2 = Player('CPU', Brain(), Dice(Mode.SOLO_MERCILESS))
        self.game._hand = self.game._p2

    def test_game(self):
        """Test game method using UnitTest."""
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
        """Test messages method using UnitTest."""
        g = self.game
        self.assertTrue('any key' in g._intro_message())
        self.assertTrue('any key' in g._loss_message())
        self.assertTrue('HOLD' in g._roll_or_hold_message())
        self.assertTrue('10 points' in g._hold_message(10))
        resp = g._we_have_winner_message()
        self.assertTrue('THE WINNER IS' in resp)

    @patch('game.input', return_value='Erick')
    def test_set_player_one(self, input):
        """Test set player one method using UnitTest."""
        g = Game(self.db)
        self.assertIsNone(g.set_player_one())

    @patch('game.input', return_value='Robert')
    def test_set_player_two(self, input):
        """Test set player two method using UnitTest."""
        g = Game(self.db)
        g._p1 = Player('Erick')
        self.assertIsNone(g.set_player_two())
        g._p1 = Player('Robert')
        self.assertIsNone(g.set_player_two())

    def test_game_for_test(self):
        """Test game for test method using UnitTest."""
        p1 = Player('Erick')
        p2 = Player('Robert')
        mode = Mode.DUEL
        self.game.game_for_test(p1, p2, mode)
        self.assertEqual(self.game.mode, mode)

    @patch('game.input', return_value='')
    def test_hold_roll_win(self, input):
        """Test hold or roll and win method using UnitTest."""
        g = self.game
        g._hand = g._p1
        resp = g._hold_for_win()
        self.assertEqual(resp, None)
        resp = g._choose_hold()
        self.assertEqual(resp, None)
        resp = g._rolled_one()
        self.assertIsInstance(resp, Turn)

        g._hand = g._p2
        resp = g._hold_for_win()
        self.assertEqual(resp, None)
        resp = g._choose_hold()
        self.assertEqual(resp, None)
        resp = g._rolled_one()
        self.assertIsInstance(resp, Turn)

        resp = g._play_new_solo_game()
        self.assertEqual(resp, None)

    def test_show_menu_offload(self):
        """Test show menu offload method using UnitTest."""
        g = self.game
        resp = g._show_menu_offload('Title', Start_Up.EXIT)
        self.assertTrue(len(resp) == 5)

        resp = g._show_menu_offload('Title', Mode.BACK)
        self.assertTrue(len(resp) == 5)

        resp = g._show_menu_offload('Title', Settings.BACK)
        self.assertTrue(len(resp) == 5)

    def test_set_solo_player_offload(self):
        """Test set solo player offload method using UnitTest."""
        g = self.game
        ask = g._set_solo_player_offload(Mode.SOLO_EASY)
        self.assertIn('name', ask)

    def test__resp_is_turn_settings(self):
        """Test response from setting menu method using UnitTest."""
        g = self.game
        choices = [Settings.BACK, Settings.CHEAT, Settings.QUIT]
        [self.assertIsNone(g._resp_is_turn_settings(elem)) for elem in choices]
        self.assertIsInstance(g._resp_is_turn_settings(Settings.PAUSE), str)
        self.assertIsInstance(g._resp_is_turn_settings(Settings.NAME), list)

    def test_start_of_trun_scoreboard(self):
        """Test opening scoreboard display method using UnitTest."""
        g = self.game
        g._p2.add_points_to_score(34)
        [g._p2.roll_dice() for _ in range(4)]
        g._p1.add_points_to_score(34)
        [g._p1.roll_dice() for _ in range(4)]
        g._back_from_settings = True
        self.assertIsNone(g._start_of_turn_scoreboard())
        g._back_from_settings = False
        self.assertIsNone(g._start_of_turn_scoreboard())

    @patch('game.input', return_value='Erick')
    def test_set_solo_player(self, input):
        """Test set solo player method using UnitTest."""
        g = self.game
        mode = Mode.SOLO_HARD
        self.assertIsNone(g.set_solo_player(mode))

    @patch('game.input', return_value='Jane')
    def test_request_codename_from_user(self, input):
        """Test request codename method using UnitTest."""
        g = self.game
        self.assertEqual(g.request_codename_from_user(), 'Jane')

    @patch('game.input', return_value='1')
    def test_show_menu(self, input):
        """Test show menu method using UnitTest."""
        g = self.game
        self.assertIsInstance(g.show_menu('Title', Mode.MENU), Mode)

    @patch('game.input', return_value='Erick')
    def test_show_menu_raise(self, input):
        """Test show menu raise method using UnitTest."""
        g = self.game
        self.assertIsInstance(g.show_menu('Title', Mode.MENU), Mode)

    @patch('game.input', return_value='')
    def test_resp_is_turn_hold_for_win(self, input):
        """Test response on hold for win method using UnitTest."""
        g = self.game
        g._p2.add_points_to_score(99)
        [g._p2.roll_dice() for _ in range(4)]
        self.assertIsNone(g._resp_is_turn_hold_value())

    @patch('game.input', return_value='')
    def test_resp_is_turn_choose_hold(self, input):
        """Test response is turn play method using UnitTest."""
        g = self.game
        g._p1.add_points_to_score(34)
        [g._p1.roll_dice() for _ in range(4)]
        self.assertIsNone(g._resp_is_turn_hold_value())

    def test_playing_a_turn_1(self):
        """Test playing turn one method using UnitTest."""
        g = self.game
        g._hand = g._p1
        [g._p1.roll_dice() for _ in range(12)]
        self.assertIsNone(g._playing_a_turn())

    @patch('game.input', return_value='')
    def test_playing_a_turn_2(self, input):
        """Test playing turn two method using UnitTest."""
        g = self.game
        g._hand = g._p2
        [g._p2.roll_dice() for _ in range(5)]
        self.assertIsNone(g._playing_a_turn())

    @patch('game.input', return_value='')
    def test_resolve_Show_settings_menu(self, input):
        """Test resolve show settings menu method using UnitTest."""
        g = self.game
        s = Settings
        sets = [s.BACK, s.CHEAT, s.NAME, s.QUIT, s.PAUSE]
        [self.assertIsNone(g._resolve_show_settings_menu(se))for se in sets]

    @patch('game.input', return_value='1')
    def test_play_new_game(self, input):
        """Test play new game method using UnitTest."""
        g = self.game
        g._winner = Winner('E', 104)
        self.assertIsNone(g._play_new_game(True))

        g._winner = None
        g._has_quit = True
        self.assertIsNone(g._play_new_game(False))

    @patch('game.input', return_value='1')
    def test_play_with_codename(self, input):
        """Test play with codename method using UnitTest."""
        g = self.game
        g._winner = Winner('E', 104)
        self.assertIsNone(g.play())

        self.assertIsNone(g.play('Neva'))

    def test_mode(self):
        """Test mode method using UnitTest."""
        self.game.mode = Mode.DUEL
        self.assertNotEqual(self.game.mode, Mode.SOLO_EASY)
        with self.assertRaises(TypeError):
            self.game.mode = 'Mode.SOLO_EASY'
            self.assertIsInstance(self.game.mode, Game)


# if __name__ == '__main__':
#     unittest.main()
