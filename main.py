#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Main program file for Marvin
"""

import marvin
import inventory
import emission_functions

marvin_image = r"""
             ."-------".
            / o       o \
           /   \     /   \
          /     )-"-(     \
         /     ( 6 6 )     \
        /       \ " /       \
       /         )=(         \
      /   o   .--"-"--.   o   \
     /    I  /  -   -  \  I    \
 .--(    (_}y/\       /\y{_)    )--.
(    ".___l\/__\_____/__\/l___,"    )
 \                                 /
  "-._      o O o O o O o      _,-"
      `--Y--.___________.--Y--'
         |==.___________.==|
         `==.___________.=='


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
        print("Hi there, I'm Marvin. I come in peace, take me to your "
              "leader or choose one of the below!")
        print("1) Present yourself to Marvin.")
        print("2) Ask Marvin to convert a temperature from Celsius to Farenheit.")
        print("3) Marvin will perform word multiplication!")
        print("4) Ask Marvin produce sum and average of given numbers.")
        print("5) Enter a string and let Marvin work some magic on it!")
        print("6) Enter a word and let Marvin check wether it is an isogram.")
        print("7) Enter numbers, Marvin will tell you if the last number is "
              "greater, smaller or the same than the one before.")
        print("8) Randomize string, send a string to Marvin and see what "
              "comes out!")
        print("9) Get acronym, see Marvin combine your favorite words!")
        print("10) String masking, don't spill the secret!")
        print("11) Find indexes of substring in string!")
        print("12) Country data, see if a country is in the dataset")
        print("13) Check out the emission changes for a country!")
        print("14) Get country data!")
        print("a1) Marvin will compare two strings for character match.")
        print("a2) Give Marvin a number and he will multiply by two until all "
              "numbers between 0 and 9 are present.")
        print("a3) Tabs to spaces, watch as Marvin formats a string!")
        print("a4) Concatenate some names, let Marvin create Hollywoods next "
              "power couple!")
        print("a5) Let Marvin help with calculating scores!")
        print("b1) Points to grade, get your scores while they're still warm!")
        print("b2) Has strings, why say many words when few do trick?")
        print("e1) Which country is the hottest right now, find out here!")
        print("e2) Where do the filthiest people live? Find out here!")
        print("e3) Where to establish your cleaning service? find out!")
        print("q) Quit.")

        choice = input("Enter your choice: ")

        if choice.lower() == "q":
            print("Come back soon!")
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
            my_string = input("Enter your string: ")

            print(marvin.randomize_string(my_string))

        elif choice == "9":
            my_string = input("Enter your favorite words: ")

            print(marvin.get_acronym(my_string))

        elif choice == "10":
            my_string = input("Tell me your secret: ")

            print(marvin.mask_string(my_string))

        elif choice == "11":
            my_first_string = input("Enter first string: ")
            my_second_string = input("Enter second string: ")

            print(marvin.find_all_indexes(my_first_string, my_second_string))

        elif choice == '12':
            search_word = input("Enter search word: ")

            try:
                print(emission_functions.search_country(search_word))

            except ValueError:
                print("Country does not exist!")

        elif choice == '13':
            search = input("Enter country and year(s), separated by a ',': ")
            search_words = search.split(",")

            if len(search_words) == 2:

                try:
                    print(emission_functions.get_country_year_data_megaton(
                        search_words[0], search_words[1]))

                except ValueError:
                    print("Wrong year!")

            elif len(search_words) == 3:

                try:
                    result = emission_functions.get_country_change_for_years(
                        search_words[0], search_words[1], search_words[2])
                    print(f"{search_words[0]}:{result}%")

                except ValueError:
                    print("Wrong year!")

        elif choice == '14':
            search_word = input("Enter country name:")
            emission_functions.get_country_data(search_word)

        elif choice == "a1":
            marvin.string_comparison()

        elif choice == "a2":
            marvin.times_to_all()

        elif choice == "a3":
            marvin.tab_to_spaces()

        elif choice == "a4":
            marvin.combine_names()

        elif choice == "a5":
            marvin.string_to_scores()

        elif choice == "b1":
            max_score = input("Enter max score: ")
            my_score = input("Enter your score: ")

            print(marvin.points_to_grade(max_score, my_score))

        elif choice == "b2":
            string_1 = input("Enter first string: ")
            string_2 = input("Enter second string: ")
            string_3 = input("Enter third string: ")
            string_4 = input("Enter fourth string: ")

            print(marvin.has_strings(string_1, string_2, string_3, string_4))

        elif "inv pick" in choice:
            choice_to_list = choice.split()

            if choice_to_list[-1].isdigit():
                inventory.pick(
                    backpack, choice_to_list[-2], choice_to_list[-1])

            else:
                inventory.pick(backpack, choice_to_list[-1])

        elif "inv drop" in choice:
            item_list = choice.split()
            inventory.drop(backpack, item_list[-1])

        elif "inv swap" in choice:
            item_list = choice.split()

            if len(item_list) == 4:
                inventory.swap(backpack, item_list[-1], item_list[-2])

        elif choice == "inv":
            # print("\nAvailable inv commands: \npick\nswap\ndrop")
            choice_to_list = choice.split()

            if len(choice_to_list) == 3:
                inventory.inventory(
                    backpack, choice_to_list[-2], choice_to_list[-1])

            else:
                inventory.inventory(backpack)

        elif choice == 'e1':
            search = input("Enter year and number of results: ")
            search_words = search.split()

            if len(search_words) == 1:

                try:
                    emission_functions.country_data_toplist(
                        search_words[0])

                except ValueError:
                    print("Wrong year!")

            elif len(search_words) == 2:

                try:
                    emission_functions.country_data_toplist(
                        search_words[0], search_words[1])

                except ValueError:
                    print("Wrong year!")

        elif choice == 'e2':
            search = input("Enter year and number of results: ")
            search_words = search.split()

            if len(search_words) == 1:

                try:
                    emission_functions.emission_capita(
                        search_words[0])

                except ValueError:
                    print("Wrong year!")

            elif len(search_words) == 2:

                try:
                    emission_functions.emission_capita(
                        search_words[0], search_words[1])

                except ValueError:
                    print("Wrong year!")

        elif choice == 'e3':
            search = input("Enter year and number of results: ")
            search_words = search.split()

            if len(search_words) == 1:

                try:
                    emission_functions.emission_area(
                        search_words[0])

                except ValueError:
                    print("Wrong year!")

            elif len(search_words) == 2:

                try:
                    emission_functions.emission_area(
                        search_words[0], search_words[1])

                except ValueError:
                    print("Wrong year!")

        else:
            print("Not a valid choice")
        input("\nPress enter to continue...")


if __name__ == "__main__":
    main()
