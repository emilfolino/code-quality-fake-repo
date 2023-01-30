#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Torkel with a simple menu to start up with.
Torkel doesnt do anything, just presents a menu with some choices.
You should add functinoality to Torkel.
"""

import random

def greet():
    """Menuchoice 1, greets the user."""
    name = input("What is your name? ")
    print("\nTorkel says:\nHello %s - your are awesome!\nWhat can I do for you?!" % name)

def celcius_to_farenheit():
    """Menuchoice 2, converts celsius to farenheit"""
    celsius = float(input("Tell me the temperature in °C and i will return in °F: "))
    farenheit = round(celsius * 9 / 5 + 32, 2)
    print("Your " + str(celsius) + "°C is " + str(farenheit) + "°F")

def word_manipulation():
    """Menuchoice 3, repeats the word the user wrote"""
    input_name = input("Tell me a word and i will repeat it: ")
    input_times = int(input("How many times do you want me to repeat?: "))
    print(multiply_str(input_name, input_times))

def sum_and_average():
    """Menuchoice 4, """
    input_math = 0
    result_math = 0
    counter = 0
    while input_math != "done":
        input_math = input("Write some numbers and i will add them together, when you are done write done:")
        if input_math != "done":
            result_math += float(input_math)
            counter += 1

    result_average = round(float(result_math) / int(counter), 2)
    print("The sum of your number is: " + str(result_math) + " and the average is " + str(result_average))

def hyphen_string():
    """Menuchoice 5, """
    input_word = input("Write an word: ")
    word_length = len(input_word)
    result_word = ""
    for i in range(0, word_length):
        for _ in range(i+1):
            result_word += input_word[i]
        if i != (len(input_word) - 1):    
            result_word += "-"    
    
    print(result_word)

def is_isogram():
    """Menuchoice 6, checks if the word the user wrote is an isogram"""
    input_word = input("Write an word and i will check if its an isogram: ")
    isogram = False
    char_list = []
    if input_word.isalpha():
        for char in input_word.lower():
            if char in char_list:
                isogram = True
            char_list.append(char)

        if isogram:
            print("No match!")
        else:
            print("Match!")
    else: 
        print("You need to input an string!")

def compare_numbers():
    """Menuchoice 7, compares numbers if they are larger, smaller or equal """
    print("Write some numbers and determine if its `smaller`, `larger` or `same` when you hade enough write done!")
    input_value = ""
    number_list = []
    while input_value != "done":
        try:
            input_value = input(">>")
            if input_value != "done":
                converted_value = int(input_value)
                number_list.append(converted_value)
                if len(number_list) > 1:
                    if number_list[0] > number_list[1]:
                        print("smaller!")
                    elif number_list[1] > number_list[0]:
                        print("larger!")
                    else: 
                        print("same!")
                    number_list.pop(0)
        except ValueError:
            print("not a number!")
    print("I hope I was of some help!")

def randomize_string(string):
    """Menuchoice 8, randomizes an string (Hej -> jeH)"""
    shuffled_string = ""
    shuffled = list(string)
    random.shuffle(shuffled)
    return string + " --> " + shuffled_string.join(shuffled)

def get_acronym(string):
    """Menuchoice 9, gets the acronym of an string"""
    acronym_list = []
    converted_string = ""
    for char in string:
        if char.isupper():
            acronym_list.append(char)
    return converted_string.join(acronym_list)

def mask_string(string):
    """Menuchoice 10, masks an string"""
    masked_part = multiply_str("#", len(string[:-4]))
    unmasked_part = string[-4:]
    result = masked_part + unmasked_part
    return result

def find_all_indexes(string, index_char):
    """Menuchoice 11, finds all indexes of an specific input in a string"""
    index_list = []
    position = 0
    while True: 
        try:
            position = string.index(index_char, position)
            index_list.append(position)
            position += 1
        except ValueError:
            break
    if len(index_list) > 0:
        converted_list_string = ','.join(map(str, index_list))
    else:
        converted_list_string = ""
    return converted_list_string

def multiply_str(string, input_number):
    """Multiplies the string x amount times and makes it to an new string"""
    result_word = ""
    for _ in range(0, input_number):
        result_word += string
    return result_word
