#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Main for the marvin program
"""
import marvin
import inventory
import emission_functions

bag = []

def main():
    """
    Its an eternal loop, until q is pressed.
    It should check the choice done by the user and call a appropriate
    function.
    """
    #Ascii -image of Quirk the robot helper saved as a variable
    marvin_image = r"""
    ..............
    .  *      *  .
    [.      '     .]
    .            .
    .     ~~     .
    ..............
    """
    while True:
        print(chr(27) + "[2J" + chr(27) + "[;H")
        print(marvin_image)
        print("Hi, I'm Quirk, your personal robot helper. What can I do to help?")
        print("1) Present yourself to Quirk.")
        print("2) Celsius to fahrenheit")
        print("3) Word repeating")
        print("4) Sum and average")
        print("5) Repeat letters")
        print("6) Isogram")
        print("7) Check numbers")
        print("8) Randomize a string")
        print("9) Make an acronym")
        print("10) Mask a string")
        print("11) Find all indexes")
        print("12) Search for countries in emission data")
        print("13) Show emission change for country")
        print("14) Show country data")
        print("a1) Check strings")
        print("a2) Double a number")
        print("a3) Tabs to spaces")
        print("a4) Merge names")
        print("a5) Scoring")
        print("b1) Points to grade")
        print("b2) Has strings")
        print("e1) Display emissions by country")
        print("e2) Display emissions per capita")
        print("e3) Display emissions divided by area")
        print("q) Quit.")
        print("\nTry out my cool inv commands!")
        print("------------")

        choice = input("--> ")

        choice = choice.rstrip()
        choice = choice.split(" ")

        if choice[0] == "q":
            print("Bye, bye - and welcome back anytime!")
            break

        elif choice[0] == "1":
            marvin.greet()
        
        elif choice[0] == "2":
            marvin.celcius_to_farenheit()

        elif choice[0] == "3":
            marvin.word_manipulation()

        elif choice[0] == "4":
            marvin.sum_and_average()

        elif choice[0] == "5":
            marvin.hyphen_string()

        elif choice[0] == "6":
            marvin.is_isogram()

        elif choice[0] == "7":
            marvin.compare_numbers()
        
        elif choice[0] == "8":
            print("Sure I will randomize a string for you!")
            string = input("Enter a string to randomize: ")
            print(marvin.randomize_string(string))
        
        elif choice[0] == "9":
            print("Sure I will make an acronym for you!")
            string = input("Enter a string to make an acronym: ")
            print(marvin.get_acronym(string))

        elif choice[0] == "10":
            print("Sure I will mask a string for you!")
            string = input("Enter a string to mask it: ")
            print(marvin.mask_string(string))
        
        elif choice[0] == "11":
            print("Sure I will find all indexes where a string contains another string: ")
            string = input("Enter the first string: ")
            substring = input("Enter the second string: ")
            print(marvin.find_all_indexes(string, substring))

        elif choice[0] == "12":
            search_word = input("Type in a country to search for: ")
            try:
                results = emission_functions.search_country(search_word)
                print("Following countries where found: " + ", ".join(results) )
            except ValueError as e:
                print(str(e))

        elif choice[0] == "13":
            user_input = input("Which country and what years to you want to compare (enter: country,year1,year2): ")
            user_input = user_input.split(',')
            try:
                change = emission_functions.get_country_change_for_years(user_input[0], user_input[1], user_input[2])
                print(user_input[0] + ":" + str(change) + "%")
            except ValueError as e:
                print(str(e))
            except IndexError:
                print("Too few arguments for get_country_change")
        
        elif choice[0] == "14":
            country = input("Which country do you wish to display data for: ")
            try:
                country_data = emission_functions.get_country_data(country)
                emission_functions.print_country_data(country_data)
            except ValueError as e:
                print(str(e))
        
        elif choice[0] == "a1":
            marvin.check_strings()
        
        elif choice[0] == "a2":
            marvin.double_a_number()

        elif choice[0] == "a3":
            marvin.tabs_to_spaces()

        elif choice[0] == "a4":
            marvin.merge_names()

        elif choice[0] == "a5":
            marvin.scoring()

        elif choice[0] == "b1":
            print("Sure I will calculate your grade for you!")
            max_score = input("Please enter the max score: ")
            score = input("Please enter your score: ")
            print(marvin.points_to_grade(max_score, score))

        elif choice[0] == "b2":
            print("Sure I will help you look for three strings in another string!")
            string = input("Please enter the first string: ")
            start_string = input("Please enter a string to look for at the start of the first string: ")
            contained_string = input("Please enter a string to look for in the first string: ")
            end_string = input("Please enter a string to look for at the end of the first string: ")
            print(marvin.has_strings(string, start_string, contained_string, end_string))
        
        elif choice[0] == "e1":
            args = input("Please input a year and optionally a number of countries to display (year nr): ")
            args = args.split(" ")
            #If more than one arg was entered call the function with the args at args[0] and args[1].
            #And the argument "country" for the parameter operation.
            #Check for value errors, if caught print error message
            if len(args) > 1:
                try:
                    data = emission_functions.get_emission_data_for_countries("country", args[0], args[1])
                    emission_functions.print_emission_data(data)
                except ValueError as e:
                    print(str(e))
            #If no/one arg was entered call the function with argument att args[0]
            #Check for value errors, if caught print error message
            else:
                try:
                    data = emission_functions.get_emission_data_for_countries("country", args[0])
                    emission_functions.print_emission_data(data)
                except ValueError as e:
                    print(str(e))

        elif choice[0] == "e2":
            args = input("Please input a year and optionally a number of countries to display (year nr): ")
            args = args.split(" ")
            #If more than one arg was entered call the function with the args at args[0] and args[1].
            #And the argument "capita" for the parameter operation.
            #Check for value errors, if caught print error message
            if len(args) > 1:
                try:
                    data = emission_functions.get_emission_data_for_countries("capita", args[0], args[1])
                    emission_functions.print_emission_data(data)
                except ValueError as e:
                    print(str(e))
            #If no/one arg was entered call the function with argument att args[0]
            #Check for value errors, if caught print error message
            else:
                try:
                    data = emission_functions.get_emission_data_for_countries("capita", args[0])
                    emission_functions.print_emission_data(data)
                except ValueError as e:
                    print(str(e))

        elif choice[0] == "e3":
            args = input("Please input a year and optionally a number of countries to display (year nr): ")
            args = args.split(" ")
            #If more than one arg was entered call the function with the args at args[0] and args[1].
            #And the argument "area" for the parameter operation.
            #Check for value errors, if caught print error message
            if len(args) > 1:
                try:
                    data = emission_functions.get_emission_data_for_countries("area", args[0], args[1])
                    emission_functions.print_emission_data(data)
                except ValueError as e:
                    print(str(e))
            #If no/one arg was entered call the function with argument att args[0]
            #Check for value errors, if caught print error message
            else:
                try:
                    data = emission_functions.get_emission_data_for_countries("area", args[0], args[1])
                    emission_functions.print_emission_data(data)
                except ValueError as e:
                    print(str(e))

        elif choice[0] == "inv":
            #Only 'inv' has been given
            if len(choice) == 1:
                inventory.inventory(bag)
            #Some command is entered find out which
            elif len(choice) > 1:
                #For inv command pick
                if choice[1] == "pick":
                    #If two arguments for pick(position has been given)
                    if len(choice) == 4:
                        inventory.pick(bag, choice[2], choice[3])
                    #If one argument for pick (position has not been given)
                    elif len(choice) == 3:
                        inventory.pick(bag, choice[2])
                    else:
                        print("To many or few arguments for pick")
                #For inv command drop
                elif choice[1] == "drop":
                    #If number of arguments for drop checks out
                    if len(choice) == 3:
                        inventory.drop(bag, choice[2])
                    else:
                        print("To many or few arguments for drop")
                elif choice[1] == "swap":
                    #If number of arguments for swap checks out
                    if len(choice) == 4:
                        inventory.swap(bag, choice[2], choice[3])
                    else:
                        print("To many of few arguments for swap")
                #If none of the above, check if user entered two ints after inv
                #Using helper function check_sequence
                elif inventory.check_sequence(choice):
                    inventory.inventory(bag, choice[1], choice[2])
                else:
                    print("Unknown inv command")
        else:
            print("That is not a valid choice. You can only choose from the menu or give me correct inv commands!")

        input("\nPlease press enter to continue...")

if __name__ == "__main__":
    main()
