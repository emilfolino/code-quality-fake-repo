#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Marvin main code"""
import marvin
import inventory
import emission_functions as em
# https://dbwebb.se/uppgift/din-egen-chattbot-marvin-steg-1-v3
"""
Its an eternal loop, until q is pressed.
It should check the choice done by the user and call a appropriate
function.
"""


def main():
    """Program main loop"""
    bag = []
    while True:
        # marvin.menu()
        choice = input("--> ")
        if choice == "q":
            marvin.printExit()
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
            print(marvin.randomize_string(input("Input")))
        elif choice == "9":
            print(marvin.get_acronym(input("Input")))
        elif choice == "10":
            print(marvin.mask_string(input("Input")))
        elif choice == "11":
            in1 = input("In1")
            in2 = input("In2")
            print(marvin.find_all_indexes(in1, in2))
        elif choice == "12":
            in1 = input("In1")
            try:
                print(em.search_country(in1))
            except ValueError:
                print("Country does not exist!")
        elif choice == "13":
            try:
                in1 = input("In1")
                args = in1.split(",")
                print("{}:{}%".format(args[0], em.get_country_change_for_years(
                    args[0], args[1], args[2])))
            except ValueError:
                print("Wrong year!")
        elif choice == "14":
            in1 = input("In1")
            em.print_country_data(em.get_country_data(in1))
        elif choice == "a1":
            marvin.wordMatchA1()
        elif choice == "a2":
            marvin.howManyTimesForAllNumbersAtleastOnce()
        elif choice == "a3":
            marvin.replaceTabs()
        elif choice == "a4":
            marvin.nameGenerator()
        elif choice == "a5":
            marvin.pointCounter()
        elif choice == "b1":
            grade = marvin.points_to_grade(input("MaxScore"), input("Score"))
            print(grade)
        elif choice == "b2":
            r = marvin.has_strings(input("In1"), input(
                "In2"), input("In3"), input("In4"))
            print(r)
        elif "inv" in choice:
            args = choice.split()[1:]
            try:
                if args[0] == "pick":
                    if(len(args) == 2):
                        bag = inventory.pick(bag, args[1])
                    else:
                        bag = inventory.pick(bag, args[1], args[2])
                elif args[0] == "drop":
                    bag = inventory.drop(bag, args[1])
                elif args[0] == "swap":
                    bag = inventory.swap(bag, args[1], args[2])
                elif args[0].isdigit():
                    inventory.inventory(bag, args[1], args[2])
                else:
                    print("Unknown command")
            except IndexError:
                inventory.inventory(bag)
        else:
            print("That is not a valid choice. You can only choose from the menu.")
        input("\nPress enter to continue...")


if __name__ == "__main__":
    main()
