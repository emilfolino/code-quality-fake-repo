#!/usr/bin/env python3
# -*- coding: utf-8 -*-
    
"""
Marvin with a simple menu to start up with.
Marvin doesnt do anything, just presents a menu with some choices.
You should add functinoality to Marvin.
"""
import random

def greet():
    """Greet"""
    name = input("What is your name? ")
    print("\nFalkenDev says:\n")
    print("Hello %s - your awesomeness!" % name)
    print("What can I do you for?!")

def celcius_to_farenheit():
    """Celsius"""
    temp = input("Enter a temperature in Celsius that you want me to convert to Fahrenheit: ")
    farenheit_converter = round(float(temp) * 9 / 5 + 32,2)
    print(str(temp) + " °C is equivalent to " + str(farenheit_converter) + "°F")

def word_manipulation():
    """Manipulation"""
    word = input("Enter a word you want me to multiply: ")
    times = input("How many times do you want me to multiply the word? ")

    print(multiply_str(word, times))

def sum_and_average():
    """Sum"""
    total = 0
    times = 0
    print("Enter one number per input when you are done write done in the input")
    number = input("Enter the number: ")
    while not(number == "done"):
        number = float(number)
        total += number
        times += 1
        number = input("Enter the number: ")
    mean = total / times
    mean = round(mean, 2)
    total = round(total, 2)

    print("\nThe sum of all numbers are " + str(total) + " and the average is " + str(mean))

def hyphen_string():
    """Hyphen"""
    output = ""
    times = 0
    print("write a word and i will add +1 more in every letter")
    word = input("The word: ")
    for letter in word:
        times += 1
        if times == 1:
            output += letter * times
        else:
            output += "-" + letter * times
    print("\n" + output)

def is_isogram():
    """Isogram"""
    word = input("Input the word: ")
    output = False
    for letter in word:
        if word.count(letter) > 1:
            output = True
            break
        else:
            output = False
    if output is True:
        print("No match!")
    else:
        print("Match!")

def compare_numbers():
    """Compare"""
    before = ""
    number = ""
    check = True
    while check is not False:
        before = input("input first number: ")
        try:
            before = float(before)
            while number != "done" or before != "done":
                check = False
                number = input("input a number: ")
                try:
                    number = float(number)
                    if number < before:
                        print("smaller!")
                        before = number
                    elif number > before:
                        print("larger!")
                        before = number
                    else:
                        print("same!")
                        before = number

                except ValueError:
                    if(number != "done"):
                        print("not a number!")
                    else:
                        break
        except ValueError:
            if(before != "done"):
                print("not a number!")
            else:
                break

def randomize_string(original):
    """Random a string"""
    random_original = ""
    randomize_array = [] 
    for letter in original:
        randomize_array.append(letter)
        random.shuffle(randomize_array)
    for letters in randomize_array:
        random_original += letters

    result = original + " --> " + random_original
    return str(result)
    
def get_acronym(string):
    """Getting a akronym from a string"""
    mask_result = ""
    for capital_letter in string:
        if capital_letter.isupper():
            mask_result += capital_letter  
    return mask_result

def mask_string(string):
    """string that creates #"""
    number = len(string) - 4
    last_four_string = string[-4:]

    return  multiply_str("#", number) + last_four_string


def multiply_str(string, number):
    """Multi"""
    string_result =""
    loop = 0
    while loop < int(number):
        string_result += str(string)
        loop += 1
    return string_result

def find_all_indexes(string, index_part):
    """index"""
    result = ""
    start = 0
    position = 0
    try:
        for i in range(0, len(string), 1):
            position = string.index(index_part, start, len(string))
            if i == 0:
                result += str(position)
            else:
                result += "," + str(position)
            start = position + 1

        return result
    except ValueError:
        return result
        