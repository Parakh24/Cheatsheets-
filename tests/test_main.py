import os
import unittest 
import sys

# The subprocess module in Python is used for running new applications or programs by 
# creating new processes. 
# It provides a powerful way to execute external commands (like shell commands or other programs)
#  from within a Python script.
import subprocess

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

class BashClone(unittest.TestCase):


    def run_script(self , *args):
        result = subprocess.run (['python3' , 'main.py'] + list(args) 
        
        capture_output=True, text=True
        )
        
        return result 
    

    
