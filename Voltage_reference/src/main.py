from dataclasses import dataclass
import sympy as sp

@dataclass
class VoltageReference:
    """Calculating the value of voltage reference from the given model"""

    vgo: float = 1.2          # Bandgap voltage
    n: float = 3.6            # Process constant
    vt: float = 25.8e-3       # Thermal voltage
    vbe_tr: float = 0.67       # Base-emitter voltage at room temperature
    temp: float = 330         # Operating temperature
    room_temp: float = 300    # Room temperature
    iptat: float = 15e-6      # Current through rptat_2

    def __init__(self):
        # Base emitter voltage at any temperature
        self._base_emitter_voltage = self.get_base_emitter_voltage(
            self.vgo, self.n, self.vt, self.vbe_tr, self.temp, self.room_temp)
        
        # Solving rptat_2 and using it for further calculations
        self.rptat_2_solution = self._solve_rptat_2(
            self.vgo, self.n, self.vt, self.vbe_tr, self.temp, self.room_temp, self.iptat)
        
        # vptat is the voltage across the resistance where we calculate the voltage reference
        self._vptat = self.get_vptat(self.iptat, self.rptat_2_solution)

        # net voltage across rptat_2
        self._vref = self.get_vref(self._base_emitter_voltage, self._vptat)
   
    @property    
    def base_emitter_voltage(self) -> float:
        return self._base_emitter_voltage

    @property
    def vptat(self) -> float:
        return self._vptat

    @property
    def vref(self) -> float:
        return self._vref
    
    @property
    def rptat(self):
        return self.rptat_2_solution

    @staticmethod
    def get_base_emitter_voltage(vgo: float, n: float, vt: float, vbe_tr: float, temp: float, room_temp: float) -> float:
        r = vgo + (n - 1) * vt - ((vgo + (n - 1) * vt - vbe_tr) / room_temp) * temp
        return r 
      
    @staticmethod
    def _solve_rptat_2(vgo: float, n: float, vt: float, vbe_tr: float, temp: float, room_temp: float, iptat: float) -> float:
        rptat_2 = sp.symbols('rptat_2')  # Define rptat_2 as a symbol for solving
        
        # Derivative of the equation of get_base_emitter_voltage function
        dvbe_dtemp = -((vgo + (n - 1) * vt - vbe_tr) / room_temp)
        dvptat_dtemp = ((3 * iptat) / room_temp) * rptat_2                        

        # Set up the equation based on the sum of the derivatives
        derivative_eq = sp.Eq(dvbe_dtemp + dvptat_dtemp, 0)

        # Solve for rptat_2
        rptat_2_solution = sp.solve(derivative_eq, rptat_2)

        return rptat_2_solution[0]

    @staticmethod
    def get_vptat(iptat: float, rptat_2: float) -> float:
        return 3 * iptat * rptat_2

    @staticmethod
    def get_vref(vbe: float, vptat: float) -> float:
        return vbe + vptat


if __name__ == "__main__":
    # Initialize the VoltageReference class
    stablevolt = VoltageReference()

    print(f"Base-emitter voltage: {stablevolt.base_emitter_voltage}")
    print(f"vptat: {stablevolt.vptat}")
    print(f"Stable voltage reference: {stablevolt.vref}") 
