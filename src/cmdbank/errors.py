from rich import print

# Interrupt errors
def error_keyboard_interrupt():
    print("\n[red]Keyboard Interrupt - No command saved to clipboard[/red]")

# File errors
def error_file_invalid_char():
    print("[red]ERROR - File name cannot include the following characters: . , / \\ (space)[/red]")

def error_file_invalid_int():
    print("[red]ERROR - File name cannot be an integer[/red]")

def error_file_already_exists():
    print("[red]ERROR - This file already exists[/red]")

def error_file_doesnt_exist():
    print("[red]ERROR - This file does not exist[/red]")

def error_file_menu_option():
    print("[red]ERROR - File cannot have the same name as a menu option[/red]")

# Input errors
def error_input_invalid():
    print("[red]ERROR - Invalid input. This is not a saved command, or a menu option. Please try again[/red]")

# Read errors
def error_read_file_path(cmd_path):
    print("[red]ERROR - Could not read[/red]", cmd_path)

def error_read_READCMD():
    print("[red]ERROR - Could not read .READCMD[/red]")