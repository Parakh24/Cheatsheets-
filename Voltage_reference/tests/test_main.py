import sys
import os 
import unittest
import sympy as sp

# Add parent directory to sys.path to find `src`
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import the RcCircuit class
from src.main import VoltageReference 

class TestVoltageReference(unittest.TestCase):
     

     def test_base_emitter_voltage(self):
          
        volt = VoltageReference()
        total_value =  volt.vgo + (volt.n-1)*volt.vt - ((volt.vgo + (volt.n - 1) * volt.vt - volt.vbe_tr)/volt.room_temp)* volt.temp 
        self.assertEqual(volt.base_emitter_voltage , total_value)  
        
                                        
     def test_vptat(self):
          volt = VoltageReference()
          total_value = 3 * volt.iptat * volt.rptat
          self.assertAlmostEqual(total_value, volt.vptat)


     def test_vref(self):
          volt = VoltageReference()
          total_value = volt.base_emitter_voltage + volt.vptat 
          self.assertAlmostEqual(volt.vref, total_value)   

     

     def test_solve_rptat_2_correct_solution(self):
        # Known input values
        vgo = 1.2          # Bandgap voltage
        n = 3.6            # Process constant
        vt = 25.8e-3       # Thermal voltage
        vbe_tr = 6.7       # Base-emitter voltage at room temperature
        temp = 330         # Operating temperature
        room_temp = 300    # Room temperature
        iptat = 15e-6      # Current through rptat_2

        # Call the function
        rptat_2_solution = VoltageReference._solve_rptat_2(vgo, n, vt, vbe_tr, temp, room_temp, iptat)

        # Manually create the derivative equation for verification
        rptat_2 = sp.symbols('rptat_2')
        dvbe_dtemp = -((vgo + (n - 1) * vt - vbe_tr) / room_temp)
        dvptat_dtemp = ((3 * iptat) / room_temp) * rptat_2
        derivative_eq = sp.Eq(dvbe_dtemp + dvptat_dtemp, 0)

        # Verify that the equation is correctly differentiated
        # and that the solution for rptat_2 satisfies the equation
        expected_solution = sp.solve(derivative_eq, rptat_2)[0]
        self.assertAlmostEqual(rptat_2_solution, expected_solution, places=6)   



     def test_solve_rptat_2_incorrect_solution(self):
        # Known input values
        vgo = 1.2          # Bandgap voltage
        n = 3.6            # Process constant
        vt = 25.8e-3       # Thermal voltage
        vbe_tr = 6.7       # Base-emitter voltage at room temperature
        temp = 330         # Operating temperature
        room_temp = 300    # Room temperature
        iptat = 15e-6  

        # Modify an input value (iptat) to an incorrect value
        incorrect_iptat = 5e-6  # Set an incorrect value intentionally

        # Call the function
        rptat_2_solution = VoltageReference._solve_rptat_2(vgo, n, vt, vbe_tr, temp, room_temp, iptat)

        # Manually create the derivative equation for verification
        rptat_2 = sp.symbols('rptat_2')
        dvbe_dtemp = -((vgo + (n - 1) * vt - vbe_tr) / room_temp)
        dvptat_dtemp = ((3 * incorrect_iptat) / room_temp) * rptat_2
        derivative_eq = sp.Eq(dvbe_dtemp + dvptat_dtemp, 0)

        # The solution should not match when incorrect input is provided
        expected_solution = sp.solve(derivative_eq, rptat_2)[0]
        self.assertNotEqual(rptat_2_solution, expected_solution)  

                                        
if __name__ == '__main__':
    unittest.main()                                              