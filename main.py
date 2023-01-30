"""
Choose from the menu what to ask the Log Lady's log.
"""

import marvin
import inventory
import emission_functions as em_f

"""
Contains the functions for each menu option
"""

loglady_img = r"""
                   ____
               _.~'    \.~.
             _,         \  \
            /   /    _      \
           /   /~~/~/ /~\ \  \
           |  |.---.._.----|  |
           / /=|  ~ / \  ~ |  /
          |  \|\___/|  \___|  |
           \  \     \_ \   |  \
           /   |   /___    |   \
          |  _/\\        _/.   |
           \___/.\   ---/  \___/
         ______/ |\---/ |   \___
       _/      \ | \_/ /|  /    '~.
      /         \|/ |\/ |_/        \_
     /           |  |   |            \
    /            /  |   \ ______.----'|\
   /            |   |.---'            | \
  /             |---'____             \  \
 |       \-----' ___/_   \___          \_|
 |        \_   _/          \ '-.______.--/
 |          '-|_            \            \
  \             '-_____-----|__           \
   \__               |       / '--._______/
      '--.___________|______/
"""

answered = False
backpack = []

def main():
    """
    It's an eternal loop, until q is pressed.
    It should check the choice done by the user and call an appropriate
    function.
    """
    while True:
        global answered    # är det så här man använder global?
        answered = False
        print(chr(27) + "[2J" + chr(27) + "[;H")
        print(loglady_img)
        print("Welcome to Twin Peaks. I am known as the Log Lady.")
        print("What would you like to ask my log? It knows many secrets.\n")
        print("1) Introduce yourself to the Log Lady.")
        print("2) Ask the log to convert Celsius to Fahrenheit.")
        print("3) Ask the log to repeat a word.")
        print("4) Ask the log to calculate the sum and mean of a set of numbers.")
        print("5) Ask the log to say a word s-ll-ooo-wwww-lllll-yyyyyy.")
        print("6) Ask the log if a given word is an isogram.")
        print("7) Ask the log to compare numbers.")
        print("a1) Ask the log to check if one word contains all the characters of another word.")
        print("a2) Ask the log how many times a given number must me multiplied by 2 to contain all digits 0-9.")
        print("a3) Ask the log to replace tabs with 3 spaces.")
        print("a4) Ask the log to make a portmanteau of two names.")
        print("a5) Ask the log to calculate the scoreboard of a game.")
        print("8) Ask the log to shuffle the order of letters in a string.")
        print("9) Ask the log to make an acronym.")
        print("10) Ask the log to mask all but the last 4 characters in a string.")
        print("11) Ask the log to find all occurrences of a substring within a string and output"
            " a list of their indices.")
        print("b1) Ask the log what grade you will get.")
        print("b2) Check if one string contains three substrings at certain places.")
        print("\nMY LOG CAN ANALYZE EMISSIONS DATA")
        print("12) Search for country names.")
        print("13) Calculate the change in emissions between years.")
        print("14) Display all data for one country.")
        print("e1) Display the top polluters for a certain year.")
        print("e2) Display the top polluters per capita for a certain year.")
        print("e3) Display emissions per km2 for a certain year.")

        print("\nq) Quit.\n\n")

        print("You may also try out the log's 'inv' commands.")
        print("--------------\n")

        choice = input("--> ")

        if choice == "q":
            print("You're leaving?")
            print("One day my log will have something to say about this. Goodbye.")
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
        
        elif choice == "a1":
            marvin.contains_letters()

        elif choice == "a2":
            marvin.multiply()

        elif choice == "a3":
            marvin.tabs_to_3spaces()

        elif choice == "a4":
            marvin.make_portmanteau()

        elif choice == "a5":
            marvin.count_points()

        elif choice == "8":
            inp = input("Enter a string for my log to shuffle: ")
            print(marvin.randomize_string(inp))

        elif choice == "9":
            print("My log will take all the upper-case letters from your input and concatenate them to an acronym.")
            inp = input("Enter a string: ")
            print("My log says the acronym is " + marvin.get_acronym(inp) + ".")

        elif choice == "10":
            print("My log will turn all the characters in your input to #, except the last 4.")
            inp = input("Enter a string: ")
            print("Your string is now a secret: " + marvin.mask_string(inp))

        elif choice == "11":
            print("Input two strings. My log will find all the indices of instances of the second"
                " string within the first string.")
            string = input("Enter string to search in: ")
            substring = input ("Enter a substring to search for: ")
            print(marvin.find_all_indexes(string, substring))

        elif choice == "b1":
            print("My log wants to calculate the grade for your class.")
            max_points = input("Enter the max number of points for the course: ")
            your_points = input("Enter your earned points: ")
            print(marvin.points_to_grade(max_points, your_points))
        
        elif choice == "b2":
            print("My log asks for four strings. It will check if the first begins with the second,"
                " contains the third, and ends with the fourth. If any of the three criteria are not"
                " met, my log will be very disappointed.")
            string1 = input("Enter the main string to check the other strings against: ")
            string2 = input("Enter a substring that the main string begins with: ")
            string3 = input("Enter a substring that the main string contains: ")
            string4 = input("Enter a substring that the main string ends with: ")
            print(marvin.has_strings(string1, string2, string3, string4))


        # emissions data

        elif choice == "12":
            try:
                search_result = em_f.search_country(input("My log will search the data for "
                " countries containing your input: "))
            except ValueError as e:
                print(str(e))
            else:
                print("My log found these countries: " + ", ".join(search_result))

        elif choice == "13":
            print("My log will calculate the change in emissions in a certain country between two years.")
            print("My log knows the data for 1990, 2005 and 2017.")
            country, year1, year2 = input("Input country,year1,year2: ").split(',')
            try:
                print("{country}:{change}%".format(
                    country=country,
                    change=str(em_f.get_country_change_for_years(country, year1, year2))
                    ))
            except ValueError as e:
                print(str(e))
        
        elif choice == "14":
            try:
                em_f.print_country_data(em_f.get_country_data(input("Input the country whose data"
                    " you want to display: ")))
            except ValueError as e:
                print(str(e))

        elif choice == "e1":
            print("Enter a year to show the top polluters for. To only show a certain number of top countries,"
                " enter that number as well in the format 'year n'.")
            print("My log knows the data for 1990, 2005 and 2017.")
            inp = input("Enter: ").split(' ')
            try:
                if len(inp) == 2:
                    print("\n" + em_f.top_emissions_gross(inp[0], inp[1]))
                elif len(inp) == 1:
                    print("\n" + em_f.top_emissions_gross(inp[0]))
                else:
                    raise ValueError("Error: Input must formatted as 'year (n)'!")
            except ValueError as e:
                print(str(e))
        
        elif choice == "e2":
            print("Enter a year to show the top per capita polluters for. To only show a certain"
                " number of top countries, enter that number as well in the format 'year n'.")
            print("My log knows the data for 1990, 2005 and 2017.")
            inp = input("Enter: ").split(' ')
            try:
                if len(inp) == 2:
                    print("\n" + em_f.top_emissions_per_capita(inp[0], inp[1]))
                elif len(inp) == 1:
                    print("\n" + em_f.top_emissions_per_capita(inp[0]))
                else:
                    raise ValueError("Error: Input must formatted as 'year (n)'!")
            except ValueError as e:
                print(str(e))

        elif choice == "e3":
            print("Enter a year to show the pollution proportional to the land area of the"
                    " country. To only show a certain number of the biggest countries, enter that"
                    " number as well in the format 'year n'.")
            print("My log knows the data for 1990, 2005 and 2017.")
            inp = input("Enter: ").split(' ')
            try:
                if len(inp) == 2:
                    print("\n" + em_f.emissions_per_km2(inp[0], inp[1]))
                elif len(inp) == 1:
                    print("\n" + em_f.emissions_per_km2(inp[0]))
                else:
                    raise ValueError("Error: Input must formatted as 'year (n)'!")
            except ValueError as e:
                print(str(e))


        # inv commands

        elif choice.startswith("inv"):
            global backpack
            inv_cmd = choice.split()
            len_inv_cmd = len(inv_cmd)
            if len_inv_cmd > 1:
                if inv_cmd[1] == "pick":
                    if len_inv_cmd == 3:
                        backpack = inventory.pick(backpack, inv_cmd[2])
                    elif len_inv_cmd == 4:
                        backpack = inventory.pick(backpack, inv_cmd[2], inv_cmd[3])
                    else:
                        print("Error: 'inv pick' must be formatted as: inv pick x (i)")
                elif inv_cmd[1] == "drop":
                    if len_inv_cmd == 3:
                        backpack = inventory.drop(backpack, inv_cmd[2])
                    else:
                        print("Error: 'inv drop' must be formatted as: inv drop x")
                elif inv_cmd[1] == "swap":
                    if len(inv_cmd) == 4:
                        backpack = inventory.swap(backpack, inv_cmd[2], inv_cmd[3])
                    else:
                        print("Error: 'inv swap' must be formatted as: inv swap x y")
                elif len(inv_cmd) == 3:
                    inventory.inventory(backpack, inv_cmd[1], inv_cmd[2])
            elif inv_cmd == ["inv"]:
                inventory.inventory(backpack)
            else:
                print(str(inv_cmd[1]) + " is not a valid 'inv' command!")
            print(backpack)



        else:
            print("You gave an invalid input. You can only choose from the menu.")

        input("\nPress enter to continue...")
    if answered:
        print("\nThere is a depression after an answer is given. It was almost fun not knowing.")


if __name__ == '__main__':
    main()
