import os
import stat
                                                                                                        
# Directory creation function
def mkdir(path_1):
    """Creates new directories and necessary intermediate ones"""
    try:
        if not os.path.exists(path_1):
            os.makedirs(path_1, exist_ok=True)
            print(f"Directory path is created: {path_1}")
        else:
            print(f"The directory already exists: {path_1}")
    
        # Permission to read, write, and execute
        os.chmod(path_1, stat.S_IRUSR | stat.S_IWUSR | stat.S_IXUSR | stat.S_IROTH)      
        print(f"Permissions set for {path_1}")
    except PermissionError:
        print("Permission is denied")
    except Exception as e:
        print(f"Error creating the directory: {e}")



# Change directory function
def cd(path_2): 
    """Changes the cwd to specified path_2"""
    try:
        if os.path.exists(path_2):
            print(f"Directory already exists: {path_2}")
            # Permission to read, write, and execute
            os.chmod(path_2, stat.S_IRUSR | stat.S_IWUSR | stat.S_IXUSR | stat.S_IROTH)
            print(f"Permission set for: {path_2}")

        os.chdir(path_2)
        print(f"Changed the directory: {os.getcwd()}")
    except FileNotFoundError:
        print(f"Directory does not exist: {path_2}")
    except PermissionError:
        print("Permission is denied")
    except Exception as e:
        print(f"Cannot change directory: {e}")


                                                     

# File creation function
def create_file_cwd(file_name):
    """Creates a file in the specified directory"""
     
    cwd = os.getcwd()
    print(f"Current working directory: {cwd}")
    file_path = os.path.join(cwd , file_name)              


    # Create the file in the specified directory
    try:
        with open(file_path, 'w') as file:  # Use file_path to create the file
            file.write("Hello! Hope you liked the Content")  # Writing some content to the file
            print(f"File created: {file_path}")
    except PermissionError:
        print("Permission is denied. You may need elevated privileges to create the file.")
    except Exception as e:
        print(f"Error creating the file: {e}")




# List contents of directory function
def ls_al():
    """Lists all the directories and files in the specified directory"""
    try:
        with os.scandir(os.getcwd()) as entries:
            for entry in entries:
                if entry.is_file():
                    print(f"File: {entry.path}, Size: {os.path.getsize(entry.path)}")
                elif entry.is_dir():
                    print(f"Directory: {entry.name}, Size: {os.path.getsize(entry.path)}")
    except PermissionError:
        print("Permission is denied")
    except Exception as e:
        print(f"Exception: {e}")
      
  




# Print current working directory function
def pwd():
    """Finding the current working directory"""
    try:
        print(f"Current working directory is: {os.getcwd()}")
    except Exception as e:
        print(f"Error: {e}")



# Grep-like function to search in files
def grep(path_6):
    """Extracting the contents of the file"""
    try:
        os.chmod(path_6, stat.S_IRUSR | stat.S_IWUSR | stat.S_IXUSR | stat.S_IROTH)
        print(f"Permissions are set for the file")
        with open(path_6, 'r') as fhand:
            found = False
            for contents in fhand:
                # Checking both conditions in a single if statement
                if contents.startswith('Hello') and contents.strip().endswith('Content'):
                    print(contents, end='')
                    found = True
            if not found:
                print("No matching contents found.")
    except PermissionError:
        print(f"Permission Denied: {path_6}")
    except FileNotFoundError:
        print(f"File does not exist: {path_6}")
    except Exception as e:
        print(f"Error: {e}")



def main():
# Call the functions in the correct order
 path_1 = input('Enter the directory name to create: ')
 mkdir(path_1)

 path_2 = input("Enter the directory name to change the current working directory: ")
 cd(path_2)


 file_name = input("Enter the name of the file: ")
 create_file_cwd(file_name)

 path_4 = input("Enter the directory name to list contents: ")
 ls_al()

 pwd()  # Print the current working directory

 path_6 = input("Enter the name of the file for grep-like operation: ")
 grep(path_6) 


if __name__ == "__main__":
    main()
