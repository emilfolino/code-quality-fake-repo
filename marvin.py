#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Module that contains the functions of each menuchoice in main.py
gets impoted in main.
"""

import random

def greet():
    """
    Function to greet the user
    """
    name = input("What is your name? ")
    print("\nPopeye says:\n")
    print("Hello %s - fellow sailor!" % name)
    print("What can I do you for?!")

def celcius_to_farenheit():
    """
    Function to convert Celsius to Farenheit
    """
    print("\nPopeye says:\n")
    temp = input("Give me a value in Celsius and I will convert it for you: ")
    temp = round(float(temp) * 9 / 5 + 32, 2)
    print(f"Your temp in Farenheit is {temp}.")

def word_manipulation():
    """
    Function which prints a word multiple times
    """
    print("\nPopeye says:\n")
    word = input("Give me a word: ")
    times = input("How annoying do you want me to be? ")
    print(multiply_str(word, times))

def sum_and_average():
    """
    Function that takes multiple numbers and prints the sum and average of those numbers
    """
    print("\nPopeye says:\n")
    print("Give me the numbers you want and end with done.")
    amount_of_numbers = 0
    sum_value = 0.0
    while True:
        sum_avg_input = input("Value or done: ")
        if sum_avg_input == "done":
            break
        else:
            try:
                sum_value += float(sum_avg_input)
                amount_of_numbers += 1
            except ValueError:
                print("Not a valid number try again.")
    try:
        print(f"The sum of your numbers is {round(sum_value, 2)}"
              f" and the average is {round(sum_value / amount_of_numbers, 2)}")
    except ValueError:
        print("No valid numbers!")

def hyphen_string():
    """
    Function that manipulates a word and hypes it
    """
    print("\nPopeye says:\n")
    word = input("Give me a word: ")
    new_word = ""
    letter_counter = 0
    for letter in word:
        letter_counter += 1
        new_word += letter * letter_counter + "-"
    # Removes the last "-", or rater leaves that out, and prints
    print(new_word[:-1])

def is_isogram():
    """
    Function which checks if words are isograms
    """
    print("\nPopeye says:\n")
    word = input("Give me a word and i will check if it is an isogram: ")
    boolean_is_isogram = True
    for letter in word:
        if word.count(letter) > 1:
            boolean_is_isogram = False
            break
    if boolean_is_isogram:
        print("Match!")
    else:
        print("No match!")

def compare_numbers():
    """
    Function which compares current number with new number(larger, smaller or same)
    """
    print("\nPopeye says:\n")
    while True:
        prev_number = input("Give me the start value: ")
        try:
            prev_number = int(prev_number)
            break
        except ValueError:
            print("not a number!")
    while True:
        new_number = input("Give me a compare number: ")
        if new_number == "done":
            break
        else:
            try:
                new_number = int(new_number)
                if prev_number < new_number:
                    print("larger!")
                elif prev_number > new_number:
                    print("smaller!")
                elif prev_number == new_number:
                    print("same!")
                prev_number = new_number
            except ValueError:
                print("not a number!")

def randomize_string(usr_input):
    """
    Function to return a randomized string from an original
    by moving the characters around. 
    """
    original_string = usr_input
    string_to_randomize = usr_input
    randomized_string = ""
    while len(string_to_randomize) > 0:
        string_to_rand_list = list(string_to_randomize)
        random_index = random.randint(0, len(string_to_randomize) - 1)
        randomized_string += string_to_randomize[random_index]
        del(string_to_rand_list[random_index])
        string_to_randomize = "".join(string_to_rand_list)
    return f"{original_string} --> {randomized_string}"

def get_acronym(usr_input):
    """
    Function which removes all characters but the uppercases
    returns a string with all uppercases
    """
    string_to_process = str(usr_input)
    acro_string = ""
    for letter in string_to_process:
        if letter.isupper():
            acro_string += letter
    return acro_string

def mask_string(usr_input):
    """
    Function that returns a string with all but the last four characters masked.
    """
    string_to_process = str(usr_input)
    last_four_chars = string_to_process[-4 :]
    masked_last_chars = multiply_str("#", len(string_to_process[: -4]))
    return f"{masked_last_chars}{last_four_chars}"

def multiply_str(word, times):
    """
    Function which prints a word multiple times
    """
    return (word * int(times))

def find_all_indexes(first_str, part_first_str):
    """
    Functions that returns a string with all indexes 
    where part_first_str can be found in first_str
    """
    try:
        size_of_first_str = len(first_str)
    except ValueError:
        print("Datatype of type int has no length!")
        return ""
    search_index_saver = 0
    index_str = ""
    while search_index_saver < size_of_first_str:
        search_index = str(first_str).find(part_first_str, search_index_saver)
        if search_index >= 0:
            index_str += str(search_index) + ","
            search_index_saver = search_index + len(part_first_str)
        else:
            break
    return index_str[:-1]
