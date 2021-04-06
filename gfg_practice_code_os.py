"""
https://www.geeksforgeeks.org/os-module-python-examples/
## Getting the Current working directory

# Python program to explain os.getcwd() method
		
# importing os module
import os
	
# Get the current working
# directory (CWD)
cwd = os.getcwd()
	
# Print the current working
# directory (CWD)
print("Current working directory:\n", cwd)

# Python program to change the
# current working directory
"""


"""
## Changing the Current working directory

import os
	
# Function to Get the current
# working directory
def current_path():
	print("Current working directory")
	print(os.getcwd())
	print()


# Driver's code
# Printing CWD before
current_path()
	
# Changing the CWD
os.chdir('..') # os.chdir('../') ADDING SLASH IS OPTIONAL
# SAFER WITHOUT "/"
	
# Printing CWD after
current_path()
"""


# Creating a Directory

# Python program to explain os.mkdir() method

# importing os module
'''
Apparently, Python can use the os module a little bit without it being imported.
'''

# Directory
import sys
import pytest
import os
directory = "the_new_directory"
# Parent Directory path
cwd = os.getcwd()  # "current_working_directory" # or desired parent directory
print("You are in the directory of:\n '% s' " % cwd)
# os.chdir('..') # This took me from "treemaker_folder".
print()

parent_dir = os.getcwd()
print("The current working directory also serves as the parent directory (..)\n See? '% s' " % parent_dir)
print()

# Path
# A string concatenation with address/path
path = os.path.join(parent_dir, directory)
# prints the new directory called "the_new_directory"
print(
    f'Now we are going to join the parent directory path\n and the name of our directory we saved into our "path" . \n See? {path} ')
print()

# Now create the directory:
# "the_new_directory" in
# "C:\Users\default.DESKTOP-P3E3RAC\
# Documents\School\BYU-I\Winter 2021\
# 6. CSE 111 Programming with Functions\treemaker_folder"
if os.path.exists(path):
    print("Working path directory exists.\n")
    pass
elif not os.path.exists(path):
    print("Working path directory does not exist.\n")
    os.mkdir(path)
    print("Now it does exist")
    print("We just created '{}' at: '{}' ".format(directory, path))
    print()
# Another way to format strings. Older?
# This has issues. So it's out.
# 		# print("We just created '% s' at: '% s' " % directory, path)
# Python 2, perhaps?
'''
import os 
 
main_dir = "C:/JournalDev"
 
os.mkdir(main_dir,mode = 0o666) 
print("Directory '% s' is built!" % main_dir) 

https://docs.python.org/3.4/library/string.html
'''

# Directory
directory = "the_mode_0o666_directory"

# Parent Directory path
parent_dir = os.getcwd()
print(f"Let's do it again. \n See? {path} ")
print()

# mode
mode = 0o666  # I have no idea what this does.
# Does this even matter?
# Is this ignored on Windows?
'''
# Setting mode = 0o666, allows read and write file operations within the created directory.

# https://docs.python.org/3/library/os.html#os.mkdir
'''

# Path
path = os.path.join(parent_dir, directory)

# Now create the directory:
# "the_mode_0o666_directory" in
# "C:\Users\default.DESKTOP-P3E3RAC\
# Documents\School\BYU-I\Winter 2021\
# 6. CSE 111 Programming with Functions\treemaker_folder"
# # with mode 0o666

# You will use this:
# 				os.mkdir(path, mode)
if os.path.exists(path):
    print("Working path directory exists.\n")
    pass
elif not os.path.exists(path):
    print("Working path directory does not exist.\n")
    os.mkdir(path, mode)
    print("Now it does exist")
    print()
    # print("Directory '% s' created" % directory)
    print("We just created '{}' at: '{}' ".format(directory, path))

'''
https://www.askpython.com/python/examples/create-a-directory-in-python
#This was another good way to make a directory
'''
# Output:

# Directory "the_new_directory" created
# Directory "the_mode_0o666_directory" created


'''
## Using os.makedirs()

# Python program to explain os.makedirs() method 
      
# importing os module 
import os 
      
# Leaf directory 
directory = "Nikhil"
      
# Parent Directories 
parent_dir = "D:/Pycharm projects/GeeksForGeeks/Authors"
      
# Path 
path = os.path.join(parent_dir, directory) 
      
# Create the directory 
# 'Nikhil' 
os.makedirs(path) 
print("Directory '% s' created" % directory) 
      
# Directory 'GeeksForGeeks' and 'Authors' will 
# be created too 
# if it does not exists 
      
      
      
# Leaf directory 
directory = "c"
      
# Parent Directories 
parent_dir = "D:/Pycharm projects/GeeksforGeeks/a/b"
      
# mode 
mode = 0o666
      
path = os.path.join(parent_dir, directory) 
      
# Create the directory 'c' 
      
os.makedirs(path, mode) 
print("Directory '% s' created" % directory) 
      
      
# 'GeeksForGeeks', 'a', and 'b' 
# will also be created if 
# it does not exists 
      
# If any of the intermediate level 
# directory is missing 
# os.makedirs() method will 
# create them 
      
# os.makedirs() method can be 
# used to create a directory tree 

# Output:

# Directory 'Nikhil' created
# Directory 'c' created
'''


'''
## Listing out Files and Directories with Python

# Python program to explain os.listdir() method 
      
# importing os module 
import os 
  
# Get the list of all files and directories 
# in the root directory 
path = "/"
dir_list = os.listdir(path) 
  
print("Files and directories in '", path, "' :") 
  
# print the list 
print(dir_list) 

# Output:

# Files and directories in ' / ' :
# ['sys', 'run', 'tmp', 'boot', 'mnt', 'dev', 'proc', 'var', 'bin', 'lib64', 'usr', 
# 'lib', 'srv', 'home', 'etc', 'opt', 'sbin', 'media']
'''


'''
## Deleting Directory or Files using Python
## See: python-os.remove-input.png

# Python program to explain os.remove() method 
      
# importing os module 
import os 
      
# File name 
file = 'file1.txt'
      
# File location 
location = "D:/Pycharm projects/GeeksforGeeks/Authors/Nikhil/"
      
# Path 
path = os.path.join(location, file) 
      
# Remove the file 
# 'file.txt' 
os.remove(path) 
e)

# Output: See: python-os.remove-output.png
'''


# Using os.rmdir()
