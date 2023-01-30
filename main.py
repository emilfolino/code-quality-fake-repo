"""
this is the main function for Marvin that contains the menu
"""

import marvin
import inventory
import emission_functions

def main():
    """
    loop the menu until q is pressed
    when the user chooses an option, the appriopriate function from marvin.py is called
    """
    marvin_image = r"""
    `\
    \\,
    \\\,^,.,,.
    ,;7~((\))`;;,,
    ,(@') ;)`))\;;',
        )  . ),((  ))\;,
    /;`,,/7),)) )) )\,,      ,,,... ,
    (& )`   (,((,((;( ))\,_,,;'`    `\\,
    `"    ` ), ))),/( (            `)\,
            '1/';/;  `               ))),
            (, (     /         )    ((/,
            / \                /     ((('
            ( 6--\%  ,>     ,,,(     /'))\'
            \,\,/ ,/`----~`\   \    >,))))'
                \/ /          `--7>' /((((('
                (,9             // /'('((\\\,
                \ \,,         (/,/   '\`\\'\
                `\_)1        (_)Kk    `\`\\`\
                    `\|         \Z          `\
                    `          "            `
    """
    while True:
        print(chr(27) + "[2J" + chr(27) + "[;H")
        print(marvin_image)
        print("Hi, I'm Marvin. I know the answer to everything. What can I do for you?")
        print("1) Introduce yourself to Marvin.")
        print("2) Convert a temperature from Celsius to Fahrenheit.")
        print("3) Multiply some words!")
        print("4) Sum and average.")
        print("5) W-oo-rrr-dddd-sssss")
        print("6) Check for isograms!")
        print("7) Comparing numbers!")
        print("8) Randomize string!")
        print("9) Ger acronym.")
        print("10) Conceal letters in a word.")
        print("11) Find all indexes.")
        print("12) Find countries by name.")
        print("13) Change in emissions between 2 years.")
        print("14) Print country data.")
        print("a1) Compare strings.")
        print("a2) Double until you get all digits.")
        print("a3) Change tab to spaces.")
        print("a4) Create a portmanteau.")
        print("a5) Count points.")
        print("b1) Convert points to a grade.")
        print("b2) Compare four strings.")
        print("e1) Print emissions by country.")
        print("e2) Print emissions per capita, descending.")
        print("e3) Print emissions per surface area, descending.")
        print("q) Quit.")
        print("\n\nTry my new 'inv' commands!")

        choice = input("--> ")
        if choice in ("q", "Q"):
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
            string = input("Enter a name you want to create an acronym of: ")
            print(marvin.get_acronym(string))
        elif choice == "10":
            string = input("What word would you like to conceal: ")
            print(marvin.mask_string(string))
        elif choice == "11":
            string1 = input("The first word: ")
            string2 = input("The second word: ")
            print(marvin.find_all_indexes(string1,string2))
        elif choice == "12": 
            searched_name = input("What country are you looking for? ")
            try:
                emission_functions.search_country(searched_name)
            except ValueError as e:
                print(str(e)) # if a marching country hasn't been found, catch the exception
        elif choice == "13":
            input_13 = input("Write the country and years you're interested in: ")
            try:
                emission_functions.handle_input13(input_13)
            except ValueError as e:
                print(str(e))
        elif choice == "14":
            country = input("What country would you like to check? ")
            try:
                data = emission_functions.get_country_data(country)
                emission_functions.print_country_data(data)
            except ValueError as e:
                print(str(e))
        elif choice == "a1":
            marvin.a1()
        elif choice == "a2":
            marvin.a2()
        elif choice == "a3":
            marvin.a3()
        elif choice == "a4":
            marvin.a4()
        elif choice == "a5":
            marvin.a5()
        elif choice == "b1":
            print("What was the maximal score possible?")
            max_points = marvin.get_float()
            print("How many points did you get?")
            points = marvin.get_float()
            print(marvin.points_to_grade(max_points, points))
        elif choice == "b2":
            str1 = input("The first string: ")
            str2 = input("The second string: ")
            str3 = input("The third string: ")
            str4 = input("The fourth string: ")
            print(marvin.has_strings(str1,str2,str3,str4))
        elif choice == "e1":
            input_e1 = input("What year and how many countries would you like to see? ")
            try:
                emission_functions.e1(input_e1)
            except ValueError as e:
                print(str(e))
        elif choice == "e2":
            input_e2 = input("What year are you interested in? Optional: how many countries? ")
            try:
                emission_functions.e2(input_e2)
            except ValueError as e:
                print(str(e))
        elif choice == "e3":
            input_e3 = input("What year are you interested in? Optional: how many countries? ")
            try:
                emission_functions.e3(input_e3)
            except ValueError as e:
                print(str(e))
        else:
            handle_commands(choice)
        input("\nPress any key to continue...")

marvins_backpack = []

def handle_commands(user_input):
    """
    handles commands that are not menu choices.
    I don't really like sorting by the command length rather than its purpose
    but when I sorted by purpose, I ended up with 6 nested loops which didn't pass validation
    so command length it is
    """
    commands = user_input.split(" ") #splits user unput into separate strings to handle
    if len(commands) == 1: #if the command is only one word
        if commands[0] == "inv": #check if it calls for inventory
            inventory.inventory(marvins_backpack) #run inventory function
        else: #if it's one word and NOT "inv":
            print("I don't understand.")
    elif len(commands) == 2: #if it's a two-word command:
        if commands[1] == "pick": #if it's pick, it needs an argument
            print("Error! You need to write an object to add.")
        elif commands[1] == "drop": #drop needs an argument
            print("Error! You need to write an object to remove.")
        elif commands[1] == "swap": #swap needs two arguments
            print("Error! You need to write two objects to swap.")
        else: #if it's none of the inv functions
            print("I don't understand.")
    elif len(commands) == 3: #if it's a 3-word command:
        if commands[1] == "pick": #if it's pick, run pick without index
            inventory.pick(marvins_backpack, commands[2])
        elif commands[1] == "drop": #if it's drop, run drop
            inventory.drop(marvins_backpack,commands[2])
        elif commands[1] == "swap": #if it's swap, it needs another argument
            print("Error! You need to write two objects to swap.")
        else: 
            try:
                int1 = int(commands[1])
                int2 = int(commands[2])
                inventory.inventory(marvins_backpack,int1,int2)
            except ValueError:
                print("I don't understand.")
    elif len(commands) == 4: # if it's a 4-word command:
        if commands[1] == "pick": # if it's pick, try to run pick function with index:
            try:
                user_index = int(commands[3]) #try to convert the 4th element to int (index)
                inventory.pick(marvins_backpack, commands[2], int(user_index)) #run pick with index
            except ValueError: #the fourth element is not an int, can't be used as index:
                print("Error: the fourth item needs to be an integer representing an index.")
        elif commands[1] == "swap": #run swap with 2 args:
            inventory.swap(marvins_backpack,commands[2],commands[3])
    else: 
        print("I don't understand.")

if __name__ == "__main__":
    main()
