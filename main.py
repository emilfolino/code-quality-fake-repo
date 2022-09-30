#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Main program Marvin
"""
import marvin
import inventory
import emission_functions

bag = []

def main():
    """
    Main function
    """
    while True:
        marvin.print_menu()
        choice = input("--> ")

        if (choice in ("q", "Q")):
            print("Bye, bye - and welcome back anytime!")
            break # När man trycker Q hoppar den ur while-satsen

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
            word = input("Enter a string to randomize: ")
            print(marvin.randomize_string(word))

        elif choice == "9":
            string = input("Please add a string: ")
            print(marvin.get_acronym(string))

        elif choice == "10":
            string = input("Please add a string: ")
            print(marvin.mask_string(string))

        elif choice == "11":
            string1 = input("Please add a string: ")
            string2 = input("Please add a string part: ")
            print(marvin.find_all_indexes(string1, string2))

        elif choice == "12":
            word = input("Please add a search string: ")
            try:
                print("Following countries were found: " + ", ".join(emission_functions.search_country(word)))
            except ValueError:
                print("Country does not exist!")

        elif choice == "13":
            string = input("Please add country, year1, year2: ")
            args = string.split(",")
            if (len(args) == 3):
                try:
                    change = emission_functions.get_country_change_for_years(
                        args[0].strip(), args[1].strip(), args[2].strip())
                    print(args[0] + ":" + str(change) + "%")
                except ValueError:
                    print("Wrong year!")
                except TypeError:
                    print("Country doesn't exist! Be sure to start each country with a capital letter.")
            else: 
                print("Please write one country and two years.")


        elif choice == "14":
            string = input("Add a country: ")
            string = string.capitalize()
            data = emission_functions.get_country_data(string)
            emission_functions.print_country_data(data)

        elif choice == "a1":
            marvin.letters_in_word()

        elif choice == "a2":
            pass

        elif choice == "a3":
            pass

        elif choice == "a4":
            pass
        
        elif choice == "a5":
            pass

        elif choice == "b1":
            string1 = int(input("Enter max points: "))
            string2 = int(input("Enter your points: "))
            print(marvin.points_to_grade(string1, string2))

        elif choice == "b2":
            string1 = input("Please add a string: ")
            string2 = input("Please add a string: ")
            string3 = input("Please add a string: ")
            string4 = input("Please add a string: ")
            print(marvin.has_strings(string1, string2, string3, string4))

        elif choice == "e1":
            inp = input("Add a year, 1990/ 2005/ 2017, and, if you want, number of countries to show: ")
            inp_list = inp.split()

            if (len(inp_list) == 1):
                try:
                    emission_functions.print_countries_CO2(inp_list[0])
                except ValueError:
                    print("Please write one of the years 1990/ 2005 or 2015.")
            elif (len(inp_list) == 2):
                try:
                    emission_functions.print_countries_CO2(inp_list[0], inp_list[1])
                except ValueError:
                    print("Please write one of the years 1990/ 2005 or 2017, and number as an integer.")
            else: 
                print("Please only add one year and one number.")

        elif choice == "e2":
            inp = input("Add a year (1990/ 2005/ 2017) and, if you want, number of countries to show: ")
            inp_list = inp.split()

            if (len(inp_list) == 1):
                try:
                    int(inp_list[0])
                    emission_functions.print_emission_per_capita(inp_list[0])
                except KeyError:
                    # Annars finns inte data["capita"] som används
                    print("Please add one of the years 1990/ 2005 or 2017.")
                except ValueError:
                    print("Please add one of the years 1990/ 2005 or 2017.")

            elif (len(inp_list) == 2):
                try:
                    int(inp_list[0])
                    emission_functions.print_emission_per_capita(inp_list[0], inp_list[1])
                except KeyError:
                    print("Please add one of the years 1990/ 2005 or 2017.")
                except ValueError:
                    print("Please add one of the years 1990/ 2005/ 2017, and number as an integer.")
            else: 
                print("Please only add one year and one number.")

        elif choice == "e3":
            inp = input("Add a year (1990/ 2005/ 2017) and, if you want, number of countries to show: ")
            inp_list = inp.split()

            if (len(inp_list) == 1):
                try:
                    int(inp_list[0])
                    emission_functions.print_emission_per_area(inp_list[0])
                except KeyError:
                    print("Please add one of the years 1990/ 2005 or 2017.")
                except ValueError:
                    print("Please add one of the years 1990/ 2005 or 2017.")

            elif (len(inp_list) == 2):
                try:
                    int(inp_list[0])
                    emission_functions.print_emission_per_area(inp_list[0], inp_list[1])
                except KeyError:
                    print("Please add one of the years 1990/ 2005 or 2017.")
                except ValueError:
                    print("Please add one of the years 1990/ 2005/ 2017, and number as an integer.")
            else: 
                print("Please only add one year and one number.")

        elif choice.startswith("inv pick"):
            arg_list = choice.split(" ")

            if (len(arg_list)==3):
                inventory.pick(bag, arg_list[2])

            elif (len(arg_list)==4):
                inventory.pick(bag, arg_list[2], arg_list[3])

            elif (arg_list == [] or len(arg_list) < 3 or len(arg_list) > 4):
                print("Error. Please write 'inv pick <item> (<index> as int).")

        elif choice.startswith("inv drop"):
            arg_list = choice.split(" ")

            if (len(arg_list)==3):
                inventory.drop(bag, arg_list[2])

            elif (arg_list == [] or len(arg_list) < 3 or len(arg_list) > 3):
                print("Error. Please ¨write 'inv drop <item>.")

        elif choice.startswith("inv swap"):
            arg_list = choice.split(" ")

            if (len(arg_list)==4):
                inventory.swap(bag, arg_list[2], arg_list[3])

            elif (arg_list == [] or len(arg_list) < 4 or len(arg_list) > 4):
                print("Error. Please ¨write 'inv swap <item> <item>.")

        elif choice.startswith("inv"):
            arg_list = choice.split(" ")

            if (len(arg_list)==1):
                inventory.inventory(bag)

            if (len(arg_list)==3):
                inventory.inventory(bag, arg_list[1], arg_list[2])

            elif (arg_list ==  [] or len(arg_list) == 2 or len(arg_list) > 3):
                print("Error. Please write 'inv (<start> <stop>).")

        else:
            print("That is not a valid choice. You can only choose from the menu")
            print(" - or write an expression that starts with 'inv'.")

        input("\nPress enter to continue...")

if __name__ == "__main__":
    main()
