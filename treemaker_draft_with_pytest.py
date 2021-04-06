import os

# BEGIN FILE UTILITY LOOP
def look_or_move():  # Inside change_dir
    try:
        choice = 1
        while choice != 0:  # THE CD (change directory) LOOP
            # Print out options
            
                cwd = os.getcwd()
                print(f"\nYour are in:\n {cwd}") # check exit loop
                choice = int(input(f"""
                Do you want to:
                (0) Quit changing directory?
                (1) Go up one file?
                (2) See full contents of the directory?
                (3) See only the folders in the directory?
                (4) Go into a file/folder?
                """))
                # Dirty terminal?
                    # Use sys.cls OR sys.clear
                    # sys is using a system command
                os.system("cls")  # This cleans up the terminal
                if choice == 0:
                    break
                elif choice == 1:  # the ".."
                    os.chdir('..')  # GOES TO PARENT DIRECTORY
                    # .. means parent directory
                    print("Going up")
                    pass
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
                        if os.path.isdir(directory) == True:
                            print(directory)
                # WORKING
                elif choice == 4:
                    print()
                    for directory in os.listdir(os.getcwd()):
                        if os.path.isdir(directory) == True:
                            print(directory)
                    new_dir = input("\nThose are the current folders in this current working directory. \n What folder do you want to go into? ")
                    os.chdir(new_dir)
                    print("CWD changed") # Does this show up? Cleared?
                # WORKING
                else:
                    pass
    except ValueError as ex:
        print()
        print(f"ValueError: {ex} Try again: ")
           # NOW USER LIKES IT

# CHANGES DIRECTORY
def change_dir():
    try:
        key = True
        while key == True:
            # try:
            cwd = os.getcwd()  # Prints Current Working Directory
            print(f"\nYour are in:\n {cwd}\n")

            # OPTION TO SEE
            inquiry = input('Are you happy with your current location/directory? ("yes" or "no") ').lower()
            os.system("cls")  # This cleans up the terminal
            if inquiry == "yes": # IF YES, GOES BACK TO main()
                key = False  # flag variable
            elif inquiry == "no": # STARTS DIRECTORY FINDING LOOP 
                look_or_move()
            else:
                pass
    except ValueError as ex:
            print()
            print(f"ValueError: {ex} Try again: ")

# MAKES FOLDER/S AND/OR FILE/S
def make_dir():
    try:
        key = True
        while key == True:
            os.system("cls")  # Terminal Clean-Up
            cwd = os.getcwd()  # Prints Current Working Directory
            print(f"\nYour are in:\n {cwd}\n")
            inquiry = input('Would you like to make a directory here? ("yes" or "no") ').lower()
            # print(inquiry) # location on memory means telling where .lower() function is instead of actually running the function.
            # Will this scope allow me to use "inquiry" variable again?
            if inquiry == "yes":
                create_folder()
                key = False
                pass
            # IF YES, GO TO FILE MAKER "create_folder()"
            elif inquiry == "no":
                inquiry_where = input('Would you like to make a directory somewhere else? ("yes" or "no") ').lower()
                if inquiry_where == "yes":
                    key = False # Comes back here when done with create_folder()
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
    except ValueError as ex:
            print()
            print(f"ValueError: {ex} Try again: ")

# OKAY, THIS ACTUALLY MAKES FOLDER/S AND/OR FILE/S
def create_folder():
    try:
        key_two = True
        while key_two == True:
            directory = ""
            # Parent Directory path
            parent_dir = os.getcwd() # The current working directory also serves as the parent directory.
            print("You are in: '% s'\n" % parent_dir) # "current_working_directory" # or desired parent directory
            print()
            for directory in os.listdir(parent_dir):
                if os.path.isdir(directory) == True:
                    print(directory)
            new_path = input("These are the current folders in this directory.\n Please give your directory a new name: ")
            print()
            path = os.path.join(parent_dir, new_path) # Create path using string concatenation with address/path
            print()
            # PATH CHECKER
            if os.path.exists(path):
                print("You already have this directory here.\n Please try again.")
                pass
            elif not os.path.exists(path):
                # unhappy = True
                # while unhappy == True:
                os.system("cls")  # This cleans up the terminal
                print(f"'{new_path}' is a valid directory name.")
                name_inquiry = input('Are you happy with the name of your directory? ("yes" or "no") ').lower()
                if name_inquiry == "no":
                    print("Okay, let's try again.")
                    pass
                elif name_inquiry == "yes":
                    os.mkdir(path)
                    print("Nice! You just created the directory called '{}'\n  at: \n'{}' ".format(directory, path))
                    print()
                    # more_inquiry = input('Do you want to make a series of folders in this directory? ("yes" or "no") ').lower()
                    # if more_inquiry == "no":
                    #     print("Alright. Going to directory prompt.")
                    key_two = False
                    #     pass
                    # elif more_inquiry == "yes":
                    pass
                        # pass
        pass
    except ValueError as ex:
            print()
            print(f"ValueError: {ex} Try again: ")
# Leaving deleter() out until further notice
# Too dangerous
# DELETE FOR OR FOLDER
# WARNING, THIS MAY CAUSE HARM
# def deleter():
#     pass

# THE MAIN GATE
def main():
    try:
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
                            sure = False
                            main()
                            pass
                        else:
                            pass
                    break
                elif option == 1:
                    # run == False
                    change_dir()  # Change directory
                    pass
                elif option == 2:
                    # run == False
                    look_or_move()  # View files and directories
                    pass
                elif option == 3:
                    # run == False
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
    except ValueError as ex:
        print()
        print(f"ValueError: {ex} Try again: ")
            
if __name__ == '__main__':
    main()
