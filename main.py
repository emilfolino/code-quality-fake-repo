"""
A simple text analyzer program
"""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import menu
import analyzer

def main():
    """
    Its an eternal loop, until q is pressed.
    It should check the choice done by the user and call a appropriate
    function.
    """
    filename = "phil.txt"

    while True:
        menu.show_meny()

        choice = input("--> ")


        if choice == "q":
            print("Bye, bye!")
            break

        elif choice == "lines":
            print(analyzer.count_lines(filename))

        elif choice== "words":
            print(analyzer.count_words(filename))

        elif choice == "letters":
            print(analyzer.count_letters(filename))

        elif choice== "letter_frequency":
            answer_letter= analyzer.letter_frequency(filename)
            for key, value in answer_letter:
                print(f"{key}: {value[0]} | {value[1]}%")


        elif choice== "word_frequency":
            answer= analyzer.word_frequency(filename)

            for key, value in answer:
                print(f"{key}: {value[0]} | {value[1]}%")


        elif choice== "all":
            answer_all = analyzer.all_functions(filename)
            for key, value in answer_all.items():
                print(value)


        elif choice == "change":
            filename = input("Enter the name of the new file: ")


        else:
            print()
            print("Wrong! You can only choose from the menu!")

        input("\nPress enter to continue...")






if __name__ == "__main__":
    main()
