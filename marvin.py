#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Menu choices for Marvin
"""

import random

def greet():
    """
    K-9 greets you
    """
    name = input("What is your name? ")
    print("\nK-9 says:\n")
    print("Hello, %s - nice to meet you!" % name)

def celcius_to_farenheit():
    """
    Converts Celsius to Fahrenheit
    """
    temp = float(input("Give me a temperature in Celsius: ")) * 9 / 5 + 32
    print("That's " + str(round(temp, 2)) + " Fahrenheit")

def word_manipulation():
    """
    Repeats a word
    """
    word = input("Give me a word: ")
    number = int(input("How many times should I repeat it? "))
    for _ in range(number):
        print(word, end = "")
    print("")

def sum_and_average():
    """
    Calculates sum and average of severals numbers
    """
    total = 0
    count = 0
    while True:
        text = input("Give me a number or type 'done': ")
        if text == "done":
            break
        else:
            total += float(text)
            count += 1
    if count == 0:
        count = 1
    print("The sum of all numbers is " + str(total) + " and the average is " + str(round(total / count, 2)))

def hyphen_string():
    """
    Repeats letters in a word with hyphens between them
    """
    word = input("Give me a word: ")
    new_word = ""
    count = 1
    for letter in word:
        new_word += letter * count + "-" * int(count < len(word))
        count += 1
    print(new_word)

def is_isogram():
    """
    Checks if a word is an isogram
    """
    word = input("Give me a word: ")
    length = len(word)
    isogram = True
    for index in range(length):
        for index2 in range(index + 1, length):
            if word[index] == word[index2]:
                isogram = False
                break
        if not isogram:
            break
    if isogram:
        print("Match!")
    else:
        print("No match!")

def compare_numbers():
    """
    Compares numbers
    """
    while True:
        try:
            previous = int(input("Give me the first number: "))
        except ValueError:
            print("not a number!")
            continue
        break
    while True:
        text = input("Give me a number or type 'done': ")
        if text == "done":
            break
        else:
            try:
                current = int(text)
            except ValueError:
                print("not a number!")
                continue

            if current > previous:
                print("larger!")
            elif current < previous:
                print("smaller!")
            else:
                print("same!")
            previous = current

def letters_in_word():
    """
    Checks if word contains letters
    """
    word = input("Give me a word: ").lower()
    letters = input("Give me some letters: ").lower()
    match = True
    for letter in letters:
        if not letter in word:
            match = False
            break
    if match:
        print("Match!")
    else:
        print("No match!")

def double_number():
    """
    Doubles a number until it contains all digits
    """
    number = int(input("Give me a number: "))
    max_times = int(input("How many times should I try? "))
    times = 0
    while times <= max_times:
        all_digits = True
        for digit in range(10):
            if str(digit) not in str(number):
                all_digits = False
                break
        if all_digits:
            break
        number *= 2
        times += 1
    if not all_digits:
        times = -1
    print("Answer:", times, "times")

def tab_to_spaces():
    """
    Replaces tab with three spaces
    """
    text = input("Give me some text: ")
    new_text = ""
    for letter in text:
        if letter == "\t":
            new_text += "   "
        else:
            new_text += letter
    print(new_text)

def combine_names():
    """
    Combines two names
    """
    name1 = input("Give me a name: ")
    name2 = input("Give me another name: ")
    new_name = ""
    vowels = "aeiouy"
    for letter in name1:
        if letter in vowels:
            break
        else:
            new_name += letter
    found_first_vowel = False
    for letter in name2:
        if found_first_vowel:
            new_name += letter
        elif letter in vowels:
            found_first_vowel = True
            new_name += letter
    print(new_name)

def randomize_string(string):
    """
    Randomizes a string
    """
    return string + " --> " + "".join(random.sample(string, len(string)))

def get_acronym(string):
    """
    Creates acronym for string
    """
    acronym = ""
    for letter in string:
        if letter.isupper():
            acronym += letter
    return acronym

def multiply_str(string, integer):
    """
    Multiplies string with integer
    """
    return string * integer

def mask_string(string):
    """
    Hides all characters except the last four in a string
    """
    return multiply_str("#", len(string) - 4) + string[-4:]

def find_all_indexes(string, substring):
    """
    Returns all indexes where substring appears in string
    """
    start = 0
    indexes = ""
    while start < len(string):
        try:
            index = string.index(substring, start)
        except ValueError:
            break
        indexes += str(index) + ","
        start = index + 1
    if not indexes == "":
        indexes = indexes[0:-1]
    return indexes

def points_to_grade(max_points, points):
    """
    Calculates grade based on points and max_points
    """
    percentage = float(points) / float(max_points)
    score = "score: "
    if percentage >= 0.9:
        score += "A"
    elif percentage >= 0.8:
        score += "B"
    elif percentage >= 0.7:
        score += "C"
    elif percentage >= 0.6:
        score += "D"
    else:
        score += "F"
    return score

def has_strings(string, start, substring, end):
    """
    Checks if string starts with start, contains substring, and ends with end
    """
    if string.startswith(start) and substring in string and string.endswith(end):
        return "Match"
    return "No match"
