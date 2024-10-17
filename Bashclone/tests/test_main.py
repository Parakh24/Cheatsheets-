import unittest         
import os                  
import stat     
import shutil       
import sys          
import pytest              
  
                 
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))   
# Import the functions from your script

from src.main import mkdir, cd, create_file_cwd, ls_al, pwd, grep

class TestScriptFunctions(unittest.TestCase):

    def setUp(self):
        """Set up test environment: create a test directory and file."""
        self.test_dir = "test_dir"
        self.test_file = "test_file.txt"
        self.test_path = os.path.join( self.test_dir, self.test_file)
        assert self.test_path == "test_dir/test_file.txt"
        os.makedirs(self.test_dir, exist_ok=True)

    def tearDown(self):
        """Clean up test environment: remove test directory and file."""
        if os.path.exists(self.test_dir):
            shutil.rmtree(self.test_dir)  

    def test_mkdir(self):
        """Test directory creation."""
        mkdir(self.test_dir)
        self.assertTrue(os.path.exists(self.test_dir))
        shutil.rmtree(self.test_dir)

    def test_cd(self):
        """Test changing directory."""
        mkdir(self.test_dir)
        current_dir = os.getcwd()
        cd(self.test_dir)
        self.assertEqual(os.getcwd(), os.path.join(current_dir, self.test_dir))
        os.chdir(current_dir)  # Change back to the original directory


    def test_create_file(self):
        """Test file creation in a directory."""
        mkdir(self.test_dir)
        self.current_dir = os.getcwd()              
        # cd(self.test_dir)
        create_file_cwd(self.test_path)
        # self.assertEqual(os.getcwd(), os.path.join(self.current_dir, self.test_dir))
        # print(f"{os.path.abspath(self.test_file)=}")
        self.assertTrue(os.path.isfile(self.test_path))  
        # cd('..')
        shutil.rmtree(self.test_dir)


    def test_ls_al(self):
        """Test listing contents of the directory."""
        create_file_cwd(self.test_file)
        ls_al()
        os.remove(self.test_file)
        # This is a simple check, you could capture the output with a context manager

    def test_pwd(self):
        """Test printing the current working directory."""
        current_dir = os.getcwd()
        pwd()
        # Again, output capturing could be used to assert

    def test_grep(self):
        """Test grep-like function."""
        create_file_cwd(self.test_file)
        # Write to the test file
        with open(self.test_path, 'w') as f:
            f.write("Hello! Hope you liked the Content\n")
        grep(self.test_path)  # This should print the matching line
        os.remove(self.test_file)

    def test_mkdir_permission_error(self):
        """Test mkdir with permission error by using a restricted directory."""
        restricted_dir = "/root/restricted_dir"
        mkdir(restricted_dir)  # Expect permission denied or handled gracefully

    def test_grep_file_not_found(self):
        """Test grep with a non-existent file."""
        grep("non_existent_file.txt")  # Expect file not found handling

if __name__ == '__main__':
    unittest.main()



                                   
