"""
Functions for the analyzer
"""
import analyzer

textfile = "phil.txt"

def menuchoices():
    """
    Choices for the menu
    """
    print(chr(27) + "[2J" + chr(27) + "[;H")
    print("Welcome!")
    print("This is the menu for the analyzing program:")
    print(f"The chosen text file is: {textfile}")
    print("letters) Number of letters in your chosen text file")
    print("words) Number of words in your chosen text file")
    print("lines) Number of lines in your chosen text file")
    print("word_frequency) Shows the frequency of words in your chosen text file")
    print("letter_frequency) Shows the frequency of letters in your chosen text file")
    print("all) Shows the analysis of everything")
    print("change) Changes the text file that the program is analyzing")
    print("q) Quit.")

def quit_program():
    """
    Quit
    """
    print("The program will now quit.")

def wrongchoice():
    """
    Wrong choice
    """
    print("Invalid choice. You can only choose from the menu.")

def frequency(choice):
    """
    Text analyzer
    """
    print(analyzer.textanalyzer(choice))

def word_frequency(choice):
    """
    Word frequency
    """
    print(analyzer.word_frequency(choice))

def all_analysis():
    """
    All of the analysis
    """
    analyzer.totalanalyzer()

def change():
    """
    Change text file
    """
    return analyzer.change()
    
