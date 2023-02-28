import unittest
import DiceGame.dice as dice

class TestDice(unittest.TestCase):
    def test_roll(self):
        d = dice.Dice()
        roll = d.roll()
        self.assertTrue(1 <= roll <=6)


if __name__ == 'main':
    unittest.main()
        
