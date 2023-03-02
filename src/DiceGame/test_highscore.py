import unittest
import highscore

class TestHighscore(unittest.TestCase):
    
    def test_init(self):
        #Init 
        hs = highscore.HighScore("Robert", 0, 0)

        #Prepare
        hs_name = hs._name
        hs_streak = hs._streak
        hs_ovrpoints = hs._overallpoints

        #Assert
        self.assertEqual(hs_name, "Robert")
        self.assertEqual(hs_streak, 0)
        self.assertEqual(hs_ovrpoints, 0)

    def test_addStreak(self):
         #Init
        hs = highscore.HighScore("Robert", 0, 0)

        #prepare
        hs.add_streak(1)
        hs_streak = hs._streak
        
        #Assert
        self.assertEqual(hs_streak, 1)

    def test_addOverallPoints(self):
        #Init
        hs = highscore.HighScore("Robert", 0, 0)

        #prepare
        hs.add_overallpoints(105)
        hs_overallpoints = hs._overallpoints

        #Assert
        self.assertEqual(hs_overallpoints, 105)





if __name__ == '__main__':
    unittest.main()