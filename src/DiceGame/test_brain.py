import unittest
from helpers import Turn, Tactic
from player import Player
from brain import Brain

class TestBrain(unittest.TestCase):
    
    # runs at the start of EVERY test method execution
    def setUp(self):
        self.brain = Brain()


    # instantiate a object brain
    def test_brain(self):
        self.assertIsNotNone(Brain())


    def test_random_strategy(self):
        strategy = self.brain._strategy
        self.assertIsInstance(strategy, Tactic)
        self.assertIn(strategy, list(Tactic))


    def test_action(self):
        self.brain.strategy = Tactic.TWENTY_FIVE
        
        my_action = self.brain.action(45, 19)
        self.assertIsInstance(my_action, Turn)
        self.assertEqual(my_action, Turn.ROLL)

        my_action = self.brain.action(20, 27)
        self.assertEqual(my_action, Turn.HOLD)
        
        # context manager
        with self.assertRaises(TypeError):
            self.brain.action('Twenty')
            self.brain.action('Twenty-Five')
            self.brain.action('21')




if __name__ == '__main__':
    unittest.main()