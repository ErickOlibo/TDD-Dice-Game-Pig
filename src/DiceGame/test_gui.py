import unittest
from gui import GUI


class TestGUI(unittest.TestCase):
    
    def setUp(self):
        self.gui = GUI()


    def test_gui(self):
        self.assertIsNotNone(GUI())
        
        
    def test_display_hand_results(self):
        self.assertIsNone(self.gui.display_hand_results([], 20))
    
    
    def test__get_rolls_points(self):
        self.assertIn("47", "\n".join(self.gui._get_rolls_points(47)))
        self.assertTrue(len(self.gui._get_rolls_points(47)) == 5)
    
    
    def test_display_scoreboard(self):
        pass
    
    
    def test__shrink_name(self):
        s_name = self.gui._shrink_name("Christopher")
        self.assertEqual("Christopher", s_name)
        s_name = self.gui._shrink_name("Matthew-Lorenzo")
        self.assertTrue(len(s_name) == 13)
        self.assertTrue(s_name[-3:] == "...")
        
        pass
    
    


if __name__ == '__main__':
    unittest.main()