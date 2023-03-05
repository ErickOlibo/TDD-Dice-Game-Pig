import unittest
from cpu import CPU_Player
from helpers import Turn, Tactic

# CLASS TO DELETE
class TestCPU_Player(unittest.TestCase):
    
    def setUp(self):
        self.cpu = CPU_Player()

    
    def test_CPU_Player(self):
        
        self.assertIsNotNone(self.cpu)
        self.assertEqual(self.cpu._name, 'CPU')
        self.assertIsInstance(self.cpu._brain._strategy, Tactic)
        self.assertIn(self.cpu._brain._strategy, list(Tactic))
        pass
    
    
    def test_action_choice(self):
        action = self.cpu.action_choice(36, 6)
        self.assertIsInstance(action, Turn)
    
    def test_add_to_score_points(self):
        self.cpu.add_to_score_points(5)
        self.assertEqual(self.cpu._score, 5)
        self.cpu.add_to_score_points(2)
        self.assertEqual(self.cpu._score, 7)
        
    def test_add_to_turn_points(self):
        self.cpu.add_to_turn_points(5)
        self.assertEqual(self.cpu._turn_points, 5)
        self.cpu.add_to_turn_points(2)
        self.assertEqual(self.cpu._turn_points, 7)



if __name__ == '__main__':
    unittest.main()