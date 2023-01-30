"""
Marvin with a simple menu to start up with.
Marvin doesnt do anything, just presents a menu with some choices.
You should add functinoality to Marvin.
"""
import marvin
import inventory
import emission_functions
marvin_image = r"""
  ############################################################# 
###################################################   ####### 
###############################################   /~\   #####
############################################   _- `~~~', ####
##########################################  _-~       )  ####
#######################################  _-~          |  ####
####################################  _-~            ;  #####
##########################  __---___-~              |   #####
#######################   _~   ,,                  ;  `,,  ##
#####################  _-~    ;'                  |  ,'  ; ##
###################  _~      '                    `~'   ; ###
############   __---;                                 ,' ####
########   __~~  ___                                ,' ######
#####  _-~~   -~~ _                               ,' ########
##### `-_         _                              ; ##########
#######  ~~----~~~   ;                          ; ###########
#########  /          ;                        ; ############
#######  /             ;                      ; #############
#####  /                `                    ; ##############
###  /                                      ; ###############
#                                            ################
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
        print(marvin_image)
        print("Hi, I'm Maro. I know it all. What can I do you for?")
        print("1) Present yourself to Maro.")
        print("2) Convert temperature from Celsius to Fahrenheit")
        print("3) Multiply word")
        print("4) Calculate the numbers")
        print("5) Multiply letters of a word by the order of the letter")
        print("6) Test if letters of a word are not duplicated")
        print("7) Test if the number is bigger or smaller")
        print("8) Randomize a string")
        print("9) Acronym creator.")
        print("10) Mask the string")
        print("11) Find all indexes")
        print("12) Search for country")
        print("13) Show emission for a country")
        print("14) Show all data for a country")
        print("q) Quit.")
        print("")
        print("")
        print('Try out my "inv" commands')
        print("------------")

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
            strin = input("Enter a string to randomize: ")
            print(marvin.randomize_string(strin))
        elif choice == "9":
            string = input("Enter a string to get acronym: ")
            print(marvin.get_acronym(string))
        elif choice == "10":
            string = input("Enter a string mask: ")
            print(marvin.mask_string(string))
        elif choice == "11":
            string = input("Enter a string: ")
            stringTwo = input("Enter a second string: ")
            print(marvin.find_all_indexes(string,stringTwo))
        elif choice == "12":
            try:
                StrCon = input("Enter country name or part of country name to see if exist: ")
                print(emission_functions.search_country(StrCon))
            except ValueError:
                print("Country does not exist!")
        elif choice == "13":
            try:
                newStr = input("Enter country, year and year:").split(",")
                if len(newStr) == 3:
                    valBack = emission_functions.get_country_change_for_years(newStr[0],newStr[1],newStr[2])
                    print(f"{newStr[0]}:{valBack}%")
                elif len(newStr) == 2:
                    print(emission_functions.get_country_year_data_megaton(newStr[0],newStr[1]))
            except ValueError:
                print("Wrong year!")
        elif choice == "14":
            conName = input("Enter country:")
            emission_functions.get_country_data(conName)
        elif "inv" in choice:
            cho = choice.split(" ")
            if len(cho) == 1:
                inventory.inventory(backpack)
            elif len(cho) >= 1 and "inv pick" in choice:
                try:
                    inventory.pick(backpack ,cho[2], cho[3])
                except IndexError:
                    inventory.pick(backpack,cho[2])
            elif len(cho) >= 1 and "inv swap" in choice:
                inventory.swap(backpack, cho[2], cho[3])
            elif len(cho) >= 1 and "inv drop" in choice:
                inventory.drop(backpack, cho [2])
               
            

        else:
            print("That is not a valid choice. You can only choose from the menu.")

        input("\nPress enter to continue...")
    
if __name__ == "__main__":
    main()
