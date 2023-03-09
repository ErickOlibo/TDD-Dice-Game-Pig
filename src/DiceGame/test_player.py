"""This module test player using unittest."""
import unittest
from player import Player
from helpers import Turn, Mode
from brain import Brain
from dice import Dice


class TestPlayer(unittest.TestCase):
    """Test classes and methods using UnitTest."""

    def setUp(self):
        """Test set up method using UnitTest."""
        self.jen = Player('Jennifer')

    def test_player(self):
        """Test player method using UnitTest."""
        erick = Player('Erick')
        self.assertIsNotNone(erick)
        cpu = Player('CPU', Brain(), Dice(Mode.SOLO_MERCILESS))
        self.assertIsNotNone(cpu)
        self.assertEqual(cpu.score, 0)
        self.jen.reset_rolls()
        self.assertEqual(len(self.jen.rolls), 0)

    def test_name(self):
        """Test name method using UnitTest."""
        previous = self.jen.name
        self.jen.name = 'Oliver'
        self.assertNotEqual(self.jen.name, previous)

    def test_brain(self):
        """Test brain method using UnitTest."""
        with self.assertRaises(TypeError):
            self.jen.brain = 'Brain'

        self.jen.brain = Brain()
        self.assertIsInstance(self.jen.brain, Brain)

    def test_score(self):
        """Test score method using UnitTest."""
        self.assertEqual(self.jen.score, 0)

    def test_playing_choice(self):
        """Test playing choice method using UnitTest."""
        self.assertIsNone(self.jen.playing_choice(45, 5))
        cpu = Player('CPU', Brain())
        self.assertIn(cpu.playing_choice(35, 10), Turn)

    def test_add_points_to_score(self):
        """Test add points to score method using UnitTest."""
        self.jen.add_points_to_score(23)
        self.assertEqual(self.jen.score, 23)
        self.jen.add_points_to_score(17)
        self.assertNotEqual(self.jen.score, 23)

    def test_roll_dice(self):
        """Test roll of dice method using UnitTest."""
        roll = self.jen.roll_dice()
        self.assertIsInstance(roll, int)
        self.assertIn(roll, range(1, 7))


# if __name__ == '__main__':
#     unittest.main()
