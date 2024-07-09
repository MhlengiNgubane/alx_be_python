import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-2, 5), 3)
        
    def test_subtraction(self):
        """Test the subtract method."""
        self.assertEqual(self.calc.subtract(3, 2), 1)
        self.assertEqual(self.calc.subtract(1, 1), 0)
        self.assertEqual(self.calc.subtract(-5, 2), -3)    
        
    def test_multiplication(self):
        """Test the multiply method."""
        self.assertEqual(self.calc.multiply(3, 2), 6)
        self.assertEqual(self.calc.multiply(1, -1), -1)
        self.assertEqual(self.calc.multiply(5, 0), 0)
        
    def test_division(self):
        """Test the divide method."""
        self.assertEqual(self.calc.divide(4, 2), 2)
        self.assertEqual(self.calc.divide(1, -1), -1)
        self.assertEqual(self.calc.divide(5, 0), None)       
