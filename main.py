#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Marvin with a simple menu to start up with.
Marvin doesnt do anything, just presents a menu with some choices.
You should add functinoality to Marvin.
"""


import marvin
import inventory
import emission_functions

marvin_image = r"""
	
||====================================================================||
||//$\\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\//$\\||
||(100)==================| FEDERAL RESERVE NOTE |================(100)||
||\\$//        ~         '------========--------'                \\$//||
||<< /        /$\              // ____ \\                         \ >>||
||>>|  12    //L\\            // ///..) \\         L38036133B   12 |<<||
||<<|        \\ //           || <||  >\  ||                        |>>||
||>>|         \$/            ||  $$ --/  ||        One Hundred     |<<||
||<<|      L38036133B        *\\  |\_/  //* series                 |>>||
||>>|  12                     *\\/___\_//*   1989                  |<<||
||<<\      Treasurer     ______/Franklin\________     Secretary 12 />>||
||//$\                 ~|UNITED STATES OF AMERICA|~               /$\\||
||(100)===================  ONE HUNDRED DOLLARS =================(100)||
||\\$//\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\\$//||
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
        print("Hey, I'm FalkenDev. Im a BOT, What can I help you with?")
        print("1) Present yourself to FalkenDev.")
        print("2) Celsius to Fahrenheit")
        print("3) Word multiplication")
        print("4) The sum and the mean")
        print("5) Word that adds letters per word")
        print("6) Look up if a word is Isogram")
        print("7) Look up if a number is larger or smaller or same")
        print("8) Roll over letters")
        print("9) Acronym creator")
        print("10) String masking")
        print("11) Find all indexes")
        print("12) Search for country")
        print("13) Show emission change for a country")
        print("14) Show all data for a country")
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
            original_string = input("Write a word: ")
            print(marvin.randomize_string(original_string))

        elif choice == "9":
            akronym_string = input("Skriv in en sträng här: ")
            print(marvin.get_acronym(akronym_string))

        elif choice == "10":
            mask = input("Write a string of numbers: ")
            print(marvin.mask_string(mask))

        elif choice == "11":
            index_string = input("Write index here: ")
            index_partstring = input("write second index here: ")
            print(marvin.find_all_indexes(index_string, index_partstring))

        elif choice == "12":
            country_word = input("Write the country / chars you me to search for countries: ")
            try:
                print(emission_functions.search_country(country_word))
            except ValueError:
                print("Country does not exist!")

        elif choice == "13":
            country_year1_year2 = input("Write the country and years: ")
            list_input = str(country_year1_year2).split(",")
            try:
                data = emission_functions.get_country_change_for_years(list_input[0], list_input[1], list_input[2])
                print(list_input[0] + ":" + str(data) + "%")
            except ValueError:
                print("Wrong year!")

        elif choice == "14":
            country = input("Input country: ")
            emission_functions.print_country_data(emission_functions.get_country_data(country))

        elif "inv pick" in choice:
            result_choise = choice.split(" ")
            try:
                inventory.pick(bag, result_choise[2], result_choise[3])

            except IndexError:
                inventory.pick(bag, result_choise[2])

        elif "inv drop" in choice:
            result_choise = choice.split(" ")
            try:
                delete = result_choise[2]
                inventory.drop(bag,delete)

            except IndexError:
                print("You need to enter a word to delete from the backpack")

        elif "inv swap" in choice:
            result_choise = choice.split(" ")
            try:
                swap1 = result_choise[2]
                swap2 = result_choise[3]
                inventory.swap(bag,swap1, swap2)
            except IndexError:
                print("Enter 2 words that you want to be swapped with")

        elif "inv" in choice:
            inventory.inventory(bag)

        else:
            print("That is not a valid choice. You can only choose from the menu.")

        input("\nPress enter to continue...")

if __name__ == "__main__":
    main()
    