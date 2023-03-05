import unittest
from winner import Winner

class TestWinner(unittest.TestCase):
    
    def setUp(self):
        self.winner1 = Winner('Erick', 'CPU', 104)
        self.winner2 = Winner('Robert', 'Erick', 101)
        self.winner3 = Winner('CPU', 'Robert', 102)
        self.winner4 = Winner('CPU', 'Erick', 105)
    

    def test_winner(self):
        winner = Winner('CPU', 'Steve', 100)
        self.assertIsNotNone(winner)
    
    
    def test_data(self):
        winners = [self.winner1, self.winner2, self.winner3, self.winner4]
        names_scores = [winner.data for winner in winners]
        self.assertEqual(len(names_scores), 4)
    
if __name__ == '__main__':
    unittest.main()