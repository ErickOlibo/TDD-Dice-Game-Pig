import unittest
import calc # import what we are testing. if in module (folder) then from module import ---
    
# free to name class but with use Camel case with TestClassNameToTest
class TestCalc(unittest.TestCase):
    
    # Naming convention 'test_' and what method we are testing
    def test_add(self):
        self.assertEqual(calc.add(10, 5), 15) # normal case
        self.assertEqual(calc.add(-1, 1), 0) # fringe case
        self.assertEqual(calc.add(-1, -1), -2) # fringe case
    
    def test_substract(self):
        self.assertEqual(calc.substract(10, 5), 5) # normal case
        self.assertEqual(calc.substract(-1, 1), -2) # fringe case
        self.assertEqual(calc.substract(-1, -1), 0) # fringe case
    
    def test_multiply(self):
        self.assertEqual(calc.multiply(10, 5), 50) # normal case
        self.assertEqual(calc.multiply(-1, 1), -1) # fringe case
        self.assertEqual(calc.multiply(-1, -1), 1) # fringe case
    
    def test_divide(self):
        self.assertEqual(calc.divide(10, 5), 2) # normal case
        self.assertEqual(calc.divide(-1, 1), -1) # fringe case
        self.assertEqual(calc.divide(-1, -1), 1) # fringe case
        self.assertEqual(calc.divide(5, 2), 2.5) # fringe case
        
        self.assertRaises(ValueError, calc.divide, 10, 0) # no failed if error raised
        
        # With using a context manager for evaluatin errors
        with self.assertRaises(ValueError):
            calc.divide(10, 0)
    
        
if __name__ == '__main__':
    
    unittest.main()