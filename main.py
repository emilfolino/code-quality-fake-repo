"""
Main code of the marvin program
"""

import marvin
import inventory
import emission_functions

marvin_image = r"""
                             ;;\\/;;;;;;;;
                          ;;;;;;;;;;;;;;;;;
                       ;;;;;;;;;;;;     ;;;;;
                      ;;;;;    ;;;         \;;
                     ;;;;;      ;;          |;
                    ;;;;         ;          |
                    ;;;                     |
                     ;;                     )
                      \    ~~~~ ~~~~~~~    /
                       \    ~~~~~~~  ~~   /
                     |\ \                / /|
                      \\| %%%%%    %%%%% |//
                     [[====================]]
                      | |  ^          ^  | |
                      | | :@: |/  \| :@: | |
                       \______/\  /\______/
                        |     (@\/@)     |
                       /                  \
                      /  ;-----\  ______;  \
                      \         \/         /
                       )                  (
                      /                    \
                      \__                  /
                       \_                _/
                        \______/\/\______/
                         _|    /--\    |_
                        /%%\  /"'"'\  /%%\
         ______________/%%%%\/\'"'"/\/%%%%\______________
        / :  :  :  /  .\%%%%%%%\"'/%%%%%%%/.  \  :  :  : \
       )  :  :  :  \.  .\%%%%%%/'"\%%%%%%/.  ./  :  :  :  (
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
        print(marvin_image)
        print("Hi, I'm Marvin. I know it all. What can I do you for?")
        print("1) Present yourself to Marvin.")
        print("2) Convert celsius too Fahrenheit.")
        print("3) Word multiplication.")
        print("4) Sum and avrage.")
        print("5) Character adding. ")
        print("6) Isogram checker.")
        print("7) Larger, same or smaller.")
        print("8) Randomize word.")
        print("9) Get acronym.")
        print("10) Mask a password.")
        print("11) Find letters in word.")
        print("12) Search for country.")
        print("13) Show emission change for a country.")
        print("14) Show all data for a country.")
        print("q) Quit.")
        print("\n\nTry out my \"inv\" commands!")
        print("-----------------")

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
            marvin.sum_and_avrage()

        elif choice == "5":
            marvin.hyphen_string()

        elif choice == "6":
            marvin.is_isogram()

        elif choice == "7":
            marvin.compare_numbers()

        elif choice == "8":
            word = input("Give me a word you want rearranged. ")
            print("\nMarvin says:\n")
            print(marvin.randomize_string(word))
            print("What can I do you for?!")

        elif choice == "9":
            word = input("Give me a name. ")
            print("\nMarvin says:\n")
            print(marvin.get_acronym(word))
            print("What can I do you for?!")

        elif choice == "10":
            password = input("Give me a password. ")
            print("\nMarvin says:\n")
            print(marvin.mask_string(password))
            print("What can I do you for?!")

        elif choice == "11":
            word = input("give me a word. ")
            part = input("What part are you looking for? ")
            print("\nMarvin says:\n")
            print(marvin.find_all_indexes(word, part))
            print("What can I do you for?!")

        elif choice[:8] == "inv pick":
            pickup = choice.split(" ")
            if len(pickup) == 3:
                backpack = inventory.pick(backpack, pickup[2])
            elif len(pickup) == 4:
                try:
                    backpack = inventory.pick(backpack, pickup[2], pickup[3])
                except ValueError:
                    print("Index need too be a integer")
            else:
                print("Command written wrong!")
                print("inv pick \"item\" \"index\"")

        elif choice[:8] == "inv drop":
            drop_item = choice.split(" ")
            if len(drop_item) == 3:
                backpack = inventory.drop(backpack, drop_item[2])
            else:
                print("Command written wrong!")
                print("inv drop \"item\"")

        elif choice[:8] == "inv swap":
            swap_item = choice.split(" ")
            if len(swap_item) == 4:
                backpack = inventory.swap(backpack, swap_item[2], swap_item[3])
            else:
                print("Command written wrong!")
                print("inv drop \"item\" \"item\"")

        elif choice[:3] == "inv":
            check_inv = choice.split(" ")
            if len(check_inv) == 1:
                inventory.inventory(backpack)
            elif len(check_inv) == 3:
                try:
                    inventory.inventory(backpack, int(check_inv[1]), int(check_inv[2]))
                except ValueError:
                    print("Index need too be a integer")
            else:
                print("Command written wrong!")
                print("inv \"start\" \"end\"")

        elif choice == "12":
            search_word = input("What country are you looking for? ")
            try:
                countries = emission_functions.search_country(search_word)
                found_countries = "Following countries were found: " + countries[0]
                for i in countries[1:]:
                    found_countries += ", " + i
                print("\nMarvin says:\n")
                print(found_countries)
                print("What can I do you for?!")
            except ValueError:
                print("Country does not exist!")

        elif choice == "13":
            emission_input = input("what country and between which years do you want to se the emission change? ")
            emission_change = emission_input.split(",")
            try:
                if len(emission_change) == 3:
                    change = emission_functions.get_country_change_for_years(
                        emission_change[0], emission_change[1], emission_change[2])
                    print("\nMarvin says:\n")
                    print(emission_change[0] + ":" + str(change) + "%.")
                    print("What can I do you for?!")
                else:
                    print("Input written wrong!")
            except ValueError:
                print("Wrong year!")
            except KeyError:
                print("Country does not exist!")

        elif choice == "14":
            country_name = input("What country do you want data from? ")
            try:
                country_data = emission_functions.get_country_data(country_name)
                print("\nMarvin says:\n")
                emission_functions.print_country_data(country_data)
                print("What can I do you for?!")
            except KeyError:
                print("Country does not exist!")

        else:
            print("That is not a valid choice. You can only choose from the menu.")

        input("\nPress enter to continue...")

if __name__ == "__main__":
    main()
