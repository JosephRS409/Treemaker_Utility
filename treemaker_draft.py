import pytest, os, sys

# This is a program that makes a file tree with files in it.

# print(os.path.abspath(os.getcwd())) # This shows path of user.
print(os.path.dirname(os.path.abspath(__file__)))
working_path = os.path.dirname(os.path.abspath(__file__)) # This show path of current file: TREEMAKER.PY
print()

# Make user friendly.
# Ask where they want to go.
# cd using relative OR absolute path option
# USER WILL NOT DELETE FOLDERS VIA THIS PROGRAM (obvious reasons, i.e. death)
# Let's make a sand box.

if not os.path.exists(working_path):
    print("Working path directory does not exist.\n")
elif os.path.exists(working_path):
    print("Working path directory exists.\n")
   
# We created a path for the test folder in "working_path".
# Make a folder.
# print(os.path.join(path, "/home", "file.txt"))
## FORWARD SLASH MEANS ABSOLUTE DIRECTORY!!!
# Strip the user's entry of "\" and "/".

print(os.path.join(working_path, "test_directory", "another_test_dir")) ##****You could ask the user for input to make these.
newpath = os.path.join(working_path, "test_directory", "another_test_dir") # created a folder(directory) not a textfile
print()

# Test it.
if not os.path.exists(newpath):
    print("newpath directory does not exist.")
    os.makedirs(newpath)
    # if os.path.exists(newpath): ## REDUNDANT
    # # Triple quotes includes the newline break "\n".
    print(f'''
    You have now created {newpath} 
    That is the another_test_dir.
    \n''' )
elif os.path.exists(newpath):
    print("newpath directory already exists.\n")
# Directory should not exist at this point, unless I used mkdirs

# Now experiment with the cd command!
# Let the user see where they are in the file tree.
# Let the user choose where they want their folders(directories) to go.
# UI/UX

destination = input("Enter the path name: ")
change_path = os.chdir(destination)
print(change_path) # gives None
'''
The current directory can be changed using chdir():
os.chdir(path)
The listdir() function returns the content of a directory. Note, however, that it mixes directories and files.
'''
    # os.makedirs(newpath)
# os.makedirs()

# Make a file.
# Test it.

# Python program to explain os.path.join() method 

# Bunch of commands from makeuseof.com/python-os-system
print("What's my OS?")
print(os.name)
print()
print("Give me more details.")
# os.uname()  NOT WORKING
print()
print("What directory am I in?")
os.getcwd()
print()
print("Take me to the treemaker folder.")
os.chdir(r"C:\\Users\\default.DESKTOP-P3E3RAC\\Documents\\School\\BYU-I\\Winter 2021")
print()
print("See? Did it work?")
os.getcwd()
