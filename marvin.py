"""
Marvin with a simple menu to start up with.
Marvin doesnt do anything, just presents a menu with some choices.
You should add functinoality to Marvin.
"""


#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random


# 1
def greet():
    """ Docstring """
    name = input("Great! ... What can I call you? ")
    print("\nMarvin says:\n")
    print("Hello %s - your awesomeness!" % name)
    print("What can I do you for?!")
# 2
def celcius_to_farenheit():
    """ Docstring """
    try:
        celsius = float(input("Please enter your desired conversion to Fahrenheit in nummbers: " ))
        fahrenheit = (celsius * (9/5)) + 32
        print("Input: " + str(celsius) +"°C" + " Output: " + str(round(fahrenheit, 2)) + "°F")
    except ValueError:
        print("ValueError: Enter nummbers") 
# 3
def word_manipulation():
    """ Docstring """
    word = input("Please enter word that is desired to be multiplied: ")
    try:
        multiply = int(input("Please enter the amout of multiply: "))
        word *= multiply
        print("output: " + word)
    except ValueError:
        print("ValueError: Enter nummbers ")
# 4
def sum_and_average():
    """ Docstring """
    Totalt = 0
    Antal = 0
    try:
        while True:
            Counter = input("Skriv Ett Hel Tal Eller Done: ")
            if (Counter == "done"):
                Average = round((Totalt/Antal), 2)
                print(f"The sum of all numbers are {Totalt} and the average is {Average},")
                break
            Totalt += float(Counter)
            Antal += 1
    except ValueError:    
        Average = round((Totalt/Antal), 2)
        print(f"The sum of all numbers are {Totalt} and the average is {Average},")
# 5
def hyphen_string():
    """ Docstring """
    multiply = 1
    output = ""
    word = input("Please enter word : ")
    
    for char in word:
        if len(word) > multiply:
            output += char * multiply + "-"
            multiply += 1
        else:
            output += char * multiply
    print("Output: " + output)
# 6
def is_isogram():
    """ Docstring """
    word = input("Please enter a word to check if its an Isogram or not: ")
    isogram = False

    for char in word:
        if char.isdigit():
            isNr = True
            break
        else:
            isNr = False
            
    if isNr is False:
        for char in word:
            if word.count(char) > 1:
                isogram = False
                break
            else:
                isogram = True
        if isogram is True:
            print("Match!")
        else:
            print("No match!")
    else:
        print("ErrorValue: Enter string ")
# 7
def compare_numbers():   
    """ Docstring """
    Previous = int(input("Provie a number: "))
    Current = ""

    while True:
        Current = input(f"Your Previous is: {Previous}, Give me another one to compare: ")
        if Current == 'done':
            break
        else:
            try:
                Current = int(Current)
                if Current > Previous:
                    print("larger!")
                elif Current < Previous:
                    print("smaller!")
                else:
                    print("same!")
                Previous = Current
            except ValueError:
                print("not a number!")
# 8
def randomize_string(Rstr):
    """ Docstring """
    a_list = []
    for char in Rstr:
        a_list.append(char)

    random.shuffle(a_list)
    result = Rstr + " --> " + "".join(a_list)
    return result
# 9
def get_acronym(name):
    """ Docstring """
    acronym = ""
    for char in name:
        if char.isupper() is True:
            acronym += char
    return acronym
# 10
def multiply_str(char, mult):
    """ Docstring """
    try:
        multStr = char * mult
        return multStr
    except ValueError:
        return "Error:"

def mask_string(maskStr):
    """ Docstring """
    return multiply_str("#", len(maskStr) - 4) + maskStr[len(maskStr) - 4 : None]
    
#11
def find_all_indexes(Texten, Ordet):
    """
    Find Indexes In A String
    """
    Save = []
    Start = 0
    Stop = (Texten.count(Ordet))
    Answer = ""

    for i in range(Start, Stop):
        if i != Stop:
            try:
                Result = Texten.index(Ordet, Start)
                Save.append((Result))
                Start = 1 + Result

            except ValueError:
                print("")
                break

    for char in Save:
        Answer += (str(char) + ",")
    Answer = Answer[:-1]

    return (Answer)

# Extra
def guess_nummber():
    """ Docstring """
    value = random.randint(1, 10)
    guess = 0
    try:
        while guess != value:
            guess = int(input("\nPlease guess a nummber between 1 and 10: ")) 
            if isinstance(guess, int) is True:
                if guess < value:
                    print("Guess an higher nummber")
                elif guess > value:
                    print("Guess an lower nummber")
                elif guess == value:
                    print("Congratulations you guessed right nummber") 
                else:
                    print("Error")
        
    except ValueError: 
        print("ValueError: Enter nummbers ")
            
def not_valid():
    """ Docstring """
    print("That is not a valid choice. You can only choose from the menu.")

def enter_to_continue():
    """ Docstring """
    input("\nPress enter to continue...")
