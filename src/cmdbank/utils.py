import pyperclip, os
from pathlib import Path
from .paths import READCMD, DATA_DIR
from .errors import *

def copy_command():
    cmd_choice = input("\n> ")

    # Return to main menu if back option is selected
    if cmd_choice == "b":
        return True, None
        
    select = False
    with open(READCMD, "r") as f1:

        # Iterates through all lines in .READCMD
        for l in f1:
            if select:
                select = False
                saved_cmd = l.strip()

            if l.strip() == cmd_choice and cmd_choice != "":
                select = True
            else:
                pass

    try:
        pyperclip.copy(saved_cmd)
        print("Command has been copied to you clipboard!")

        # os.system(saved_cmd)
        return False, None
    except:
        error_input_invalid()
        return None, True

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