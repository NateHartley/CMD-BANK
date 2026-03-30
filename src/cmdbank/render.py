from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.columns import Columns

### Renders main menu, including main menu outline box, "View Saved Commands" column, and "Menu Options" column
def main_menu(stored_commands):
    console = Console()

    # "View Saved Commands" column
    VSC_table = Table(show_header=False, box=None, pad_edge=False)
    VSC_table.add_column("No.", style="green", width=2, justify="right")
    VSC_table.add_column("Option", style="cyan")

    if stored_commands:
        for i, opt in enumerate(stored_commands, start=1):
            VSC_table.add_row(str(i)+")", opt)
    else:
        VSC_table.add_row("", "[red](Directory is empty)[/red]")

    # "Menu Options" column
    MO_table = Table(show_header=False, box=None, pad_edge=False)
    MO_table.add_column("Option")
    MO_table.add_row("[green]a)[/green] add")
    MO_table.add_row("[green]e)[/green] edit")
    MO_table.add_row("[green]d)[/green] delete")
    MO_table.add_row("[green]q)[/green] quit")

    # Panels inside of main box
    columns = Columns(
        [
            Panel(VSC_table, title="View Saved Commands", padding=(1,4)), # Don't set to white bc of light theme
            Panel(MO_table, title="Menu Options", padding=(1,4)),
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

### Renders the content of a command file, including command numbering, commands, and comments
def command_file_content(text, cmd_path, f1, f2):
    cmd_num = 0
    if cmd_path.stat().st_size != 0:
        previous_line = " "
        for line in f2:
            # If line is not blank, no else statement so ignoring all blank lines
            if line.strip():
                # If reading the info text
                if line[0] == "#":
                    info = line[1:].strip()
                    text.append(info+"\n\n", style="italic")
                # If reading the command text
                else:
                    # If two commands next to each other, no space in between them
                    if previous_line[0] != "#" and previous_line != " ":
                        text.append("\n")
                    cmd_num += 1
                    number = "["+str(cmd_num)+"]"
                    f1.write("%d\n" % cmd_num)
                    f1.write(line + "\n")
                    command = line.rstrip()
                    text.append(number, style="yellow")
                    text.append(" ")
                    text.append(command+"\n", style="cyan")
                previous_line = line
        return previous_line
    else:
        text.append("(File is empty)\n\n", style="red")

### Renders the structure of the command file, including main file outline box, and back option
def command_file_structure(console, text, cmd_path, previous_line, selected_cmd_file):
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
            title="[bold]"+selected_cmd_file+"[/bold]",
            border_style="green",
        )
    )