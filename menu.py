"""Menu function for the analyzer program."""

def menu():
    '''Prints out the menu and returns the input.'''
    print("Welcome to the text analyzer. Enter an option. Enter 'q' to quit.")
    print("- lines")
    print("- words")
    print("- letters")
    print("- word_frequency")
    print("- letter_frequency")
    print("- all")
    print("- change")
    return input("What would you like to do?")
