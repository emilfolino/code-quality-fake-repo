#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
main dokument
"""


import emission_functions
import marvin
import inventory


def main():
    """
    Its an eternal loop, until q is pressed.
    It should check the choice done by the user and call a appropriate
    function.
    """
    backpack = []
    
    marvin_image = r"""
               _..._
             .'     '.
            /`\     /`\    |\
           (__|     |__)|\  \\  /|
           (     "     ) \\ || //
            \         /   \\||//
             \   _   /  |\|`  /
              '.___.'   \____/
               (___)    (___)
             /`     `\  / /
            |         \/ /
            | |     |\  /
            | |     | "`
            | |     |
            | |     |
            |_|_____|
           (___)_____)
           /    \   |
          /   |\|   |
         //||\\  Y  |
        || || \\ |  |
        |/ \\ |\||  |
            \||__|__|
            (___|___)
             /   A   \
            /   / \   \
           \___/   \___/
                """
    while True:
        print(chr(27) + "[2J" + chr(27) + "[;H")
        print(marvin_image)
        print("Hi, I'm Azan and I come from a planet in another galaxy far away. I know it all, test me.")
        print("1) Present yourself to Azan.")
        print("2) Celsius till Fahrenheit.")
        print("3) Multiply words.")
        print("4) Sum and average.")
        print("5) Magic with words.")
        print("6) Isogram.")
        print("7) Is it smaller, bigger or equal?")
        print("8) Randomize String.")
        print("9) Get acronym.")
        print("10) Mask String.")
        print("11) Find all indexes.")
        print("12) Search country.")
        print("13) Show emission change for country.")
        print("14) Show all data for a country.")
        print("q) Quit.")
        print("")
        print("What do you want to do?")
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
            string1 = input("Enter a string to randomize: ")
            print(marvin.randomize_string(string1))
            print("\nAzan says:")
            print("Wanna see what else I can do?!")

        elif choice == "9":
            new_word = input("Enter a sentence with both upper and lower letters: ")
            print(marvin.get_acronym(new_word))
            print("\nAzan says:\n")
            print("Wanna see what else I can do?!")
        
        elif choice == "10":    
            result = input("Enter a string: ")
            print(marvin.mask_string(result))
            print("\nAzan says:\n")
            print("Wanna see what else I can do?!")


        elif choice == "11":
            string = input("Enter a string: ")
            letter = input("Enter a letter: ")
            print(marvin.find_all_indexes(string, letter))
            print("\nAzan says:\n")
            print("Wanna see what else I can do?!")
        
        elif choice == "12":
            search_word = input("Enter country name or a part of country name to see if it exists: ")
            try:
                country = emission_functions.search_country(search_word)
                string_countries = ", ".join(country)
                print("Following countries were found: %s" % string_countries)
            except ValueError:
                print("Country does not exist!")


        elif choice == "13":
            emission_change = input("Enter country and two different years with a comma between: ")
            try:
                list_inp = emission_change.split(",")
                country_name = list_inp[0]
                year1 = list_inp[1]
                year2 = list_inp[2]
                country_cal = emission_functions.get_country_change_for_years(country_name, year1, year2)
                print("{}:{}%".format(country_name, country_cal))
            except ValueError:
                print("Wrong year!")

        elif choice == "14":
            country_name = input("Enter a country:n ")
            try:
                data = emission_functions.get_country_data(country_name)
                print(emission_functions.print_country_data(data))
            except ValueError:
                print("You must write a country")

        elif "inv pick" in choice:
            list1 = choice.split(" ")
            item = list1[2]
            print(inventory.pick(backpack, item, index = -1))
        
        elif "inv drop" in choice:
            list1 = choice.split(" ")
            item = list1[2]
            print(inventory.drop(backpack, item))
        
        elif "inv swap" in choice:
            list1 = choice.split(" ")
            item1 = list1[2]
            item2 = list1[3]
            print(inventory.swap(backpack, item1, item2))
        
        elif "inv" in choice:
            print(inventory.inventory(backpack))

        else:
            print("That is not a valid choice. You can only choose from the menu.")
        input("\nPress enter to continue...")


if __name__ == "__main__":
    print(main())
