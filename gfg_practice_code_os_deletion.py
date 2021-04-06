


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

# Output: See: python-os.remove-output.png


"""
# Using os.rmdir()
os.rmdir() method in Python is used to remove or delete a empty directory. OSError will be raised if the specified path is not an empty directory.

Example: Suppose the directories are –



# Python program to explain os.rmdir() method 
      
# importing os module 
import os 
      
# Directory name 
directory = "Geeks"
      
# Parent Directory 
parent = "D:/Pycharm projects/"
      
# Path 
path = os.path.join(parent, directory) 
      
# Remove the Directory 
# "Geeks" 
os.rmdir(path) 
Output:



Commonly Used Functions
1. os.name: This function gives the name of the operating system dependent module imported. The following names have currently been registered: ‘posix’, ‘nt’, ‘os2’, ‘ce’, ‘java’ and ‘riscos’


import os
  
print(os.name)
Output:

posix
Note: It may give different output on different interpreters, such as ‘posix’ when you run the code here.

2. os.error: All functions in this module raise OSError in the case of invalid or inaccessible file names and paths, or other arguments that have the correct type, but are not accepted by the operating system. os.error is an alias for built-in OSError exception.

import os
  
  
try:
    # If the file does not exist,
    # then it would throw an IOError
    filename = 'GFG.txt'
    f = open(filename, 'rU')
    text = f.read()
    f.close()
  
# Control jumps directly to here if 
# any of the above lines throws IOError.    
except IOError:
  
    # print(os.error) will <class 'OSError'>
    print('Problem reading: ' + filename)
      
# In any case, the code then continues with 
# the line after the try/except
Output:

Problem reading: GFG.txt
 

3. os.popen(): This method opens a pipe to or from command. The return value can be read or written depending on whether mode is ‘r’ or ‘w’.
Syntax:

 os.popen(command[, mode[, bufsize]])
Parameters mode & bufsize are not necessary parameters, if not provided, default ‘r’ is taken for mode.

import os
fd = "GFG.txt"
  
# popen() is similar to open()
file = open(fd, 'w')
file.write("Hello")
file.close()
file = open(fd, 'r')
text = file.read()
print(text)
  
# popen() provides a pipe/gateway and accesses the file directly
file = os.popen(fd, 'w')
file.write("Hello")
# File not closed, shown in next function.
Output:

Hello
Note: Output for popen() will not be shown, there would be direct changes into the file.

4. os.close(): Close file descriptor fd. A file opened using open(), can be closed by close()only. But file opened through os.popen(), can be closed with close() or os.close(). If we try closing a file opened with open(), using os.close(), Python would throw TypeError.

import os
  
  
fd = "GFG.txt"
file = open(fd, 'r')
text = file.read()
print(text)
os.close(file)
Output:

Traceback (most recent call last):
  File "C:\Users\GFG\Desktop\GeeksForGeeksOSFile.py", line 6, in 
    os.close(file)
TypeError: an integer is required (got type _io.TextIOWrapper)
Note: The same error may not be thrown, due to non-existent of file or permission privilege.

5. os.rename(): A file old.txt can be renamed to new.txt, using the function os.rename(). The name of the file changes only if, the file exists and user has sufficient privilege permission to change the file.

import os
  
  
fd = "GFG.txt"
os.rename(fd,'New.txt')
os.rename(fd,'New.txt')
Output:


Traceback (most recent call last):
  File "C:\Users\GFG\Desktop\ModuleOS\GeeksForGeeksOSFile.py", line 3, in 
    os.rename(fd,'New.txt')
FileNotFoundError: [WinError 2] The system cannot find the
file specified: 'GFG.txt' -> 'New.txt'
Understanding the Output: A file name “GFG.txt” exists, thus when os.rename() is used the first time, the file gets renamed. Upon calling the function os.rename() second time, file “New.txt” exists and not “GFG.txt”
thus Python throws FileNotFoundError.

This article is contributed by Piyush Doorwar. If you like GeeksforGeeks and would like to contribute, you can also write an article using contribute.geeksforgeeks.org or mail your article to contribute@geeksforgeeks.org. See your article appearing on the GeeksforGeeks main page and help other Geeks.

Please write comments if you find anything incorrect, or you want to share more information about the topic discussed above.


"""