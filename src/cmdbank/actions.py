import platform
from subprocess import run
from rich.console import Console
from rich.text import Text
from .errors import *
from .paths import READCMD
from .render import command_file_content as render_command_file_content, command_file_structure as render_command_file_structure
from .utils import *

### Creates new command file named after user input
def add(stored_commands):
    print("Enter the name of a file to add:")
    file_name = get_user_input()
    valid = is_valid_file_name(file_name, stored_commands)
    if valid:
        path = get_command_file_path(file_name)
        open(path, "x")
        print(file_name, "has been added.")

### Edits content of selected command file
def edit(stored_commands):
    print("Enter the name of a file to edit:")
    cmd = get_user_input()
    if cmd in stored_commands:
        path = get_command_file_path(cmd)
        if platform.system() == "Windows":
            run(["edit", path])
        if platform.system() == "Linux" or platform.system() == "Darwin":
            run(["nano", path])
    else:
        error_file_doesnt_exist()

### Deletes selected command file
def delete(stored_commands):
    print("Enter the name of a file to delete:")
    cmd = get_user_input()
    if cmd in stored_commands:
        path = get_command_file_path(cmd)
        print("Are you sure you want to delete", cmd+"? (y/n)")
        confirm = get_user_input().upper()
        if confirm == 'Y' or confirm == 'YES':
            path.unlink()
        else:
            print("Deletion cancelled...")
    else:
        error_file_doesnt_exist()

### Displays contents of selected command file and copies chosen command from command file,
### returns return_to_menu bool
def view(stored_commands, usr_input):
    return_to_command_file = True
    while return_to_command_file:
        cmd_file_path, selected_cmd_file = view_input_handling(stored_commands, usr_input)

        # Error handling when user input isn't command file name or menu option
        if cmd_file_path == None or selected_cmd_file == None:
            error_input_invalid()
            return True

        # Format and write contents of command file to .READCMD
        try:
            with open(READCMD, "w") as f1:
                try:
                    console = Console()
                    text = Text()
                    with open(cmd_file_path, "r") as f2:
                        previous_line = render_command_file_content(text, cmd_file_path, f1, f2)
                    render_command_file_structure(console, text, cmd_file_path, previous_line, selected_cmd_file)
                except:
                    error_read_file_path(cmd_file_path)
                    return False
        except:
            error_read_READCMD()
            return False
        return_to_menu, return_to_command_file = copy_run_command()
    return return_to_menu

### Handles user input when selecting a command file to view, 
### returns path to selected file and selected command
def view_input_handling(stored_commands, usr_input):
    # Need to define strings here, otherwise edge cases error because vars aren't defined
    cmd_file_path = None
    selected_cmd_file = None

    # If user input is an integer
    try:
        selection = int(usr_input)

        # Error handling if user input is 0 or too high
        if selection != 0 and selection <= len(stored_commands):
            selected_cmd_file = stored_commands[selection-1]
            cmd_file_path = get_command_file_path(selected_cmd_file)

    # If user input is a string
    except ValueError:
        i = 0
        for i in stored_commands:
            if i == usr_input:
                selected_cmd_file = i
                cmd_file_path = get_command_file_path(i)
                break
    return cmd_file_path, selected_cmd_file