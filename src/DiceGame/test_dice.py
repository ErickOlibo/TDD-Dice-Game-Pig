import unittest
from dice import Dice, CPUDice
from helpers import Mode

class TestDice(unittest.TestCase):
    def test_roll(self):
        d = Dice()                      #Instantiate the dice class
        roll = d.roll()                 #roll the dice
        self.assertTrue(1 <= roll <=6)  #Assert that the rolled dice value is between 1 ansd 6


class TestCPUDice(unittest.TestCase):
    
    def setUp(self):
        self.cpu_dice = CPUDice(Mode.SOLO_EASY)
    
    # instantiate an object CPUDice
    def test_cpudice(self):
        self.assertIsNotNone(self.cpu_dice)
        
        # Test error raised
        with self.assertRaises(TypeError):
            self.cpu_dice = CPUDice('Mode.EASY')
        
        with self.assertRaises(ValueError):
            self.cpu_dice = CPUDice(Mode.DUEL)
        

    def test_roll(self):
        self.cpu_dice.mode = Mode.SOLO_HARD
        self.assertIsInstance(self.cpu_dice.roll(), int)
        self.assertIn(self.cpu_dice.roll(), range(1,7))
        
    
    def test__items(self):
        self.cpu_dice.mode = Mode.SOLO_EASY
        list_items = self.cpu_dice._items()
        self.assertEqual(len(list_items), 6)
        
        self.cpu_dice.mode = Mode.SOLO_MEDIUM
        list_items = self.cpu_dice._items()
        self.assertEqual(len(list_items), 11)
        
        self.cpu_dice.mode = Mode.SOLO_HARD
        list_items = self.cpu_dice._items()
        self.assertEqual(len(list_items), 18)
        
        self.cpu_dice.mode = Mode.SOLO_MERCILESS
        list_items = self.cpu_dice._items()
        self.assertEqual(len(list_items), 38)
        
        


if __name__ == '__main__':
    unittest.main()
        
