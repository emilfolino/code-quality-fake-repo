'''main marvin file'''
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import marvin
import inventory
import emission_functions
"""
Marvin with a simple menu to start up with.
Marvin doesnt do anything, just presents a menu with some choices.
You should add functinoality to Marvin.
"""

marvin_image = r"""
      \_/
     (* *)
    __)#(__
   ( )...( )(_)
   || |_| ||//
>==() | | ()/
    _(___)_
   [-]   [-]
"""

def main():
    """
    Its an eternal loop, until q is pressed.
    It should check the choice done by the user and call a appropriate
    function.
    """

    backpack = []

    while True:
        print(chr(27) + "[2J" + chr(27) + "[;H")
        print(marvin_image)
        print("Hi, I'm Marvin. I know it all. What can I do you for?")
        print("1) Present yourself to Marvin.")
        print("2) Celsius to fahrenheit.")
        print("3) Word manipulation")
        print("4) Sum and Avarage")
        print("5) Hyphen string")
        print("6) Isogram")
        print("7) Compare numbers")
        print("8) Randomize word")
        print("9) Acronym")
        print("10) Mask word")
        print("11) Find all indexes")
        print("12) Search for country")
        print("13) Show emission change for a country")
        print("14) Display country data")
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
            word = input("Enter a string: ")
            print(marvin.mask_string(word))

        elif choice == "11":
            str1 = input("Enter a string: ")
            str2 = input("Enter another string: ")
            print(marvin.find_all_indexes(str1, str2))

        elif choice == "12":
            country = input("Enter a country: ")
            try:
                print(emission_functions.search_country(country))
            except ValueError:
                print("Country does not exist!")

        elif choice == "13":
            user_input = input("Enter a country and two years(country,year1,year2):")
            country = user_input.split(",")[0]
            year1 = user_input.split(",")[1]
            year2 = user_input.split(",")[2]
            try:
                percentage = emission_functions.get_country_change_for_years(country, year1, year2)
                print(f"{country}:{percentage}%")
            except ValueError:
                print("Wrong year!")

        elif choice == "14":
            user_input = input("Enter a country: ")
            print(emission_functions.print_country_data(emission_functions.get_country_data(user_input)))


        elif choice.startswith("inv pick"):
            choice_list = choice.split(" ")
            try:
                item = choice_list[2]
                try:
                    index = int(choice_list[3])
                except IndexError:
                    inventory.pick(backpack, item)
                else:
                    inventory.pick(backpack, item, index)
            except IndexError:
                print("You didn't specify what to pick")

        elif choice == "inv":
            inventory.inventory(backpack)

        elif choice.startswith("inv drop"):
            choice_list = choice.split(" ")
            try:
                item = choice_list[2]
                inventory.drop(backpack, item)
            except IndexError:
                inventory.drop(backpack, item)

        elif choice.startswith("inv swap"):
            choice_list = choice.split(" ")
            try:
                item = choice_list[2]
                item2 = choice_list[3]
            except IndexError:
                print("You didn't specify what to swap")
            else:
                inventory.swap(backpack, item, item2)

        else:
            print("That is not a valid choice. You can only choose from the menu.")

        input("\nPress enter to continue...")

if __name__ == "__main__":
    main()
    