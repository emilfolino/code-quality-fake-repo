"""
Mainfunktionen för marvin

"""
import marvin
import inventory
import emission_functions

def main():
    """
    Marvin with a simple menu to start up with.
    Marvin doesnt do anything, just presents a menu with some choices.
    You should add functinoality to Marvin.
    """

    marvin_image = r"""
                        _
                       /_'. _
                     _   \ / '-.
                    < ``-.;),--'`
                     '--.</()`--.
                       / |/-/`'._\
                       |/ |=|
                     ~`   |-| ~~      ~
                 ~~  ~~ __|=|__   ~~            ~~
    ~~         ~~   .-'`  |_|  ``""-._   ~~
                ~ .'                  '-.  ~
         ~~        '-.__.--._         .-'          ~
            ~~          ~~   `--...-'`    ~~
                ~~         ~          ~

    """

    """
    Its an eternal loop, until q is pressed.
    It should check the choice done by the user and call a appropriate
    function.
    """

    backpack = []

    while True:
        print(chr(27) + "[2J" + chr(27) + "[;H")
        print(marvin_image)
        print("Hi, you are stranded on this deserted island."\
        + "I'm the Magic Bucket and I can help you, what would you need?")
        print("1) Present yourself.")
        print("2) Convert Celsius to Fahrenheit")
        print("3) Multiply words")
        print("4) Get the sum and average")
        print("5) Add hyphen to word")
        print("6) Check if isogram")
        print("7) Compare numbers ")
        print("8) Randomize string")
        print("9) Create acronym")
        print("10) Mask a string")
        print("11) Find indexes")
        print("12) Search for country")
        print("13) Show emission change for country")
        print("14) Show all data for a country")
        print("q) Quit.")

        choice = input("--> ")

        choice = choice.split(" ")

        if len(choice) == 1:

            if choice[0] == "q":
                print("Bye, bye - and welcome back anytime!")
                break

            elif choice[0] == "1":
                marvin.greet()

            elif choice[0] == "2":
                marvin.celcius_to_farenheit()

            elif choice[0] == "3":
                marvin.word_manipulation()

            elif choice[0] == "4":
                marvin.sum_and_average()

            elif choice[0] == "5":
                marvin.hyphen_string()

            elif choice[0] == "6":
                marvin.is_isogram()

            elif choice[0] == "7":
                marvin.compare_numbers()

            elif choice[0] == "8":
                word = input('Enter a word: ')
                print(marvin.randomize_string(word))

            elif choice[0] == "9":
                name = input("Enter a string to make akronym: ")
                print(marvin.get_acronym(name))


            elif choice[0] == "10":
                to_mask = input("Enter a string to partially mask: ")
                print(marvin.mask_string(to_mask))


            elif choice[0] == "11":
                first_string = input("Enter the first string: ")
                second_string = input("Enter the second string: ")
                print(marvin.find_all_indexes(first_string, second_string))

            elif choice[0] == "12":
                word = input('Seach for a country: ')
                try:
                    print(emission_functions.search_country(word))
                except ValueError as e:
                    print(str(e))

            elif choice[0] == "13":
                c_input = input("Select a country and two years (seperate with ,): ")
                c_input = c_input.split(",")
                try:
                    print(c_input[0] + ":" \
                    + str(emission_functions.get_country_change_for_years(c_input[0], c_input[1], c_input[2]))+"%")
                except ValueError as e:
                    print(str(e))

            elif choice[0] == "14":
                country_name = input("Enter a country: ")
                emission_functions.print_country_data(emission_functions.get_country_data(country_name))

            elif choice[0] == 'inv':
                inventory.inventory(backpack)

        elif len(choice) == 3:

            if choice[0] == 'inv' and choice[1] == 'pick':
                inventory.pick(backpack, choice[2])

            elif choice[0] == 'inv' and choice[1] == 'drop':
                inventory.drop(backpack, choice[2])

        elif len(choice) == 4:
            if choice[0] == 'inv' and choice[1] == 'pick':
                inventory.pick(backpack, choice[2], choice[3])

            elif choice[0] == 'inv' and choice[1] == 'swap':
                inventory.swap(backpack, choice[2], choice[3])

        else:
            print("That is not a valid choice. You can only choose from the menu.")

        input("\nPress enter to continue...")

if __name__ == "__main__":
    main()
