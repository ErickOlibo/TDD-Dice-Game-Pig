import unittest
import event

class TestEvent(unittest.TestCase):
    def test_Init(self):
        e = event.Event(99, "Robert")
        self.assertEqual(e._id, 99)
        self.assertEqual(e._name, "Robert")

    def test_Count(self):
        e = event.Event(99, "Robert")
        e._rolls = [1, 5, 7, 2]
        self.assertEqual(e._points, 0)
    
    def test_Rolls(self):
        e = event.Event(99, "Robert")
        e.add_roll(5)
        self.assertEqual(e._rolls[0], 5)


        


if __name__ == 'main':
    unittest.main()