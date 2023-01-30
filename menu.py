"""This is the menu module for analyzer. It displays the menu and choises for the user."""
import analyzer

txt = """
Hello and welcome to word analyzer!
We are here for all your analytical needs!

Please choose from the menu below:
words - returns the amount of words in the file
letter -  returns the amount of letters in the file
lines - returns the amount of lines in the file
word_frequency - returns the seven most common words in the file.
letter_frequency - returns the seven most common letter in the file.
all -  returns all of the info from choises above
change - change which file to analyze
q - Exit the program
menu - show this text
"""

def menu(state):
    """This is the menu function, it prints a menu and takes the user input"""

    usr_choice = input('--> ')

    if usr_choice == 'q':
        state = False
    elif usr_choice != 'menu':
        analyzer.function_call(usr_choice)
    else:
        print(txt)
    return state
