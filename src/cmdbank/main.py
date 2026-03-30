#!/usr/bin/env python3
import sys
from .paths import init_paths
from .render import main_menu as render_main_menu
from .actions import add, edit, delete, view
from .errors import *
from .utils import *

### Executes main menu actions (add, edit, delete, quit, view command file) based on user input, and invokes rendering
def app():
    return_to_menu = True
    menu_options = ['a', 'e', 'd', 'q']
    while return_to_menu:
        stored_commands, return_to_menu = list_command_files()
        render_main_menu(stored_commands)
        usr_input = get_user_input()
        print("")
        try:
            if usr_input in menu_options:
                match usr_input:
                    case "a":
                        add(stored_commands)
                    case "e":
                        edit(stored_commands)
                    case "d":
                        delete(stored_commands)
                    case "q":
                        return_to_menu = False
            else:
                return_to_menu = view(stored_commands, usr_input)
        except KeyboardInterrupt:
            error_keyboard_interrupt()
            sys.exit()

### Runs main application
def main():
    init_paths()
    try:
        app()
    except KeyboardInterrupt:
        error_keyboard_interrupt()
        sys.exit()
    
if __name__ == "__main__":
    main()