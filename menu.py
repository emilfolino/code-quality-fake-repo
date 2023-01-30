"""Dotline"""

# import os

def menu():
    """dotstring"""
    print("Make your choose\n")
    print("lines)            Count lines in file")
    print("words)            Count words in file")
    print("letters)          Count letters in file")
    print("word_frequency)   Show 7 most used words in file")
    print("letter_frequency) Show 7 most used letter in file")
    print("all)              Do everything")
    print("change)           Change file")
    print("q)                Quit program")

def invalidChoice():
    """dotstring"""
    print("Invalid choice try again")

def pressEnter():
    """dotstring"""
    input("Press enter to contine: ")

#def clearTerminal():
#    """dotstring"""
#    command = 'clear'
#    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
#        command = 'cls'
#    os.system(command)
