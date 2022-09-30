#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Main program.
"""
import marvin
import inventory
import emission_functions
"""
Importing module marvin and inventory.
"""

def main():
    """
    Function for main program that holds the while loop/menu options.
    """
    kevin_image = r"""
                                   ___-------___
                               _-~~             ~~-_
                            _-~                    /~-_
         /^\__/^\         /~  \                   /    \
       /|  O|| O|        /      \_______________/        \
       | |___||__|      /       /                \          \
       |          \    /      /                    \          \
       |   (_______) /______/                        \_________ \
        |         / /         \                      /            \
          \         \^\         \                  /               \     /
           \         ||           \______________/      _-_       //\__//
             \       ||------_-~~-_ ------------- \ --/~   ~\    || __/
               ~-----||====/~     |==================|       |/~~~~~
               (_(__/  ./     /                    \_\      \.
                      (_(___/                         \_____)_)-jurcy


    """

    """
    Its an eternal loop, until q is pressed.
    It should check the choice done by the user and call a appropriate
    function.

    All functions are called within the if/elif statements depending on which
    choice the user selects in the menu.
    """
    bag = []

    while True:
        print(chr(27) + "[2J" + chr(27) + "[;H")
        print(kevin_image)
        print("Hi, my name is Kevin the magic turtle.")
        print("\n1) Please present yourself to the magic turtle.")
        print("2) Celsius to Fahrenheit.")
        print("3) Let's play parrot! You write a word and I'll repeat it!")
        print("4) Math time!")
        print("5) Repeating letters in a word.")
        print("6) Check if word is isogram.")
        print("7) Larger, smaller or the same?")
        print("8) Randomize a word or sentence.")
        print("9) I will make an acronym for you!")
        print("10) I can hide parts of your string.")
        print("11) Find all indexes.")
        print("12) Search for country.")
        print("13) Show emission change for a country.")
        print("14) Show all data for a country.")
        print("q) Quit.")
        print("\n\nTry out Kevin's magical 'inv' commands!")
        print("\n***************************************")

        choice = input("\n--> ")

        if choice == "q":
            print("\nSee you soon!")
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
            string = input("\nEnter a string to randomize: ")
            print(marvin.randomize_string(string))

        elif choice == "9":
            string = input("\nGive me a string, I will make an acronym: ")
            print(marvin.get_acronym(string))

        elif choice == "10":
            string = input("\nEnter a string, I can make some of it disappear: ")
            print(marvin.mask_string(string))

        elif choice == "11":
            string1 = input("\nGive me a string, please: ")
            string2 = input("\nGive me a pattern to find in the string, please: ")
            print(marvin.find_all_indexes(string1, string2))

        elif choice == "12":
            search_word = input("\nEnter country name or part of country name to see if it exists: ")
            try:
                countries = emission_functions.search_country(search_word)
                print("\nThe following country/countries were found:\n" + "\n".join(countries))
            except ValueError:
                print("\nCountry does not exist!")

        elif choice == "13":
            string4 = input("\nEnter country, year and year: ")
            try:
                country, year1, year2 = string4.split(",")
                change = emission_functions.get_country_change_for_years(country, year1, year2)
                print(country + ":" + str(change) + "%")
            except ValueError:
                print("Wrong year!")

        elif choice == "14":
            country_name = input("\nEnter country: ")
            data = emission_functions.get_country_data(country_name)
            emission_functions.print_country_data(data)

        elif choice == "inv":
            inventory.inventory(bag)

        elif "inv pick" in choice:
            try:
                item, index = choice.split()[2], choice.split()[3]
                bag = inventory.pick(bag, item, index=index)
            except IndexError:
                item = choice.split()[2]
                bag = inventory.pick(bag, item)

        elif "inv drop" in choice:
            item = choice.split()[2]
            bag = inventory.drop(bag, item)

        elif "inv swap" in choice:
            item1, item2 = choice.split()[2], choice.split()[3]
            bag = inventory.swap(bag, item1, item2)

        else:
            print("That is not a valid choice. You can only choose from the menu.")

        input("\nPress enter to continue...")

if __name__ == "__main__":
    main()
