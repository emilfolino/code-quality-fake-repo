""" Main to marvin """

import marvin as marvin1
import inventory as inventory1

marvin_image = r"""
              ____
          \__/         # ##
         `(  `^=_ p _###_
          c   /  )  |   /
   _____- //^---~  _c  3
 /  ----^\ /^_\   / --,-
(   |  |  O_| \\_/  ,/
|   |  | / \|  `-- /
(((G   |-----|
      //-----\\
     //       \\
   /   |     |  ^|
   |   |     |   |
   |____|    |____|
  /______)   (_____\

"""

"""
Its an eternal loop, until q is pressed.
It should check the choice done by the user and call a appropriate
function.
"""
def main():
    """ Marvin main function """

    backpack = []

    while True:
        print(chr(27) + "[2J" + chr(27) + "[;H")
        print(marvin_image)
        print("Hi, I'm Marvin. I know it all. What can I do you for?")
        print("1) Present yourself to Marvin.")
        print("2) Celcius to farenheit.")
        print("3) Lets play parrot! You say it, i'll repeat it.")
        print("4) Sure I can do your math for you.")
        print("5) Repeat letters in a word.")
        print("6) Isogram.")
        print("7) Is smaller, bigger or equal.")
        print("8) Randomize word")
        print("9) Acronym maker")
        print("10) Mask string")
        print("11) Find all indexes")
        print("12) Search for country")
        print("13) Emission change for country")
        print("14) Show data for a country")
        print("a1) Check if all letters in a word.")
        print("a2) Check when number includes all digits")
        print("a3) Use the tab converter")
        print("a4) Let me put to names together for you")
        print("a5) Count points")
        print("b1) Points to grade")
        print("q) Quit)")
        print("\n")
        print("Try out my 'inv' commands!")
        print("--------------------------")

        choice = input("--> ")

        if choice == "q":
            print("Bye, bye - and welcome back anytime!")
            break

        elif choice == "1":
            marvin1.greet()
        elif choice == "2":
            marvin1.celcius_to_farenheit()
        elif choice == "3":
            marvin1.word_manipulation()
        elif choice == "4":
            marvin1.sum_and_average()
        elif choice == "5":
            marvin1.hyphen_string()
        elif choice == "6":
            marvin1.is_isogram()
        elif choice == "7":
            marvin1.compare_numbers()
        elif choice == "8":
            string = input("Enter a string to randomize: ")
            print(marvin1.randomize_string(string))
        elif choice == "9":
            string = input("Enter a string to make an acronym of: ")
            print(marvin1.get_acronym(string))
        elif choice == "10":
            string = input("Enter a string to mask: ")
            print(marvin1.mask_string(string))
        elif choice == "11":
            string = input("Enter a string: ")
            partstring = input("Enter a part-string to check indexes: ")
            print(marvin1.find_all_indexes(string, partstring))
        elif choice == "12":
            country = input("What country are you looking for?: ")
            print(marvin1.search_function(country))
        elif choice == "13":
            input_info = input("Enter country, year and year: ")
            input_split = input_info.split(",")
            if len(input_split) == 3:
                print(marvin1.change_function(input_split[0], input_split[1], input_split[2]))
            else:
                print("Make sure to enter country, year and year")
        elif choice == "14":
            country = input("Enter a country: ")
            print(marvin1.data_function(country))
        elif choice == "a1":
            marvin1.word_exist()
        elif choice == "a2":
            marvin1.multiply_number()
        elif choice == "a3":
            marvin1.tab_converter()
        elif choice == "a4":
            marvin1.consunants_vowels()
        elif choice == "a5":
            marvin1.score_line()
        elif choice == "b1":
            maxpoints = input("Enter max points: ")
            mypoints = input("Enter your points: ")
            try:
                print(marvin1.points_to_grade(int(maxpoints), int(mypoints)))
            except ValueError:
                print("Your points must be numeric...")

        elif choice == "inv":
            inventory1.inventory(backpack)

        elif "inv pick" in choice:
            choice_params = choice.split()
            if len(choice_params) < 3:
                print("Error: You have to pick an item")
            elif len(choice_params) == 3:
                print(inventory1.pick(backpack, choice_params[2]))
            elif len(choice_params) == 4:
                print(inventory1.pick(backpack, choice_params[2], choice_params[3]))
            elif len(choice_params) > 4:
                print("Error: You can not enter more than the item and the position")

        elif "inv drop" in choice:
            choice_params = choice.split()
            if len(choice_params) < 3:
                print("Error: You have to pick an item")
            elif len(choice_params) == 3:
                inventory1.drop(backpack, choice_params[2])
            elif len(choice_params) > 3:
                print("Error: You can only drop one item at a time.")
                

        elif "inv swap" in choice:
            choice_params = choice.split()
            if len(choice_params) < 4:
                print("Error: You have to pick two items")
            elif len(choice_params) == 4:
                inventory1.swap(backpack, choice_params[2], choice_params[3])
            elif len(choice_params) > 4:
                print("Error: You can only swap two items at a time.")
        else:
            print("That is not a valid choice. You can only choose from the menu.")

        input("Press enter to continue...")


if __name__ == "__main__":
    main()
