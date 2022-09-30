"""
Text analyzer
"""
import menu

def main():
    """
    loops until user types q
    """
    result = 0
    while True:
        command = input("> ")
        result = menu.resovleActionFromCommand(command.lower())
        if result == -1:
            break
        if result == 0:
            print("Command not recognized! Type 'menu' to see the command list.")


if __name__ == "__main__":
    main()
