"""
Modulen menu.py skall enbart innehålla kod för att visa menyn.

Menyvalet menu ska skriva ut menyn och vilka val man kan göra.
"""

import analyzer


def menu():
    """
    Menyn för programmet
    """
    filename = "phil.txt"

    while True:
        print("Make a choice: \n")
        print("  lines:")
        print("  words:")
        print("  letters:")
        print("  word_frequency:")
        print("  letter_frequency:")

        print("\n")

        choice = input("--> ")

        if choice == "q":
            print("Bye!")
            break

        elif choice == "lines":
            print(analyzer.lines(filename))

        elif choice == "words":
            print(analyzer.words(filename))


        elif choice == "letters":
            print(analyzer.letters(filename))


        elif choice == "word_frequency":
            analyzer.word_frequency(filename)

        elif choice == "letter_frequency":
            analyzer.letter_frequency(filename)

        elif choice == "all":
            print(analyzer.lines(filename))
            print(analyzer.words(filename))
            print(analyzer.letters(filename))
            analyzer.word_frequency(filename)
            analyzer.letter_frequency(filename)

        elif choice == "change":
            filename = input("Enter filename: ")

        elif choice == "test":
            filename = "lorum.txt"
            print(analyzer.get_words(filename))


        else:
            ("You didnt enter a valid choice")

        input("\n Press enter to continue...")
