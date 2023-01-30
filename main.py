""" Dotstring """

import marvin
import inventory
import emission_functions


marvin_image = r"""
            
/\     /\
{  `---'  }
{  O   O  }
~~>  V  <~~
\  \|/  /
`-----'____
/     \    \_
{       }\  )_\_   _
|  \_/  |/ /  \_\_/ )
\__/  /(_/     \__/
    (__/

"""
bag = []

def main():
    """Docstring"""
    choice = ""
    while True:

        print(chr(27) + "[2J" + chr(27) + "[;H")
        print(marvin_image)
        print("Hi, I'm Marvin. I know it all. What can I do you for?")
        print("1) Present yourself to Marvin.")
        print("2) Celsius to Fahrenheit converter ")
        print("3) Word multiplication")
        print("4) Total and average value")
        print("5) Sentence extender")
        print("6) Isogram")
        print("7) Complair nummber")
        print("8) Randomize string")
        print("9) Get acronym")
        print("10) String masking")
        print("11) Find indexes in string")
        print("12) Emission search country")
        print("13) Country emission year ccomparison")
        print("Try out my inv fuctionality")
        print("E) Extra: Guess the nummber")
        print("Q) Quit.")

        choice = input("--> ")

        if (choice == "1"):
            marvin.greet()

        elif (choice == "2"):
            marvin.celcius_to_farenheit()

        elif (choice == "3"):
            marvin.word_manipulation()

        elif (choice == "4"):
            marvin.sum_and_average()

        elif (choice == "5"):
            marvin.hyphen_string()

        elif (choice == "6"):
            marvin.is_isogram()

        elif (choice == "7"):
            marvin.compare_numbers()

        elif (choice == "8"):
            a_string = input("Enter a string to be r1andomized: ")
            print (marvin.randomize_string(a_string))

        elif (choice == "9"):
            a_string = input("Enter your name: ")
            print (marvin.get_acronym(a_string))

        elif (choice == "10"):
            a_string = input("Enter your desired word to be masked: ")
            print (marvin.mask_string(a_string))

        elif (choice == "11"):
            a_string = str(input("Enter your desired word to be index: "))
            index = str(input("Enter your index: "))
            print (marvin.find_all_indexes(a_string, index))

        elif (choice == "12"):
            search_word = input("Enter search word: ")
            try:
                print(emission_functions.search_country(search_word))
            except ValueError:
                print("Country does not exist!")

        elif (choice == "13"):
            a_string = input("Enter word: ")
            try:
                search_list =  a_string.split(",", 3)
                country = str(search_list[0]) + ":"
                print(country + str(emission_functions.get_country_change_for_years
                (search_list[0], search_list[1], search_list[2])) + "%")
            except ValueError:
                print("Wrong year!")
       
        elif (choice == "14"):
            a_string = input("Enter word: ")
            emission_functions.print_country_data(emission_functions.get_country_data(a_string))

        elif (choice in ("E", "e")):
            marvin.guess_nummber()

        elif (choice in ("q", "Q")  ):
            break

        elif ("inv pick" in choice.lower()):
            choice = choice.split(" ")
            try:
                if len(choice) < 4:
                    inventory.pick(bag, choice[2])
                else:
                    inventory.pick(bag, choice[2], choice[3])
                    
            except ValueError:
                print("Error: ")

            except IndexError:
                print ("IndexError:")

        elif ("inv drop" in choice.lower()):
            choice = choice.split(" ")
            inventory.drop(bag, choice[2])

        elif ("inv swap" in choice.lower()):
            choice = choice.split(" ")
            try:
                inventory.swap(bag, choice[2], choice[3])
            except ValueError:
                print("Error: list index out of range")

        elif ("inv" in choice.lower()):
            inventory.inventory(bag)

        else:
            marvin.not_valid()

        marvin.enter_to_continue()

if __name__ == "__main__":
    main()
