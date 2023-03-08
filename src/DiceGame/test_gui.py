import unittest
from gui import GUI


class TestGUI(unittest.TestCase):
    
    def setUp(self):
        self.gui = GUI()


    def test_gui(self):
        pass
        
        
    def test_player_one(self):
        pass
        
    def test_player_two(self):
        pass
    
    def test_display_hand_results(self):
        pass
    
    
    def test__get_rolls_points(self):
        pass
    
    
    def test_display_scoreboard(self):
        self.assertIsNone(self.gui.display_scoreboard('E', 10, 'R', 12, 'E'))
    
    
    
    def test__shrink_name(self):
        s_name = self.gui._shrink_name("Christopher", 13)
        self.assertEqual("Christopher", s_name)
        s_name = self.gui._shrink_name("Matthew-Lorenzo", 13)
        self.assertTrue(len(s_name) == 13)
        self.assertTrue(s_name[-3:] == "...")
        
        pass
    
    


if __name__ == '__main__':
    unittest.main()