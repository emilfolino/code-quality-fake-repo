#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Marvin with a simple menu to start up with.
    Marvin doesnt do anything, just presents a menu with some choices.
    You should add functinoality to Marvin.
"""

import marvin
import inventory
import emission_functions



def main ():
    """
    Its an eternal loop, until q is pressed.
    It should check the choice done by the user and call a appropriate
    function.
    """

    marvin_image = r"""
        /\___/\
       (  o o  )
       /   *   \
       \__\_/__/ meow!
         /   \
        / ___ \
        \/___\/
    """

    marvin_backpack = []

    while True:
        print(chr(27) + "[2J" + chr(27) + "[;H")
        print(marvin_image)
        print("Hi, I'm a cat. I know it all. What can I do you for?")
        print("1) Present yourself to the cat.")
        print("2) Let the cat convert celsius to fahrenheit.")
        print("3) Make the cat repeat a word.")
        print("4) Make the cat calculate the sum of a series of numbers and their average")
        print("5) Let the cat make a word longer")
        print("6) Ask the cat to check if a word is an isogram")
        print("7) Play 'smaller or larger' numbers game with the cat")
        print("8) Randomize a word")
        print("9) Get acronym")
        print("10) Mask all characters except the last four in a string")
        print("11) Find substring in a string")
        print("12) Search for a country in emission data")
        print("13) Find the difference in emissions for a country between two years")
        print("14) Print emission data for a country")
        print("b1) Calculate your grade")
        print("b2) Compare strings")
        print("q) Quit.")

        print("Try out my 'inv' commands!")
        choice = input("--> ")

        if choice == "q":
            print("Bye, bye - and welcome back anytime!")
            break

        elif choice == "1":
            marvin.greet()

        elif choice == "2":
            marvin.celcius_to_farenheit()

        elif choice == "3":
            string = input("Please enter a word: ")
            number = input("How many times do you want the cat to repeat the word? ")
            print(marvin.multiply_str(string, number))

        elif choice == '4':
            marvin.sum_and_average()

        elif choice == '5':
            marvin.hyphen_string()

        elif choice == '6':
            marvin.is_isogram()

        elif choice == '7':
            marvin.compare_numbers()
        elif choice == '8':
            string = input("Enter a string to randomize: ")
            print(marvin.randomize_string(string))
        elif choice == '9':
            string = input("Enter a word to create an acronym: ")
            print(marvin.get_acronym(string))
        elif choice == '10':
            string = input("Enter a string to mask: ")
            print(marvin.mask_string(string))
        elif choice == '11':
            string = input("Enter a string: ")
            sub_string = input("Enter a substring: ")
            print(marvin.find_all_indexes(string, sub_string))
        elif choice == 'b1':
            max_score = input("Enter the max score: ")
            score = input("Enter your score")
            print(marvin.points_to_grade(max_score, score))
        elif choice == 'b2':
            string1 = input("Enter first string: ")
            string2 = input("Enter second string: ")
            string3 = input("Enter third string: ")
            string4 = input("Enter forth string: ")
            print(marvin.has_strings(string1, string2, string3, string4))

        elif ("inv pick") in choice:
            command = choice.split(" ")
            item = command[2]

            try:
                item_index = command[3]
            except IndexError:
                item_index = ""

            inventory.pick(marvin_backpack, item, item_index)

        elif ("inv drop") in choice:
            command = choice.split(" ")
            item = command[2]
            inventory.drop(marvin_backpack, item)

        elif ("inv swap") in choice:
            command = choice.split(" ")
            if len(command) == 4:
                item1 = command[2]
                item2 = command[3]
            else:
                "Error! Items don't exist in Marvins backpack"
            inventory.swap(marvin_backpack, item1, item2)

        elif 'inv' in choice:
            command = choice.split(" ")
            try:
                start = int(command[1])
                stop = int(command[2])
                inventory.inventory(marvin_backpack, start, stop)
            except IndexError:
                inventory.inventory(marvin_backpack)

        elif choice == "12":
            search_word = input("Enter a search term: ")
            try:
                print(emission_functions.search_country(search_word))
            except ValueError:
                print("Country does not exist!")

        elif choice == "13":
            usr_input = input("Enter a country and years you want to compare: ")
            country, year1, year2 = usr_input.split(",")

            try:
                # emission_functions.get_country_change_for_years(country, year1, year2)
                print(f"{country}:{emission_functions.get_country_change_for_years(country, year1, year2)}%")

            except ValueError:
                print("Wrong year!")

        elif choice == "14":
            country_name = input("Enter a country: ")
            emission_functions.print_country_data(emission_functions.get_country_data(country_name))
        else:
            print("That is not a valid choice. You can only choose from the menu.")

        input("\nPress enter to continue...")


if __name__ == "__main__" :
    main()
