#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
All the functions of Marvin.
Called from the main file.
"""

import random

penguin_jokes = {
    1: "What do penguins like to wear on the beach?\nA beak-ini.", 
    2: "How does a group of penguins make a difficult decision?\n"
       "Flipper coin.",
    3: "What do you call a cold penguin?\nA brrr-d.",
    4: "What is a penguin’s favorite family member?\nAunt Artica!",
    5: "Why did the two penguins jump when they first met?\nThey "
       "were trying to break the ice.",
    6: "Where do penguins go dancing?\nThe Snow Ball.",
    7: "Why would a penguin cross the road twice?\nTo prove he "
       "isn’t a chicken.",
    8: "What is a penguin’s favorite Mexican food?\nBrrrrrr-itos.",
    9: "Why don’t you ever see penguins in Great Britain?\nBecause "
       "they’re scared of Wales!",
    10: "Why didn’t the penguin jump off the iceberg?\nHe got cold "
        "feet.",
    11: "When visiting England, what do nuclear scientists penguins"
        " eat?\nFission chips."
}

def multiply_str(string, number):
    """Multiplies a string"""
    new_string = string * number
    return new_string

def greet():
    """Greets the user"""
    name = input("What is your name? ")
    print("Penguin says:\n")
    print("Hello %s, hope you're having a wonderful day!" % name)
    print("What can I do for you?!")
    
def celcius_to_farenheit():
    """Converts degrees celsius to degrees fahrenheit"""
    try:
        celsius = float(input("Input a temperature in °C, and I'll "
                            "convert it to °F for you: "))
        fahrenheit = round(celsius * 1.8 + 32, 2)
        print(fahrenheit)
    except ValueError:
        print("You did not enter a number.")

def word_manipulation():
    """Repeats a word a number of times"""
    word = input("Input a word: ")
    try:
        repetitions = int(input("Input an integer and I'll "
                                "repeat the word that many "
                                "times: "))
        print(multiply_str(word, repetitions))
    except ValueError:
        print("That was not an integer.")

def sum_and_average():
    """Calculates sum and average for input numbers"""
    user_input = ""
    total = 0
    num_of_ints = 0
    while user_input != "done":
        user_input = input("Input a number, or input "
                            "'done' when you're done: ")
        if user_input == "done":
            try:
                average = round(total/num_of_ints, 2)
                print("The sum of all numbers are " + str(total)
                        + " and the average is " + str(average))
            except ZeroDivisionError:
                print("The sum of all numbers is 0 and the "
                        "average is 0.")
        else:
            try:
                user_input = float(user_input)
                total += user_input
                num_of_ints += 1
            except ValueError:
                print("That was not an integer.")

def hyphen_string():
    """Spells out word with a '-' between each letter"""
    new_word = ""
    word = input("Input a word: ")
    first = True
    for index, letter in enumerate(word):
        if first:
            new_word += letter
            first = False
        else:
            new_word = new_word + "-" + (index + 1) * letter
    print(new_word)

def is_isogram():
    """Checks if a word is an isogram"""
    word = input("Input a word, and I'll check if it's an "
                    "isogram: ").lower()
    if len(word) == len(set(word)):
        print("Match!")
    else:
        print("No match!")

def compare_numbers():
    """Compares an input number with the previous input number"""
    first = True
    old_number = ""
    new_number = ""
    while new_number != "done":
        new_number = input("Input a number: ")
        if new_number == "done":
            break
        else:
            try:
                new_number = int(new_number)
                if first:
                    first = False
                else:
                    if new_number > old_number:
                        print("larger!")
                    elif new_number == old_number:
                        print("same!")
                    else:
                        print("smaller!")
                old_number = new_number
            except ValueError:
                print("not a number!")

def randomize_string(string):
    """Randomize the letters in a string"""
    string_list = list(string)
    random.shuffle(string_list)
    shuffled_string = ''.join(string_list)
    result = f"{string} --> {shuffled_string}"
    return result

def get_acronym(string):
    """Create an acronym for a string"""
    acronym = ""
    for letter in string:
        if letter.isupper():
            acronym += letter
    return acronym

def mask_string(string):
    """Masks all characters of a string but the last four"""
    string_length = len(string)
    new_string = multiply_str("#", string_length - 4) + string[-4:]
    return new_string

def find_all_indexes(string1, string2):
    """
    Find all indexes for the first string where the second string
    occurs
    """
    start = 0
    indexes = ""
    first = True
    while True:
        try:
            index = string1.index(string2, start)
            start = index + 1
            if first:
                indexes += str(index)
                first = False
            else: 
                indexes = indexes + "," + str(index)
        except ValueError:
            break
    return indexes


def word_comparison():
    """
    Checks if all the letters of the second word are included in
    the first word.
    """
    word1 = input("Input a word: ").lower()
    word2 = input("Input another word: ").lower()
    same_letters = True
    for letter in word2:
        if letter not in word1:
            same_letters = False
            break
    if same_letters:
        print("Match!")
    else:
        print("No match!")

def multiplication():
    """
    Multiplies a number with 2 until all digits 0-9 are included
    in the result
    """
    all_numbers = 1234567890
    try:
        number = int(input("Input an integer which I will "
                        "multiply with 2 until all numbers 0-9 "
                        "are included: "))
        multiplications = int(input("Input the max amount of "
                                    "times you want me to "
                                    "multiply: "))
    except ValueError:
        print("That was not an integer.")
    previous_multiplications = multiplications
    while multiplications > 0:
        if set(str(number)) == set(str(all_numbers)):
            print(previous_multiplications - multiplications,
                    "times")
            break
        else:
            number *= 2
            multiplications -= 1
    if multiplications == 0:
        if set(str(number)) == set(str(all_numbers)):
            print(previous_multiplications, "times")
        else:
            print(-1)

def replace_tab():
    """Replaces each tab with three spaces"""
    string = input("Input a string and all the tabs will be "
                    "replaced by 3 spaces: ")
    new_string = ""
    for character in string:
        if character == "\t":
            new_string += "   "
        else:
            new_string += character
    print(new_string)
    
def merge_names():
    """Merges two names into one"""
    vowels = "aoueiy"
    index_name1 = 0
    index_name2 = 0
    name1 = input("Input the first name: ")
    name2 = input("Input the second name: ")
    for index, letter in enumerate(name1):
        if letter in vowels:
            index_name1 = index
            break
    for index, letter in enumerate(name2):
        if letter in vowels:
            index_name2 = index
            break
    merged_name = name1[:index_name1] + name2[index_name2:]
    print(merged_name)

def penguin_joke():
    """Tell a penguin-related joke"""
    joke_number = random.randint(1, 11)
    print(penguin_jokes[joke_number])
