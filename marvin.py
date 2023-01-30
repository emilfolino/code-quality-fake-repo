#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Marvin with a simple menu to start up with.
Marvin doesnt do anything, just presents a menu with some choices.
You should add functinoality to Marvin.
"""


import random
import emission_functions as emiFun


marvin_image = r"""
.     .       .  .   . .   .   . .    +  .
  .     .  :     .    .. :. .___---------___.
       .  .   .    .  :.:. _".^ .^ ^.  '.. :"-_. .
    .  :       .  .  .:../:            . .^  :.:\.
        .   . :: +. :.:/: .   .    .        . . .:\
 .  :    .     . _ :::/:               .  ^ .  . .:\
  .. . .   . - : :.:./.                        .  .:\
  .      .     . :..|:                    .  .  ^. .:|
    .       . : : ..||        .                . . !:|
  .     . . . ::. ::\(                           . :)/
 .   .     : . : .:.|. ######              .#######::|
  :.. .  :-  : .:  ::|.#######           ..########:|
 .  .  .  ..  .  .. :\ ########          :######## :/
  .        .+ :: : -.:\ ########       . ########.:/
    .  .+   . . . . :.:\. #######       #######..:/
      :: . . . . ::.:..:.\           .   .   ..:/
   .   .   .  .. :  -::::.\.       | |     . .:/
      .  :  .  .  .-:.":.::.\             ..:/
 .      -.   . . . .: .:::.:.\.           .:/
.   .   .  :      : ....::_:..:\   ___.  :/
   .   .  .   .:. .. .  .: :.:.:\       :/
     +   .   .   : . ::. :.:. .:.|\  .:/|
     .         +   .  .  ...:: ..|  --.:|
.      . . .   .  .  . ... :..:.."(  ..)"
 .   .       .      :  .   .: ::/  .  .::\
"""

"""
Its an eternal loop, until q is pressed.
It should check the choice done by the user and call a appropriate
function.
"""

menu = """
    1)   Present yourself to Marvin.
    2)   Celsius to Fahrenheit.
    3)   Word multiplication.
    4)   Sum and average
    5)   Repeat letters in word
    6)   Isogram
    7)   Is smaller, bigger, equel.
    8)   Kasta om bokstäver
    9)   Akronym skapare
    10)  Sträng maskering
    11)  Hitta alla index 
    12)  Sök land 
    13)  Visa utsläppskillnad för ett land 
    14)  Visa allt data för ett land
    q)   Quit

    Try out my "inv" commands
    """


def welcome():
    """
    Introduce marvin
    """
    print(chr(27) + "[2J" + chr(27) + "[;H")
    print(marvin_image)
    print("Hi, I'm Marvin. I know it all. What can I do you for?")
    print(menu)


def multiply_str(string, num):
    """
    Multiply a string num times
    """
    return string * num


def greet():
    """
    Give more info about marvin
    """
    usersName = input("What is your name? ")
    print("\nMarvin says:\n")
    print(f"Hello {usersName} - It’s very nice to meet you ")
    print("Know the answer to the magic question 1+1, and I will grand you knowledge if asked!")


def celcius_to_farenheit():
    """
    Convert celcius to farenheit
    """
    cel = input("Please write the temperature in Celsius: ")
    fah = round((float(cel) * 9 / 5) + 32, 2)
    print(f"{cel}°C in Fahrenheit: {fah} °F")


def word_manipulation():
    """
    Multiply a word multi times
    """
    word = input("Write the word you want to multiply: ")
    multi = input("How many times you want to multiply? ")
    print(multiply_str(word, int(multi)))


def sum_and_average():
    """
    Give sum and average of numbers
    """
    sum_ = 0
    num = 0
    countOfNumbers = -1
    while num != 'done':
        sum_ += float(num)
        countOfNumbers += 1
        num = input("Input: ")

    sum_ = round(sum_, 2)
    average = round(sum_ / countOfNumbers, 2)
    print(countOfNumbers)
    print(
        f"The sum of all numbers are {sum_} and the average is {average}")


def hyphen_string():
    """
    Repeat characters in a word 
    """
    word = input("Write the word: ")
    newString = ""
    for index, letter in enumerate(word):
        if index != len(word) - 1:
            newString += letter * (index + 1) + "-"
        else:
            newString += letter * (index + 1)
    print(newString)


def is_isogram():
    """
    Check if a word is isogram
    """
    word = input("Write the word: ")
    isIsogram = True
    charList = []
    for char in word:
        if char not in charList:
            charList.append(char)
        else:
            isIsogram = False
            break

    if isIsogram:
        print("Match!")
    else:
        print("No match!")


def compare_numbers():
    """
    Compare numbers
    """
    firstTime = True
    previous_tal = ""
    tal = ""
    while tal != "done":
        try:
            if firstTime:
                tal = input("Input: ")
                previous_tal = float(tal)
                tal = input("Input: ")
                firstTime = False
            else:
                tal = input("Input: ")

            if(float(tal) == previous_tal):
                print("same!")
            elif (float(tal) > previous_tal):
                print("larger!")
            else:
                print("smaller!")
            previous_tal = float(tal)
        except ValueError:
            print("not a number!")
        except TypeError:
            print("not a number!")


def randomize_string(text):
    """
    randomize text 
    """
    randomText = ""
    if(len(text) > 0):
        randomText = ''.join(random.sample(text, len(text)))

    return f"{text} --> {randomText}"


def get_acronym(name):
    """
    Get acronym 
    """
    acronym = ""
    for char in name:
        if char.isupper():
            acronym += char
    return acronym


def mask_string(text):
    """
    Mask the text
    """
    maskedString = multiply_str("#", len(text) - 4)
    for index, char in enumerate(text):
        if len(text) - (index + 1) < 4:
            maskedString += char
    return maskedString


def find_all_indexes(string, searchValue):
    """
    Find all searchValues in the string
    """
    indexes = ""
    startIndex = 0
    while True:
        try:
            findedIndex = string.index(searchValue, startIndex)
            indexes += str(findedIndex) + ','
            startIndex = findedIndex + 1
            print(findedIndex)
        except ValueError:
            if(len(indexes) > 0):
                indexes = indexes[:-1]
            break
    return indexes


def searchForCountry(searchWord):
    """
    Search for searchWord in countries name
    """
    try:
        result = emiFun.search_country(searchWord)
        if len(result) == 1:
            print(f"Following countries were found: {result[0]}")
        else:
            print(f"Following countries were found: {','.join(result)}")
    except ValueError:
        print("Country does not exist!")

def calculatePercentageEmissionDifference(text):
    """
    Calculate percentage emission difference for a given country between two years
    """
    inputs = text.split(',')
    inputs = [n.strip() for n in inputs]
    try:
        percentageEmissionDifference= emiFun.get_country_change_for_years(*inputs)
        print(f"{inputs[0]}:{percentageEmissionDifference}%") 
    except ValueError:
        print("Wrong year!")

def showAllDataForCountry(countryName):
    """
    Show all data for a given country
    """
    data = emiFun.get_country_data(countryName)
    emiFun.print_country_data(data)
