import unittest
from highscore import HighScore

class TestHighscore(unittest.TestCase):
    # CLASS TO DELETE
    def setUp(self):
        self.hs = HighScore("Robert", 0, 0)
    
    
    def test_init(self):
        self.assertEqual(self.hs._name, "Robert")
        self.assertEqual(self.hs._streak, 0)
        self.assertEqual(self.hs._overallpoints, 0)


    def test_addStreak(self):
        self.hs.add_streak(1)
        self.assertEqual(self.hs._streak, 1)


    def test_addOverallPoints(self):
        self.hs.add_overallpoints(105)
        self.assertEqual(self.hs._overallpoints, 105)





if __name__ == '__main__':
    unittest.main()