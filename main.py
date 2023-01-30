"""
This is the main file where all code is assembled
"""

import marvin
import inventory
import emission_functions

def main():
    """
    This will contain the code for while-loop for Marvin program
    """
    backpack = []

    marvin_image = r"""
    
       /\     /\
      {  `---'  }
      {  O   O  }
      ~~>  V  <~~
       \  \|/  /
        `-----'__
        /     \  `^\_
           {       }\ |\_\_   W
       |  \_/  |/ /  \_\_( )
        \__/  /(_E     \__/
          (  /
           MM
    """

    """
    Its an eternal loop, until q is pressed.
    It should check the choice done by the user and call a appropriate
    function.
    """
    #Menu options are presented:
    while True:
        print(chr(27) + "[2J" + chr(27) + "[;H")
        print(marvin_image)
        print("""
        Hi there, Marvin here! I've got all the answers to the questions you're pondering! So feel free to ask me what you want to know! What can I do you for?
        """)
        print("1) Present yourself to Marvin.")
        print("2) Celsius to fahrenheit.")
        print("3) Word repetition.")
        print("4) Sum and average.")
        print("5) Recreating a string by gradual multiplication of letters.")
        print("6) Isogram validator.")
        print("7) Number sizing indicator") #Prints "smaller", "larger", or "same" depending on current number
        print("a1) Check word in word.")
        print("a3) Replace tab with 3 spaces.")
        print("8) Randomize word.")
        print("9) Convert a word or string into acronym with the upper case letters.")
        print("10) Mask all but the four last letters of a string.")
        print("11) Find all indexes.")
        print("b1) Grading points.")
        print("b2) Check strings in string.")
        print("q) Quit.")
        print("12) Search country")
        print("13) Change in country's emission data")
        print("14) Country data") # Fix!!
        print("e1) Ranking countries with highest emission in year.")
        print("e2) Ranking countries with highest emission per capita in year.")
        print("e3) Ranking countries with highest emission per area in year")

        print("\n")
        print("""
Try out my inv commands:

'inv' to check your inventory items
'inv pick' to pick up items and place in bag 
'inv drop' to drop an item in your bag
'inv swap' to swap places of two items in your bag
        """)

        choice = input("--> ")
    
        if choice == "q":
            print("Bye, bye - and welcome back anytime!")
            break

        elif choice == "1":
            marvin.greet()

        elif choice == "2":
            marvin.celsius_to_fahrenheit()

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

        elif choice == "a1":
            marvin.word_in_word()

        elif choice == "a3":
            marvin.replace_tab_in_string()

        elif choice == "8":
            original_word = input("Enter a word: ")
            print(marvin.randomize_string(original_word))

        elif choice == "9":
            user_string = input("Enter a string: ")
            print(marvin.get_acronym(user_string))

        elif choice == "10":
            word_to_mask = input("Enter a word: ")
            print(marvin.mask_string(word_to_mask))

        elif choice == "11":
            string = input("Enter a string: ")
            substring = input("Enter a substring that exists within the string: ")
            print(marvin.find_all_indexes(string, substring))

        elif choice == "b1":
            maximum_points = input("Enter the maximum amount of points: ")
            your_points = input("Enter your points: ")
            print(marvin.points_to_grade(your_points, maximum_points))

        elif choice == "b2":
            str1 = input("Enter your first word: ")
            str2 = input("Enter your other word/prefix: ")
            str3 = input("Enter your third word: ")
            str4 = input("Enter your fourth word/suffix: ")
            print(marvin.has_strings(str1, str2, str3, str4))

        elif choice == "inv":
            inventory.inventory(backpack)
            
        elif choice.startswith("inv pick"):
            split_choice = choice.split(" ")
            if len(split_choice) == 4:
                item = split_choice[2]
                place = split_choice[3]
                print(inventory.pick(backpack, item, place))
            elif len(split_choice) == 3:
                item = split_choice[-1]
                print(inventory.pick(backpack, item))

        elif choice.startswith("inv drop"):
            split_choice = choice.split(" ")
            item_to_drop = split_choice[2]
            inventory.drop(backpack, item_to_drop)

        elif choice.startswith("inv swap"):
            split_choice = choice.split(" ")
            item1 = split_choice[2]
            item2 = split_choice[3]
            inventory.swap(backpack, item1, item2)

        elif choice == "12":
            search_word = input("Search for country: ")
            try:
                matching = emission_functions.search_country(search_word)
                print("Following countries were found: " + (", ".join(matching)))
            except ValueError as e:
                print(str(e))

        elif choice == "13":
            inp = input("Enter 'country,year1,year2': ")
            country, year1, year2 = inp.split(",")
            try:
                change = emission_functions.get_country_change_for_years(country, year1, year2)
                print(f"{country}:{change}%")
            except ValueError as er:
                print(str(er))

        elif choice == "14":
            inp = input("Enter a country: ")
            data = emission_functions.get_country_data(inp)
            emission_functions.print_country_data(data)

        elif choice == "e1":
            inp = input("Enter 'year number': ")
            year, number = inp.split(" ")
            try:
                number = int(number)
            except ValueError:
                print("Number is not a valid number.")
            try:
                emission_functions.print_country_emmission_in_year(year, number)
            except ValueError as e:
                print(str(e))
        
        elif choice == "e2":
            inp = input("Enter 'year number': ")
            year, number = inp.split(" ")
            try:
                number = int(number)
            except ValueError:
                print("Number is not a valid number.")
            try:
                emission_functions.emission_per_capita(year, number)
            except ValueError as e:
                print(str(e))

        elif choice == "e3":
            inp = input("Enter 'year number': ")
            year, number = inp.split(" ")
            try:
                number = int(number)
            except ValueError:
                print("Number is not a valid number.")
            try:
                emission_functions.emission_per_area(year, number)
            except ValueError as e:
                print(str(e))

        else:
            print("That is not a valid choice. You can only choose from the menu.")

        input("\nPress enter to continue...")

if __name__ == "__main__":
    main()
