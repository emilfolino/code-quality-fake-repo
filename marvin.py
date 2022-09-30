#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Marvin with a simple menu to start up with.
Marvin doesn't do anything, just presents a menu with some choices.
You should add functionality to Marvin.
"""

import random

# choice == 1
def greet():
    """
    Marvin greets user and asks for name
    """
    name = input("Say, what should I call you? ")
    print("\nMarvin says:\n")
    print("Hello %s - your awesomeness! A pleasure to meet you!" % name)
    print("What can I do you for?!")

# choice == 2
def celsius_to_fahrenheit():
    """
    Converts given celsius to fahrenheit 
    """
    try: #The use of float() makes it possible to enter decimals as well as integers
        celsius = float(input("Enter the temperature in celsius degrees: ")) 
        fahrenheit = round((celsius * (9 / 5) + 32), 2)
        print(fahrenheit)
    except ValueError:
        print("This is not a valid number, please re-enter your menu choice and try again.")

# choice == 3
def word_manipulation():
    """
    Multiplies a given word by a given amount of times
    """
    word = input("Please enter the word you would like to multiply: ")
    try:
        digit = int(input("Please enter a digit: "))
        print(multiply_str(word, digit))
    except ValueError:
        print("That is not a valid digit, please re-enter your menu choice and try again.")

# choice == 4
def sum_and_average():
    """
    Continuously asks for a number until user enters 'done'.
    Calculates the sum and average of the inputted numbers and concatenates the result into a string.
    """
    the_sum = 0 #gatherer variable
    counter = 0 #stepper
    average = 0 # This variable is dependent on the two above
    number_input = input("Enter a number or 'done' for results: ") #most recent holder
    while number_input != "done":
        try:
            number_input = float(number_input)
            the_sum += number_input
            counter += 1
            number_input = input("Enter a number or 'done' for results: ")
        except ValueError:
            print("Oops! This is not a valid number.")
            number_input = input("Enter a number or 'done' for results: ")
    average = round((the_sum / counter), 2)
    print("The sum of all numbers is " + str(the_sum) + " and the average is " + str(average) + ".")

# choice == 5
def hyphen_string():
    """
    Takes a string input and creates a new string where each character in the given string has 
    gradually increased by 1 more than the previous character.
    Prints the new string.
    """
    user_string = input("Enter something: ")
    recreated_string = ""
    stepper = 1 #gradually increases with +1 for each character
    for char in user_string:
        recreated_string += multiply_str(char, stepper) + "-"
        stepper += 1
    #recreated_string = recreated_string ...Remove "-" from the end????
    print(recreated_string)

# choice == 6
def is_isogram():
    """
    Checks if a word is an isogram.
    Prints "Match!" or "no match!" depending on the answer.
    """
    word_isogram = input("Enter a word: ") #For entered numbers, should there be a different output than "match!"?
    word_validator = "" # Word is reassembled letter by letter until two of the same letter are discovered
    isogram = True # one-way-flag (truthiness)
    for letter in word_isogram:
        if letter in word_validator:
            isogram = False
        else:
            word_validator += letter
    if isogram:
        print("Match!")
    else:
        print("No match!")

# choice == 7
def compare_numbers():
    """
    Compare a current inputted number with a previous and prints "larger!", "smaller!", or "same!" accordingly.
    """
    previous_number = input("Enter a number: ") #previous variable / follower
    current_number = 0
    while current_number != "done":
        try:
            previous_number = float(previous_number)
            current_number = input("Enter a number or 'done' to quit: ") #current variable / recent holder
            if current_number == "done":
                print("Quitting")
            else:
                try:
                    current_number = float(current_number)
                except ValueError:
                    print("not a number!")
                    continue
                if current_number > previous_number:
                    print("larger!") 
                elif current_number == previous_number: 
                    print("same!")
                else:
                    print("smaller!") 
                previous_number = current_number
        except ValueError:
            print("This is not a valid number. Please try again")
            previous_number = input("Enter a number: ")

# choice == a1
def word_in_word():
    """
    This function is used to check if the second given word exist in the first
    """
    word1 = input("Enter your first word: ")
    word2 = input("Enter your second word: ")
    match = True
    for letters in word2:
        if letters not in word1:
            match = False
    if match:
        print("Match!")
    else:
        print("No match!")

# choice == a3
def replace_tab_in_string():
    """
    Takes strings with at least one tab and replaces the tab with three spaces.
    Prints the new string with replaced tabs.
    """
    tab = "\t" 
    string_with_tab = input("Enter a string with at least one tab: ")
    new_string_spaces = ""
    if tab not in string_with_tab:
        print("Please enter a string with at least one tab and try again.")
    else:
        for letter in string_with_tab:
            if letter == tab:
                letter = "   "
            new_string_spaces += letter
    print(new_string_spaces)

# choice == 8
def randomize_string(original_word):
    """
    Takes a original word/string and builds up another word with the letters picked randomly from the given word.
    """
    also_word = original_word
    randomized_word = ""
    while original_word:
        letter_index = random.randint(0, len(original_word) - 1)
        randomized_word += original_word[letter_index]
        original_word = original_word[0:letter_index] + original_word[letter_index +1:]
    return f"{also_word} --> {randomized_word}"

# choice == 9
def get_acronym(user_string):
    """
    Creates an acronym with all upper case letters of a given string.
    """
    acronym = ""
    for letters in user_string:
        if letters.isupper():
            acronym += letters
    if acronym:
        msg = acronym
    else:
        msg = "There were no upper case letters in your string."
    return msg

# choice == 10
def mask_string(string):
    """
    Replaces all but the last four characters of a string with # using the function "multiply_str".
    """
    number_of_hashtags = len(string) - 4
    masked_string = multiply_str("#", number_of_hashtags) + string[-4:]
    return masked_string

# multiply_str function used in choice 10, and 3
def multiply_str(word, integer):
    """
    Multiplies the string with the integer and returns the new multiplied string.
    """
    return word * integer

# choice == 11
def find_all_indexes(string, substring):
    """
    Asks for a string and a substring and returns all the indexes of the substring in the string. 
    If the substring does not exist in the string, an empty string will be returned.
    """
    indexes = ""
    current_index = 0
    string_found = True
    start = 0
    try:
        current_index = string.index(substring, start)
        indexes += str(current_index) + ","
        start = current_index
    except ValueError:
        indexes = ","
        string_found = False
    while string_found:
        try:
            current_index = string.index(substring, start + 1)
            indexes += str(current_index) + ","
            start = current_index
        except ValueError:
            string_found = False
    return indexes[:len(indexes) - 1]

# choice == b1
def points_to_grade(your_points, maximum):
    """
    Calculates your grade based on your points and the maximum amount of points.
    """
    grade = ""
    try:
        percentage = (float(your_points) / float(maximum)) * 100
        if percentage >= 90:
            grade += "A"
            msg = f"score: {grade}"
        elif percentage >= 80:
            grade += "B"
            msg = f"score: {grade}"
        elif percentage >= 70:
            grade += "C"
            msg = f"score: {grade}"
        elif percentage >= 60:
            grade += "D"
            msg = f"score: {grade}"
        else:
            grade += "F"
            msg = f"score: {grade}"
    except (ValueError, ZeroDivisionError):
        msg = "This is either not a valid number, or your number leads to a zero division."
    return msg

# choice == b2
def has_strings(string1, string2, string3, string4):
    """
    Compares 4 given strings. 
    Checks whether first string starts with second string, contains third, and ends with last string.
    """
    include_strings = False
    if string1.startswith(string2):
        if string3 in string1:
            if string1.endswith(string4):
                include_strings = True
    if include_strings:
        msg = "Match"
    else:
        msg = "No match"
    return msg


if __name__ == "__main__":
    randomize_string("elephant")
