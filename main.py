#!/usr/bin/env python3

"""
Main file for Marvin
"""

import marvin
import inventory
import emission_functions

marvin_image = r"""
 \      oo
  \____|\mm
  //_//\ \_\
 /K-9/  \/_/
/___/_____\
-----------
"""

backpack = []

def main():
    """
    Its an eternal loop, until q is pressed.
    It should check the choice done by the user and call a appropriate
    function.
    """
    while True:
        print(chr(27) + "[2J" + chr(27) + "[;H")
        print(marvin_image)
        print("Hi, I'm K-9. I know it all. What can I do you for?")
        print("1) Present yourself to K-9.")
        print("2) Convert Celsius to Fahrenheit.")
        print("3) Repeat a word.")
        print("4) Sum and average.")
        print("5) Repeat letters in word.")
        print("6) Isogram.")
        print("7) Compare numbers.")
        print("8) Randomize string.")
        print("9) Get acronym.")
        print("10) Mask string.")
        print("11) Find all indexes.")
        print("12) Search for countries.")
        print("13) Calculate difference in emissions.")
        print("14) Print country data.")
        print("a1) Letters in word.")
        print("a2) Double until all digits present.")
        print("a3) Replace tab with spaces.")
        print("a4) Combine names.")
        print("b1) Points to grade.")
        print("b2) Has strings.")
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
            print(marvin.randomize_string(input("Enter a string to randomize: ")))

        elif choice == "9":
            print(marvin.get_acronym(input("Enter a string to create an acronym for: ")))

        elif choice == "10":
            print(marvin.mask_string(input("Enter a string to mask: ")))

        elif choice == "11":
            string = input("Enter a first string: ")
            substring = input("Enter a substring of the first string: ")
            print(marvin.find_all_indexes(string, substring))

        elif choice == "12":
            search_word = input("Enter search word: ")
            try:
                countries = emission_functions.search_country(search_word)
                print("Following countries were found: " + ", ".join(countries))
            except ValueError:
                print("Country does not exist!")

        elif choice == "13":
            country, year1, year2 = input("Enter country and two years separated by commas: ").split(",")
            try:
                print(country + ":" + str(emission_functions.get_country_change_for_years(country, year1, year2)) + "%")
            except ValueError:
                print("Wrong year!")

        elif choice == "14":
            country = input("Enter a country name: ")
            data = emission_functions.get_country_data(country)
            emission_functions.print_country_data(data)

        elif choice == "a1":
            marvin.letters_in_word()

        elif choice == "a2":
            marvin.double_number()

        elif choice == "a3":
            marvin.tab_to_spaces()

        elif choice == "a4":
            marvin.combine_names()

        elif choice == "b1":
            max_points = input("Enter the max points: ")
            points = input("Enter your points: ")
            print(marvin.points_to_grade(max_points, points))

        elif choice == "b2":
            string = input("Enter a first string: ")
            start = input("Enter a string at the start of the first string: ")
            substring = input("Enter a substring of the first string: ")
            end = input("Enter a string at the end of the first string: ")
            print(marvin.has_strings(string, start, substring, end))

        elif choice[:3] == "inv":
            command = choice.split(" ")
            if len(command) == 1:
                inventory.inventory(backpack)
            elif command[1] == "pick":
                if len(command) > 3:
                    inventory.pick(backpack, command[2], command[3])
                else:
                    inventory.pick(backpack, command[2])
            elif command[1] == "drop":
                inventory.drop(backpack, command[2])
            elif command[1] == "swap":
                inventory.swap(backpack, command[2], command[3])

        else:
            print("That is not a valid choice. You can only choose from the menu.")

        input("\nPress enter to continue...")

if __name__ == "__main__":
    main()
