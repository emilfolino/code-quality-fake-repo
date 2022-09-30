#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""This is the main program for the amazing marvin"""

import inventory
import marvin
import emission_functions

backpack = []

def main():
    """
    Marvin with a simple menu to start up with.
    Marvin doesnt do anything, just presents a menu with some choices.
    You should add functinoality to Marvin.
    """

    marvin_image = r"""
            __
    _(\    |@@|
    (__/\__ \--/ __
    \___|----|  |   __
        \ }{ /\ )_ / _\
        /\__/\ \__O (__
        (--/\--)    \__/
        _)(  )(_
        `---''---`
    """

    """
    Its an eternal loop, until q is pressed.
    It should check the choice done by the user and call a appropriate
    function.
    """
    while True:
        print(chr(27) + "[2J" + chr(27) + "[;H")
        print(marvin_image)
        print("Greetings human, I am Colossus. How may I be of service to you?")
        print("1) Present yourself to Colossus.")
        print("2) Convert Celsius to Fahrenheit.")
        print("3) Multiply words.")
        print("4) Add numbers together and display sum and average.")
        print("5) Make funny words.")
        print("6) Check if word is an isogram.")
        print("7) Check if number is large or smaller.")
        print("8) Randomize string.")
        print("9) Make acronym.")
        print("10) Mask string.")
        print("11) Find all indexes.")
        print("12) Search for country.")
        print("13) Compare emission for country between two years")
        print("14) Print all emission data for a country.")
        print("q) Quit.")

        choice = input("--> ")

        if choice == "q":
            print("Bye, bye - and welcome back anytime!")
            break

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

        elif choice == "8":
            word = input("Enter a word: ")
            print(marvin.randomize_string(word))

        elif choice == "9":
            word = input("Enter a word: ")
            print(marvin.get_acronym(word))

        elif choice == "10":
            word = input("Enter a word: ")
            print(marvin.mask_string(word))

        elif choice == "11":
            word = input("Enter a word: ")
            part_of_word = input("Enter a word: ")
            print(marvin.find_all_indexes(word, part_of_word))

        elif choice[0:8] == "inv pick":
            choice_list = choice.split(" ")
            try:
                item = choice_list[2]  
                try:
                    index = int(choice_list[3])
                    inventory.pick(backpack, item, index)  
                except ValueError:
                    index = int(len(backpack))
                    print("Incorrect index specified, using default value.")
                    inventory.pick(backpack, item, index)
                except IndexError:
                    index = int(len(backpack))
                    print("No index specified, using default value.")
                    inventory.pick(backpack, item, index)
            except IndexError:
                print("Error: Enter an item.")
        
        elif choice[0:3] == "inv" and int(len(choice) <= 3):
            inventory.inventory(backpack)
        
        elif choice[0:8] == "inv drop":
            choice_list = choice.split(" ")
            try:
                item = choice_list[2]
            except (IndexError, ValueError):
                print("Error: " + item + " does not exist.")
                break
            inventory.drop(backpack, item)

        elif choice[0:8] == "inv swap":
            choice_list = choice.split(" ")
            item1 = choice_list[2]  
            item2 = choice_list[3]  
            inventory.swap(backpack, item1, item2)

        elif choice == "12":
            word = input("Enter a country: ")
            try:
                print(emission_functions.search_country(word))
            except ValueError:
                print("Country does not exist!")

        elif choice == "13":
            user_input = input("Enter a country followed by two years: ")
            user_input_list = user_input.split(",")
            country = user_input_list[0]
            first_year_comparison = user_input_list[1]
            second_year_comparison = user_input_list[2]
            try:
                print(country + ":" + str(emission_functions.get_country_change_for_years
                (country, first_year_comparison, second_year_comparison)) + "%")
            except ValueError:
                print("Wrong year!")

        elif choice == "14":
            user_input = input("Enter a country: ")
            emission_functions.print_country_data(emission_functions.get_country_data(user_input))

        else:
            print("That is not a valid choice. You can only choose from the menu.")

        input("\nPress enter to continue...")

if __name__ == "__main__":
    main()
