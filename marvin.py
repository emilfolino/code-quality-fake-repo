#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Marvin with a simple menu to start up with.
Marvin doesnt do anything, just presents a menu with some choices.
You should add functinoality to Marvin.
"""

import random

marvin_image = r"""
                 .
             /\ /l
            ((.Y(!
             \ |/
             /  6~6,
             \ _    +-.
              \`-=--^-'
               \ \
              _/  \
             (  .  Y
            /"\ `--^--v--.
           / _ `--"T~\/~\/
          / " ~\.  !
    _    Y      Y./'
   Y^|   |      |~~7
   | l   |     / ./'
   | `L  | Y .^/~T
   |  l  ! | |/| |          
   | .`\/' | Y | !
   l  "~   j l j_L______
    \,____{ __"~ __ ,\_,\_
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""

"""
Its an eternal loop, until q is pressed.
It should check the choice done by the user and call a appropriate
function.
"""

    
def greet():
    """
    Ber användaren skriva in namn
    """
    name = input("Vad är ditt namn? ")
    print("\nElvis säger:\n")
    print("Hej %s!" % name)
    print("Hur kan jag hjälpa till?")

def celcius_to_farenheit():
    """
    Konverterar celsius till fahrenheit
    """
    celsius = input("Ange temperatur i celsius: ")
    fahr = float(celsius) * 9 / 5 + 32
    fahr = round(fahr, 2)
    print("Temperaturen blir: " + str(fahr) + " grader i fahrenheit")

def word_manipulation():
    """
    Tar 2 inputs, en siffra och ett ord och konkatenerar ordet med sig själv så många gånger det behövs
    """
    word = input("Skriv ett valfritt ord: ")
    number = int(input("Ange ett valfritt nummer: "))
    num_word = word * number
    print(str(num_word))

def sum_and_average():
    """
    Tar inputs från användaren tills användaren sätter stop och adderar talen för att skriva ut summan och medelvärdet
    """
    add_sum = 0
    add_counter = 0
    add_med = 0
    while True:
        add = input("Ange ett tal eller skriv 'done' om du är färdig: ")
        if add == "done":
            break
        else:
            add_sum += float(add)
            add_counter += 1
            add_sum = round(add_sum, 2)
            add_med = add_sum / add_counter
            add_med = round(add_med, 2)
    print("Summan av talen blir: " + str(add_sum) + " och medelvärdet blir: " + str(add_med))

def hyphen_string():
    """
    Förökar varje bokstavsutskrift med +1 så länge ordet räcker
    """
    conc_str = ""
    multiplier = 0
    word_str = input("Skriv in ett valfritt ord: ")
    for letter in word_str:
        multiplier += 1
        letrs = letter * multiplier
        conc_str += letrs + "-"
        
    conc_str = conc_str[:-1]
    print(conc_str)

def is_isogram():
    """
    Kollar om ett ord är ett isogram d.v.s innehåller mer än en av samma bokstav
    """
    word = input("Skriv in ett ord för att kolla om det är ett isogram: ")
    word = word.lower()
    stored = 0

    for i in word:
        stored += word.count(i)
    if stored != len(word):
        print("No match!")
    else:
        print("Match!")


# 
def compare_numbers():
    """
    Tar 2 inputs från användaren och gör en utskrift som bestämmer om det är större eller mindre. 
    Fortsätter jämföra med föregående tal tills användaren säger stopp
    """

    previous = int(input("Skriv ett heltal: "))

    while True:
        current = input("Skriv in ett nytt heltal: ")
        if current == "done":
            print("Färdig!")
            break
        else:
            try:
                current = int(current)
            except ValueError:
                print("not a number!")
                continue

        if current > previous:
            print("larger!")
        elif current < previous:
            print("smaller!")
        elif current == previous:
            print("same!")
        previous = current

def randomize_string(random_str):
    """
    Makes a string into a list to easily randomze the orders of the letters
    and then makes the list into a string
    """
    empty_str = ""
    random_list = list(random_str)
    random.shuffle(random_list)
    new_word = empty_str.join(random_list)
    return random_str + ' --> ' + new_word

def get_acronym(acro):
    """
    Takes every letter and checks if its uppercase and creates an acronym
    """
    conc_str = ""
    for letter in acro:
        if letter.isupper():
            conc_str += letter
        else:
            continue
    return conc_str

def multiply_str(word, num):
    """
    Multiplies a string by an integer
    """
    new_str = ""
    try:
        new_str = word * int(num)
    except ValueError:
        print("Not a number")
    return new_str


def mask_string(word):
    """
    Replaces all letters with "#" except for the 4 last ones
    """
    new_word = multiply_str(word, 1)
    empty_str = ""
    for letter in new_word[:-4]:
        letter = letter.replace(letter, '#')
        empty_str += letter
    empty_str = empty_str + new_word[-4:]
    return empty_str

def find_all_indexes(index1, index2):
    """
    Finds all the indexes comparing a substring to a string
    """
    list3 = []
    counter = 0
    empty_str = ""

    for _ in index1:
        try:
            list3.append(index1.index(index2, counter, counter + len(index2)))
            counter += 1
            
        except ValueError:
            counter += 1
            continue

    for i in list3:
        empty_str += str(i) + ","
    
    empty_str = empty_str[:-1]
    return empty_str

if __name__ == "__main__":
    print("hello in marvin")
