import unittest
from enums import Difficulty, Turn
from brain import Brain

class TestBrain(unittest.TestCase):
    
    # runs at the start of EVERY test method execution
    def setUp(self):
        self.ai = Brain()
        # self.points = 20
        
    # instantiate a object brain
    def test_brain(self):
        self.assertIsNotNone(self.ai)
        
    
    def test_hold_20_25(self):
        self.assertEqual(self.ai.hold_20(19), Turn.ROLL)
        self.assertEqual(self.ai.hold_20(21), Turn.HOLD)
        self.assertEqual(self.ai.hold_20(-20), Turn.ROLL)
        
        # With using a context manager for evaluating Errors Raised
        with self.assertRaises(ValueError):
            self.ai.hold_20('Twenty')
            self.ai.hold_25('Twenty-Five')
            self.ai.hold_20('21')

    
    def test_hold_25(self):
        pass
    
    def test_race_pace(self):
        pass



if __name__ == '__main__':
    
    unittest.main()