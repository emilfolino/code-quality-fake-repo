#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
Chattbot 2000
"""


from marvin import celcius_to_farenheit, compare_numbers, greet, hyphen_string, is_isogram, sum_and_average,\
    word_manipulation, meImage, randomize_string, get_acronym, mask_string, find_all_indexes

from inventory import pick, inventory, drop, swap

from emission_functions import search_country, get_country_change_for_years, get_country_data, print_country_data


def main():
    """
    Its an eternal loop, until q is pressed.
    It should check the choice done by the user and call a appropriate
    function.
    """
    
    backpack = []

    while True:
        print(chr(27) + "[2J" + chr(27) + "[;H")
        print(meImage())
        print("Hi, I'm Marvin. I know it all. What can I do you for?")
        print("1) Present yourself to Marvin.")
        print("2) Celsius to farenheit.")
        print("3) Lets play parrot! Tell me what to repeat.")
        print("4) Let me do your math!")
        print("5) Repeat letters in word.")
        print("6) Check for Isogram.")
        print("7) Bigger or smaller?")
        print("8) Shuffle")
        print("9) Create an acronym")
        print("10) Mask string")
        print("11) Find all index")
        print("12) Search for countries")
        print("13) Change in emission")
        print("14) View data from country")
        print("q) Quit.")

        choice = input("--> ")

        if choice == "q":
            print("Bye, bye - and welcome back anytime!")
            break

        elif choice == "1":
            greet()

        elif choice == "2":
            celcius_to_farenheit()

        elif choice == "3":
            word_manipulation()

        elif choice == "4":
            sum_and_average()

        elif choice == "5":
            hyphen_string()

        elif choice == "6":
            is_isogram()

        elif choice == "7":
            compare_numbers()

        elif choice == "8":
            randomize_input = input("Enter a word or sentence to randomize it: ")
            randomize_string(randomize_input)
            print(randomize_string(randomize_input))

        elif choice == "9":
            acronym_input = input("Enter a series of words with each word starting on a capital letter: ")
            get_acronym(acronym_input)
            print(get_acronym(acronym_input))

        elif choice == "10":
            mask_string_input = input("Enter letters or numbers to mask: ")
            mask_string(mask_string_input)
            print(mask_string(mask_string_input))

        elif choice == "11":
            sentence = input("Enter a word or sentence: ")
            sub_sentence = input("Enter what you're searching for in previous input: ")
            find_all_indexes(sentence, sub_sentence)
            print(find_all_indexes(sentence, sub_sentence))

        elif choice == "12":
            try:
                search_word = input("Enter a search word: ")
                search_result = search_country(search_word)
                for values in search_result:
                    print(values)
            except ValueError:
                print("Country does not exist!")

        elif choice == "13":
            try:
                search_word = input("Enter a country and two years, comma seperated: ")
                search_word = search_word.split(",")
                country_name = search_word[0]
                year1 = search_word[1]
                year2 = search_word[2]
                result = get_country_change_for_years(country_name, year1, year2)
                print(f"{country_name}:{result}%")
            except ValueError:
                print("Wrong year!")

        elif choice == "14":
            search_word = input("Type which country you wish to view: ")
            country_data_return = get_country_data(search_word)
            print_country_data(country_data_return)


        elif "inv pick" in choice:
            pick_list = choice.split()
            item = pick_list[2]
            position = len(backpack)
            if len(pick_list) == 4:
                position = pick_list[3]
            backpack = pick(backpack, item, position)

        elif "inv drop" in choice:
            drop_list = choice.split()
            item = drop_list[2]
            backpack= drop(backpack, item)

        elif "inv swap" in choice:
            swap_list = choice.split()
            item1 = swap_list[2]
            item2 = swap_list[3]
            swap(backpack, item1, item2)
            
        elif choice == "inv":
            inventory(backpack)

        else:
            print("That is not a valid choice. You can only choose from the menu.")

        input("\nPress enter to continue...")

if __name__ == "__main__":
    meImage()
    main()
