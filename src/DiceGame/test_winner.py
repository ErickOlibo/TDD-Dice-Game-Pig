import unittest
from winner import Winner
class TestWinner(unittest.TestCase):
    
    def setUp(self):
        self.winner1 = Winner('Erick', 104)
        self.winner2 = Winner('Robert', 101)
        self.winner3 = Winner('CPU', 102)
        self.winner4 = Winner('CPU', 105)
    

    def test_winner(self):
        winner = Winner('Steve', 100)
        self.assertIsNotNone(winner)
        name = winner.name
        self.assertEqual(name, 'Steve')
        winner.name = 'Erick'
        self.assertNotEqual('Steve', winner.name)
    
    
    def test_data(self):
        winners = [self.winner1, self.winner2, self.winner3, self.winner4]
        names_scores = [winner.data for winner in winners]
        self.assertEqual(len(names_scores), 4)
    
    def test_to_string(self):
        win = Winner('Erick', 99)
        self.assertEqual(win.to_string[13:], 'Erick - 99')


# if __name__ == '__main__':
#     unittest.main()