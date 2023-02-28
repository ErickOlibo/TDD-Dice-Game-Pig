import unittest
from enums import Difficulty
from brain import Brain

class TestBrain(unittest.TestCase):
    
    # runs at the start of EVERY test method execution
    def setUp(self):
        self.ai = Brain()
        self.points = 20
        
    # instantiate a object brain
    def test_brain(self):
        self.assertIsNotNone(self.ai)
        
    
    def test_hold_20(self):
        
        self.assertTrue(self.ai.hold_20(self.points))
        pass
    
    def test_hold_25(self):
        pass
    
    def test_race_pace(self):
        pass



if __name__ == '__main__':
    
    unittest.main()