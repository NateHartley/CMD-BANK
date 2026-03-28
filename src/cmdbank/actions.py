from pathlib import Path
import platform
from subprocess import run
from rich.console import Console
from rich.text import Text
from .errors import *
from .paths import DATA_DIR, READCMD
from .render import command_file_content as render_command_file_content, command_file_structure as render_command_file_structure
from .utils import copy_command

def add(stored_commands):
    print("Enter the name of a file to add:")
    cmd = input("> ")
    invalid_char = ['.', ',', '/', '\\', ' ']

    if cmd.isnumeric() == False:
        for i in cmd:
            if i in invalid_char:
                error_file_invalid_char()
                return
        
        if cmd in stored_commands:
            error_file_already_exists()
        elif cmd == 'a' or cmd == 'e' or cmd == 'd' or cmd == 'q':
            error_file_menu_option()
        else:
            cmd_file = cmd + ".txt"
            path = Path.cwd().joinpath(DATA_DIR, cmd_file)
            open(path, "x")
            print(cmd, "has been added.")
    else:
        error_file_invalid_int()

def edit(stored_commands):
    print("Enter the name of a file to edit:")
    cmd = input("> ")
    if cmd in stored_commands:
        cmd_file = cmd + ".txt"
        path = Path.cwd().joinpath(DATA_DIR, cmd_file)
        if platform.system() == "Windows":
            run(["edit", path])
        if platform.system() == "Linux" or platform.system() == "Darwin":
            run(["nano", path]) # TODO: Replace run with os.system()?
    else:
        error_file_doesnt_exist()

def delete(stored_commands):
    print("Enter the name of a file to delete:")
    cmd = input("> ")

    if cmd in stored_commands:
        cmd_file = cmd + ".txt"
        path = Path.cwd().joinpath(DATA_DIR, cmd_file)
        print("Are you sure you want to delete", cmd,"? (Y/N)")
        confirm = input("> ").upper()
        if confirm == 'Y' or confirm == 'YES':
            path.unlink()
        else:
            print("Delete cancelled...")
    else:
        error_file_doesnt_exist()

def view(stored_commands, usr_input):
    console = Console()
    text = Text()

    return_to_command_file = True
    while return_to_command_file:

        # If user input is an integer
        try:
            selection = int(usr_input)

            # Error handling if user input is 0 or too high
            if selection != 0 and selection <= len(stored_commands):
                selected_cmd = stored_commands[selection-1]
                cmd_file = selected_cmd + ".txt"
                cmd_path = Path.cwd().joinpath(DATA_DIR, cmd_file)

        # If user input is a string
        except ValueError:
            i = 0
            for i in stored_commands:
                if i == usr_input:
                    selected_cmd = i
                    cmd_file = i + ".txt"
                    cmd_path = Path.cwd().joinpath(DATA_DIR, cmd_file)
                    break

        # Format contents of command file to .READCMD
        cmd_num = 0
        try:
            with open(READCMD, "w") as f1:
                try:
                    with open(cmd_path, "r") as f2:
                        previous_line = render_command_file_content(text, cmd_path, f1, f2, cmd_num)

                    render_command_file_structure(console, text, cmd_path, previous_line, selected_cmd)

                # User inputted '0' therefore cmd_path is not set, triggering UnboundLocalError
                except UnboundLocalError:
                    error_input_invalid()
                    return True
                except:
                    error_read_file_path(cmd_path)
                    return False
        except:
            error_read_READCMD()
            return False
    
        return_to_menu, return_to_command_file = copy_command()

    return return_to_menu