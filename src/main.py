import os
import stat 


path_1 = input("Enter the directory name: ")

# Permission to read , write and execute
os.chmod(path_1, stat.S_IRUSR | stat.S_IWUSR | stat.S_IXUSR | stat.S_IROTH)

def make_directory(path_1):
 """creates new directories and necessary intermeditate ones"""
try:
     os.makedirs(path_1, exist_ok=True) # type: ignore
     print("Directory path is created: {path_1}") 

except PermissionError:
       print("Permission is denied")

except Exception as e:
     print("Error creating the directory: {e}") 
make_directory(path_1)          




path_2 = input("Enter the directory name: ")

# Permission to read , write and execute
os.chmod(path_2, stat.S_IRUSR | stat.S_IWUSR | stat.S_IXUSR | stat.S_IROTH)

def change_directory(path_2):
   """changes the cwd to specified path_2"""
try:
      os.chdir(path_2)
      print(f"Changes the directory: {os.getcwd()}")
except FileNotFoundError:
       print(f"File does not exist : {path_2}")

except PermissionError:
       print("Permission is denied")

except Exception as e:
       print(f"cannot change directory: {path_2}") 
change_directory(path_2)       




path_3 = input("Enter the directory name: ")

# Permission to read , write and execute
os.chmod(path_3, stat.S_IRUSR | stat.S_IWUSR | stat.S_IXUSR | stat.S_IROTH)

def list_all_contents(path_3):
   """lists all the directories of the current working directory"""
try:
      with os.scandir(path_3) as entries:
        for entry in entries:
         if entry.is_file():   
            print(f"File: {entry.path}, Size: {os.path.getsize(entry.path)}")     
         elif entry.is_dir():
            print(f"Directory: {entry.name}, Size: {os.path.getsize(entry.path)}") 
except PermissionError:
         print("Permission is denied") 
list_all_contents(path_3)         




path_4 = input("Enter the present_working_directory: ") 

# Permissions to read , write and execute
os.chmod(path_4, stat.S_IRUSR | stat.S_IWUSR | stat.S_IXUSR | stat.S_IROTH)

def present_working_directory(path_4):
   """Finding the current working directory""" 
try: 
  print(f"Current working directory is: {os.getcwd()}") 
except FileNotFoundError: 
  print(f"Directory does not exist") 
present_working_directory(path_4) 



path_5 = input("Enter the name of the file: ")

#Permission to read, write and execute
os.chmod(path_5, stat.S_IRUSR | stat.S_IWUSR | stat.S_IXUSR | stat.S_IROTH)
    
def grep(path_5):
   """Extracting the contents of the file""" 
   try:
      with open('path_5' , 'r') as fhand:
         for contents in fhand:
            if contents.startswith('My'):
                if contents.endswith('Parakh'):
                  print(contents, end='') 
            else:
                print("No such contents")      

   except PermissionError: 
         print(f"Permission Denied: {path_5}")

   except FileNotFoundError:
         print(f"File does not exist: {path_5}")
 
   except Exception as e:
         print("Error: {e}") 
grep(path_5) 

    
      
   