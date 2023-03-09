"""This module test gui using unittest."""
from unittest.mock import patch
import unittest
from gui import GUI


class TestGUI(unittest.TestCase):
    """Test classes and methods using UnitTest."""

    def setUp(self):
        """Test set up method using UnitTest."""
        self.gui = GUI()

    def test_gui_display(self):
        """Test gui display method using UnitTest."""
        self.assertIsNone(self.gui.clear_terminal())
        self.assertIsNone(self.gui.display_info('Content', 'Title'))
        ask = 'ROLL OR HOLD (R, H)? '
        answer = self.gui.get_simple_answer_from_cpu(ask, 'Title')
        self.assertIn(ask, answer)
        self.assertTrue(ask in answer)
        self.assertIsNone(self.gui.display_hand_results([1, 2], 30))
        sent = self.gui.display_hand_results_split([1, 2, 3, 4], 30, 1)
        self.assertIsNone(sent)
        sent = self.gui.display_scoreboard('E', 10, 'R', 12, 'E')
        self.assertIsNone(sent)
        sent = self.gui.display_scoreboard('E', 10, 'R', 12, 'R')
        self.assertIsNone(sent)
        scores = [('One', 1, 102), ('Two', 2, 209), ('Three', 3, 315)]
        sent = self.gui.display_highscore(scores, 10)
        self.assertIsNone(sent)
        resp = self.gui.insert_line_breaks()
        self.assertIsNone(resp)
        resp = self.gui.print_to_display(ask)
        self.assertIsNone(resp)
        resp = self.gui.cpu_question_answer_animation('A', 'B')
        self.assertIsNone(resp)
        resp = self.gui._get_rolls_points(45)
        self.assertEqual(len(resp), 5)

    @patch('gui.input', return_value='R')
    def test_get_answer_from_user(self, input):
        """Test get answer from user method using UnitTest."""
        ask = 'ROLL OR HOLD (R, H)? '
        title = 'Title'
        resp = self.gui.get_simple_answer_from_user(ask, title)
        self.assertEqual(resp, 'R')

    @patch('gui.input', return_value='')
    def test_display_message_and_continues(self, input):
        """Test display message and continues method using UnitTest."""
        ask = 'Select an option? '
        resp = self.gui.display_message_and_continues(ask)
        self.assertEqual(resp, None)

    @patch('gui.input', return_value='2')
    def test_display_paused_game_message(self, input):
        """Test display paused game message method using UnitTest."""
        ask = 'Select an option? '
        resp = self.gui.display_paused_game_message(ask)
        input(resp)
        self.assertIsNotNone(resp, None)

    def test__shrink_name(self):
        """Test shrink name method using UnitTest."""
        s_name = self.gui._shrink_name("Christopher", 13)
        self.assertEqual("Christopher", s_name)
        s_name = self.gui._shrink_name("Matthew-Lorenzo", 13)
        self.assertTrue(len(s_name) == 13)
        self.assertTrue(s_name[-3:] == "...")


# if __name__ == '__main__':
#     unittest.main()
