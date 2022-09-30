"""
Devin with a simple menu to start up with.
Devin doesn't do anything, just presents a menu with some choices.
You should add functinoality to Devin.
"""

import marvin
import inventory
import emission_functions

backpack = []

Devin_image = r"""
                                                      /===-_---~~~~~~~~~------____
                                                |===-~___                _,-'
                 -==\\                         `//~\\   ~~~~`---.___.-~~
             ______-==|                         | |  \\           _-~`
       __--~~~  ,-/-==\\                        | |   `\        ,'
    _-~       /'    |  \\                      / /      \      /
  .'        /       |   \\                   /' /        \   /'
 /  ____  /         |    \`\.__/-~~ ~ \ _ _/'  /          \/'
/-'~    ~~~~~---__  |     ~-/~         ( )   /'        _--~`
                  \_|      /        _)   ;  ),   __--~~
                    '~~--_/      _-~/-  / \   '-~ \
                   {\__--_/}    / \\_>- )<__\      \
                   /'   (_/  _-~  | |__>--<__|      |
                  |0  0 _/) )-~     | |__>--<__|     |
                  / /~ ,_/       / /__>---<__/      |
                 o o _//        /-~_>---<__-~      /
                 (^(~          /~_>---<__-      _-~
                ,/|           /__>--<__/     _-~
             ,//('(          |__>--<__|     /                  .----_
            ( ( '))          |__>--<__|    |                 /' _---_~\
         `-)) )) (           |__>--<__|    |               /'  /     ~\`\
        ,/,'//( (             \__>--<__\    \            /'  //        ||
      ,( ( ((, ))              ~-__>--<_~-_  ~--____---~' _/'/        /'
    `~/  )` ) ,/|                 ~-_~>--<_/-__       __-~ _/
  ._-~//( )/ )) `                    ~~-'_/_/ /~~~~~~~__--~
   ;'( ')/ ,)(                              ~~~~~~~~~~
  ' ') '( (/
    '   '  `
"""
def main():
    """
    Its an eternal loop, until q is pressed.
    It should check the choice done by the user and call a appropriate
    function.
    """
    while True:
        print(chr(27) + "[2J" + chr(27) + "[;H")
        print(Devin_image)
        print("Yo, Devin is my name. Why do you seek me?")
        print("1) Present yourself to Devin.")
        print("2) Ask what temperature in Celsius is in Fahrenheit.")
        print("3) Ask Devin to multiply a word.")
        print("4) Ask Devin to sum up values.")
        print("5) Ask Devin to show you one of his talents.")
        print("6) Ask Devin if the word is an isogram.")
        print("7) Ask Devin high or lower.")
        print("8) Ask Devin to randomize a word or text.")
        print("9) Ask Devin to get the acronym.")
        print("10) Ask Devin to mask something.")
        print("11) Ask Devin to search through something.")
        print("12) Search up a country.")
        print("13) Find emission change in country between years.")
        print("14) Get country info.")
        print("q) Leave Devin's lair.")
        print("Try the inv function")

        choice = input("--> ")

        list_choice = choice.split(" ")
        
        if len(list_choice) > 1:
            choice = list_choice[0] + " " +  list_choice[1]

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
            text = input("Please tell me what you want to randomize... ")
            print(marvin.randomize_string(text))
        
        elif choice == "9":
            text = input("Can you give me the sentence or word...")
            print(marvin.get_acronym(text))
        
        elif choice == "10":
            text = str(input("What do you want to mask... "))
            print(marvin.mask_string(text))

        elif choice == "11":
            text = input("In what sentence do you want me to look through... ")
            search = input("What are you looking for... ")
            print(marvin.find_all_indexes(text, search))

        elif choice == "12":
            try:
                list_country = emission_functions.search_country(input("What country do you want to search for..."))
                result = f"Following countries were found:{emission_functions.list_to_string(list_country)}"
            except ValueError:
                result = "Country does not exist!"
            print(result)
            
        elif choice == "13":
            inp = input("Please give me the country's name, the first year, and the second year...")
            country, year1, year2 = inp.split(",")
            try:
                procent = emission_functions.get_country_change_for_years(country, year1, year2)
                result = f"{country}:{procent}%"
            except ValueError:
                result = "Wrong year!"
            print(result)           

        elif choice == "14":
            info = emission_functions.get_country_data(input("What county do you want the info from..."))
            emission_functions.print_country_data(info)

        elif choice == "inv pick":
            if len(list_choice) > 3 and list_choice[3].isdigit():
                inventory.pick(backpack, list_choice[2], list_choice[3])
            else:
                inventory.pick(backpack, list_choice[2])
                  
        elif choice == "inv":
            inventory.inventory(backpack)

        elif choice == "inv drop":
            inventory.drop(backpack, list_choice[2])
        
        elif choice == "inv swap":
            inventory.swap(backpack, list_choice[2], list_choice[3])
    
        else:
            print("Devin doesn't understand what choice you picked. You can only choose from the menu.")

        input("\nPress enter to continue...")

if __name__ == "__main__":
    main()
