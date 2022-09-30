#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Marvin with a simple menu to start up with.
Marvin doesnt do anything, just presents a menu with some choices.
You should add functinoality to Marvin.
"""
import inventory
import marvin
import emission_functions

def main():
    """main"""
    backpack = []
    choice = ""
    while choice != "q":
        print(chr(27) + "[2J" + chr(27) + "[;H")
        print(marvin.marvin_image())
        print("Hi, I'm Marvin. How can i help you?")
        print("1) Present yourself to Marvin.")
        print("2) Convert celsius to fahrenheit.")
        print("3) Word multiplier.")
        print("4) Sum and average calculator.")
        print("5) Wordletter adder multiplicator.")
        print("6) Isogram checker.")
        print("7) Smaller/larger checker.")
        print("a1) Matching string comparator")
        print("a2) Double match tester")
        print("a3) Tab shortener")
        print("a4) Name combiner")
        print("a5) Point calculator")
        print("8) Randomize string")
        print("9) Acronymize")
        print("10) Mask string")
        print("11) Find all indexes")
        print("b1) Find out your grade")
        print("b2) Check string for things")
        print("12) Country search")
        print("13) Country emission change")
        print("14) Country data print")
        print("inv commands : pick, drop, swap")

        print("q) Quit.")

        choice = input("--> ")
        choice = choice.lower()
        if choice == "q":
            print("Bye, bye - and welcome back anytime!")
        elif choice == "1":
            marvin.greet()
        elif choice == "2":
            marvin.celcius_to_farenheit()
        elif choice == "3":
            marvin.word_manipulation()
        elif choice == "4":
            marvin.sum_and_average()
        elif choice == "5":
            marvin.hyphen_string()
        elif choice == "6":
            marvin.is_isogram()
        elif choice == "7":
            marvin.compare_numbers()
        elif choice == "a1":
            marvin.string_compare_menu()
        elif choice == "a2":
            marvin.all_numbers_menu()
        elif choice == "a3":
            marvin.tab_shortener_menu()
        elif choice == "a4":
            marvin.word_combiner_menu()
        elif choice == "a5":
            marvin.point_calculator_menu()
        elif choice == "8":
            cli_input = input("Enter string to randomize: ")
            new_string = marvin.randomize_string(cli_input)
            print(new_string)
        elif choice == "9":
            cli_input = input("Enter string to acronymize: ")
            print(marvin.get_acronym(cli_input))
        elif choice == "10":
            cli_input = input("Enter string to mask: ")
            print(marvin.mask_string(cli_input))
        elif choice == "11":
            cli_input = input("Enter string to search: ")
            cli_key = input("Enter what to search for: ")
            print(marvin.find_all_indexes(cli_input, cli_key))
        elif choice == "b1":
            cli_input = int(input("Enter max points: "))
            cli_input2 = int(input("Enter your points: "))
            print("score: " + marvin.points_to_grade(cli_input, cli_input2))
        elif choice == "b2":
            full_string = input("Enter your fullstring: ")
            start_string = input("Enter your start string: ")
            contains_string = input("Enter your containing string: ")
            end_string = input("Enter your end string: ")
            print(marvin.has_strings(full_string, start_string, contains_string, end_string))
        elif choice.startswith("inv"):
            backpack = inventory.parse_command(backpack, choice)
        elif choice == "12":
            emission_functions.handle_search()
        elif choice == "13":
            emission_functions.handle_country_change()
        elif choice == "14":
            emission_functions.handle_country_data()
        else:
            print("That is not a valid choice. You can only choose from the menu.")
        if(choice != "q"):
            input("Press enter to continue")
if __name__ == "__main__":
    main()
