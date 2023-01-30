"""
Contains code providing a visualisation of the menu.
"""
def choice():
    """
    This is where all the menu-choices are printed.
    The users choice is also returned here so it can be used in main.py.
    """
    print("""
lines) Analyze the amount of lines (empty lines not included)
words) Analyze the amount of words
letters) Analyze the amount of letters
word_frequency) prints the 7 most frequented words in file
letter_frequency) prints the 7 most frequented letters in file
all) prints all the results from commands above
change) changes which file commands run on
    """
    )
    return input("Choice: ")

if __name__ == "__main__":
    pass
