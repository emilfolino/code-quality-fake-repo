"""
Loop for the program
"""
import menu


def main():
    """
    Loop
    """
    file = "phil.txt"
    while True:
        try:
            file = menu.menu(file)
        except ValueError:
            break


if __name__ == "__main__":
    main()
