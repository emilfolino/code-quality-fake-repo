#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Module containing main loop. Imports all the functions for the menu choices
"""
from marvin import get_acronym, greet, celcius_to_farenheit, randomize_string 
from marvin import sum_and_average, hyphen_string, is_isogram, compare_numbers, mask_string 
from marvin import find_all_indexes, word_manipulation
from inventory import pick, inventory, drop, swap
from emission_functions import search_country, get_country_change_for_years, get_country_data
from emission_functions import print_country_data

def main():
    """
    Marvin with a simple menu to start up with.
    Marvin doesnt do anything, just presents a menu with some choices.
    You should add functinoality to Marvin.
    """

    bag = []

    marvin_image = r"""
            ____
            \__/         $ $$
            `(  `^=_ p _$$__
            c   /  )  |   /
    _____- //^---~  _c  3
    /  ----^\ /^_\   / --,-
    (   |  |  O_| \\_/  ,/
    |   |  | / \|  `-- /
    (((G   |-----|
        //-----\\
        //       \\
    /   |     |  ^|
    |   |     |   |
    |____|    |____|
    /______)   (_____\
    """

    """
    Its an eternal loop, until q is pressed.
    It should check the choice done by the user and call a appropriate
    function.
    """

    while True:
        print(chr(27) + "[2J" + chr(27) + "[;H")
        print(marvin_image)
        print("Hi, I'm Popeye the silorman. What can I do you for?")
        print("1) Present yourself to Popeye.")
        print("2) Celsius to Frenheit.")
        print("3) Word manipulation.")
        print("4) Sum and average.")
        print("5) Destroy word.")
        print("6) Check if isogram.")
        print("7) Compare values.")
        print("8) Randomize string.")
        print("9) Get acronym.")
        print("10) Mask string.")
        print("11) Find all indexes.")
        print("12) Search for countries.")
        print("13) Check country emission change.")
        print("14) Get data from country.")
        print("q) Quit.")
        print("Try my inv-commands")

        choice = input("--> ")
        
        if choice == "q":
            print("Bye, bye - and welcome back anytime!")
            break

        # Not an empty command?
        elif choice == "":
            continue

        elif choice == "1":
            greet()

        elif choice == "2":
            celcius_to_farenheit()

        elif choice == "3":
            word_manipulation()

        elif choice == "4":
            sum_and_average()

        elif choice == "5":
            hyphen_string()

        elif choice == "6":
            is_isogram()

        elif choice == "7":
            compare_numbers()

        elif choice == "8":
            print("\nPopeye says:\n")
            string = input("Enter a string to randomize: ")
            print(randomize_string(string))

        elif choice == "9":
            print("\nPopeye says:\n")
            string = input("Enter a string to get acronym: ")
            print(get_acronym(string))

        elif choice == "10":
            print("\nPopeye says:\n")
            string = input("Enter a string to mask: ")
            print(mask_string(string))

        elif choice == "11":
            print("\nPopeye says:\n")
            string = input("Enter a string to search: ")
            search_string = input("Enter the search string: ")
            print(find_all_indexes(string, search_string))

        elif choice == "12":
            print("\nPopeye says:\n")
            string = input("Enter a string to search for countries: ")
            try:
                print(search_country(string))
            except ValueError as e:
                print(str(e))

        elif choice == "13":
            print("\nPopeye says:\n")
            string = input("Enter a string to find emission change: ")
            inputList = string.split(",")
            if len(inputList) == 3:
                inputCountry = inputList[0]
                inputYear1 = inputList[1]
                inputYear2 = inputList[2]
                try:
                    print(inputCountry + ":" + str(get_country_change_for_years(inputCountry, 
                                                                            inputYear1, 
                                                                            inputYear2)) + "%")
                except ValueError as e:
                    print(str(e))
            else:
                print("Wrong amount of inputs!")
        
        elif choice == "14":
            print("\nPopeye says:\n")
            string = input("Enter a country to get data: ")
            try:
                print_country_data(get_country_data(string))
            except ValueError as e:
                print(str(e))
 
        # Is an inventory command?
        elif choice.split()[0] == "inv":
            inv_command_list = choice.split()
            # Command not just "inv"?
            if len(inv_command_list) > 1:
                # second word in command is "pick"?
                if inv_command_list[1] == "pick":
                    # command is without index
                    if len(inv_command_list) == 3:
                        pick(bag, inv_command_list[2])
                    # command is with index
                    elif len(inv_command_list) == 4:
                        pick(bag, inv_command_list[2], inv_command_list[3])
                    # too many input words
                    else:
                        print("Not sure what you want, expected 3 or 4 words.")
                # second word in command is "drop"?
                elif inv_command_list[1] == "drop":
                    if len(inv_command_list) == 3:
                        drop(bag, inv_command_list[2])
                    else:
                        print("Not sure what you want, expected 3 words.")
                # second word in command is "swap"?
                elif inv_command_list[1] == "swap":
                    if len(inv_command_list) == 4:
                        swap(bag, inv_command_list[2], inv_command_list[3])
                    else: 
                        print("Not sure what you want, expected 4 words.")
                # not a valid function command.
                else:
                    print("Unknown command: " + inv_command_list[1])
            # command is only inv.
            else:
                inventory(bag)

        else:
            print("That is not a valid choice. You can only choose from the menu. Or the 'inv' commands")

        input("\nPress enter to continue...")


if __name__ == "__main__":
    main()
