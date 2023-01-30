"""
Torkel with a simple menu to start up with.
Torkel doesnt do anything, just presents a menu with some choices.
You should add functinoality to Torkel.
"""
import marvin
import inventory
import emission_functions

torkel_image = r"""
     .--.   |V|
     /    \ _| /
     q .. p \ /
      \--/  //
     __||__//
    /.    _/
   // \  /
  //   ||
  \\  /  \
   )\|    |
  / || || |
  |/\| || |
     | || |
     \ || /
   __/ || \__
  \____/\____/
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
        print(torkel_image)
        print("Hi, I'm Torkel. I can answer all your questions. What can I do you for?")
        print("1) Present yourself to Torkel.")
        print("2) Celsius to farenheit")
        print("3) You say it! I repeat it!")
        print("4) I will do some math for you!")
        print("5) I will repeat letters in word")
        print("6) Isogram")
        print("7) Smaller, Larger or Equal")
        print("8) Randomize an string!")
        print("9) Get an acronym of an string!")
        print("10) I will mask an string for you!")
        print("11) I will find all indexes for you!")
        print("12) Search for country!")
        print("13) Show emission change for a country!")
        print("14) Show all data for a country!")
        print("A1) Check if all letter in a word")
        print("A2) Match brackets")
        print("q) Quit.")
        print("Try out Torkels inv command!")

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
            string = input("Enter a string to get an acronym: ")
            print(marvin.get_acronym(string))
        elif choice == "10":
            string = input("Enter a string and i will mask it for you: ")
            print(marvin.mask_string(string))
        elif choice == "11":
            string = input("Enter a string: ")
            index = input("Enter the number och character you want to find the index of: ")
            print(marvin.find_all_indexes(string, index))
        elif choice == "12":
            search_word = input("Search for an country: ")
            try:
                print(emission_functions.search_country(search_word))
            except ValueError:
                print("Country does not exist!")
        elif choice == "13":
            search_word = input("Enter a country, year and year: ")
            fixed_word = search_word.split(",")
            try:
                if len(fixed_word) > 2:
                    print(fixed_word[0]+":"+
                        str(emission_functions.get_country_change_for_years(
                            fixed_word[0], fixed_word[1], fixed_word[2])) + "%")
                else:
                    print("You need to write one country and two years in the format ´Country,Year,Year´")
            except ValueError:
                print("Wrong year!")
        elif choice == "14":
            input_country = input("Enter country: ")
            emission_functions.get_country_data(input_country)
        elif choice.startswith("inv pick"):
            fixed_choice = choice.split(" ")
            index = -1
            item = -1
            if len(fixed_choice) >= 3:
                item = fixed_choice[2]
            else:
                print("You need to write an item to pick.")
    
            if len(fixed_choice) == 4:
                index = fixed_choice[3]

            backpack = inventory.pick(backpack, item, index)
        elif choice.startswith("inv drop"):
            fixed_choice = choice.split(" ")
            if len(fixed_choice) == 3:
                item = fixed_choice[2]
                backpack = inventory.drop(backpack, item)
            else:
                print("You need to write an item to drop.")
        elif choice.startswith("inv swap"):
            fixed_choice = choice.split(" ")
            if len(fixed_choice) == 4:
                item_one = fixed_choice[2]
                item_two = fixed_choice[3]
                backpack = inventory.swap(backpack, item_one, item_two)
            else:
                print("You need to write to items to swap place.")
        elif choice == "inv":
            inventory.inventory(backpack)
        else:
            print("That is not a valid choice. You can only choose from the menu.")

        input("\nPress enter to continue...")


if __name__ == "__main__":
    main()
