#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Marvin with a simple menu to start up with.
Marvin doesnt do anything, just presents a menu with some choices.
You should add functinoality to Marvin.
"""

import random


marvin_image = r"""
       
               _/       \_
              / |       | \
             /  |__   __|  \
            |__/((o| |o))\__|
            |      | |      |
            |\     |_|     /|
            | \           / |
             \| /  ___  \ |/
              \ | / _ \ | /
               \_________/
                _|_____|_
           ____|_________|____
          /                   \ 
"""

"""
Its an eternal loop, until q is pressed.
It should check the choice done by the user and call a appropriate
function.
"""


def multiply_str(string_to_multiply, multiple):
    """Returns string_to_mulyiply multiplied multiple times"""
    return string_to_multiply * multiple


def c_to_f(celsius):
    """Convert celsius to farenheit"""
    return round(celsius * 9 / 5 + 32, 2)


# From https://stackoverflow.com/q/2356925
def isFloat(string):
    """Check if a string is representing a float"""
    try:
        float(string)
        return True
    except ValueError:
        return False


ROBOT_NAME = "Cark"


def greet():
    """Greets the user"""
    name = input("What is your name? ")
    print(f"\n{ROBOT_NAME} says:\n")
    print("Hello %s - your awesomeness!" % name)
    print("What can I do you for?!")


def celcius_to_farenheit():
    """Converts the user inputted ceelcius to farenheit"""
    c = float(input("Enter temperature in celisus: "))
    print(f"The temperature in farenheit is {c_to_f(c)}")


def word_manipulation():
    """Repeats a word as many times as what the user inputs"""
    word = input("What is the wors you want me to repeat? ")
    times = int(input("How many times do you want me to repeat it? "))
    output = ""
    for _ in range(times):
        output += word
    print(f"{output}")


def sum_and_average():
    """Sums the numbers inputted and also calculates the average."""
    print(
        "Enter a number one after the other, and I will sum them and calculate the average."
        + "Type 'done' and I'll print the result for you."
    )
    number_or_done = ""
    number_sum = 0
    number_of_inputs = 0
    while number_or_done != "done":
        number_or_done = input("Enter number or 'done': ")
        if number_or_done == "done":
            break
        elif isFloat(number_or_done):
            number_of_inputs += 1
            number_sum += float(number_or_done)
        else:
            print("Faulty input, you can either input numbers or 'done'")
    if number_of_inputs == 0:
        print("No numbers have been put in, returning to menu... BEEP BOOP")
    else:
        print(
            f"The sum is {round(number_sum, 2)} and the average is"
            f" {round(number_sum/number_of_inputs, 2)}"
        )


def hyphen_string():
    """
    Draws out a word, where each letter will be repeated i+1
    times where i is the index of the letter.
    """
    word = input("Enter a word and I will read it in slowmotion: ")
    slowmo_output = ""
    repetitions = 1
    for letter in word:
        slowmo_output += multiply_str(letter, repetitions) + "-"
        repetitions += 1
    slowmo_output = slowmo_output[:-1]
    print(slowmo_output)


def is_isogram():
    """Check if the inputted word is an isogram."""
    potential_isogram = input("Enter a word and I will check if it's an isogram: ")
    seen_letters = []
    isogram = True
    for letter in potential_isogram:
        if letter in seen_letters:
            isogram = False
        seen_letters.append(letter)
    if isogram:
        print("Match!")
    else:
        print("No match!")


def compare_numbers():
    """
    Will compare each consecutive number and outputt if it's
    smaller, larger or the same as the previous one.
    """
    inital_number = input(
        "Start with entering a number, then for each new subsequent number, "
        + "I'll tell you if it's larger or smaller than the previous: "
    )
    if not isFloat(inital_number):
        print("Faulty input, enter a number:")
    else:
        inital_number = float(inital_number)
    while True:
        number = input("Enter a number or 'done': ")
        if number == "done":
            print("Returning to menu... ZOOORP")
            break

        if isFloat(number):
            number = float(number)
            if number == inital_number:
                print("same!")
            elif number < inital_number:
                print("smaller!")
            else:
                print("larger!")
            inital_number = number
        else:
            print("not a number!")


def randomize_string(string_to_shuffle):
    """Shuffles the inputted string"""
    shuffled_string = list(string_to_shuffle)
    random.shuffle(shuffled_string)
    shuffled_string = "".join(shuffled_string)
    return f"{string_to_shuffle} --> {shuffled_string}"


def get_acronym(string_to_acronymisize):
    """Makes an acronym of each uppercase letter in the inputted string"""
    acronym = ""
    for letter in string_to_acronymisize:
        if letter.isupper():
            acronym += letter
    return acronym


def mask_string(string_to_mask):
    """Masks each character except for the last four with a hashtag"""
    masked_characters = multiply_str("#", len(string_to_mask) - 4)
    last_four_characters = string_to_mask[-4:]
    return f"{masked_characters}{last_four_characters}"


def find_all_indexes(base_string, substring):
    """Finds all indexes where substring exists in base_string and returns the locations"""
    index_list = []
    for i in range(len(base_string)):
        try:
            index = base_string.index(substring, i)
            if index not in index_list:
                index_list.append(index)
        except ValueError:
            break
    string_to_print = ""
    for index in index_list:
        string_to_print += f"{index},"
    return string_to_print[:-1]
