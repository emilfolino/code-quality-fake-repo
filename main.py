#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Text analyzer
"""

import menu
import analyzer

def main():
    """The main function"""

    file_name = "phil.txt"
    file_string = analyzer.read_file_string(file_name).lower()
    limit = 7
    quit_main_loop = False
    menu_choice = ""

    while not quit_main_loop:

        analyzer.clear_terminal()
        menu.display(file_name)

        if menu_choice.lower() == "q":
            quit_main_loop = True
            analyzer.clear_terminal()
            print("Goodbye!")
            continue

        if menu_choice.lower() in ["lines", "words", "letters"]:
            counter = getattr(analyzer, f"count_{menu_choice}")(file_string)
            menu.display(file_name)
            print(f"{file_name} has {counter} {menu_choice}.")

        elif menu_choice.lower() == "word_frequency":
            print(analyzer.word_frequency(file_string, limit))

        elif menu_choice.lower() == "letter_frequency":
            print(analyzer.letter_frequency(file_string, limit))

        elif menu_choice.lower() == "all":
            print(analyzer.do_all(file_string, limit))

        elif menu_choice.lower() == "change":
            file_name = analyzer.change_file(file_name)
            file_string = analyzer.read_file_string(file_name).lower()

        else:
            choice_message = "Make your choice"

        menu_choice = analyzer.get_input(choice_message)
        choice_message = "\n What do you want to do now?"

if __name__ == "__main__":
    main()
