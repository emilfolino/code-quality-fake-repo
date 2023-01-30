"""
A simple programm to print menu choices for our analyzer
"""
def menu_showcase():
    """
    A function to showcase all the meny choice for the analyzer
    """


    print(chr(27) + "[2J" + chr(27) + "[;H")
    print("""
lines) Count lines in a text 
words) Count words in a text
letters) Count letters in a text
word_frequency) Find 7 most used words in a text
letter_frequency) Find 7 most used letters in a text
all) Do all of the above
change) Change file that will represent the text
q) Quit
""")
