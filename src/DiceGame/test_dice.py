"""This module test dice using unittest."""
import unittest
from dice import Dice
from helpers import Mode


class TestDice(unittest.TestCase):
    """Test classes and methods using UnitTest."""

    def setUp(self):
        """Test setup method using UnitTest."""
        self.dice = Dice()

    def test_dice(self):
        """Test dice method using UnitTest."""
        die = Dice()
        self.assertIsNotNone(die)
        die2 = Dice(Mode.SOLO_MEDIUM)
        self.assertNotEqual(die, die2)

    def test_mode(self):
        """Test mode method using UnitTest."""
        self.dice.mode = Mode.SOLO_MERCILESS
        self.assertEqual(self.dice.mode, Mode.SOLO_MERCILESS)
        self.assertIn(self.dice.mode, Mode)

        with self.assertRaises(TypeError):
            self.dice.mode = 'SOLO_MERCILESS'

        with self.assertRaises(ValueError):
            self.dice.mode = Mode.DUEL

    def test_roll(self):
        """Test roll method using UnitTest."""
        # Balanced Dice
        dice = Dice()
        self.assertIn(dice.roll(), range(1, 7))

        # Unbalanced Dice
        size = 10000
        proba = [0.167, 0.091, 0.055, 0.026]
        modes = [
            Mode.SOLO_EASY,
            Mode.SOLO_MEDIUM,
            Mode.SOLO_HARD,
            Mode.SOLO_MERCILESS
            ]
        for i in range(len(proba)):
            rolls = 0
            dice.mode = modes[i]
            for j in range(size):
                if dice.roll() == 1:
                    rolls += 1
            self.assertAlmostEqual(rolls/size, proba[i], 1)

    def test__items(self):
        """Test get items method using UnitTest."""
        dice = Dice()
        dice.mode = Mode.SOLO_EASY
        list_items = dice._items()
        self.assertEqual(len(list_items), 6)

        dice.mode = Mode.SOLO_MEDIUM
        list_items = dice._items()
        self.assertEqual(len(list_items), 11)

        dice.mode = Mode.SOLO_HARD
        list_items = dice._items()
        self.assertEqual(len(list_items), 18)

        dice.mode = Mode.SOLO_MERCILESS
        list_items = dice._items()
        self.assertEqual(len(list_items), 38)


# if __name__ == '__main__':
#     unittest.main()
