import unittest
from event import Event

class TestEvent(unittest.TestCase):
    
    def setUp(self):
        self.event = Event('Robert')
        
    def test_Init(self):
        e = Event("Robert")
        self.assertEqual(e.name, "Robert")

    def test_add_roll(self):
        self.event.add_roll(5)
        self.event.add_roll(2)
        self.event.add_roll(6)
        self.event.add_roll(1)
        self.assertListEqual(self.event._rolls, [5,2,6,1])
    
    def test__count_points(self):
        self.event.add_roll(5)
        self.event.add_roll(6)
        self.event.add_roll(4)
        self.assertEqual(self.event.points, 15)


if __name__ == '__main__':
    unittest.main()