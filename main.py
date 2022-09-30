"""
The module docstring for marvin2.
"""

import marvin
import inventory
import emission_functions

def main():
    """ The function which our marvin-menu lies within. """
    backpack = []

    marvin_image = r"""
                        . . . .
                        ,`,`,`,`,
    . . . .               `\`\`\`\;
    `\`\`\`\`,            ~|;!;!;\!
    ~\;\;\;\|\          (--,!!!~`!       .
    (--,\\\===~\         (--,|||~`!     ./
    (--,\\\===~\         `,-,~,=,:. _,//
    (--,\\\==~`\        ~-=~-.---|\;/J,
    (--,\\\((```==.    ~'`~/       a |
        (-,.\\('('(`\\.  ~'=~|     \_.  \
            (,--(,(,(,'\\. ~'=|       \\_;>
            (,-( ,(,(,;\\ ~=/        \
            (,-/ (.(.(,;\\,/          )
            (,--/,;,;,;,\\         ./------.
                (==,-;-'`;'         /_,----`. \
        ,.--_,__.-'                    `--.  ` \
        (='~-_,--/        ,       ,!,___--. \  \_)
    (-/~(     |         \   ,_-         | ) /_|
    (~/((\    )\._,      |-'         _,/ /
        \\))))  /   ./~.    |           \_\;
    ,__/////  /   /    )  /
    '===~'   |  |    (, <.
            / /       \. \
            _/ /          \_\
            /_!/            >_\
    """

    """
    Its an eternal loop, until q is pressed.
    It should check the choice done by the user and call a appropriate
    function.
    """
    while True:
        print(chr(27) + "[2J" + chr(27) + "[;H")
        print(marvin_image)
        print("Nghhhh--Hi! You're in the presence of Marvin, the all-neighing Unicorn. How may I assist?")
        print("1) Present yourself to Marvin.")
        print("2) Celsius to Farenheit")
        print("3) Word multiplication")
        print("4) Sum and average")
        print("5) Give me a string and you'll get it back, transformed!")
        print("6) Let me check if your word is an isogram!")
        print("7) Present me with a number!") 
        print("8) the String Randomizer!")
        print("9) the Acronym Maker!")
        print("10) the Mysterious String!")
        print("11) Find all the indexes!")
        print("    Or enter 'inv pick' and an item and put in Marvin's backpack! ")
        print("    Enter 'inv' to see how many and which items are in the backpack! ")
        print("    Enter 'inv drop' to drop items from the backpack! ")
        print("    Enter 'inv swap' to swap places between two items in the backpack! ")
        print("12) Search for a country")
        print("13) Show emission data for country")
        print("14) Show all data for a country")


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
            marvin.word_manipulator()

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
            marvin.randomize_string(string)

        elif choice == "9":
            string_9 = input("Write some words, both in lower and upper case: ")
            marvin.get_acronym(string_9)

        elif choice == "10":
            string_10_string = input("Write me a sentance: ")
            marvin.mask_string(string_10_string)

        elif choice == "11":
            string_11_a = input("Write a word: ")
            string_11_b = input("Write a character: ")
            marvin.find_all_indexes(string_11_a, string_11_b)

        elif choice == "12":
            try:
                search_word = str(input("Enter a part of or the country name to see if we have information in store: "))
                emission_functions.search_country(search_word)

            except ValueError as wrong_message:
                print(wrong_message)

        elif choice == "13":
            try: 
                input_13 = input("Write a country, a year, one more year: ")
                list_13 = input_13.split(",")
                country = list_13[0]
                year1 = list_13[1]
                year2 = list_13[2]

                emission_difference_procent = emission_functions.get_country_change_for_years(country, year1, year2)
                print(country + ":" + str(emission_difference_procent) + "%")

            except ValueError as wrong_message:
                print(wrong_message)


        elif choice == "14":
            try:
                country_name = input("Enter a country: ")

                country_data = emission_functions.get_country_data(country_name)

                emission_functions.print_country_data(country_data)

            except ValueError as wrong_message:
                print(wrong_message)





        else:
            list_a = choice.split()
            if list_a[0] == "inv":
                if len(list_a) > 1:
                    if list_a[1] == "pick" and len(list_a) == 4:
                        backpack = inventory.pick(backpack, list_a[2], list_a[3]) #2, item. 3, index.
                    elif list_a[1] == "pick" and len(list_a) < 4:
                        backpack = inventory.pick(backpack, list_a[2]) #2, item.
                    if list_a[1] == "drop":
                        inventory.drop(backpack, list_a[2])
                    if list_a[1] == "swap" and len(list_a) == 4:
                        backpack = inventory.swap(backpack, list_a[2], list_a[3])
                    elif list_a[1] == "swap" and len(list_a) < 4:
                        print("Hey, I can't swap it with itself!")
                else:
                    inventory.inventory(backpack)




        input("Press 'enter' to continue!")




if __name__ == "__main__":
    main()
