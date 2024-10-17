import unittest
import sys 
import os

# Add parent directory to sys.path to find `src`
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import the RcCircuit class
from src.main import RcCircuit 

class TestRcCircuit(unittest.TestCase):
    
    def test_time_constant(self):
        rccircuit = RcCircuit()
        exp_value = rccircuit.res * rccircuit.cap
        self.assertEqual(rccircuit.time_constant, exp_value)

    def test_rise_time(self):
        rccircuit = RcCircuit()
        exp_value = rccircuit.time_constant * 0.22
        self.assertEqual(rccircuit.rise_time, exp_value)

    def test_delay_time(self):
        rccircuit = RcCircuit()
        exp_value = rccircuit.time_constant * 0.69
        self.assertEqual(rccircuit.delay_time, exp_value)

    def test_settling_time(self):
        rccircuit = RcCircuit()
        exp_value = rccircuit.time_constant * 5  
        self.assertEqual(rccircuit.settling_time, exp_value)

    def test_energy(self):
        rccircuit = RcCircuit()
        volt = rccircuit.res
        exp_value = 0.5 * rccircuit.cap * (volt ** 2)
        self.assertEqual(rccircuit.energy, exp_value)

    def test_get_settling_time(self):
        rccircuit = RcCircuit()
        if rccircuit.settling_accuracy <= 95.0:
            exp_value = 3 * rccircuit.time_constant
        elif rccircuit.settling_accuracy <= 98.2:
            exp_value = 4 * rccircuit.time_constant
        elif rccircuit.settling_accuracy == 99.3:
            exp_value = 5 * rccircuit.time_constant
        else:
            with self.assertRaises(TypeError):
                rccircuit.get_settling_time(rccircuit.res , rccircuit.cap)

        # This needs to be outside of the else block
        self.assertEqual(rccircuit.get_settling_time(rccircuit.res , rccircuit.cap), exp_value)

if __name__ == '__main__':
    unittest.main()
