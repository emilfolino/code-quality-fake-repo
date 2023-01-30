
 
"""
Marvin with a simple menu to start up with.
Marvin doesnt do anything, just presents a menu with some choices.
You should add functinoality to Marvin.
"""

import marvin
import inventory
import emission_functions

marvin_image = r"""
          _,.-------.,_
     ,;~'             '~;,
   ,;                     ;,
  ;                         ;
 ,'                         ',
,;                           ;,
; ;      .           .      ; ;
| ;   ______       ______   ; |
|  `/~"     ~" . "~     "~\'  |
|  ~  ,-~~~^~, | ,~^~~~-,  ~  |
 |   |        }:{        |   |
 |   l       / | \       !   |
 .~  (__,.--" .^. "--.,__)  ~.
 |     ---;' / | \ `;---     |
  \__.       \/^\/       .__/
   V| \                 / |V
    | |T~\___!___!___/~T| |
    | |`IIII_I_I_I_IIII'| |
    |  \,III I I I III,/  |
     \   `~~~~~~~~~~'    /
       \   .       .   /     
         \.    ^    ./
           ^~~~^~~~^

"""

def main():
    
    """
    Its an eternal loop, until q is pressed.
    It should check the choice done by the user and call a appropriate
    function.
    """
    inv = []
    while(True):
        print(chr(27) + "[2J" + chr(27) + "[;H")
        print(marvin_image)
        print("Hi, I'm Marvin. I know it all. What can I do you for?")
        print("1) Present yourself to Marvin.")
        print("2) Convert Celsius to Fahrenheit.")
        print("3) Multiply word.")
        print("4) Sum numbers and calculate average.")
        print("5) Fun word printer.")
        print("6) Check word for Isogram.")
        print("7) Compare numbers.")
        print("8) Randomize string.")
        print("9) Get acronym.")
        print("10) Mask string.")
        print("11) Find index in string.")
        print("a1) Exists in.")
        print("a2) Times to duplicate.")
        print("a3) Replace Tab.")
        print("a4) Short concatenation.")
        print("a5) Calculate Score.")
        print("b1) Grade points.")
        print("b2) Check if in.")
        print("q) Quit.")

        command = input("--> ").split(" ")
        choice = command[0]

        if choice == "q":
            print("Bye, bye - and welcome back anytime!")
            break

        if choice == "inv":
            length = len(command)
            if length == 1:
                inventory.inventory(inv)
            elif command[1] == "pick":
                if length == 3:
                    inv = inventory.pick(inv, command[2])
                elif length == 4:
                    try:
                        inv = inventory.pick(inv, command[2], int(command[3]))
                    except ValueError:
                        print("The Place chosen is not a number")
                else:
                    print("Wrong call to inv:pick, correct use is inv pick <item> <(Optional) Place>")
            elif command[1] == "drop":
                if length == 3:
                    inv = inventory.drop(inv, command[2])
                else:
                    print("Wrong call to inv:drop, correct use is inv drop <item>")
            elif command[1] == "swap":
                if length == 4:
                    inv = inventory.swap(inv, command[2], command[3])
                else:
                    print("Wrong call to inv:swap, correct use is inv swap <first item> <second item>")
            else:
                inventory.inventory(inv, command[1], command[2])
            
        

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
            prev_number = marvin.compare_numbers(prev_number)

        elif choice == "8":
            string = input("Enter a string to randomize: ")
            print(marvin.randomize_string(string))

        elif choice == "9":
            string = input("Enter a string to achronym: ")
            print(marvin.get_acronym(string))

        elif choice == "10":
            string = input("Enter a string to mask: ")
            print(marvin.mask_string(string))

        elif choice == "11":
            string = input("string to find indexes in: ")
            string2 = input("index: ")
            print(marvin.find_all_indexes(string, string2))

        elif choice == "12":
            Country = input("Country: ")
            try:
                emission_functions.search_country(Country)
            except ValueError:
                print("Country does not exist!")
        elif choice == "13":
            Data = input("Data: ")
            try:
                args = Data.split(",")
                print(f"{args[0]}:{str(emission_functions.get_country_change_for_years(args[0], args[1], args[2]))}%")
            except ValueError:
                print("Country does not exist!")
        elif choice == "14":
            Country = input("Country: ")
            try:
                data = emission_functions.get_country_data(Country)
                emission_functions.print_country_data(data)
            except ValueError:
                print("Country does not exist!")
        elif choice == "e1":
            Data = input("Year: ").split(" ")
            try:
                if(len(Data) == 2):
                    emission_functions.sorted_emissions(Data[0], Data[1])
                else:
                    emission_functions.sorted_emissions(Data[0])
            except ValueError:
                print("Country does not exist!")
        elif choice == "e2":
            Data = input("Year: ").split(" ")
            try:
                if(len(Data) == 2):
                    emission_functions.sorted_emissions_per_capita(Data[0], Data[1])
                else:
                    emission_functions.sorted_emissions_per_capita(Data[0])
            except ValueError:
                print("Country does not exist!")
        elif choice == "e3":
            Data = input("Year: ").split(" ")
            try:
                if(len(Data) == 2):
                    emission_functions.sorted_emissions_per_area(Data[0], Data[1])
                else:
                    emission_functions.sorted_emissions_per_area(Data[0])
            except ValueError:
                print("Country does not exist!")
        elif choice == "a1":
            marvin.check_if_in()

        elif choice == "a2":
            marvin.multiply_till_complete()

        elif choice == "a3":
            marvin.replace_tab_with_space()

        elif choice == "a4":
            marvin.name_concatenation()

        elif choice == "a5":
            marvin.count_score()

        elif choice == "b1":
            max_points = input("What was the max score? ")
            points = input("How many points were scored? ")
            print(marvin.points_to_grade(max_points, points))

        elif choice == "b2":
            sa = input("What string should i compare to? ")
            sb = input("What should it begin with? ")
            sc = input("What should it contain? ")
            sd = input("What should it end with? ")
            print(marvin.has_strings(sa, sb, sc, sd))

        else:
            print("That is not a valid choice. You can only choose from the menu.")
        
        input("\nPress enter to continue...")
if __name__ == "__main__":
    main()
    