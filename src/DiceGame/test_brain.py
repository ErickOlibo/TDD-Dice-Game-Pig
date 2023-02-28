import unittest
from enums import Difficulty, Turn, Tactic
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
        self.mind.strategy = Tactic.RACE_PACE
        self.assertEqual(self.mind.strategy, Tactic.RACE_PACE)
        
        with self.assertRaises(TypeError):
            self.mind.strategy = Difficulty.HARD
            self.mind.strategy = 'Tactic.TWENTY'
            self.mind.strategy = 1

    
    def test_hold_20_25(self):
        self.assertEqual(self.mind.hold_20(19), Turn.ROLL)
        self.assertEqual(self.mind.hold_20(21), Turn.HOLD)
        self.assertEqual(self.mind.hold_20(-20), Turn.ROLL)
        
        # With using a context manager for evaluating Errors Raised
        with self.assertRaises(TypeError):
            self.mind.hold_20('Twenty')
            self.mind.hold_25('Twenty-Five')
            self.mind.hold_20('21')



if __name__ == '__main__':
    
    unittest.main()