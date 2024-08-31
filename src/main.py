import os

path_1 = input("Enter the directory name: ")
def make_directory(path_1):
 """creates new directories and necessary intermeditate ones"""
try:
     os.makedirs(path_1, exist_ok=True) # type: ignore
     print("Directory path is created: {path_1}") 
except Exception as e:
     print("Error creating the directory: {e}") 
make_directory(path_1)




path_2 = input("Enter the directory name: ")
def change_directory(path_2):
   """changes the cwd to specified path_2"""
try:
      os.chdir(path_2)
      print(f"Changes the directory: {os.getcwd()}")
except FileNotFoundError:
       print(f"File does not exist : {path_2}")
except Exception as e:
       print(f"cannot change directory: {path_2}") 
change_directory(path_2)       




path_3 = input("Enter the directory name: ")
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
def present_working_directory(path_4):
   """Finding the current working directory""" 
try: 
  print(f"Current working directory is: {os.getcwd()}") 
except FileNotFoundError: 
  print(f"Directory does not exist") 
present_working_directory(path_4) 



path_5 = input("Enter the name of the file: ")
def cat(path_5):
    
    try:
        with open('path_5' , 'r') as fhand:
            for contents in fhand:
                print(contents, end='') 

    except PermissionError: 
         print(f"Permission Denied: {path_5}")

    except FileNotFoundError:
         print(f"File does not exist: {path_5}")

    except Exception as e:
         print("Error: {e}") 




    
      
   