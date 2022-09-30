"""
Main program for marvin
"""
import marvin
import inventory
import emission_functions
marvin_image = r"""
                                  _____
                                 |     |
                                 | | | |
                                 |_____|
                           ____ ___|_|___ ____
                          ()___)         ()___)
                          // /|           |\ \\
                         // / |           | \ \\
                        (___) |___________| (___)
                        (___)   (_______)   (___)
                        (___)     (___)     (___)
                        (___)      |_|      (___)
                        (___)  ___/___\___   | |
                         | |  |           |  | |
                         | |  |___________| /___\
                        /___\  |||     ||| //   \\
                       //   \\ |||     ||| \\   //
                       \\   // |||     |||  \\ //
                        \\ // ()__)   (__()
                              ///       \\\
                             ///         \\\
                           _///___     ___\\\_
                          |_______|   |_______|
"""


def main():
    """
    Marvin the bot 2.0
    """
    bag = []
    while True:
        print(chr(27) + "[2J" + chr(27) + "[;H")
        print(marvin_image)
        print("Hi, I'm Marvin. I know it all. What can I do you for?")
        print("1) Present yourself to Marvin.")
        print("2) Convert celcius into fahrenheit")
        print("3) Word multiplyer")
        print("4) Sum and avrage finder")
        print("5) Word play!")
        print("6) Isogram finder")
        print("7) Number compare")
        print("8) randomzie a string")
        print("9) get acronym")
        print("10) mask the string")
        print("11) find all indexes")
        print("12) search for country")
        print("13) compare diff year:")
        print("14) get country data:")
        print("q) Quit.")
        print('Try out my new "inv" commands!')
        choice = input("--> ")

        if choice == "q":
            print("Bye, bye - and welcome back anytime!")
            break

        elif choice == "1":
            marvin.greet()

        elif choice == "2":
            try:    
                marvin.celcius_to_farenheit()
                
            except ValueError:

                marvin.error_message()
                
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
            rand_word = input("Enter a string to randomize: ")
            print (marvin.randomize_string(rand_word))
            
        elif choice == "9":
            acronym_create = input("Enter a word to make a acronym: ")
            print(marvin.get_acronym(acronym_create))

        elif choice == "10":
            string_to_mask = input("Input a string to mask: ")
            print(marvin.mask_string(string_to_mask))
        
        elif choice == "11":
            main_string = input(" Enter a string: ")
            sub_string = input(" Enter a sub string: ")

            print(marvin.find_all_indexes(main_string, sub_string))

        elif choice == "12":
            search_for_country = input("Search for country: ")
            try:

                print(emission_functions.search_country(search_for_country))

            except ValueError as e:
                print(e)

        elif choice == "13":
            diff_input = input("Compare country diff: country,year1,year2: ")
            diff_list = diff_input.split(",")
            try:
                print(f"{diff_list[0]}:"\
                    f"{emission_functions.get_country_change_for_years(diff_list[0], diff_list[1], diff_list[2])}%")
            except ValueError as e:
                print(e)
            except IndexError as e:
                print(e)

        elif choice == "14":
            country_to_check = input("type country to check data for: ")
            try:
                data = emission_functions.get_country_data(country_to_check)
                emission_functions.print_country_data(data)
            except ValueError as e:
                print(e)
        
            
        elif choice.startswith("inv pick"):
            str_to_list = choice.split()
            try:
                if len(str_to_list) > 3:
                    digit_pos = str_to_list[3]
                else:
                    digit_pos = None
                inventory.pick(bag, str_to_list[2], digit_pos)
            except IndexError:
                print("Error: Do not forget to enter something to pick")
        
        elif choice.startswith("inv swap"):
            str_to_list = choice.split()
            inventory.swap(bag, str_to_list[2], str_to_list[3])
        elif choice.startswith("inv drop"):
            str_to_list = choice.split()
            inventory.drop(bag, str_to_list[2])
        elif choice.startswith("inv"):
            inventory.inventory(bag)

        else:
            print("That is not a valid choice. You can only choose from the menu.")

        input("\nPress enter to continue...")
if __name__ == "__main__":
    main()
