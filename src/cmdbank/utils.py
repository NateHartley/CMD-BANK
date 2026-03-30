import pyperclip, os
from pathlib import Path
from .paths import READCMD, DATA_DIR
from .errors import *

### Copies user selected command from current command file
def copy_command():
    cmd_choice = get_user_input()
    # User inputted an integer
    try:
        int(cmd_choice) # Don't need to set this to a var, if user input = int then try succeeds, if user input = str then try fails
        selected_cmd = get_selected_command(cmd_choice)
        # If integer is out of range, jump to except clause
        if selected_cmd == None:
            raise ValueError
        pyperclip.copy(selected_cmd) #TODO: Include option to save to clipboard or run directly with os.system(saved_cmd)
        print("Command has been copied to you clipboard!")
        return False, None
        
    # User inputted a string, return to main menu if back option is selected
    except ValueError:
        if cmd_choice == "b":
            return True, None
        else:
            error_input_invalid()
            return None, True
        
### Matches command number with user input from .READCMD,
### Returns selected command
def get_selected_command(cmd_choice):
    selected_cmd = None
    select = False
    with open(READCMD, "r") as f1:
        # Iterates through all lines in .READCMD, 
        for line in f1:
            if select:
                select = False
                selected_cmd = line.strip()
            if line.strip() == cmd_choice and cmd_choice != "":
                select = True
    return selected_cmd

### Compiles list of command files,
### returns list, and return_to_menu bool
def list_command_files():
    return_to_menu = True
    cmd_list = list(Path(DATA_DIR).iterdir())

    lst = []
    for i in range(0, len(cmd_list)):
        cmd_file = str(cmd_list[i])
        file_name = os.path.basename(cmd_file)
        file_name_no_extension = os.path.splitext(file_name)[0]
        lst.append(file_name_no_extension)

    lst = sorted(lst) # Sorts list alphabetically

    return lst, return_to_menu

### Gets path to command file from user selection and returns path
def get_command_file_path(selected_cmd_file):
    cmd_file_name = selected_cmd_file + ".txt"
    cmd_file_path = Path.cwd().joinpath(DATA_DIR, cmd_file_name)
    return cmd_file_path

### Gets user input and returns user input
def get_user_input():
    user_input = input("> ")
    return user_input

### Determines if a user inputted file name is valid or not,
### returns true or false
def is_valid_file_name(file_name, stored_commands):
    invalid_char = ['.', ',', '/', '\\', ' ']

    if file_name.isnumeric() == False:
        for i in file_name:
            if i in invalid_char:
                error_file_invalid_char()
                return False
        
        if file_name in stored_commands:
            error_file_already_exists()
            return False
        elif file_name == 'a' or file_name == 'e' or file_name == 'd' or file_name == 'q':
            error_file_menu_option()
            return False
        else:
            return True
    else:
        error_file_invalid_int()
        return False