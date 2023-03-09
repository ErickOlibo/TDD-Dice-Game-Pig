import unittest
from helpers import Turn, Tactic
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
        self.brain._strategy = Tactic.TWENTY_FIVE
        self.assertIsInstance(self.brain.action(45, 19), Turn)
        self.assertEqual(self.brain.action(45, 19), Turn.ROLL)

        self.assertEqual(self.brain.action(20, 27), Turn.HOLD)
        
        
        self.brain._strategy = Tactic.FOUR_TURNS
        self.assertEqual(self.brain.action(45, 31), Turn.HOLD)
        self.brain._current_turns = 0
        self.assertEqual(self.brain.action(45, 29), Turn.ROLL)
        
        self.brain._current_turns = 2
        self.assertEqual(self.brain.action(55, 15), Turn.ROLL)
        self.brain._current_turns = 2
        self.assertEqual(self.brain.action(55, 25), Turn.HOLD)
        
        with self.assertRaises(ZeroDivisionError):
            self.brain._current_turns = 4
            self.assertEqual(self.brain.action(45, 31), Turn.HOLD)


if __name__ == '__main__':
    unittest.main()