#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Keeps Marvin running
"""
# from me.kmom05.marvin4.emission_functions import search_country
import marvin
import inventory
import emission_functions

marvin_image = r"""
       _________
      /___   ___\
     //@@@\ /@@@\\
     \\@@@/ \@@@//
      \___ " ___/
         | - |
          \_/"""
goodbye_image = r"""
  __      __
 ( _\    /_ )
  \ _\  /_ /
   \ _\/_ /_ _
   |_____/_/ /|
   (  (_)__)J-)
   (  /`.,   /
    \/  ;   /
     | === |"""

def main():
    """
    infinity loop
    """
    backpack = []

    while True:
        print(chr(27) + "[2J" + chr(27) + "[;H")
        print(marvin_image)
        print("Hi, I'm Marvin v2. What can I do for you?\n")
        print("1) Present yourself to Marvin.")
        print("q) Quit.")
        print("2) Convert °C to °F.")
        print("3) Enter a word and a number and Marvin will multiply them.")
        print(
            "4) Enter numbers and finish with 'done. Marvin will calculate "
            "the sum and average of all the numbers."
        )
        print("5) Enter a word and Marvin will add stuff to it.")
        print("6) See if a word is an isogram.")
        print(
            "7) Enter two numbers and Marvin will tell you if the last nr is "
            "smaller, bigger or equal to the first. Type 'done' when you are "
            "done . "
        )
        print("8) Random string.")
        print("9) make an acronym")
        print("10) mask a text with #")
        print("11) find all indexes")
        print(
            "a1) Enter two words and Marvin will test if all the letters in the "
            "second word are in the first"
        )
        print(
            "a2) Enter two numbers and Marvin will multiply the first value by 2 "
            "and check if the product have all numbers from 0-9. Marvin will try "
            "this as many times as your second value.")
        print(
            "a3) Enter a sentence with atleast one [tab]. Marvin will change the "
            "[tab] to '   '."
        )
        print(
            "a4) Enter two names and marvin will combine them into one special "
            "name."
        )
        print(
            "a5) Enter a random letter followed by a random number, repeat and "
            "press [Enter] when done, Marvin will calculate which letter gets "
            "the most 'points'"
        )
        print("b1) see  your grade")
        print("b2) has strings")
        print("12) Search country")
        print("13) Emission change")
        print("14) All data about a country")
        print("e1)")
        print("e2)")
        print("e3)")

        print("\nTry out my 'inv' commands!")
        print("----------\n")

        choice = input("--> ")

        if choice == "q":
            print("\nPeace out!")
            print(goodbye_image)
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
            word = input("word: ")
            print(marvin.randomize_string(word))

        elif choice == "9":
            word = input("word: ")
            print(marvin.get_acronym(word))

        elif choice == "10":
            word = input("word : ")
            print(marvin.mask_string(word))

        elif choice == "11":
            text = input("text : ")
            sub_text = input("sub-text : ")
            print(f"{marvin.find_all_indexes(text, sub_text)}")

        elif choice == "b1":
            max_score = input("max score: ")
            score = input("Your score : ")
            print(marvin.points_to_grade(max_score, score))

        elif choice == "b2":
            str1 = input("word : ")
            str2 = input("word : ")
            str3 = input("word : ")
            str4 = input("word : ")
            print(marvin.has_strings(str1, str2, str3, str4))

        elif choice == "a1":
            marvin.compare_strings()

        elif choice == "a2":
            marvin.square_add()

        elif choice == "a3":
            marvin.replace_tab()

        elif choice == "a4":
            marvin.brangelina()

        elif choice == "a5":
            marvin.player_score()

        elif choice.startswith("inv pick"):
            usr_cmd = choice.split()
            try:
                backpack = inventory.pick(
                    backpack, usr_cmd[2], int(usr_cmd[3]))
            except IndexError:
                try:
                    backpack = inventory.pick(backpack, usr_cmd[2])
                except IndexError:
                    print("Just 'inv pick' is not a valid command.")
            except ValueError:
                print(f"{usr_cmd[3]} is not a valid index nr")
                
        elif choice.startswith("inv drop"):
            usr_cmd = choice.split()
            try:
                backpack = inventory.drop(backpack, usr_cmd[2])
            except IndexError:
                print("Just 'inv drop' is not a valid command.")
        
        elif choice.startswith("inv swap"):
            usr_cmd = choice.split()
            try:
                inventory.swap(backpack, usr_cmd[2], usr_cmd[3])
            except IndexError:
                print("Need two items.")
        
        elif choice.startswith("inv"):
            usr_cmd = choice.split()
            try:
                inventory.inventory(backpack, usr_cmd[1], usr_cmd[2])
            except IndexError:
                inventory.inventory(backpack)
        
        elif choice == '12':
            search = input('search: ')
            try:
                countries = ', '.join(emission_functions.search_country(search))
                print(f'Following countries were found: {countries}')
            except ValueError as e:
                print(e)

        elif choice == '13':
            search = input('search: ')
            search_list = search.split(',')
            try:
                result = emission_functions.get_country_change_for_years(
                    search_list[0], search_list[1], search_list[2])
                print(f'{search_list[0]}:{result}%')
            except IndexError as e:
                print(e)
            except  ValueError as e:
                print(e)

        elif choice == '14':
            search = input('Search: ')
            try:
                country_data = emission_functions.get_country_data(search)
                emission_functions.print_country_data(country_data)
            except ValueError as e:
                print(e)
            
        elif choice == 'e1':
            search = input('Year: ')
            search_list = search.split(' ')
            try:
                print(emission_functions.get_emission_max_value(
                    search_list[0], int(search_list[1])))
            except ValueError as e:
                print(e)
            except IndexError as e:
                print(e)
        
        elif choice == 'e2':
            search = input('Year: ')
            search_list = search.split(' ')
            try:
                print(emission_functions.get_emission_capita(
                    search_list[0], int(search_list[1])))
            except ValueError as e:
                print(e)
            except IndexError as e:
                print(e)
        
        elif choice == 'e3':
            search = input('Year: ')
            search_list = search.split(' ')
            try:
                print(emission_functions.get_emission_area(
                    search_list[0], int(search_list[1])))
            except ValueError as e:
                print(e)
            except IndexError as e:
                print(e)

        else:
            print("That is not a valid choice."
                  "You can only choose from the menu.")

        input("\nPress enter to continue...")

if __name__ == "__main__":
    main()
