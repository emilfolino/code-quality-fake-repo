#!/usr/bin/env python3

"""
All the main code for the Marvin program.
Handles the users choice and calls the separate functions in the
marvin-file.
"""

import marvin
import inventory
import emission_functions

penguin_image = r"""
      .___.
     /     \
    | O _ O |
    /  \_/  \ 
  .' /     \ `.
 / _|       |_ \
(_/ |       | \_)
    \       /
   __\_>-<_/__
   ~;/     \;~
"""

backpack = []

def main():
    """A loop that runs the Marvin program"""
    global backpack
    while True:
        print(chr(27) + "[2J" + chr(27) + "[;H")
        print(penguin_image)
        print("Hi, I'm Penguin. I know it all. What can I do for you?")
        print("1) Present yourself to Penguin.")
        print("2) Convert Celsius to Fahrenheit.")
        print("3) Word repetition.")
        print("4) Calculate sum and average.")
        print("5) String manipulation.")
        print("6) Isogram check.")
        print("7) Number comparison.")
        print("8) Shuffle a word.")
        print("9) Create acronym.")
        print("10) Mask a string.")
        print("11) Find index in string.")
        print("12) Search for country.")
        print("13) Show emission change for a country.")
        print("14) Show data for a country.")
        print("a1) Word comparison.")
        print("a2) Multiplication until all numbers are included.")
        print("a3) Replace tabs with 3 spaces.")
        print("a4) Merge two names.")
        print("inv) Print out inventory.")
        print("inv pick) Pick up item and add it to the backpack.")
        print("inv swap) Swap places on two items in the backpack.")
        print("inv drop) Drop an item from the backpack.")
        print("*) Easter egg.")
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
            string = input("Enter a string to randomize: ")
            print(marvin.randomize_string(string))
        
        elif choice == "9":
            string = input("Enter a sentence which I will create "
                           "an acronym for: ")
            print(marvin.get_acronym(string))
        
        elif choice == "10":
            string = input("Input a string and I'll mask all "
                           "characters but the last four: ")
            print(marvin.mask_string(string))
        
        elif choice == "11":
            string1 = input("Input a string: ")
            string2 = input("Input another string: ")
            print(marvin.find_all_indexes(string1, string2))

        elif choice == "12":
            search_word = input("Input country name or a part of "
                                "it to see if it exists: ")
            try:
                countries = emission_functions.search_country(
                    search_word)
                print("Following countries were found:", countries)
            except ValueError:
                print("Country does not exist!")
        
        elif choice == "13":
            emission_to_check = input("Input country, the first "
                                      "year and the year to compare"
                                      " with: ")
            emission_to_check = emission_to_check.split(",")
            country, year1, year2 = emission_to_check[0:3]
            try:
                emission_change = emission_functions.\
                    get_country_change_for_years(
                    country, year1, year2)
                print(f"{country}:{emission_change}%")
            except ValueError as e:
                print(e)
        
        elif choice == "14":
            country = input("Input a country which you want the "
                            "data for: ")
            country_data = emission_functions.get_country_data(
                country)
            emission_functions.print_country_data(country_data)
        
        elif choice == "a1":
            marvin.word_comparison()
        
        elif choice == "a2":
            marvin.multiplication()
        
        elif choice == "a3":
            marvin.replace_tab()
        
        elif choice == "a4":
            marvin.merge_names()
        
        elif choice == "inv":
            inventory.inventory(backpack)

        elif choice.startswith("inv pick"):
            choice = choice.split(" ")
            item = choice[2]
            if len(choice) == 4:
                position = choice[3]
            else:
                position = ""
            backpack = inventory.pick(backpack, item, position)

        elif choice.startswith("inv swap"):
            choice = choice.split(" ")
            item1 = choice[2]
            item2 = choice[3]
            backpack = inventory.swap(backpack, item1, item2)

        elif choice.startswith("inv drop"):
            choice = choice.split(" ")
            item = choice[2]
            backpack = inventory.drop(backpack, item)
        
        elif choice == "*":
            joke = input("Would you like to hear a joke (y for yes)? ")
            while joke == "y":
                marvin.penguin_joke()
                joke = input("Would you like to hear another (y)? ")
        
        else:
            print("That is not a valid choice. You can only choose from the menu.")
    
        input("\nPress enter to continue...")

if __name__ == "__main__":
    main()
