import os.path
import sys
import time
from colorama import init, Fore
init(convert=True)


def trace(name: str = "Example Name", value: str = "Example Value"):
    print(colors["GRAY"] + "  └> " + colors["WHITE"] + name.capitalize() + colors["GRAY"] + ": " + colors["CYAN"] + value + colors["RESET"])


def error(type: str = "ExecutionError", note: str = "", line: int = None):
    print()
    print(colors["RED"] + "ERROR | Tracing: ")
    trace("Type", type)
    trace("Note", note)
    trace("File", os.path.basename(path))
    trace("Line", str(line))


colors = {
    "RED": Fore.RED,
    "GREEN": Fore.GREEN,
    "YELLOW": Fore.YELLOW,
    "BLUE": Fore.BLUE,
    "CYAN": Fore.CYAN,
    "WHITE": Fore.WHITE,
    "GRAY": Fore.LIGHTBLACK_EX,
    "BLACK": Fore.BLACK,
    "MAGENTA": Fore.MAGENTA,
    "RESET": Fore.RESET
}

args = sys.argv
path = args[1]
file = open(path, mode="rt")
file_content = file.readlines()
for line in file_content:
    # Remove newlines
    line = line.rstrip()
    # Assert colors to string.
    line = line.replace("${RED} ", colors["RED"])
    line = line.replace("${GREEN} ", colors["GREEN"])
    line = line.replace("${YELLOW} ", colors["YELLOW"])
    line = line.replace("${BLUE} ", colors["BLUE"])
    line = line.replace("${CYAN} ", colors["CYAN"])
    line = line.replace("${WHITE} ", colors["WHITE"])
    line = line.replace("${GRAY} ", colors["GRAY"])
    line = line.replace("${BLACK} ", colors["BLACK"])
    line = line.replace("${MAGENTA} ", colors["MAGENTA"])
    line = line.replace("${RESET} ", colors["RESET"])
    if line.startswith("//") or line == "":
        continue
    elif line.startswith("out "):
        print(line.removeprefix("out ") + colors["RESET"])
    elif line.startswith("wait "):
        time.sleep(float(line.removeprefix("wait ")))
    elif line.startswith("do "):
        try:
            exec(line.removeprefix("do "))
        except Exception as e:
            error(type="PythonError", note=str(e))
    elif line.startswith("error "):
        error(note=line.removeprefix("error "), line=file_content.index(line)+1)
    else:
        error(type="CommandNotFound", note="The command was not found.", line=file_content.index(line)+1)

print()
input(colors["GREEN"] + "Execution finished! Press enter to exit. ")
