#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Marvin with a somewhat simple menu.
Its an eternal loop, until q is pressed.
It should check the choice done by the user and call a appropriate
function.
"""
import marvin

import inventory

import oldoptions

import emission_functions

inv = []

def main():

    """ Main"""

    while True:
        
        marvin.main()

        choice = input("--> ") 

        if choice == "inv pick" + " ":
            inventory.nothing_added()
            
        elif choice == "inv pick":
            inventory.nothing_added()

        elif "inv pick" in choice:
            pos = None
            choice_list = choice.split()
            if len(choice_list) < 4:
                choice = choice_list[-1]
            else:
                choice = choice_list[-2]
                pos = choice_list[-1]
            inventory.pick(inv, choice, pos)

        elif choice == "inv":
            inventory.inventory(inv)

        elif "inv swap" in choice:
            choice_list2 = choice.split()
            if len(choice_list2) < 4:
                print("Error there is no such item in the backpack ")
            else:
                choice1 = choice_list2[-2]
                choice2 = choice_list2[-1]
            inventory.swap(inv, choice1, choice2)

        elif "inv drop" in choice:
            choice_list3 = choice.split()
            if len(choice_list3) < 3:
                print("Error there is no such item in the backpack ")
            else: 
                inventory.drop(inv, choice_list3[-1])

        elif choice == "help":
            marvin.help_inv()
    
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
            r_s = input("Write a word to shuffle: ")               
            print(marvin.randomize_string(r_s))

        elif choice == "9":
            ana_word = input("Write a two words to check: ")
            print(marvin.anagram(ana_word))

        elif choice == "10":
            acro_word = input("Write some words with capital letters to make them into an acronym: ")
            print(marvin.get_acronym(acro_word))
            

        elif choice == "11":
            str_mask = input("Write a word to mask:")
            #mask_multi = input("Write a number for mask multiplier:")
            print(marvin.mask_string(str_mask))

        elif choice == "16":
            find_index = input("Write a word and a another word or letter to find it's position:")
            print(marvin.find_all_indexes(find_index))

        elif choice == "12":
            ser_count = input("Write a countrys name to check: ")
            try:
                print(emission_functions.search_country(ser_count))
            except ValueError:
                print("Country does not exist!")
            

        elif choice == "13":
            change = input("Write a country, a year and a year: ")
            try:
                ch_li = change.split(",")
                if len(ch_li) < 2:
                    print("Please write a year")
                elif len(ch_li)== 3:
                    cl = ch_li[0] + ":"
                    print(cl + str(emission_functions.get_country_change_for_years(ch_li[0], ch_li[1], ch_li[2])) + "%")
                else:
                    print(emission_functions.get_country_year_data_megaton(ch_li[0], ch_li[1]))
            except (ValueError, AttributeError):
                ch_li = change.split(",")
                print("Wrong year!")
        elif choice == "14":
            full_count_data = input("Write a country: ")
            try:
                if full_count_data != "":
                    f_c_d = emission_functions.get_country_data(full_count_data)
                    emission_functions.print_country_data(f_c_d)      
                else:
                    raise ValueError
            except (ValueError, AttributeError):
                print("Country does not exist!")

        elif choice == "old":
            while True:
                oldoptions.old_options()

                choice = input("--> ")

                if choice == "1":
                    marvin.filter_list()

                elif choice == "q":
                    print("Bye, bye - and welcome back anytime!")
                break

        
        elif choice == "q":
            print("Bye, bye - and welcome back anytime!")
            break
            
        
        else:
            print("That is not a valid choice. You can only choose from the menu.")

        input("Press enter to continue...")

if __name__ == "__main__":
    main()
