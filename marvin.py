#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" 
This module contains functions for every meny option available when
using Marvin.
"""

import random

def quit_program():
    """Exits the program."""
    print("Bye, bye - and welcome back anytime!")

def greet():
    """"Asks for a name and says hello."""
    name = input("What is your name? ")
    print("Darwin says:\n")
    print("Hello %s - your awesomeness!" % name)
    print("What can I do you for?!")        

def celcius_to_farenheit():
    """Converts a temperature from Celsius to Farenheit"""
    celsius_temp = float(input("What is the temperature in Celsius?"))
    farenheit_temp = celsius_temp * 1.8 + 32
    print("The temperature in Farenheit is: " + str(round(farenheit_temp,2)))

def word_manipulation():
    "Prints a word a number of times."
    word = input("What's the word?")
    number = int(input("How many times?"))
    print(word*number)

def sum_and_average():
    """Calculates the sum and average of a collection of numbers"""
    numbers = []
    answer = ""
    while(True):
        answer = input("Enter the next number. Write 'done' if you're done:")
        if answer == "done":
            break
        try: 
            float(answer)
        except ValueError: 
            print("You didn't enter a number!")
            continue
        numbers.append(float(answer))
    if len(numbers) == 0:
        print("You didn't enter any numbers!")
    else:
        total_sum = round(sum(numbers),2)
        average = round(total_sum / len(numbers),2)
        print(f"The sum is {total_sum} and the average is {average}")

def hyphen_string():
    """Puts hyphens between letters of a word, an iterates them an 
    increasing amount."""
    word = input("Please enter your word:")
    output = ""
    repeat_amount = 1
    first_iteration = True
    for letter in word:
        if not first_iteration:
            output += "-"
        output += letter * repeat_amount
        repeat_amount += 1
        first_iteration = False
    print(output)

def is_isogram():
    """Checks if a word has no repeated letters."""
    word = input("Enter your word:")
    isogram = True
    for current_letter in word:
        matches = 0
        for check_letter in word:
            if current_letter == check_letter:
                matches += 1
        if matches > 1:
            isogram = False
    if isogram:
        print("Match!")
    else:
        print("No match!")

def compare_numbers():
    """Compares the size of different numbers."""
    previousnumber = None
    newnumber = None
    while True:
        newinput = input("Please enter a number. Type in 'done'"
        " when you're done:") 
        if newinput == 'done':
            break 
        try:
            float(newinput)
        except ValueError:
            print("That's not a number!")
            continue
        if previousnumber is None:
            print("You need a second number to start comparing.")
            newnumber = float(newinput)
            previousnumber = newnumber
        else:
            previousnumber = newnumber
            newnumber = float(newinput)
            if newnumber > previousnumber:
                print("larger!")
            elif newnumber < previousnumber:
                print("smaller!")
            elif newnumber == previousnumber:
                print("same!")

def compare_strings():
    """Compare if a string contains every letter of a second string."""
    print("This tool asks for two strings, and checks if the first string"
    " contains every letter in the second string")
    first_string = input("Input the first string:")
    second_string = input("Input the second string:")
    match = True
    for letter_second in second_string:
        ind = first_string.find(letter_second)
        if ind == -1:
            match = False
            break
        else:
            first_string = first_string[:ind] + first_string[ind+1:]

    if match:
        print("Match!")
    else:
        print("No match!")

def double_number_check():
    """Doubles a numbers until the result contains every digit."""
    number = int(input("Enter a number to double:"))
    max_times = int(input("How many times should I try before I give up?"))
    answer = -1
    current_times = 0
    for _ in range(0,max_times+1):
        match = True
        for dig in range(0,10):
            if str(dig) not in str(number):
                match = False
        if match:
            answer = current_times
            break 
        number = number * 2
        current_times += 1
    print("Answer: " + str(answer) + " times")
    
def replace_tabs():
    """Replaces tabs with spaces."""
    input_string = input("Input a string:")
    input_string = input_string.replace("\t","   ")
    print(input_string)

def combine_names():
    """Combines two names in one."""
    first_name = input("Enter the first name:")
    second_name = input("Enter the second name:")
    short_first = ""
    short_second = ""
    vowels = "aeiouy"
    for i, letter in enumerate(first_name):
        if letter in vowels:
            short_first = first_name[:i]
            break
    for i, letter in enumerate(second_name):
        if letter in vowels:
            short_second = second_name[i:]
            break
    print(short_first + short_second)   
    
def calculate_points():
    """Calculate the points of different players based on input."""
    input_str = input("Enter your string:")
    players = []
    points = []

    #Check every letter, add to players if new, add points based on case.
    #The indexes of the players list matches the indexes of the point list.
    for i, letter in enumerate(input_str):
        if i % 2 == 1:
            continue
        if letter.lower() not in players:
            players.append(letter.lower())
            points.append(0)
        index = players.index(letter.lower())
        if letter.islower():
            points[index] += int(input_str[i+1])
        else:
            points[index] -= int(input_str[i+1])
            print(points[index])
            print(int(input_str[i+1]))

    result_string = ""
    first_iteration = True

    # Create result string and print it
    for i, player in enumerate(players):
        if first_iteration:
            result_string = result_string + player + " " + str(points[i])
            first_iteration = False
        else:
            result_string = result_string + ", " + player + " " + str(points[i])
    print(result_string)    

def randomize_string(string):
    """Randomizes the order of letters in a string."""
    list_of_string = list(string)
    random.shuffle(list_of_string)
    new_string = "".join(list_of_string)
    return string + " --> " + new_string

def get_acronym(string):
    """Finds and acronym based on capital letters in a string."""
    acronym = ""
    for letter in string:
        if letter.isupper():
            acronym = acronym + letter
    return acronym

def mask_string(string):
    """Masks every letter in a string except the final four."""
    if len(string) < 5:
        return string
    return multiply_str("#",len(string)-4) + string[-4:]

def multiply_str(string,repeat):
    """Multiples a string a certain number of times."""
    return string * repeat

def find_all_indexes(long_string,short_string):
    """Finds every index of occurences of a shorter string in a longer string."""
    if short_string not in long_string:
        return ""
    start = 0
    index_string = ""
    while True:
        try:
            found_index = long_string.index(short_string,start)
        except ValueError:
            break          
        start = found_index+1
        index_string += str(found_index) + ","
    return index_string[:-1]

def points_to_grade(max_points,your_points):
    """Calculates a grade based on a maximum of points and the actual points."""
    ratio = int(your_points) / int(max_points)
    grade = ""
    if ratio > 0.9:
        grade = "A"
    elif ratio > 0.8:
        grade = "B"
    elif ratio > 0.7:
        grade = "C"
    elif ratio > 0.6:
        grade = "D"
    else:
        grade = "F"
    return "score: " + grade

def has_strings(first,second,third,fourth):
    """Checks whether the first string starts with the second, contains the third,
    and ends with the third."""
    if not first.startswith(second):
        return "No match"
    if third not in first:
        return "No match"
    if not first.endswith(fourth):
        return "No match"
    return "Match"
