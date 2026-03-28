from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.columns import Columns

def main_menu(s_c):
    stored_commands = s_c
    console = Console()

    # View Saved Commands column
    table1 = Table(show_header=False, box=None, pad_edge=False)
    table1.add_column("No.", style="green", width=2, justify="right")
    table1.add_column("Option", style="cyan")

    if not stored_commands:
        table1.add_row("", "[red](Directory is empty)[/red]")
    else:
        for i, opt in enumerate(stored_commands, start=1):
            table1.add_row(str(i)+")", opt)

    # Menu Options column
    table2 = Table(show_header=False, box=None, pad_edge=False)
    table2.add_column("Option")
    table2.add_row("[green]a)[/green] add")
    table2.add_row("[green]e)[/green] edit")
    table2.add_row("[green]d)[/green] delete")
    table2.add_row("[green]q)[/green] quit")

    # Panels inside of main box
    columns = Columns(
        [
            Panel(table1, title="View Saved Commands", padding=(1,4)), # Don't set to white bc of light theme
            Panel(table2, title="Menu Options", padding=(1,4)),
        ],
        equal=False,
        expand=True,
    )

    # Main box
    console.print(
        Panel(
            columns,
            title="[bold]CMD-BANK[/bold]",
            border_style="green",
            padding=(0, 1),
        )
    )

def command_file_content(text, cmd_path, f1, f2, cmd_num):
    if cmd_path.stat().st_size == 0:
        text.append("(File is empty)\n\n", style="red")
    else:
        previous_line = " "
        for l in f2:

            # If line is not blank, no else statement so ignoring all blank lines
            if l.strip():

                # If reading the info text
                if l[0] == "#":
                    info = l[1:].strip()
                    text.append(info+"\n\n", style="italic")

                # If reading the command text
                else:
                    # If two commands next to each other, no space in between them
                    if previous_line[0] != "#" and previous_line != " ":
                        text.append("\n")

                    cmd_num += 1
                    number = "["+str(cmd_num)+"]"
                    f1.write("%d\n" % cmd_num)
                    f1.write(l + "\n")
                    command = l.rstrip()
                    text.append(number, style="yellow")
                    text.append(" ")
                    text.append(command+"\n", style="cyan")
        
                previous_line = l
        return previous_line

def command_file_structure(console, text, cmd_path, previous_line, selected_cmd):
    # Back option
    if cmd_path.stat().st_size != 0:
        if previous_line[0] != "#":
            text.append("\nb)", style="green")
        else:
            text.append("b)", style="green")
    else:
        text.append("b)", style="green")
    text.append(" ")
    text.append("back", style="white")

    console.print(
        Panel(
            text,
            title="[bold]"+selected_cmd+"[/bold]",
            border_style="green",
        )
    )