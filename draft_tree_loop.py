# loop to see if the user is happy with where they want to be

import pytest
import os, sys
# If "1" is cwd then...
    # 1. .. (parent/out)
        # 2. / (child/in)
            # Lists folders
        # 3. / (child/in)
        # 4. / (child/in)
# OR
#All in a loop
    # At each listed file ask if they want to go to the file.
        # OPTIONS
        # 1. Stay
        # 2. Go In
        # 3. Go Out
        # 4. Quit File Search (Program)


def main():
    print("Welcome to the Treemaker program.")
    change_dir() # Change directory
    make_dir() # Make directory
    deleter() # Delete file or folder
        # WARNING, THIS MAY CAUSE HARM.
    
# BEGIN FILE UTILITY LOOP

def look_or_move(): # Inside change_dir
    choice = 1
    while choice != 0:  # THE CD (change directory) LOOP
        # JUST. THE. FOLDERS.
        # KEEP
            # S I M P L E.
        # Print out options
        try:
            cwd = os.getcwd()
            print(f"\nYour are in:\n {cwd}")
    ## Matthew's is UI/UX friendly.
    ## Mine is coder friendly.
            choice = int(input(f"""
            Do you want to:
            (0) Quit changing directory?
            (1) Go up one file?
            (2) See full contents of the directory?
            (3) See only the folders in the directory?
            (4) Go into a file/folder?
                    Which file/folder do you want to go into?
            """))
                    # Show folders option for (4)?

            # (5) Go down the filetree (away from root/{cwd}drive) # I removed this to reduce redundancy.
            os.system("cls") # This cleans up the terminal
            if choice == 0:
                break
            elif choice == 1:  # the ".."
                os.chdir('..')  # GOES TO PARENT DIRECTORY
                                # .. means parent directory
                print("Going up")
                pass
            # just show what's in the directory (STARTS LISTING FILES)
            # WORKING
            elif choice == 2:
                                # See full contents in this directory?
                for directory in os.listdir(os.getcwd()):
                    print(directory)
                pass
            # WORKING
            elif choice == 3:  # See only the folders in the directory?
                for directory in os.listdir(os.getcwd()):
                    # isdir = os.path.isdir(directory) # Unnecessary line
                    # cwd is in directory variable
                    if os.path.isdir(directory) == True:
                        print(directory)
            # WORKING
            elif choice == 4:
                new_dir = input("What folder do you want to go into? ")
                os.chdir(new_dir)
                print("CWD changed")
            # WORKING

                # cwd = os.getcwd()
                # print(f"\nYour are in:\n {cwd}\n")
            #     pass
            # elif choice == 3: # Go into a file/folder?
            #     pass
                # (3) Go into a file/folder? # Toggle Button with GUI
                #    Which file/folder do you want to go into?
                #    (Show folders)
                        # Toggle Button with GUI
                #     pass
            # if choice == 4:
            #     pass
            else:
                pass
        except:
            pass
                    # Insert 0 and 1 into the dirlist
                    # dirlist makes a new list each time

# NOW USER LIKES IT

def change_dir():
    # Print CWD
    cwd = os.getcwd()
    print(f"\nYour are in:\n {cwd}\n")

    # OPTION TO SEE
    inquiry = input(
        'Are you happy with your current location/directory? ("yes" or "no") ').lower()
    # add error handling random characters
    # use a while loop as a control
    # try:
    if inquiry == "yes":
        pass
    # IF YES, GO TO FILE MAKER
    elif inquiry == "no":
        look_or_move()
        # START LOOP TO GET TO DIRECTORY
    else:
        pass
    # except:

# MAKE FOLDER/S AND/OR FILE/S

def make_dir():

    pass


# DELETE FOR OR FOLDER
# WARNING, THIS MAY CAUSE HARM

def deleter(): 

    pass

# FUNCTIONATE AT THE END! (break into functions at the end)

if __name__ == '__main__':
    main()


# Dirty terminal?
    # Use sys.cls OR sys.clear
    # sys is using a system command