#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
main module text analyzer
"""
import menu
import analyzer

def main():
    """main menu loop"""
    cli_input = "!q"
    current_file = "phil.txt"
    while cli_input != "q":
        print(chr(27) + "[2J")#clear screen
        print(menu.build_full_menu(current_file), end="")
        cli_input = input().lower()
        if cli_input == "menu":
            pass
        elif cli_input == "lines":
            analyzer.handle_line_count(current_file)
        elif cli_input == "words":
            analyzer.handle_word_count(current_file)
        elif cli_input == "letters":
            analyzer.handle_letter_count(current_file)
        elif cli_input == "word_frequency":
            analyzer.handle_word_fq(current_file)
        elif cli_input == "letter_frequency":
            analyzer.handle_letter_fq(current_file)
        elif cli_input == "all":
            analyzer.handle_all(current_file)
        elif cli_input == "change":
            current_file = analyzer.change_file(current_file)
        elif cli_input != "q":
            print("Invalid command")
        if cli_input != "q":
            input("Press enter to continue..")
    print("Thank you, come again..")


if __name__ == "__main__":
    main()
