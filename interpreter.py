import sys
import time
from colorama import init, Fore

init(convert=True)


def trace(name: str = "Name", value: str = "Value"):
    print(colors["GRAY"] + "  └" + colors["CYAN"] + "> " + colors["WHITE"] + name.capitalize() + colors["GRAY"] + ": " + colors["CYAN"] + value)


def error(type: str = "Undefined", line: int = None):
    print(colors["RED"] + "An error occurred while trying to run your Scrypt.")
    print(colors["RED"] + "Tracing: ")
    trace("Error", type)
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
    line = line.replace("${RED}", colors["RED"])
    line = line.replace("${GREEN}", colors["GREEN"])
    line = line.replace("${YELLOW}", colors["YELLOW"])
    line = line.replace("${BLUE}", colors["BLUE"])
    line = line.replace("${CYAN}", colors["CYAN"])
    line = line.replace("${WHITE}", colors["WHITE"])
    line = line.replace("${GRAY}", colors["GRAY"])
    line = line.replace("${BLACK}", colors["BLACK"])
    line = line.replace("${MAGENTA}", colors["MAGENTA"])
    line = line.replace("${RESET}", colors["RESET"])
    if line.startswith("//"):
        continue
    if line.startswith("out "):
        print("SCRYPT: " + line.removeprefix("out ") + colors["RESET"])
    if line.startswith("wait "):
        time.sleep(float(line.removeprefix("wait ")))
    else:
        error("CommandNotFound", )

input("Execution finished! Press enter to exit. ")
