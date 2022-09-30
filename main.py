"""
This is the main file for running the program "marvin", which presents a picture of Homer Simpson's face.
It then gives you eleven different option you can choose from.
Every option calls for a function in the file marvin.py that executes what the option from the menu says it should.
"""
import marvin
import inventory
import emission_functions
Bag = []
def main():
    """
    This function presents the image of Homer and prints all options. Then calls for the other functions,
    engraved in the options from the menu. This function runs as long as this is the executed file,
    expressed in the if-loop at the bottom of this file.
    """
    homer_image = r"""
    ___  _____
    .'/,-Y"     "~-.
    l.Y             ^.
    /\               _\_
    i            ___/"   "\
    |          /"   "\   o !
    l         ]     o !__./
    \ _  _    \.___./    "~\
    X \/ \            ___./
    ( \ ___.   _..--~~"   ~`-.
    ` Z,--   /               \
        \__.  (   /       ______)
        \   l  /-----~~" /
        Y   \          /
        |    "x______.^
        |           \
        j            Y
                        
    """
    while True:
        print(chr(27) + "[2J" + chr(27) + "[;H")
        print(homer_image)
        print("Hello, my name is Homer, what do you want me to do?")
        print("1) Greet Homer.")
        print("2) Convert Celsius to Fahrenheit")
        print("3) Make me do magic with your words.")
        print("4) Sum and average your numbers.")
        print("5) Produce a hyphen string.")
        print("6) Isogram.")
        print("7) Compare numbers' value.")
        print("8) Randomize your input.")
        print("9) Tell you the acronym of your word.")
        print("10) Let me blur out your string except the last four characters: ")
        print("11) Type in a word and then a small part of that word, and I will tell you at what indexes it occurs: ")
        print("inv) Shows the inventory")
        print("inv pick) Add a thing to the inventory")
        print("inv drop) Remove a thing from the inventory")
        print("inv swap) Swap the position of two things in the inventory")
        print("12) Search for a country in the emission datasheet")
        print("13) Calculate how much a country's emission has changed between two years.")
        print("14) Show all data for a specific country.")
        print("q) Quit.")

        choice = input("--> ")

        if choice == "q":
            print("Douh!")
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
            randomize = input("Give me a word to randomize: ")
            print(marvin.randomize_string(randomize))
        
        elif choice == "9":
            strängen = input("Give me a string: ")
            print(marvin.get_acronym(strängen))
        
        elif choice == "10":
            inputt = input("Type something that I will blur out except the last four characters: ")
            print(marvin.mask_string(inputt))
        
        elif choice == "11":
            twelveword = input("Tell me a word that you want to be the haystack: ")
            twelvebit = input("Now tell me a piece of that word you want to find in the haystack: ")
            print(marvin.find_all_indexes(twelveword, twelvebit))

        elif choice in ("inv", "inv ", "inv  ", "inv   "):
            inventory.inventory(Bag)

        elif choice.startswith("inv pick"):
            if choice not in ("inv pick", "inv pick "):
                try:
                    thing_input = choice[9:]
                    thing_input = thing_input[:thing_input.index(" ")]
                except ValueError:
                    thing_input = choice[9:]
                try:
                    pos_input = choice[9:]
                    pos_input = pos_input[pos_input.index(" "):]
                except ValueError:
                    pos_input = ""
                inventory.pick(Bag, thing_input, pos_input)
            else:
                print("Use the following formula: 'inv pick (item) (position)'.")
        
        elif choice.startswith("inv drop"):
            if choice not in ("inv drop", "inv drop "):
                throw_input = choice[9:]
                inventory.drop(Bag, throw_input)
            else:
                print("Use the following formula: 'inv drop (item)'.")
                
        elif choice.startswith("inv swap"):
            if choice not in ("inv swap", "inv swap "):
                swaplist = choice.split(" ")
                swap1 = swaplist[2]
                swap2 = swaplist[3]
                inventory.swap(Bag, swap1, swap2)

        elif choice == "12":
            sökord= input("Enter a country: ")
            try:
                print(emission_functions.search_country(sökord))
            except ValueError:
                print("Country does not exist!")
        
        elif choice == "13":
            cyy = input("Enter with the following format: 'country, year one, year two': ")
            cyylist = cyy.split(",")
            try:
                emissionchange = emission_functions.get_country_change_for_years(cyylist[0], cyylist[1], cyylist[2])
                if emissionchange >= 0:
                    change_str = "+" + str(emissionchange) + "%"
                else:
                    change_str = str(emissionchange) + "%"
                print(cyylist[0] + ":" + change_str)
            except ValueError:
                print("Wrong year!")
        elif choice == "14":
            country = input("Enter a country: ")
            data = emission_functions.get_country_data(country)
            emission_functions.print_country_data(data)
        else:
            print("That is not a valid choice. You can only choose from the menu.")

        input("\nPress enter to continue...")



if __name__ == "__main__":
    main()
