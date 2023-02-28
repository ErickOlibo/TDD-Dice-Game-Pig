import unittest
from brain import Brain

class TestBrain(unittest.TestCase):
    
    # instantiate a object brain
    def test_brain(self):
        ai = Brain()
        self.assertIsNotNone(ai)


if __name__ == '__main__':
    
    unittest.main()