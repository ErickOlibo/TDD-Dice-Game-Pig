import unittest
from enums import Difficulty, Turn, Tactic
from player import Player
from brain import Brain

class TestBrain(unittest.TestCase):
    
    # runs at the start of EVERY test method execution
    def setUp(self):
        self.mind = Brain()


    # instantiate a object brain
    def test_brain(self):
        self.assertIsNotNone(self.mind)


    def test_level(self):
        self.assertIsInstance(self.mind.level, Difficulty)
        self.mind.level = Difficulty.HARD
        self.assertEqual(self.mind.level, Difficulty.HARD)
        
        with self.assertRaises(TypeError):
            self.mind.level = '4'
            self.mind.level = 'Difficulty.HARD'
            self.mind.level = 1


    def test_strategy(self):
        self.assertIsInstance(self.mind.strategy, Tactic)
        self.mind.strategy = Tactic.FOUR_TURNS
        self.assertEqual(self.mind.strategy, Tactic.FOUR_TURNS)
        
        with self.assertRaises(TypeError):
            self.mind.strategy = Difficulty.HARD
            self.mind.strategy = 'Tactic.TWENTY'
            self.mind.strategy = 1


    def test_action(self):
        self.mind.strategy = Tactic.TWENTY_FIVE
        
        my_action = self.mind.action()
        self.assertIsInstance(my_action, Turn)
        self.assertEqual(my_action, Turn.ROLL)

        self.mind._cpu.turn_points = 27
        my_action = self.mind.action()
        self.assertEqual(my_action, Turn.HOLD)
        
        # context manager
        with self.assertRaises(TypeError):
            self.mind.action('Twenty')
            self.mind.action('Twenty-Five')
            self.mind.action('21')
    
    
    def test_division(self):
        ceil = self.mind.ceiling_division(5, 2)
        floor = self.mind.floor_division(5, 2)
        self.assertEqual(ceil, 3)
        self.assertEqual(floor, 2)



if __name__ == '__main__':
    
    unittest.main()