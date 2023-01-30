#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Marvin with a simple menu to start up with.
Marvin doesn't do anything, just presents a menu with some choices.
You should add functionality to Marvin.
"""

import random

marvin_image = r"""
                 ______
                /     /\
               /     /##\
              /     /####\
             /     /######\
            /     /########\
           /     /##########\
          /     /#####/\#####\
         /     /#####/++\#####\
        /     /#####/++++\#####\
       /     /#####/\+++++\#####\
      /     /#####/  \+++++\#####\
     /     /#####/    \+++++\#####\
    /     /#####/      \+++++\#####\
   /     /#####/        \+++++\#####\
  /     /#####/__________\+++++\#####\
 /                        \+++++\#####\
/__________________________\+++++\####/
\+++++++++++++++++++++++++++++++++\##/
 \+++++++++++++++++++++++++++++++++\/
  ``````````````````````````````````
"""

"""
Its an eternal loop, until q is pressed.
It should check the choice done by the user and call a appropriate
function.
"""


def menu_choice():
    """Choice"""
    print(chr(27) + "[2J" + chr(27) + "[;H")
    print(marvin_image)
    print("Hello, my name is Marvin. I am an omniscient being, what do you ask of me?")
    print("1) Present yourself to Marvin.")
    print("2) Convert Celsius to Fahrenheit.")
    print("3) Word Multiplication.")
    print("4) Find the sum and average of any amount of numbers.")
    print("5) Extending words.")
    print("6) Check to see if a word is an isogram")
    print("7) See if a number is smaller, larger, or the same compared to another.")
    print("8) Randomize a string.")
    print("9) Create an acronym from a phrase.")
    print("10) Mask a string.")
    print("11) Find all indexes.")
    print("a1) Check to see if a word contains certain letters.")
    print("12) Search for a country.")
    print("13) Retrieve the change in CO2 emissions.")
    print("14) Retrieve all pertinent information about a country.")
    print("e1) Sort countries by emission in desending order.")
    print("e2) Sort countries by emission per capita in decending order.")
    print("e3) Sort countries by emission per landmass in decending order.")
    print("q) Quit.")
    print("\n\nTry out my new 'inv' command!")
    
    choice_input = input("--> ")
    choice = choice_input.split(" ")
    
    return choice


def greet():
    """Greeting"""
    name = input("What name do you go by? ")
    
    print("\nMarvin says:\n")
    print("Hello %s it is a pleasure making your acquaintance." % name)
    print("What else do you wish to ask of me?")

def celcius_to_farenheit():
    """Celsius to Fahrenheit"""
    tempCelsius = float(input("Please insert a temperature in Celsius to be converted into Fahrenheit: "))
    
    tempFahrenheit = round(tempCelsius * 1.8 + 32, 2)

    print("\nMarvin Says:\n")
    print(f"{tempCelsius} °C is equivalent to {tempFahrenheit} °F")
    print("What else do you wish to ask of me?")

def word_manipulation():
    """Word Manipulation"""
    multiplyWord = input("Enter a word you would like to see multiplied: ")
    
    while True:
        multiplyInteger = round(float(input("Enter a positive integer you wish to multiply the word by: ")))
        
        if multiplyInteger >= 0:
            print("\nMarvin Says:\n")
            print(multiply_str(multiplyWord, multiplyInteger))
            print("What else do you wish to ask of me?")
            break
        
        print("\nThat is not a valid intiger, please try again.")

def sum_and_average():
    """Sum and Average"""
    sumAndAverageInput = ""
    sumOfInput = 0
    numOfInput = 0
    
    print("Enter numbers one by one to find out what their sum and average value are.\n"
    "when all of your numbers have been entered, type 'done' to receive the results.\n")
    
    while True:
        sumAndAverageInput = input("Enter a number, or type 'done': ")  

        if sumAndAverageInput == "done":
            break
        
        numOfInput += 1
        sumOfInput += float(sumAndAverageInput)

    averageOfInput = round(sumOfInput / numOfInput, 2)

    print("\nMarvin Says:\n")
    print(f"The sum of all numbers are {round(sumOfInput, 2)} and the average is {averageOfInput}")
    print("What else do you wish to ask of me?")

def hyphen_string():
    """Hyphen String"""
    inputWord = input("Enter a word for me to extend: ")
    numOfInput = 0
    extendedWord = ""

    for i in inputWord:
        numOfInput += 1
        if len(inputWord) > numOfInput:
            extendedWord += f"{i * numOfInput}-"
        else:
            extendedWord += f"{i * numOfInput}"

    print("\nMarvin Says:\n")    
    print(extendedWord)
    print("What else do you wish to ask of me?")

def is_isogram():
    """Is Isogram"""
    inputWord = input("Enter a word to check if it is an isogram: ")
    isogramList = []

    for i in inputWord: 
        
        if i in isogramList:
            result = "No match!"
            break
        else:
            result = "Match!" 
        isogramList.append(i)

    print("\nMarvin Says:\n")
    print(result)
    print("What else do you wish to ask of me?")

def compare_numbers():
    """Compare Numbers"""
    print("Enter numbers to check if they are smaller, larger, or the same compared to the the previous one.")
    input1 = ""
    while not input1:
        try:
            input1 = float(input("\nEnter Number: "))
            previousInput1 = True
            break
        except ValueError:
            print("not a number!")

    while True:
        if previousInput1:
            input2 = input("\nEnter Number: ")
        else:
            input1 = input("\nEnter Number: ")

        try:
            input1 = float(input1)
            input2 = float(input2)                    

            if input1 == input2:
                print("same!")
            elif (previousInput1 and input1 < input2) or (not previousInput1 and input1 > input2):
                print("larger!")
            elif (previousInput1 and input1 > input2) or (not previousInput1 and input1 < input2):
                print("smaller!")
            
            previousInput1 = not previousInput1
            
        except ValueError:
            if input1 == "done" or input2 == "done":
                print("\nMarvin Says:\n")
                print("What else do you wish to ask of me?\n")
                break
            else:
                print("not a number!")

def contains_letters():
    """Contains Letters"""
    a1Input1 = input("Enter your starting word: ").lower()
    a1Input2 = input("Enter charactars to to compare against the word: ").lower() 
    
    for letter in a1Input2:
        if letter not in a1Input1:
            print("No match!")
            break

        print("Match!")

def press_enter_to_continue():
    """Press enter to continue with the program"""
    input("\nPress enter to continue...")

def randomize_string(string):
    """Randomize characters in string"""
    list_of_char = list(string)
    random.shuffle(list_of_char)
    rand_str = "".join(list_of_char)
    result = f"{string} --> {rand_str}"
        
    return result

def get_acronym(string):
    """Get an acronym from a string"""
    acronym = ""
    for i in string:
        if i.isupper():
            acronym += i
    return acronym

def mask_string(unmasked_str):
    """Masks a string using pound signs"""
    visible_char = 4
    mask_char = "#"
    stepper = 0
    masked_str = ""

    for i in unmasked_str:
        stepper += 1
        if stepper == (len(unmasked_str) - visible_char):
            masked_str = multiply_str(mask_char, stepper)
        elif stepper >= (len(unmasked_str) - visible_char):
            masked_str += i

    return masked_str

def multiply_str(string, integer):
    """Multiply a string"""
    multiplied_str = string * integer
    return multiplied_str


def find_all_indexes(string, sub_string):
    """Finds all indexes"""
    last_index = ""
    start = 0
    all_indexes = ""

    for _ in range(0, len(string) - 1):
        try:
            last_index = string.index(sub_string, start)
            all_indexes += f"{last_index},"
            
            start = last_index + 1

        except ValueError:
            all_indexes += ""

    return all_indexes[:-1]
