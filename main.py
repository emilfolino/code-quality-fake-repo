#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Marvin3 main"""

import time
import inventory
import marvin
import emission_functions

backpack = []

def main():
    """main loop for marvin2"""
    while True:
        print(chr(27) + "[2J" + chr(27) + "[;H")
        #print(marvin.morvin_image)
        print("Hello hello, I'm Morvin. I know a thing or two. What can I do for you?")
        print("1) Present yourself to Morvin.")
        print("2) Calculate Farenheit from Celsius.")
        print("3) Word multiplier.")
        print("4) Sum and average.")
        print("5) String letter multiplier.")
        print("6) Isogram checker.")
        print("7) Number comparer.")
        print("8) Randomize string")
        print("a1) Check string with string.")
        print("a2) Number doubles.")
        print("a3) Replace tab with space.")
        print("a4) Add names.")                            
        print("a5) Point counter.")
        print("q) to exit.")
        print("12) Search contries")
        print("13) Search country CO2")

        choice = input("--> ")

        if choice == "q":
            print("Buh-buy - and welcome back anytime!")
            break

        elif choice == "1":
            marvin.greet()

        elif choice == "2": #celsius to farenheit
            marvin.celcius_to_farenheit()

        elif choice == "3": # word multiplier
            marvin.word_manipulation()

        elif choice == "4": # sum and average
            marvin.sum_and_average()

        elif choice == "5": #character uh adder? apa = a-pp-aaa
            marvin.hyphen_string()

        elif choice == "6": #isogram checker
            marvin.is_isogram()
            
        elif choice == "7": #larger smaller
            marvin.compare_numbers()

        elif choice == "8":
            input8 = input("Ange en sträng: ")
            print(marvin.randomize_string(input8))
            time.sleep(1)
            print("sum")

        
        elif choice == "9":
            input9 = input("Ange en sträng: ")
            print(marvin.get_acronym(input9))
            time.sleep(1)
        
        elif choice == "10":
            input10 = input("Ange en sträng: ")
            print(marvin.mask_string(input10))
            time.sleep(1)

        elif choice == "11":
            input11 = input("Ange en sträng: ")
            input11b = input("Ange en substräng: ")
            print(marvin.find_all_indexes(input11, input11b))
            time.sleep(1)

        elif choice == "12":
            search_word = input("Ange ett sökord: ")
            try:
                returned_countries = emission_functions.search_country(search_word)
                print(returned_countries)
                time.sleep(1)
            except ValueError as e:
                print(str(e))
                time.sleep(1)

        elif choice == "13":
            input13 = input("Ange Land,år1,år2: ")
            input13_list = input13.split(",")
            print(input13)
            if len(input13_list) == 3:              
                try:
                    arg1 = str(input13_list[0])
                    arg2 = int(input13_list[1])
                    arg3 = int(input13_list[2])
                    emission = emission_functions.get_country_change_for_years(arg1,arg2,arg3)
                    print("{country}:{emission}%".format(
                        country = input13_list[0],
                        emission = emission
                    ))
                    time.sleep(1)
                except ValueError as e:
                    print(str(e))
                    time.sleep(1)
                    continue

        elif choice == "14":
            input14 = input("Ange ett land: ")
            emission_functions.print_country_data(emission_functions.get_country_data(input14))
            time.sleep(2)

        elif choice == "inv":
            global backpack
            inventory.inventory(backpack)
            time.sleep(1)

        elif choice[0:8] == "inv pick":
            temp_list = choice.split(" ")
            if len(temp_list) == 3: #normal case
                backpack = inventory.pick(backpack, temp_list[2])
            elif len(temp_list) == 4: #with index
                backpack = inventory.pick(backpack, temp_list[2], temp_list[3])
            elif len(temp_list) == 5 and isinstance(temp_list[2], list): # with list and index
                backpack = inventory.pick(temp_list[2], temp_list[3], temp_list[4])

        elif choice[0:8] == "inv drop":
            temp_list = choice.split(" ")
            if len(temp_list) == 3: #normal case
                backpack = inventory.drop(backpack, temp_list[2])
            elif len(temp_list) == 4 and isinstance(temp_list[2], list): # with list and index
                backpack = inventory.drop(temp_list[2], temp_list[3])
            return

        elif choice[0:8] == "inv swap":
            temp_list = choice.split(" ")
            if len(temp_list) == 4: #normal case
                backpack = inventory.swap(backpack, temp_list[2], temp_list[3])
            elif len(temp_list) == 5 and isinstance(temp_list[2], list): # with list and index
                backpack = inventory.swap(temp_list[2], temp_list[3], temp_list[4])
            return

if __name__ == "__main__":
    main()
