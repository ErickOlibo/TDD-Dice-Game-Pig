import unittest
from gui import GUI


class TestGUI(unittest.TestCase):
    
    def setUp(self):
        self.erick = 'Erick'
        self.robert = 'Robert'
        self.gui = GUI(self.robert, self.erick)


    def test_gui(self):
        self.assertIsNotNone(GUI(self.erick, self.robert))
        
        
    def test_player_one(self):
        self.gui.player_one = 'Ciara'
        self.assertEqual(self.gui.player_one, 'Ciara')
        
    def test_player_two(self):
        self.gui.player_two = 'Noel'
        self.assertEqual(self.gui.player_two, 'Noel')
    
    def test_display_hand_results(self):
        self.assertIsNone(self.gui.display_hand_results([], 20))
    
    
    def test__get_rolls_points(self):
        self.assertIn("47", "\n".join(self.gui._get_rolls_points(47)))
        self.assertTrue(len(self.gui._get_rolls_points(47)) == 5)
    
    
    def test_display_scoreboard(self):
        self.assertIsNone(self.gui.display_scoreboard(10,20, self.robert))
        
        with self.assertRaises(ValueError):
            self.gui.display_scoreboard(10,20, 'Ciara')
        
        with self.assertRaises(Exception):
            self.gui2 = GUI()
            self.gui2.display_scoreboard(20,30, 'Erick')
    
    
    def test__shrink_name(self):
        s_name = self.gui._shrink_name("Christopher")
        self.assertEqual("Christopher", s_name)
        s_name = self.gui._shrink_name("Matthew-Lorenzo")
        self.assertTrue(len(s_name) == 13)
        self.assertTrue(s_name[-3:] == "...")
        
        pass
    
    


if __name__ == '__main__':
    unittest.main()