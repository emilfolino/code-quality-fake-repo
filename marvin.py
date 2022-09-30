"""
Module that contains functions called from main.py
"""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random
def greet():
    """
    Greet the user.
    """
    name = input("What is your name? ")
    print("\nWolferz says:\n")
    print("Hello %s - your awesomeness!" % name)
    print("What can I do you for?!")

def celcius_to_farenheit():
    """
    Return degrees from celsius to fahrenheit.
    """
    degrees_celsius = float(input("Enter degrees in Celsius and I shall return it in Fahrenheit. "))
    degrees_fahrenheit = round((degrees_celsius * 1.8) + 32, 2)
    print(float(degrees_fahrenheit))

def word_manipulation():
    """
    Return the string that contains x number of the original string.
    """
    word = input("Give me a word. ")
    number = int(input("Give me a number. "))
    print(multiply_str(word, number))

def sum_and_average():
    """
    Return the sum and average of the values entered.
    """
    value = input("Enter a value or type 'done'. ")
    list_of_values = []
    loop = True
    if value != "done":
        list_of_values.append(float(value))
    else:
        loop = False
    while loop:
        value = input("Enter a value or type 'done'. ")
        if value == "done":
            break
        else:
            value = float(value)
            list_of_values.append(value)
    print(list_of_values)
    sum_of_values = 0
    for count_ele in enumerate(list_of_values):
        sum_of_values += list_of_values[count_ele[0]]
    sum_of_values = round(sum_of_values, 2)

    average_value = round((sum_of_values / len(list_of_values)), 2)

    print("The sum is: " + str(sum_of_values))
    print("The average value is " + str(average_value))

def hyphen_string():
    """
    Return a string where every character is added x times. X starting at 1 and increases every new character.
    """
    string = input("Write something. ")
    new_string = ""
    number = 0
    for count_ele in enumerate(string):
        new_string += string[count_ele[0]] + (string[count_ele[0]] * number)
        number += 1
        if count_ele[0] < len(string)-1:
            new_string += "-"
    print("The new string is: " + new_string)

def is_isogram():
    """
    Check if a word is an isogram.
    """
    word = input("Write a word.\n")
    word_list = []
    letter = ""
    isogram = True
    for count_ele in enumerate(word):
        word_list.append(word[count_ele[0]])

    for letter in word:
        word_list.pop(0)
        if letter in word_list:
            isogram = False
            break

    if isogram is False:
        print("No match!")
    else:
        print("Match!")

def compare_numbers():
    """
    Check if number is larger, smaller or same than the other number.
    """
    value = int(input("Enter a value to start with. "))
    while True:
        try:
            new_value = input("Enter a new value or 'done': ")

            new_value = int(new_value)

            if new_value > value:
                print("larger!")
            elif new_value < value:
                print("smaller!")
            else:
                print("same!")
            value = new_value

        except ValueError:
            if new_value == "done":
                break
            else:
                print("not a number!")

def randomize_string(string):
    """
    Shuffle the string.
    """
    string_list = list(string)
    random.shuffle(string_list)
    new_string = "".join(string_list)
    return string + " --> " + new_string

def get_acronym(string):
    """
    Turn a string into an acronym.
    """
    acronym = ""
    for count_ele in enumerate(string):
        if count_ele[1].isupper():
            acronym += count_ele[1]
    return acronym

def mask_string(string):
    """
    Replace the string with a masked version.
    """
    string_list = list(string)
    string_length = len(string)
    number_of_masks = string_length-4
    if number_of_masks <= 0:
        return string
    masked_string = multiply_str("#", number_of_masks)
    last_four = "".join(string_list[-4:])
    masked_string += last_four
    return masked_string

def multiply_str(string, number):
    """
    Return the string that contains x number of the original string.
    This function is used in other functions.
    """
    new_string = string * number
    return new_string

def find_all_indexes(string, substring):
    """
    Find all indexes where substring exists in string.
    """
    indexes = ""
    string_length = len(string)
    start = 0
    while True:
        try:
            index = string.index(substring, start+1, string_length)
            indexes += str(index) + ","
            start = index
        except ValueError:
            break
    return indexes[:-1]
