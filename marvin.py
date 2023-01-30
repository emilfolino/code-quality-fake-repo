#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""module that keeps all the functions called upon by main.py"""

import random as r

"""
Marvin with a simple menu to start up with.
Marvin doesnt do anything, just presents a menu with some choices.
You should add functinoality to Marvin.
"""

marvin_image = r"""
       _________
      /___   ___\
     //@@@\ /@@@\\
     \\@@@/ \@@@//
      \___ " ___/
jrjc     | - |
          \_/
"""


def greet():
    """asks for the users name and then greets him."""
    name = input("What is your name? ")
    print("\nMarvin says:\n")
    print("Hello %s - your awesomeness!" % name)
    print("What can I do you for?!")

def celcius_to_farenheit():
    """converts the inputted temperature to fahrenheit"""
    celsius = float(input("Input the temperature in degrees: "))
    fahrenheit = round(celsius * 1.8 + 32, 2)
    print("Celsius: " + str(celsius) + " to fahrentheit = " + str(fahrenheit))

def word_manipulation():
    """manipulates a string and multiplies it by and inputted amount of times"""
    choice3a = input("Give me a word: ")
    choice3b = input("How many times would you like to multiply this word?: ")
    print(multiply_str(choice3a, choice3b))

def multiply_str(string, inte):
    """ multiplies the words by an inputted amount"""
    multipliedString = string * int(inte)
    return multipliedString


# GOTTA FIX THIS
def sum_and_average():
    """ Sums up all of the inputs and gives back the average"""
    times = -1
    sumAvrg = 0.0
    samInput = "0"
    while True:
        if samInput != "done":
            sumAvrg += float(samInput)
            times += 1
            print(times)
        if samInput == "done":
            medel = round(sumAvrg / times, 2)
            print("medelvärdet är: " + str(medel))
            print("summan är: " + str(sumAvrg))
            break
        else: samInput = input("input: ")

    
def hyphen_string():
    """ Hyphens a string thats inputted at the beginning"""
    hyphenTimes = 0
    hyphenString = ""
    origString = input("Give me a string: ")
    for i, _ in enumerate(origString):
        hyphenTimes += 1
        hyphenString = hyphenString + origString[i] * hyphenTimes + "-"
    hyphenString = hyphenString.rstrip(hyphenString[-1])
    print("your hyphened string is: " + hyphenString)

def is_isogram():
    """ checks if a string is a isogram or not"""
    isogramString = input("Isogram: ")
    isogram = True
    for i, _ in enumerate(isogramString):
        for j, _ in enumerate(isogramString):
            if not i == j:
                #print("letter1: " + isogramString[i] + " letter2: " + isogramString[j] + " Match: " + str(isogram))
                if isogramString[i] == isogramString[j]:
                    isogram = False    
    print("your string is ")
    if isogram: 
        print("A Match!")
    elif not isogram: 
        print("No match!")

def compare_numbers():
    """ checks if the number before is larger, smaller, or equal to the new number"""
    
    newnum = input("Give me your first number: ")
    while True:
        try:
            oldnum = float(newnum)
        except ValueError:
            print(oldnum)
            print("This is not a number!")
        newnum = input("Give me another number or write done to stop: ")
        try:
            if newnum == "done":
                break
            else:   
                if oldnum == float(newnum):
                    print("same!")
                elif float(newnum) >= oldnum:
                    print("larger!")
                elif oldnum >= float(newnum):
                    print("smaller!")
        except ValueError:
            print(oldnum)
            print("This is not a number!")

def randomize_string(string):
    """randomizes the characters in a string"""
    randomized = list(string)
    r.shuffle(randomized)
    return string + " --> " + "".join(randomized)

def get_acronym(string):
    """gets the acronyms of a string"""
    newstring = ""
    for char in string:
        if char.isupper():
            newstring += char
    
    return newstring

def mask_string(string):
    """mask all the characters in a string but the last 4"""
    maskedstring = ""
    maskedstring = multiply_str("#", len(string)-4)
    for char in string[len(string)-4: len(string): 1]:
        maskedstring += char
    return maskedstring

def find_all_indexes(string, substring):
    """finds all the indexes for a substring in a string"""
    lastSub = 0
    stringSub = ""
    try:
        while string.index(substring, lastSub + 1):
            lastSub = string.index(substring, lastSub + 1)
            
            stringSub += str(lastSub) + ","
    except ValueError:
        return stringSub[:-1]
    