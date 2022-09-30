#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Main function and loop for analyzer"""

import menu
import analyzer as an

def main():
    """
    Main loop function, contains main loop, which brings the user into 
    the menu. Loop is broken when 'q' is pressed
    function.
    """
    filename = "phil.txt"

    menu.menu()

    while(True):
        user_input = input("Please choose a menu option\n-->")
        user_input = user_input.lower()

        if user_input == 'q':
            break

        elif user_input == 'menu':
            menu.menu()

        elif user_input == 'lines':
            try:
                an.count_lines(filename)
            except FileNotFoundError as e:
                print(str(e))

        elif user_input == 'words':
            try:
                an.count_words(filename)
            except FileNotFoundError as e:
                print(str(e))

        elif user_input == 'letters':
            try:
                an.count_letters(filename)
            except FileNotFoundError as e:
                print(str(e))

        elif user_input == 'word_frequency':
            try:
                an.word_frequency(filename)
            except FileNotFoundError as e:
                print(str(e))

        elif user_input == 'letter_frequency':
            try:
                an.letter_frequency(filename)
            except FileNotFoundError as e:
                print(str(e))

        elif user_input == "all":
            try:
                an.run_all(filename)
            except FileNotFoundError as e:
                print(str(e))

        elif user_input.startswith("change"):
            try:
                filename = an.change_filename()
            except FileNotFoundError as e:
                print(str(e))

        else:
            print("Error: invalid choice")

if __name__ == "__main__":
    main()
