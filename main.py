"""
Detta är en modul string.
"""

import inventory
import marvin
import emission_functions


def handle_menu(choice):
    """
    This is the main function of the program, which triggers the workflow of the program.
    """
    if choice == "1":
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
        string = input("Enter a string to get the acronym for: ")
        print(marvin.get_acronym(string))

    elif choice == "10":
        string = input("Enter a string to mask: ")
        print(marvin.mask_string(string))

    elif choice == "11":
        string = input("Enter a string: ")
        sub_string = input("Enter a substring: ")
        print(marvin.find_all_indexes(string, sub_string))

    elif choice == "12":
        search_word = input("Enter a string: ")
        try:
            countries = emission_functions.search_country(search_word)
            print("Following countries were found: ")
            for country in countries:
                print(country)
        except ValueError as e:
            print(e)

    elif choice == "13":
        comma_separated_string = input("Enter a comma-separated string: ")
        string_list = comma_separated_string.split(",")
        country = string_list[0]
        year1 = string_list[1]
        year2 = string_list[2]
        try:
            emission_change = str(emission_functions.get_country_change_for_years(country, year1, year2))
            print(country + ":" + emission_change + "%")
        except ValueError as e:
            print(e)

    elif choice == "14":
        country_name = input("Enter a country: ")
        data = emission_functions.get_country_data(country_name)
        emission_functions.print_country_data(data)


def main():
    """
    Detta är den main som hanterar den uppdaterade menyn
    """
    bag = []
    marvin.printMenu()
    inventory.printInvAdd()
    run = True
    while run:
        choice = input(">>> ")
        commando = choice.split(" ")
        if len(commando) >= 1 and commando[0] == "inv":

            if len(commando) == 1:
                inventory.inventory(bag)
            else:
                if len(commando) >= 3 and commando[1] == "pick":
                    if len(commando) == 3:
                        bag = inventory.pick(bag, commando[2])
                    else:
                        bag = inventory.pick(bag, commando[2], int(commando[3]))


                if len(commando) > 3 and commando[1] == "swap":
                    bag = inventory.swap(bag, commando[2], commando[3])

                if len(commando) >= 3 and commando[1] == "drop":
                    bag = inventory.drop(bag, commando[2])

        if choice == "":
            continue

        if marvin.choiceIsApplicable(choice):
            handle_menu(choice)
            input("\nPress enter to continue...")
            marvin.printMenu()
            inventory.printInvAdd()

        if choice in "q" "Q":
            run = False


if __name__ == '__main__':
    main()
