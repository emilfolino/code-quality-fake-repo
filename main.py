"""This is main.py, from here the program starts"""
import menu

def main():
    """This is the main part of the program"""
    state = True
    while state is True:
        state = menu.menu(state)



if __name__ == "__main__":
    main()
