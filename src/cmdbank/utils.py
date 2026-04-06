import pyperclip, os
from pathlib import Path
from .paths import READCMD, DATA_DIR, CONFIG
from .errors import *
from time import sleep

### Copies user selected command from current command file, 
### or will run the command directly then return to CMD-BANK depending on user's settings
def copy_run_command():
    cmd_choice = get_user_input()
    # User inputted an integer
    try:
        int(cmd_choice) # Don't need to set this to a var, if user input = int then try succeeds, if user input = str then try fails
        selected_cmd = get_selected_command(cmd_choice)
        # If integer is out of range, jump to except clause
        if selected_cmd == None:
            raise ValueError

        # If user sets copy_command_to_clipboard to true, copy to clipboard, else run command directly
        copy_to_clipboard = get_setting_in_config("copy_command_to_clipboard")
        if copy_to_clipboard == True:
            pyperclip.copy(selected_cmd)
            print("Command has been copied to you clipboard!")
        elif copy_to_clipboard == False:
            print("Running command...")
            os.system(selected_cmd)
            sleep(0.3) # Small delay between running command and returning to command file for readability
            return False, True

        return False, False
        
    # User inputted a string, return to main menu if back option is selected
    except ValueError:
        #TODO: replace with back_option()
        if cmd_choice == "b":
            return True, False
        else:
            error_input_invalid_command()
            return False, True
        
### Returns true if back option is selected when viewing a command file or the settings menu, this will regenerate the main menu
def back_option(usr_input):
    if usr_input == "b":
        return True, False
    else:
        return False, True
        
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
### returns list, and return_to_main_menu bool
def list_command_files():
    return_to_main_menu = True
    cmd_list = list(Path(DATA_DIR).iterdir())
    lst = []
    for i in range(0, len(cmd_list)):
        cmd_file = str(cmd_list[i])
        file_name = os.path.basename(cmd_file)
        file_name_no_extension = os.path.splitext(file_name)[0]
        lst.append(file_name_no_extension)
    lst = sorted(lst) #TODO: Sorts list alphabetically - activate with settings option
    return lst, return_to_main_menu

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
def is_valid_file_name(file_name, stored_commands, menu_options):
    invalid_char = ['.', ',', '/', '\\', ' ']

    if file_name.isnumeric() == False:
        for i in file_name:
            if i in invalid_char:
                error_file_invalid_char()
                return False
        
        for stored_command in stored_commands:
            if file_name.lower() == stored_command.lower():
                error_file_already_exists()
                return False
        
        if file_name in menu_options:
            error_file_menu_option()
            return False
        else:
            return True
    else:
        error_file_invalid_int()
        return False
    
### Takes in a particular setting option e.g. "copy_command_to_clipboard", matches that string with corresponding setting in config.toml,
### returns True if setting is set to true, False if false, and None if there's a read error
def get_setting_in_config(chosen_setting):
    matching_setting = False
    with open(CONFIG, "r") as config_file:
        for line in config_file:
            # Skip first blank line of config.toml
            if line.strip():
                if line.split()[0] == chosen_setting:
                    matching_setting = True
                    if line.split()[-1] == "true":
                        return True
                    elif line.split()[-1] == "false":
                        return False
                    else:
                        error_read_CONFIG_bool(chosen_setting)
                        return None
        if not matching_setting:
            error_read_CONFIG_flag(chosen_setting)
            return None

### Returns list of all settings in config.toml, including setting names and assigned bools
def list_config_settings():
    settings_list = []
    with open(CONFIG, "r") as config_file:
        for line in config_file:
            # Skip first blank line of config.toml
            if line.strip():
                # Doesn't add "=" to list
                setting = [i for i in line.split() if i != "="]
                settings_list.append(setting)
    return settings_list