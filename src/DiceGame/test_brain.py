"""This module test brain using unittest."""
import unittest
from helpers import Turn, Tactic
from brain import Brain


class TestBrain(unittest.TestCase):
    """Test classes and methods using UnitTest."""

    def setUp(self):
        """Test method using UnitTest."""
        self.brain = Brain()

    def test_brain(self):
        """Test the brain method using UnitTest."""
        self.assertIsNotNone(Brain())

    def test_random_strategy(self):
        """Test brain random strategy method using UnitTest."""
        strategy = self.brain._strategy
        self.assertIsInstance(strategy, Tactic)
        self.assertIn(strategy, list(Tactic))

    def test_action(self):
        """Test action method using UnitTest."""
        self.brain._strategy = Tactic.TWENTY_FIVE
        self.assertIsInstance(self.brain.action(45, 19), Turn)
        self.assertEqual(self.brain.action(45, 19), Turn.ROLL)
        self.assertEqual(self.brain.action(20, 27), Turn.HOLD)
        self.brain._strategy = Tactic.FOUR_TURNS
        self.assertEqual(self.brain.action(45, 31), Turn.HOLD)
        self.brain._current_turns = 0
        self.assertEqual(self.brain.action(45, 29), Turn.ROLL)
        self.brain._current_turns = 2
        self.assertEqual(self.brain.action(55, 15), Turn.ROLL)
        self.brain._current_turns = 2
        self.assertEqual(self.brain.action(55, 25), Turn.HOLD)

        with self.assertRaises(ZeroDivisionError):
            self.brain._current_turns = 4
            self.assertEqual(self.brain.action(45, 31), Turn.HOLD)


# if __name__ == '__main__':
#     unittest.main()
