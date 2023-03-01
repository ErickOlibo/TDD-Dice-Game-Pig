import unittest
from dice import Dice, CPUDice
from helpers import Difficulty

class TestDice(unittest.TestCase):
    def test_roll(self):
        d = Dice()                 #Instantiate the dice class
        roll = d.roll()                 #roll the dice
        self.assertTrue(1 <= roll <=6)  #Assert that the rolled dice value is between 1 ansd 6


class TestCPUDice(unittest.TestCase):
    
    def setUp(self):
        self.cpu_dice = CPUDice(Difficulty.EASY)
    
    # instantiate an object CPUDice
    def test_cpudice(self):
        self.assertIsNotNone(self.cpu_dice)
        


    def test_roll(self):
        self.cpu_dice.level = Difficulty.HARD
        self.assertIsInstance(self.cpu_dice.roll(), int)
        self.assertIn(self.cpu_dice.roll(), range(1,7))
        
    
    def test__items(self):
        self.cpu_dice.level = Difficulty.EASY
        list_items = self.cpu_dice._items()
        self.assertEqual(len(list_items), 6)
        
        self.cpu_dice.level = Difficulty.MEDIUM
        list_items = self.cpu_dice._items()
        self.assertEqual(len(list_items), 11)
        
        self.cpu_dice.level = Difficulty.HARD
        list_items = self.cpu_dice._items()
        self.assertEqual(len(list_items), 18)
        
        self.cpu_dice.level = Difficulty.IMPOSSIBLE
        list_items = self.cpu_dice._items()
        self.assertEqual(len(list_items), 38)
        
        


if __name__ == '__main__':
    unittest.main()
        
