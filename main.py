"Main module for Marvin"
import marvin
import inventory
import emission_functions

backpack = []


def main():
    """
    Main method for Marvin
    """
    while True:
        print(chr(27) + "[2J" + chr(27) + "[;H")
        print(marvin.marvin_image)
        print(f"Hello human, I'm {marvin.ROBOT_NAME}. I am all knowing, what do you want from me?")
        print("1) Present yourself to Marvin.")
        print("2) Convert celsius to Farnheit.")
        print("3) Simulate a parrot.")
        print("4) Sum numbers and get average.")
        print("5) Slow motion words.")
        print("6) Check if isogram.")
        print("7) Number comparator.")
        print("8) Word shuffler.")
        print("9) Acronym Generator.")
        print("10) Mask a string.")
        print("11) Find locations of characters in a string.")
        print("12) Search for countries in emissions database.")
        print("13) Get difference in a country's emissions between two years.")
        print("14) Get all emission data for one country.")
        print("inv pick <item> [position]) Pick up <item> and put in backpack.")
        print("inv swap <item> <item2>): Swap positions of item1 and item2 in the backpack")
        print("inv drop <item>): Remove item from backpack.")
        print("inv): Display the inventory in the backpack.")

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
            string_to_shuffle = input("Enter a string to shuffle: ")
            print(marvin.randomize_string(string_to_shuffle))
        elif choice == "9":
            string_to_acronymisize = input("Enter a string to acronymisize: ")
            print(marvin.get_acronym(string_to_acronymisize))
        elif choice == "10":
            string_to_mask = input(
                "Enter a word or sentance and I will mask everythin but the last four characters: "
            )
            print(marvin.mask_string(string_to_mask))
        elif choice == "11":
            print(
                "Enter two strings. The first a searchable string. The second a substring you want"
                " to search for within the first."
            )
            print("I will print all locations of the substring.")
            base_string = input("Enter searchable string: ")
            substring = input("Enter substring to search for: ")
            print(marvin.find_all_indexes(base_string, substring))
        elif choice == "12":
            search_string = input("Search for a country (partial names are OK): ")
            try:
                countries = emission_functions.search_country(search_string)
                print(
                    f"Following countries were found: {emission_functions.format_list(countries)}"
                )
            except ValueError:
                print("Country does not exist!")
        elif choice == "13":
            args = input(
                "Enter country, beginning year, and ending year separated by a comma. Valid years"
                " are (1990, 2005 and 2017): "
            )
            split_args = args.split(",")
            country = split_args[0]
            year1 = split_args[1]
            year2 = split_args[2]
            try:
                change = emission_functions.get_country_change_for_years(country, year1, year2)
                print(f"{country}:{change}%")
            except ValueError:
                print("Wrong year!")
        elif choice == "14":
            country = input("Enter the country you want the data from: ")
            country_data = emission_functions.get_country_data(country)
            emission_functions.print_country_data(country_data)
        elif choice.split(" ")[0] == "inv":
            arg_list = choice.split(" ")
            n_args = len(arg_list)
            if n_args > 1:
                cmd = arg_list[1]
                item = arg_list[2]
                if n_args == 4:
                    item_or_pos = arg_list[3]
                if cmd == "pick":
                    if n_args == 4:
                        inventory.pick(backpack, item, int(item_or_pos))
                    else:
                        inventory.pick(backpack, item)
                elif cmd == "drop":
                    inventory.drop(backpack, item)
                elif cmd == "swap":
                    inventory.swap(backpack, item, item_or_pos)
            else:
                inventory.inventory(backpack)

        else:
            print("That is not a valid choice. You can only choose from the menu.")
        input("\nPress enter to continue...")


if __name__ == "__main__":
    main()
