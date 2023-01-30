#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
The main file of marvin bot
"""

import marvin
import inventory



def main():
    """
    Get users input and response depending on the input
    """
    backpak = []

    while True:
        marvin.welcome()

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
            inputText = input("input: ")
            randomText = marvin.randomize_string(inputText)
            print(randomText)

        elif choice == "9":
            inputText = input("input: ")
            print(marvin.get_acronym(inputText))

        elif choice == "10":
            inputText = input("input: ")
            print(marvin.mask_string(inputText))
        elif choice == "11":
            inputText = input("text: ")
            inputSearchValue = input("sub text you want to search for: ")
            print(marvin.find_all_indexes(inputText, inputSearchValue))
        elif choice == "12":
            inputText = input("Search: ")
            marvin.searchForCountry(inputText)
        elif choice == "13":
            print("Write in this format => Country,year1,year2")
            inputText = input("Enter: ")
            marvin.calculatePercentageEmissionDifference(inputText)
        elif choice == "14":
            inputText = input("Country name: ")
            marvin.showAllDataForCountry(inputText)
        elif choice.find('inv') == 0:
            backpak = inventory.manageInvCommands(choice,backpak)
        else:
            print("That is not a valid choice. You can only choose from the menu.")

        input("\nPress enter to continue...")


if __name__ == "__main__":
    main()
