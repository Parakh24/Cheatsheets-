import os
import sys
import unittest
import pytest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.main import factorial 


#tests for factorial
class TestFactorial(unittest.TestCase):
    
    def test_factorial(self):
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(4), 24)
        self.assertEqual(factorial(2), 2) 
    
    
def test_factorial_integer():
    assert factorial(5) == 120
    assert factorial(4) == 24
    assert factorial(3) == 6

  
def test_factorial_float_fail():
    #test for float numbers
    with pytest.raises(TypeError):
        factorial(5.5)
    with pytest.raises(TypeError):
        factorial(4.4)
    with pytest.raises(TypeError):
        factorial(2.2)     

def test_factorial_negative_fail():   
    #test for negative number
    with pytest.raises(TypeError):
        factorial(-5)
    with pytest.raises(TypeError):
        factorial(-4)
    with pytest.raises(TypeError):
        factorial(-3)  


def test_factorial_large():
    #test for large numbers
    assert factorial(10) == 3628800

def test_factorial_zero():
    #test for 0 factorial
    assert factorial(0) == 1

def test_factorial_blank():    
    #test factorial for none 
   with pytest.raises(TypeError):
       factorial("") 


def test_factorial_str_fail(): 
    
    with pytest.raises(TypeError):
        factorial("5")
    with pytest.raises(TypeError):
        factorial("4")


if __name__ == '__main__':
     unittest.main() 