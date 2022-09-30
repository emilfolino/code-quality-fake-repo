#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Marvin with a simple menu to start up with.
Marvin doesnt do anything, just presents a menu with some choices.
You should add functinoality to Marvin.
"""
import marvin as mr
import inventory as inv
import emission_functions as ef
my_bag = []

def main():
    """ -- """
    marvin_image =r"""
               .andAHHAbnn.
           .aAHHHAAUUAAHHHAn.
          dHP^~"        "~^THb.
    .   .AHF                YHA.   .
    |  .AHHb.              .dHHA.  |
    |  HHAUAAHAbn      adAHAAUAHA  |
    I  HF~"_____        ____ ]HHH  I
   HHI HAPK""~^YUHb  dAHHHHHHHHHH IHH
   HHI HHHD> .andHH  HHUUP^~YHHHH IHH
   YUI ]HHP     "~Y  P~"     THH[ IUP
    "  `HK                   ]HH'  "
        THAn.  .d.aAAn.b.  .dHHP
        ]HHHHAAUP" ~~ "YUAAHHHH[
        `HHP^~"  .annn.  "~^YHH'
         YHb    ~" "" "~    dHF
          "YAb..abdHHbndbndAP"
           THHAAb.  .adAHHF
            "UHHHHHHHHHHU"
              ]HHUUHHHHHH[
            .adHHb "HHHHHbn.
     ..andAAHHHHHHb.AHHHHHHHAAbnn..
.ndAAHHHHHHUUHHHHHHHHHHUP^~"~^YUHHHAAbn.
  "~^YUHHP"   "~^YUHHUP"        "^YUP^"
       ""         "~~"
"""

    """
    Its an eternal loop, until q is pressed.
    It should check the choice done by the user and call a appropriate
    function.
    """
    while True:
        print(chr(27) + "[2J" + chr(27) + "[;H")
        print(marvin_image)
        print("Hi, I'm Droid. What can I do you for?")
        print("1) Meet Droid!")
        print("2) Celcius to Farenheit")
        print("3) Word repeater")
        print("4) Math teacher")
        print("5) Stretcher")
        print("6) Find isogram")
        print("7) Math teacher v2")
        print("8) Randomize string")
        print("9) Get acronym")
        print("10) Mask string")
        print("11) Find all indexes")
        print("12) Search county")




        print("\n\n\nTry out inv commands")


        print("q) Quit.")

        choice = input("--> ")

        if choice == "q":
            print("Bye, bye - and welcome back anytime!")
            break

        elif choice == "1":
            mr.greet()
        elif choice == "2":
            mr.celcius_to_farenheit()
        elif choice == "3":
            mr.word_manipulation()
        elif choice == "4":
            mr.sum_and_average()
        elif choice == "5":
            mr.hyphen_string()
        elif choice == "6":
            mr.is_isogram()
        elif choice == "7":
            mr.compare_numbers()
        elif choice == "8":
            word = str(input("enter a sentence or a word:"))
            print(mr.randomize_string(word))
        elif choice == "9":
            sent = str(input("enter a sentence:"))
            print(mr.get_acronym(sent))
        elif choice == "10":
            string = input("Enter numbers: ")
            print(mr.mask_string(string))
        elif choice == "11":
            string = input("Enter string: ")
            char = input("Enter char: ")
            print(mr.find_all_indexes(string, char))
        elif choice == "inv":
            inv.inventory(my_bag)
        elif "inv pick " in choice and len(choice.split()) <= 3:
            cSplit = choice.split()
            cSplit = cSplit[2:]
            inv.pick(my_bag, cSplit[0])
        elif "inv pick " in choice and len(choice.split()) >= 4:
            cSplit = choice.split()
            cSplit = cSplit[2:]
            inv.pick(my_bag, cSplit[0], cSplit[1])
        elif "inv swap " in choice:
            cSplit = choice.split()
            cSplit = cSplit[2:]
            inv.swap(my_bag, cSplit[0], cSplit[1])
        elif "inv drop " in choice:
            cSplit = choice.split()
            cSplit = cSplit[2:]
            inv.drop(my_bag, cSplit[0])
        elif choice == "12":
            county = input("Enter a country: ")
            try:
                county_list = ef.search_country(county)
                print(county_list)
            except ValueError:
                print("Country does not exist!")
        elif choice == "13":
            string = input("Enter Country, first year and secound year")
            split = string.split(",")
            county = split[0]
            year1 = split[1]
            year2 = split[2]

            try:
                change = ef.get_country_change_for_years(county, year1, year2)
                print("{}:{}%".format(county, change))
            except ValueError:
                print("Wrong year!")

        elif choice == "14":
            st = input("Enter Country, first year and secound year")
            
            ef.print_country_data(ef.get_country_data(st))
  
        else:
            print("That is not a valid choice. You can only choose from the menu.")

        input("\nPress enter to continue...")

if __name__ == "__main__":
    main()
