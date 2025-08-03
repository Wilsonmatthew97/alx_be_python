import unittest 
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = SimpleCalculator()
    
    def test_addition(self):
        self.assertEqual(self.calc.add(5,8), 13)
        self.assertEqual(self.calc.add(-5,8), 3)
        self.assertEqual(self.calc.add(6,4), 10)
        self.assertEqual(self.calc.add(-3,-7), -10)
    
    def test_subtract(self):
        self.assertEqual(self.calc.subtract(8,3), 5)
        self.assertEqual(self.calc.subtract(-3,-7), 4)
        self.assertEqual(self.calc.subtract(2,8), -6)
        self.assertEqual(self.calc.subtract(5,-5), 10)
    
    def test_multiply(self):
        self.assertEqual(self.calc.multiply(5,4), 20)
        self.assertEqual(self.calc.multiply(0,2), 0)
        self.assertEqual(self.calc.multiply(-9,-3), 27)
        self.assertEqual(self.calc.multiply(7,-7), -49)
    
    def test_divide(self):
        self.assertEqual(self.calc.divide(-14,7), -2)
        self.assertAlmostEqual(self.calc.divide(7,3), 2.3333, places=4)
        self.assertEqual(self.calc.divide(9,-3), -3)
        self.assertEqual(self.calc.divide(8,0), None)
