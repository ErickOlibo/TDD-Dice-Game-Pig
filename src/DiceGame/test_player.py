import unittest
from player import Player
from helpers import Turn, Mode
from brain import Brain
from dice import Dice


class TestPlayer(unittest.TestCase):
    
    def setUp(self):
        self.jen = Player('Jennifer')
        pass
    
    def test_player(self):
        erick = Player('Erick')
        self.assertIsNotNone(erick)
        cpu = Player('CPU', Brain(), Dice(Mode.SOLO_MERCILESS))
        self.assertIsNotNone(cpu)
        self.assertEqual(cpu.score, 0)
        

    
    
    def test_name(self):
        previous = self.jen.name
        self.jen.name = 'Oliver'
        self.assertNotEqual(self.jen.name, previous)
    
    
    def test_brain(self):
        with self.assertRaises(TypeError):
            self.jen.brain = 'Brain'
        
        self.jen.brain = Brain()
        self.assertIsInstance(self.jen.brain, Brain)
    
    
    def test_score(self):
        self.assertEqual(self.jen.score, 0)        
    
    
    def test_playing_choice(self):
        self.assertIsNone(self.jen.playing_choice(45, 5))
        cpu = Player('CPU', Brain())
        self.assertIn(cpu.playing_choice(35,10), Turn)

    
    def test_add_points_to_score(self):
        self.jen.add_points_to_score(23)
        self.assertEqual(self.jen.score, 23)
        self.jen.add_points_to_score(17)
        self.assertNotEqual(self.jen.score, 23)
        pass
    
    
    def test_roll_dice(self):
        roll = self.jen.roll_dice()
        self.assertIsInstance(roll, int)
        self.assertIn(roll, range(1, 7))
        
        cpu = Player('CPU', Brain())
    

if __name__ == '__main__':
    unittest.main()

    