"""
Module Docstring
"""
import analyzer

def menyval(doc):
    """
    Menu for giving all the options!
    """
    print("Menyval lines")
    print("Menyval words")
    print("Menyval letters")
    print("Menyval word_frequency")
    print("Menyval letter_frequency")
    print("Menyval all")
    print("Menyval cjhange")
    print("q for quit")
    choice = input("välj ditt val!: ")
    if choice == "lines":
        doc = analyzer.lines_checker(doc)
    elif choice == "words":
        doc = analyzer.words_checker(doc)
    elif choice == "letters":
        doc = analyzer.char_checker(doc)
    elif choice == "word_frequency":
        doc = analyzer.word_frequency(doc)
    elif choice == "letter_frequency":
        doc = analyzer.letter_frequency(doc)
    elif choice == "all":
        doc = analyzer.alles(doc)
    elif choice == "change":
        a = input("filnamn")
        doc = analyzer.changer_phile(a)
    elif choice == "q":
        return False
    return doc
