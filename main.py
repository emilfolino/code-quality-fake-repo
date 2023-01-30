    #!/usr/bin/env python3
    # -*- coding: utf-8 -*-




"""
Alf with a simple menu to start up with.
Alf doesnt do anything, just presents a menu with some choices.
You should add functinoality to Alf.
"""

import marvin
import inventory
import emission_functions


alf_image = r"""
.     .       .  .   . .   .   . .    +  .
  .     .  :     .    .. :. .___---------___.
       .  .   .    .  :.:. _".^ .^ ^.  '.. :"-_. .
    .  :       .  .  .:../:            . .^  :.:\.
        .   . :: +. :.:/: .   .    .        . . .:\
 .  :    .     . _ :::/:               .  ^ .  . .:\
  .. . .   . - : :.:./.                        .  .:\
  .      .     . :..|:                    .  .  ^. .:|
    .       . : : ..||        .                . . !:|
  .     . . . ::. ::\(                           . :)/
 .   .     : . : .:.|. ######              .#######::|
  :.. .  :-  : .:  ::|.#######           ..########:|
 .  .  .  ..  .  .. :\ ########          :######## :/
  .        .+ :: : -.:\ ########       . ########.:/
    .  .+   . . . . :.:\. #######       #######..:/
      :: . . . . ::.:..:.\           .   .   ..:/
   .   .   .  .. :  -::::.\.       | |     . .:/
      .  :  .  .  .-:.":.::.\             ..:/
 .      -.   . . . .: .:::.:.\.           .:/
.   .   .  :      : ....::_:..:\   ___.  :/
   .   .  .   .:. .. .  .: :.:.:\       :/
     +   .   .   : . ::. :.:. .:.|\  .:/|
     .         +   .  .  ...:: ..|  --.:|
.      . . .   .  .  . ... :..:.."(  ..)"
 .   .       .      :  .   .: ::/  .  .::\
"""
def main():
    """
    Its an eternal loop, until q is pressed.
    It should check the choice done by the user and call a appropriate
    function.
    """
    backpack = []
    while True:
        print(chr(27) + "[2J" + chr(27) + "[;H")
        print(alf_image)
        print("Hi, I'm Alf. I know almost everything. Choose something wise before i loose interest!\n")
        print("1) Your interesting name please.")
        print("2) Convert Celsius to Fahrenheit.")
        print("3) Magic with words(learned in space.)")
        print("4) Sum and average.")
        print("5) Wordlearning.")
        print("6) Isogram test.")
        print("7) Larger! Smaller! Same! (popular game in space).")
        print("8) Make a string magically shuffle.")
        print("9) Make a acronym out of a string.")
        print("10) Masking your string.")
        print("11) Find indexes for second string in first.")
        print("12) Search for country.")
        print("13) Show emission change for country.")
        print("14) Show all data for a country.")
        print("q) Quit.")


        print('\n\n\nTry out my "inv" commands!')
        print("-------------------------------------------------")
        choice = input("--> ")


        if choice == "q":
            print("Bye, bye - hope we meet again!")
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

            a_string = input("input a string for my brain to shuffle: ")
            print(marvin.randomize_string(a_string))

        elif choice == "9":

            name = input("input a string: ")
            print(marvin.get_acronym(name))

        elif choice == "10":

            string = input("Input a string for me to mask: ")
            print(marvin.mask_string(string))

        elif choice == "11":

            string = input("Input a string: ")
            substring = input("Input a substring")
            print(marvin.find_all_indexes(string, substring))

        elif choice == "12":

            inp = input("Enter a country name or part of a country name to see if it exist: ")

            try:
                print("\n".join(emission_functions.search_country(inp)))
            except ValueError:
                print("Country does not exist!")

        elif choice == "13":

            inp = input("Enter country year and year: ")

            try:
                inp = inp.split(",")
                change = emission_functions.get_country_change_for_years(inp[0], inp[1], inp[2])
                print(f"{inp[0]}:{change}%")
            except IndexError:
                print("Wrong year!")
            except ValueError:
                print("Wrong year!")

        elif choice == "14":

            inp = input("Enter country: ")

            data = emission_functions.get_country_data(inp)
            emission_functions.print_country_data(data)

        elif choice == "inv":

            inventory.inventory(backpack)

        elif choice[:8] == "inv pick":

            choice_list = choice.split(" ")
            item = choice_list[2]
            try:
                bag_index = choice_list[3]
            except IndexError:
                bag_index = -1

            print(inventory.pick(backpack, item, bag_index))

        elif choice[:8] == "inv drop":

            choice_list = choice.split(" ")
            item = choice_list[2]

            print(inventory.drop(backpack, item))

        elif choice[:8] == "inv swap":

            choice_list = choice.split(" ")
            try:
                item_1 = choice_list[2]
                item_2 = choice_list[3]
                print(inventory.swap(backpack, item_1, item_2))
            except IndexError:
                print(f"Error: not in bag! \nItems in bag: {backpack}")

        else:
            print("That is not a valid choice. You can only choose from the menu.")

        input("\nPress enter to continue...")
        continue








if __name__ == "__main__":
    main()
