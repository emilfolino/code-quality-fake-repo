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
marvin_image = r"""
              ,---------------------------,
              |  /---------------------\  |
              | |                       | |
              | |      Marvin           | |
              | |    computer of        | |
              | |     knowledge         | |
              | |                       | |
              |  \_____________________/  |
              |___________________________|
            ,---\_____     []     _______/------,
          /         /______________\           /|
        /___________________________________ /  | ___
        |                                   |   |    )
        |  _ _ _                 [-------]  |   |   (
        |  o o o                 [-------]  |  /    _)_
        |__________________________________ |/     /  /
    /-------------------------------------/|      ( )/
  /-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/ /
/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/ /
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
def main():
    """
    Its an eternal loop, until q is pressed.
    It should check the choice done by the user and call a appropriate
    function.
    """
    bag = []
    while True:
        print(chr(27) + "[2J" + chr(27) + "[;H")
        print(marvin_image)
        print("Hi, I'm Marvin. I know it all. What can I do you for?")
        print("1) Present yourself to Marvin.")
        print("2) Conversion of celsius to farenheit.")
        print("3) Word multiplication!")
        print("4) Summing up your numbers and give the avrage!")
        print("5) Ah at this choice i will make words long.")
        print("6) Check if your word is a isogram.")
        print("7) Will tell you the size comparison between numbers.")
        print("8) Will randomize a string for you.")
        print("9) I will create an acronym for you. ")
        print("10) Mask all but the last 4 in a string")
        print("11) Find all indexes")
        print("12) Search for country")
        print("13 Show emission change for a country")
        print("14 Show all data for a country")
        print("q) Quit.")

        choice = input("--> ")

        if choice == "q":
            print("Ah it would apear you have found the knowledge you were looking for, come back anytime.")
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
            string = input("Enter a string to randomize: ")
            marvin.randomize_string(string)
        
        elif choice == "9":
            string = input("Enter a string to make a acronym: ")
            marvin.get_acronym(string)

        elif choice == "10":
            string = input("Enter a string and I will mask all but the last 4: ")
            marvin.mask_string(string)

        elif choice == "11":
            string = input("Please enter a text so i can find index: ")
            find = input("Please enter the item you would like to find: ")
            marvin.find_all_indexes(string, find)
        
        elif choice == "12":
            search_word = input("Please enter the country or word you are looking for: ")
            try:
                emission_functions.search_country(search_word)
            except ValueError:
                print("Country does not exist!")
        
        elif choice == "13":
            userInput = input("type: country,year,year\n --> ")
            list1 = list(userInput.split(","))
            print(list1)
            try:
                emission_functions.get_country_change_for_years(list1[0], list1[1], list1[2])
                #emission_functions.get_country_change_for_years(list1[0])
            except ValueError:
                print("Wrong year!")
                
        
        elif choice == "14":
            userInput = input("type: country\n --> ")
            try:
                emission_functions.get_country_data(userInput)
            except ValueError:
                print("Wrong year!")

        elif "inv pick" in choice:
            index1 = choice.split(" ")
            if len(index1) == 4:
                inventory.pick(bag, index1[2], int(index1[3]))
            elif len(index1) == 3:
                inventory.pick(bag, index1[2])
            else:
                print(bag)

        elif "inv drop" in choice:
            command = choice.split(" ")
            try:
                item = command[2]
            except IndexError:
                item = None
            inventory.drop(bag, item)
            print(bag)

        elif "inv swap" in choice:
            try:
                command = choice.split(" ")
                print(command)
                item = command[2]
                item2 = command[3]
                inventory.swap(bag, item, item2)
            except (ValueError,IndexError):
                item = None
                item2 = None
                inventory.swap(bag, item, item2)
        
        elif "inv" in choice:
            inventory.inventory(bag)
    
        else:
            print("That is not a valid choice. You can only choose from the menu.")

        input("\nPress enter to continue...")

if __name__ == "__main__":
    main()
