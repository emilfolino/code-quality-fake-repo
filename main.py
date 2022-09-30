#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Marvin, here represented by Demon Cat gives you options for questions that might be answered.
The functions are saved in marvin.py
"""

import marvin
import inventory
import emission_functions as e_functions


marvin_image = r"""
                      (`.-,')
                    .-'     ;
                _.-'   , `,-
          _ _.-'     .'  /._
        .' `  _.-.  /  ,'._;)
       (       .  )-| (
        )`,_ ,'_,'  \_;)
('_  _,'.'  (___,))
 `-:;.-'
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
        print("Hi, I'm Demon Cat. I have an aproximate knowledge of many things! What do you want to almost know?")
        print("Chose an option below:")
        print("1) Present yourself to Demon Cat.")
        print("2) Convert Celsius to Farenheit.")
        print("3) Multiply words.")
        print("4) Sum and average.")
        print("5) Demon Cat language.")
        print("6) Isogram?")
        print("7) Larger or smaller.")
        print("8) Randomize string.")
        print("9) Get acronym.")
        print("10) Mask string.")
        print("11) Find all indexes.")
        print("12) Search for country")
        print("13) Show emission change for a country")
        print("14) Show all data for a country")
        print("a1) Letters in word")
        print("a2) Multiply to find 0-9")
        print("a3) Tab is space")
        print("a4) Brangelina")
        print("a5) Points")
        print("b1) Points to score")
        print("b2) Has strings")
        print("q) Quit.")

        print("You can also try out my inventory functions!")

        choice = input("--> ")
        choice_list = choice.split(" ")

        if choice == "q":
            print("You're off already? Well I almost know where you live so you can't hide")
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
            string = input("Tell me a string and I'll randomize it\n")
            print(marvin.randomize_string(string))
            input("\nPress enter to continue...")
        elif choice == "9":
            string = input("Tell me a string and I'll give you an acronym\n")
            print(marvin.get_acronym(string))
            input("\nPress enter to continue...")

        elif choice == "10":
            string = input("Give me a string and I'll make it secret\n")
            print(marvin.mask_string(string))
            input("\nPress enter to continue...")

        elif choice == "11":
            string1 = input("I need a string and then a substring that I can "
                            "locate in the first one.\n"
                            "First one:\n")
            string2 = input("Second one now:\n")
            print(marvin.find_all_indexes(string1, string2))
            input("\nPress enter to continue...")

        elif choice == "12":
            search_word = input(("Enter a search frase and I'll see if it "
                                 "matches a country\n"))
            try:
                data = e_functions.search_country(search_word)
                print("Following countries were found:")
                for i in data:
                    print(i)
            except ValueError as e:
                print(str(e))
            input("\nPress enter to continue...")

        elif choice == "13":
            search_word = input("Enter country, year and year with no spaces\n")
            search_list = search_word.split(",")
            try:
                country = search_list[0]
                year1 = search_list[1]
                year2 = search_list[2]
            except IndexError as e:
                print(str(e) + " You must specify two years")
                print("Press enter to continue")
                continue

            try:
                dif_co2 = e_functions.get_country_change_for_years(country, year1, year2)
                print("{}:{}%".format(country, dif_co2))
            except ValueError as e:
                print(str(e))
            input("\nPress enter to continue...")

        elif choice == "14":
            country_name = input("Tell me what country you want data on:\n")

            all_c_data = e_functions.get_country_data(country_name)
            e_functions.print_country_data(all_c_data)
            input("\nPress enter to continue...")

        elif choice == "a1":
            marvin.letters_in_word()

        elif choice == "a2":
            marvin.multiply_to_find()

        elif choice == "a3":
            marvin.tab_is_space()

        elif choice == "a4":
            marvin.brangelina()

        elif choice == "a5":
            marvin.points()

        elif choice == "b1":
            max_points = input("What's the maximum score?\n")
            points = input("what's your score?\n")
            print(marvin.points_to_grade(max_points, points))
            input("\nPress enter to continue...")

        elif choice == "b2":
            """
            Checks if string1 starts with string2, contains string3
            and ends with string4.
            """
            print("Give me four strings. I'll check the first with the rest\n")
            string1 = input("First:\n")
            string2 = input("Second:\n")
            string3 = input("Third:\n")
            string4 = input("Fourth:\n")
            print(marvin.has_strings(string1, string2, string3, string4))
            input("\nPress enter to continue...")

        elif choice.startswith("inv pick"):
            try:
                if len(choice_list) == 3:
                    inventory.pick(bag, choice_list[2])
                else:
                    inventory.pick(bag, choice_list[2], choice_list[3])
            except IndexError:
                print("You have to specify what you want to pick up")
            input("\nPress enter to continue...")

        elif choice.startswith("inv drop"):
            try:
                inventory.drop(bag, choice_list[2])
            except IndexError:
                print("if you want to drop an item "
                      "you have to tell me which one")
            input("\nPress enter to continue...")


        elif choice.startswith("inv swap"):
            try:
                inventory.swap(bag, choice_list[2], choice_list[3])
            except IndexError:
                print("if you want to swap items "
                      "you have to tell me which ones")
            input("\nPress enter to continue...")

        elif choice.startswith("inv"):
            if len(choice_list) == 3:
                inventory.inventory(bag, choice_list[1], choice_list[2])
            else:
                inventory.inventory(bag)
            input("\nPress enter to continue...")

        else:
            print("That is not a valid choice. You can only choose from the menu.")

        #input("\nPress enter to continue...")




if __name__ == "__main__":
    main()
