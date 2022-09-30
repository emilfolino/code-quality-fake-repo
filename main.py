"""
Marvin with a simple menu to start up with.
Marvin doesnt do anything, just presents a menu with some choices.
You should add functinoality to Marvin.
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import marvin
import inventory
import emission_functions



def main():
    """
    Marvin
    """
    marvin_image = r"""
                    ______    ____
                :  ;;;;\__/:  ;\
                    \;__/.... :  _/;
                ___:__ ..__\_/__;
                |  ## `--'   ##|;
                |_____/~;\_____|;
                    /~~~_ _ ~~   /
                    // (_:_)   \\
            _     // ,'~ `,_\\~\_
            //     ~~`,---,'~~~   \
    ___     //         ~~~~      ;; \_  __
    /_\/____::_        ,(:;:  __    ;; \/;;\  __
    \_/) _  ::(       ; ;;:    \    / ;:;;::-,-'
    |[-]_::-|       : :;;:   /  * | ;:;;:;'
    | :__:: |       :.`,:::  : +  : /___:'
    |[_ ] [\|       ;. ;--`:_:.  *| /   /
    |__| |_]|    ,-' . :uu-'/     \|UUU/
    |_______|   ;_|_|_/    :_;_;_;_:
        [=====]

    """

    """
    Its an eternal loop, until q is pressed.
    It should check the choice done by the user and call a appropriate
    function.
    """
    bag = []

    while True:
        print(chr(27) + "[2J" + chr(27) + "[;H")
        print(marvin_image)
        print("Hi, I'm Marvin. I know it all. What can I do you for?")
        print("1) Present yourself to Marvin.")
        print("2) Celsius to Fahrenheit.")
        print("3) Crazy words.")
        print("4) Calculate the total sum and the average sum.")
        print("5) Magic words.")
        print("6) Is it an isogram?")
        print("7) Compare numbers.")
        print("8) Randomize a string.")
        print("9) Make acronym.")
        print("10) Mask a string.")
        print("11) Find all indexes.")
        print("12) Search for a country.")
        print("13) Compare a country's emission.")
        print("14) Print data about a country.")
        print("a1) Characters inluced in the word?")
        print("a2) Double trouble.")
        print("a3) Tab a phrase.")
        print("a4) Crazy names.")
        print("b1) Points to grade.")

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
            string = input("Enter a string to randomize: ")
            print(marvin.randomize_string(string))

        elif choice == "9":
            stringA = input("Enter a string to make an acronym: ")
            print(marvin.get_acronym(stringA))

        elif choice == "10":
            stringB = input("Enter a string to mask it: ")
            print(marvin.mask_string(stringB))

        elif choice == "11":
            inpA = input("Whole string: ")
            inpB = input("Part of string: ")
            print(marvin.find_all_indexes(inpA, inpB))



        elif choice == "12":
            search = input("Search for a country: ")
            try:
                emission_functions.search_country(search)
            except ValueError as a:
                print(str(a))



        elif choice == "13":
            search = input("Enter country and years: ")
            list_choice = search.split(",")
            try:
                print(f"{list_choice[0]}:"\
                f"{emission_functions.get_country_change_for_years(list_choice[0], list_choice[1], list_choice[2])}%")
            except ValueError as a:
                print(str(a))

        elif choice == "14":
            search = input("Enter a country to get its data: ")
            get_data = emission_functions.get_country_data(search)
            emission_functions.print_country_data(get_data)



        elif choice == "a1":
            marvin.a1_contain()

        elif choice == "a2":
            marvin.a2_number()

        elif choice == "a3":
            marvin.a3_frenzy()

        elif choice == "a4":
            marvin.a4_crazy()

        elif choice == "b1":
            inpC = input("Enter max points: ")
            inpD = input("Enter your point: ")
            print(marvin.points_to_grade(inpC, inpD))

        elif choice.startswith("inv pick"):
            list_choice = choice.split(" ") # first value always bag-list
            # example ["inv", "pick", "flower", "2"]
            #print(bag)
            if len(list_choice) == 3:
                #print("pick index")
                inventory.pick(bag, list_choice[2])

            elif len(list_choice) == 4:
                #print("pick index")
                inventory.pick(bag, list_choice[2], list_choice[3])

        elif choice.startswith("inv swap"):
            list_choice = choice.split(" ") # first value always bag-list
            inventory.swap(bag, list_choice[2], list_choice[3])

        elif choice.startswith("inv drop"):
            list_choice = choice.split(" ") # first value always bag-list
            inventory.drop(bag, list_choice[2])

        elif choice.startswith("inv"): # if only "inv" input
            inventory.inventory(bag)

        else:
            print("That is not a valid choice. You can only choose from the menu.")

        input("\nPress enter to continue...")



if __name__ == "__main__":
    main()
