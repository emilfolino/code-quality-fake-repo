"""
Marvin with a simple menu to start up with.
Marvin doesn't do anything, just presents a menu with some choices.
You should add functionality to Marvin.
"""
# pylint: disable=line-too-long
import emission_functions
import marvin
import inventory

marvin_image = r"""
            _d@@@@L  _zzzz__
          .d@@@@@@@L]a@@@@@@z,
          d@@@@@@@@@a@@@@@@@@@,
         d@@@@@@@@@@@@@@@@@@@@@,
        .@@@@@@@@@@~@@@@@@@@@@@L
        ]@@@@@@@@@" `~@@@@@@@@@@L
        a@@@@@@@~     `@@@@@@@@@L
       .@@@@@@@'       `-@@@@@@@@,
       ]@@@@@@Lzzz,  ezz_7@@@@@@@b
       a@@@@@@@@@~'  a@@@@@@@@@@@@
      )@@@@@@@@~~aL  d[~~~~@@@@@@@,
      a@@@@@O@.__d@bz@L__   ]@@@@@[
     ]@@@@@,@@@@["a@@@"~@@zza@@@@@b
 -zzza@@@@@@-b___d@' ]L_  _d@]@@@@[
     ]Lz_@@  `~~]@@  `@@@@@~'`@@@@@,
     ][`@d[   .d~.@    ~e     ]@@@]@z_    _
     `L q@P   ?' ][     `      ]@[]@~~bz_dP
      `Ld@'    ],]'  zr-L     ]@@]a~
      )@@P    ]r_`  ]@  [    z@@'a@
      ]@@L    q_a,  "_zd'   d@@[ q@,
      ]L`@L     ][  ]% "    @[@[ ]@'
      `ad@@L,    a ]@      )@'@bd@"
       ]@@@`L    qz~       dr @@@@[
      .@@@@,`'  )%~-ze     " .@@@@[
      d@@@@[     `-zz        ]@@@@@
     _@@@@@[                 ]@@@@@L
   .z@@@@@@b     ._z='       ]@@@@@@
  _a@@@@@@@L,   `~~        _za@@@@@@b
_d@@@@@@@@@@@L,         _z@@@@@@@@@@@
q@@@@@@@@@@@@@@z_,   ._d@@@@@@@@@@@@@@_zF
 `@@@@@@@@@@@@@@@@zzza@".@@@@@@@@@@@@~~'
    `~@@@@@@@@~]@ "~~"  ]@@@@@@@@@~"
        "~~~~  ][       `@'~~~~"
            _zzd@z     _z@ze
            a@@@@@@_ .d@@@@[
            `-@@@@@@La@@@@@'
              `@@@@@@@@@@~
                ~@@@@@@@"
"""

backpack = []

def main():
    """
    Its an eternal loop, until q is pressed.
    It should check the choice done by the user and call a appropriate
    function.
    """
    while True:
        print(chr(27) + "[2J" + chr(27) + "[;H")
        print(marvin_image)
        print("Hi, I'm John. I know it all. What can I do for you?")
        print("1) Present yourself to John.")
        print("2) Convert Celsius to Fahrenheit.")
        print("3) Multiply a specified word a number of times.")
        print("4) Calculate the sum and average of your numbers.")
        print("5) String plus dash.")
        print("6) Isogram.")
        print("7) Compare numbers.")
        print("8) Randomize string")
        print("9) Get acronym")
        print("10) Mask string")
        print("11) Find all indexes")
        print("12) Emission data searcher")
        print("13) Country emission data year-difference")
        print("14) Show a country's information")
        print("inv) Inventory management")
        print("a1) Check and compare two strings.")
        print("a3) Tab replacement.")
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
            print(marvin.word_manipulation())

        elif choice == "4":
            marvin.sum_and_average()

        elif choice == "5":
            marvin.hyphen_string()

        elif choice == "6":
            marvin.is_isogram()

        elif choice == "7":
            marvin.compare_numbers()

        elif choice == "8":
            print("Enter a word and i will randomize it!")
            randomword = input("Enter a word: ")
            marvin.randomize_string(randomword)

        elif choice == "9":
            print("Enter a sentence or name and I will make an acronym out of it!")
            sentence = input("Enter here: ")
            print(marvin.get_acronym(sentence))

        elif choice == "10":
            print("Enter a string and I will mask it for you.")
            mask = input("Enter a string here: ")
            print(marvin.mask_string(mask))

        elif choice == "11":
            print("Enter two strings, whereas the second one will be used to index the first one.")
            string1 = input("First string: ")
            indexstring = input("Index-string: ")
            print(marvin.find_all_indexes(string1, indexstring))

        elif choice == "12":
            countrychoice = input("What country would you like to search for?\nEnter here: ")
            try: 
                print("Following countries were found:", emission_functions.search_country(countrychoice))
            except ValueError:
                print("Country does not exist!")

        elif choice == "13":
            print("Choose a country and two years, written in the form of 'country,year1,year2'.")
            print("The available years are: 1990, 2005, 2017.")
            countryyear = input("Enter here: ")
            countryyear = countryyear.split(",")

            try:
                print(f"{str(countryyear[0])}:{emission_functions.get_country_change_for_years(countryyear[0], countryyear[1], countryyear[2])}%")
            except ValueError:
                print("Wrong year!")

        elif choice == "14":
            countryname = input("Enter a country's name to recieve information about the country: ")
            try:
                emission_functions.print_country_data(emission_functions.get_country_data(countryname))
            except ValueError:
                print("Country does not exist!")


        elif "inv help" in choice:
            print("The inv commands are:\ninv\ninv pick 'item'\ninv pick 'item' 'position'")
            print("inv swap 'item1' 'item2'\ninv drop 'item'")
        
        elif "inv pick" in choice:
            invchoice = choice.split(" ")
            try:
                print(inventory.pick(backpack, invchoice[2], invchoice[3]))
            except IndexError:
                print(inventory.pick(backpack, invchoice[2]))

        elif "inv swap" in choice:
            invchoice = choice.split(" ")
            try:
                print(inventory.swap(backpack, invchoice[2], invchoice[3]))
            except IndexError:
                print("You have to enter 2 items to swap.")

        elif "inv drop" in choice:
            invchoice = choice.split(" ")
            print(inventory.drop(backpack, invchoice[2]))

        elif choice == "inv":
            inventory.inventory(backpack)

        elif choice == "a1":
            marvin.eua1()

        elif choice == "a3":
            marvin.eua3()

        else:
            print("That is not a valid choice. You can only choose from the menu.")

        input("\nPress enter to continue...")

if __name__ == "__main__":
    main()
