from dataclasses import dataclass

@dataclass
class RcCircuit:
    """Rc Circuit
    """                             
    res: float = 2.0
    cap: float = 1e-15
    settling_accuracy: float = 99.3
    
    def __init__(self):
        self._time_constant = self.get_time_constant(self.res , self.cap)
        self._delay_time =  0.69 * self.time_constant
        self._rise_time  =  0.22 * self.time_constant
        self._fall_time  =  0.22 * self.time_constant
        # settling time = 3Tau for 95.0% accuracy
        # settling time = 4Tau for 98.2% accuracy
        # settling time = 5Tau for 99.3% accuracy
        self._settling_time = self.get_settling_time(self.res , self.cap , accuracy = self.settling_accuracy)
        self._energy = self._get_energy(self.res , self.cap)
        
    @property 
    def time_constant(self) -> float:
        """Time Constant
        Returns: product of resistance and capacitance
        """   
        
        return self._time_constant 
        
    @property
    def rise_time(self) -> float:
        """returns the value multiplied by time_constant
        """

        return self._rise_time
    
    @property
    def delay_time(self) -> float:
        """returns the delay value
        """
        return self._delay_time     
        
    @property
    def settling_time(self) -> float:
        """returns the settling value
        """

        return self._settling_time  

    @property
    def energy(self) -> float:
        """returns the energy value
        """ 

        return self._energy                   
    
    @staticmethod
    def get_time_constant(res: float , cap: float) -> float:
        
        return res*cap
    

    @staticmethod
    def get_settling_time(res: float , cap: float , accuracy: float = 99.3):
      
      """Get energy

        tsettling = 5 * tau for 99.3% accuracy
        tsettling = 4 * tau for 98.2% accuracy
        tsettling = 3 * tau for 95.0% accuracy

        Args:
            res (float): Resistance
            cap (float): Capacitance
            accuracy (float, optional): Accuracy. Defaults to 99.3.

        Returns:
            float: Energy

        
        """ 
        
      if accuracy<=95.0:
          return 3*RcCircuit.get_time_constant(res,cap)
      
      elif accuracy <=98.2:
          return 4*RcCircuit.get_time_constant(res,cap)
      
      else:
          return 5*RcCircuit.get_time_constant(res,cap)  
      
        
    @staticmethod
    def _get_energy(res: float , cap: float):
        volt = res
        return 0.5* cap * (volt**2)
      
      
if __name__ == "__main__":
    rcfilt = RcCircuit()
    print(f"Time Constant: {rcfilt.time_constant}")
    print(f"rise time: {rcfilt.rise_time}")
    print(f"delay time: {rcfilt.delay_time}")
    print(f"settling time: {rcfilt.settling_time}")
    print(f"energy: {rcfilt.energy}")




    
    