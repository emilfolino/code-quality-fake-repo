"""
This contains only the menu function
"""

def menu():
    """
    A menu function that takes one input
    """
    print(chr(27) + "[2J" + chr(27) + "[;H")
    print( 
    """
 Pick an option to execute

 lines) Count the lines in your file
 words) Count the words in your file
 letters) Count the letters in your file
 word_frequency) Prints word frequency in your file
 letter_frequency) Prints letter frequency in your file
 all) Prints all the information you need
 change) Change file

 -'q' to quit-

    """
    )
    read_choice = input(" Option: ")
    return read_choice
