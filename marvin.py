#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Funktioner som används till programmet Marvin."""

import random

def greet():
    """Greets the user."""
    name = input("What is your name? ")
    print("\nMarvin says:\n")
    print(f"Hello {name}, it's great to have you here!")
    print("What can I do you for?!")

def celcius_to_farenheit():
    """Converts celsius to farenheit."""
    temperature = input("Enter a temperature in Celsius: ")
    print("\nMarvin says:\n")
    print(round(float(temperature) * 1.8 + 32, 2))

def word_manipulation():
    """Manipulates a string."""
    word = input("Enter a word: ")
    number = input("Enter a number: ")
    print("\nMarvin says:\n")
    print(multiply_str(word, int(number)))

def sum_and_average():
    """Calculates sum and average."""
    num_list = []
    number = ""
    while number != "done":
        number = input("Enter a number (write \"done\" if finished): ")
        if number == "done":
            break
        num_list.append(float(number))
    num_list_sum = round(sum(num_list), 2)
    num_list_average = round(num_list_sum/len(num_list), 2)
    print("\nMarvin says:\n")
    print(f"The sum of the numbers is: {num_list_sum}\nThe average of the numbers is: {num_list_average}")

def hyphen_string():
    """Finds hyphens in a string."""
    word = input("Enter a string: ")
    print("\nMarvin says:\n")
    the_string = ""
    count = 1
    for letters in word:
        the_string += letters*count+"-"
        count += 1
    the_string = the_string[:-1]
    print(the_string)

def is_isogram():
    """Checks if a word is an isogram or not."""
    word = input("Enter a word: ")
    print("\nMarvin says:\n")
    for letters in word:
        if word.count(letters) > 1:
            print("No match!")
            break
        elif letters in word[-1]:
            print("Match!")

def compare_numbers():
    """Compares different numbers."""
    previous_number = 0
    first_time = 1
    count = 0
    number = ""
    while number != "done":
        try:
            number = float(input("Enter a number: "))
        except ValueError as e:
            if "done" in str(e):
                break
            print("not a number!")
            continue
        if first_time == 1:
            previous_number = number
            while True:
                try:
                    number = float(input("Enter a second number: "))
                    break
                except ValueError as e:
                    if "done" in str(e):
                        count = 1
                        break
                    print("not a number!")
                    continue
            if count == 1:
                break
            first_time = 0
        print("\nMarvin says:\n")
        if number > previous_number:
            print("larger!\n")
        elif number < previous_number:
            print("smaller!\n")
        else:
            print("same!\n")
        previous_number = number

def randomize_string(string):
    """Randomizes the order of characters in a string."""
    string_list = list(string)
    random.shuffle(string_list)
    result = "".join(string_list)
    return f"{string} --> {result}"

def get_acronym(string):
    """Returns the acronyms in a string."""
    result = ""
    for char in string:
        if char.isupper():
            result += char
    return result

def mask_string(string): 
    """Masks part of a string."""
    if len(string) < 4:
        result = string
    elif len(string) >= 4:
        result = multiply_str("#", len(string)-4) + string[len(string)-4:]
    return result

def multiply_str(string, integer):
    """Multiplies a string with an integer."""
    return string * integer

def find_all_indexes(arg1, arg2):
    """Finds the indexes of a substring in another string."""
    count = 0
    result = ""
    while count != len(arg1):
        try:
            result += str(arg1.index(arg2, count, len(arg2)+count)) + ","
            count += 1
        except ValueError:
            count += 1
    result = result[:-1]
    return result
    
def menyval_q():
    """Prints a goodbye message."""
    print("Bye, bye - and welcome back anytime!")
