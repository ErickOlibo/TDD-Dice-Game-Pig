import unittest
import dice 

class TestDice(unittest.TestCase):
    def test_roll(self):
        d = dice.Dice()                 #Instantiate the dice class
        roll = d.roll()                 #roll the dice
        self.assertTrue(1 <= roll <=6)  #Assert that the rolled dice value is between 1 ansd 6


if __name__ == 'main':
    unittest.main()
        
