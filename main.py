#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Marvin is a chatbot that does different tasks depending on want the user want it to do.
"""
import marvin
import inventory
import emission_functions
marvin_image = r"""
 __         _           _         __
( '\___      \_  (^)  _/      ___/' )
 \ , ' \____   \ / \ /   ____/ ' , /
  \__ ' , ' \___{~V~}___/ ' , ' __/
 ____\_________ {<!>} _________/____
/ , ' , ' , ' ,`{<!>}~, ' , ' , ' , \
\_____________ /{<!>}\______________/
                 \./
                 (~)
                 (~)
                 (~)
                 (~)
                 (~)
                 (~)
                 ,0,
                  "
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
        print("2) Celsius to fahrenheit converter.")
        print("3) Let's play parrot!")
        print("4) Want me to do some math?")
        print("5) Repeat letter in word.")
        print("6) Isogram check")
        print("7) Bigger, smaller or equal?")
        print("8) Shuffle a word.")
        print("9) Make acronym.")
        print("10) Mask characters in string.")
        print("11) Find all indexes of substring in a string.")
        print("12) Search for country.")
        print("13) Show emission change for a country.")
        print("14) Show all data for a country.")
        print("q) Quit.")
        print("")
        print("Try out my 'inv' commands")
        print("---------")

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
            original_string = input("Enter a string to randomize: ")
            print(marvin.randomize_string(original_string))
            
        elif choice == "9":
            string = input("Enter a string and I will turn it into a acronym: ")
            print(marvin.get_acronym(string))
            
        elif choice == "10":
            string = input("Enter a string and I will mask all characters except the last four: ")
            print(marvin.mask_string(string))
            
        elif choice == "11":
            string = input("Enter a string: ")
            substring = input("Now enter a substring and I will find it's indexes in the original string: ")
            print(marvin.find_all_indexes(string, substring))

        elif choice == "12":
            string = input("Enter a country name or a part of a country name to se if it exists: ")
            try:
                result = ", ".join(emission_functions.search_country(string))
                print(f"Following countries were found: {result}")
            except ValueError:
                print("Country does not exist!")
            
        elif choice == "13":
            inp = input("Enter a country and two different years (country,year1,year2): ")
            inp_lst = inp.split(",")
            try:
                result = emission_functions.get_country_change_for_years(inp_lst[0], inp_lst[1], inp_lst[2])
                print(f"{inp_lst[0]}:{result}%")
            except ValueError:
                print("Wrong year!")
            
        elif choice == "14":
            inp = input("Enter the name of a country: ")
            data = emission_functions.get_country_data(inp)
            emission_functions.print_country_data(data)

        elif choice == "inv":
            inventory.inventory(bag)
        
        elif "inv pick" in choice:
            choice_split = choice.split()
            if len(choice_split) == 4:
                bag = inventory.pick(bag, choice_split[2], int(choice_split[3]))
            else:
                bag = inventory.pick(bag, choice_split[2])
        
        elif "inv drop" in choice:
            choice_split = choice.split()
            bag = inventory.drop(bag, choice_split[2])

        elif "inv swap" in choice:
            choice_split = choice.split()
            bag = inventory.swap(bag, choice_split[2], choice_split[3])

        else:
            print("That is not a valid choice. You can only choose from the menu.")

        input("\nPress enter to continue...")

if __name__ == "__main__":
    main()
