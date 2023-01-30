'''
min main fil
'''
import marvin
import inventory
import emission_functions


def main():
    ''' min func '''
    marvin_image = r"""
                _____
            _-~~     ~~-_//
        /~             ~\
        |              _  |_
        |         _--~~~ )~~ )___
        \|        /   ___   _-~   ~-_
        \          _-~   ~-_         \
        |         /         \         |
        |        |           |     (O  |
        |      |             |        |
        |      |   O)        |       |
        /|      |           |       /
        / \ _--_ \         /-_   _-~)
        /~    \ ~-_   _-~   ~~~__/
        |   |\  ~-_ ~~~ _-~~---~  \
        |   | |    ~--~~  / \      ~-_
        |   \ |                      ~-_
            \   ~-|                        ~~--__ _-~~-,
            ~-_   |                             /     |
                ~~--|                                 /
                |  |                               /
                |   |              _            _-~
                |  /~~--_   __---~~          _-~
                |  \                   __--~~
                |  |~~--__     ___---~~
                |  |      ~~~~~
                |  |
        """
    backpack = []
    
    while True:
        
        list_in = []

    #kmom 03
        print(chr(27) + "[2J" + chr(27) + "[;H")
        print(marvin_image)
        print("Hi, I'm Marvin. I know it all. What can I do you for?")
        print("1: Let us introduce ourself")
        print("2: Let me translate celsius to fahrenheit for you")
        print("3: Let me multiply a word for you")
        print("4: Let me sum up your numbers and give you the average amount")
        print("5: Let me change your string a little")
        print("6: Let me check if a word is a isogram")
        print("7: Let me compare numbers to eachother")
        print("8: Let me randomize some words")
        print("9: Let me make you a acronym")
        print("10: Let me mask your word")
        print("11: Let me find all indexes in your word")
    
    #kmom 04
        print("\ninv pick []: to add to inventory")
        print("inv: to see inventory")
        print("inv drop []: to remove from inventory")
        print("inv swap [] []: to swap items in inventory")
    
    #kmom 05
        print("\n12: Search emission_data.py for countries")
        print("13: Compare emission for a country")
        print("14: Print facts about a country")


        print("q: Quit.")

        choice = input("--> ")

        if choice == "q":
            print("Bye, bye - and welcome back anytime!")
            break


    #kmom 03
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
            print(marvin.randomize_string(input("Enter a string to randomize: ")))
        elif choice == "9":
            print(marvin.get_acronym(input("Enter name for me to acronymise: ")))
        elif choice == "10":
            print(marvin.mask_string(input("Enter string for me to mask: ")))
        elif choice == "11":
            print(marvin.find_all_indexes(input("Enter first string: "), input("Enter second string: ")))

    #kmom 04
        elif choice.startswith("inv pick"):
            list_in = choice.split(" ")
            if len(list_in) == 3: #ifall inget index angivits
                backpack = inventory.pick(backpack, list_in[2])
            else:
                backpack = inventory.pick(backpack, list_in[2], list_in[3])

        elif choice == "inv":
            inventory.inventory(backpack)

        elif choice.startswith("inv drop"):
            list_in = choice.split(" ")
            try:
                backpack = inventory.drop(backpack, list_in[2])
            except IndexError:
                print("Error: not enough inputs")

        elif choice.startswith("inv swap"):
            list_in = choice.split(" ")
            try:
                backpack = inventory.swap(backpack, list_in[2], list_in[3])
            except IndexError:
                print("Error: not enough inputs")

    #kmom 05
        elif choice == "12":
            try:
                out_data = emission_functions.search_country(input("country --> "))
                print(out_data)
            except (TypeError, ValueError):
                print("Country does not exist!")

        elif choice == "13":
            try:
                inputer = input("country -->, year 1 -->, year 2 -->  ")
                inputList = inputer.split(",")
                country = inputList[0]
                year1 = inputList[1]
                year2 = inputList[2]
                print(country + ":" + str(emission_functions.get_country_change_for_years(country, year1, year2)) + "%")
            except (TypeError, ValueError, IndexError):
                print("Country does not exist! or Wrong year!")

        elif choice == "14":
            emission_functions.print_country_data(input("country --> "))


        else:
            print("Your input did not Match anything. You can only choose from the menu.")

        input("\nPress enter to continue...")

if __name__ == "__main__":
    main()
