import os
import sys
import pytest
# If "1" is cwd then...
# 1. .. (parent/out)
# 2. / (child/in)
# Lists folders
# 3. / (child/in)
# 4. / (child/in)
# OR
# All in a loop
# At each listed file ask if they want to go to the file.
# OPTIONS
# 1. Stay
# 2. Go In
# 3. Go Out
# 4. Quit File Search (Program)


# BEGIN FILE UTILITY LOOP
def look_or_move():  # Inside change_dir
    choice = 1
    while choice != 0:  # THE CD (change directory) LOOP
        # JUST. THE. FOLDERS.
        # KEEP
        # S I M P L E.
        # Print out options
        try:
            cwd = os.getcwd()
            print(f"\nYour are in:\n {cwd}")
    # Matthew's is UI/UX friendly.
    # Mine is coder friendly.
            choice = int(input(f"""
            Do you want to:
            (0) Quit changing directory?
            (1) Go up one file?
            (2) See full contents of the directory?
            (3) See only the folders in the directory?
            (4) Go into a file/folder?
            """))
            # Show folders option for (4)?

                    # Which file/folder do you want to go into?
            # (5) Go down the filetree (away from root/{cwd}drive) # I removed these to reduce redundancy.
            os.system("cls")  # This cleans up the terminal
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
            else:
                pass
        except:
            pass
            # Insert 0 and 1 into the dirlist
            # dirlist makes a new list each time
# NOW USER LIKES IT


def change_dir():
    key = True
    while key == True:
        # try:
        cwd = os.getcwd()  # Prints Current Working Directory
        print(f"\nYour are in:\n {cwd}\n")

        # OPTION TO SEE
        inquiry = input(
            'Are you happy with your current location/directory? ("yes" or "no") ').lower()
        # add error handling random characters
        # use a while loop as a control
        if inquiry == "yes":
            key = False  # flag variable
          # IF YES, GO TO MAIN
        elif inquiry == "no":
            look_or_move()
            # START LOOP TO GET TO DIRECTORY
        else:
            pass
        # except:

# MAKE FOLDER/S AND/OR FILE/S


def make_dir():
    key = True
    while key == True:
        cwd = os.getcwd()  # Prints Current Working Directory
        print(f"\nYour are in:\n {cwd}\n")
        inquiry = input(
            'Would you like to make a directory here? ("yes" or "no") ').lower
        # Will this scope allow me to use "inquiry" variable again?
        if inquiry == "yes":
            create_folder()
            pass
        # IF YES, GO TO FILE MAKER "create_folder()"
        elif inquiry == "no":
            inquiry_where = input('Would you like to make a directory somewhere else? ("yes" or "no") ').lower
            if inquiry_where == "yes":
                change_dir()
                pass
            elif inquiry_where == "no":
                print("Alright. Going to directory menu.\n")
                key = False
                pass
            # Should I just let the loop break or call the main function?
            pass
        else:
            pass


def create_folder():
    key_two = True
    while key_two == True:
        # Parent Directory path
        # cwd = os.getcwd()  # Prints Current Working Directory
        parent_dir = os.getcwd() # The current working directory also serves as the parent directory.
        print("You are in:\n '% s'\n" % parent_dir) # "current_working_directory" # or desired parent directory
        # os.chdir('..') # This took me from "treemaker_folder".
        print()

        directory = input("Please name your new directory: ")
        print()
        
        path = os.path.join(parent_dir, directory) # Create path using string concatenation with address/path
        print()

        if os.path.exists(path):
            print("You already have this directory here.\n Please try again.")
            pass
        elif not os.path.exists(path):
            # unhappy = True
            # while unhappy == True:

            print(f"'{directory}' is a valid directory name.")
            name_inquiry = input('Are you happy with the name of your directory? ("yes" or "no") ').lower
            if name_inquiry == "no":
                print("Okay, let's try again.")
                pass
            elif name_inquiry == "yes":
                os.mkdir(path)
                print("Nice! You just created the directory called '{}'\n  at: \n'{}' ".format(directory, path))
                print()
                # more_inquiry = input('Do you want to make a series of folders in this directory? ("yes" or "no") ').lower
                # if more_inquiry == "no":
                #     print("Alright. Going to directory prompt.")
                key_two = False
                #     pass
                # elif more_inquiry == "yes":
                pass
                    # pass
    pass

# DELETE FOR OR FOLDER
# WARNING, THIS MAY CAUSE HARM
# Leaving out until further notice
# def deleter():

#     pass

# FUNCTIONATE AT THE END! (break into functions at the end)


def main():
    print("Welcome to the Treemaker program.\n Let's begin!")
    run = True
    while run == True:
        # try:
        run = input()
        option = int
        while option != 0:
            # try:
            cwd = os.getcwd()
            print(f"\nYour are in:\n {cwd}")

            option = int(input(f"""
            Would you like to:
            (0) Exit the program?
            (1) Change your location/directory?
            (2) View your files and folders?
            (3) Create a file/folder?
            
            """))
            os.system("cls")  # This cleans up the terminal
            if option == 0:
                sure = True
                while sure == True:
                    # Do I need to keep the parentheses here on "lower" method?
                    sure = input(
                        'Are you sure you want to quit? ("yes" or "no") ').lower()
                    if sure == "yes":
                        sure = False
                        run = False
                        print(
                            "\n Thank you for using Treemaker.\n      Good bye for now!")
                    elif sure == "no":
                        pass
                    else:
                        pass
                break
            elif option == 1:
                change_dir()  # Change directory
                pass
            elif option == 2:
                look_or_move()  # View files and directories
                pass
            elif option == 3:
                make_dir()  # Make directory
                pass
                """
                # (4) Delete a file/folder?
                elif option == 4:
                    deleter()  # Delete file or folder
                    # WARNING, THIS MAY CAUSE HARM.
                    pass
                """
            else:
                pass


            # except:
        # except:
if __name__ == '__main__':
    main()


# Dirty terminal?
    # Use sys.cls OR sys.clear
    # sys is using a system command
