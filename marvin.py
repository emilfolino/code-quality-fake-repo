#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Marvin functions
"""
import random

def multiply_str(word, number):
    """
    Multiplies strings
    """
    multipliedWord = ""
    for _ in range(number):
        multipliedWord = multipliedWord + word
    return multipliedWord

def quits():
    """
    Quits
    """
    print("I return to my sleep for the time being, visit me again some time.")

def greet():
    """
    Greets
    """
    name = input("Tell me your name: ")
    print("\nMalle says:\n")
    print("Hello %s!" % name)
    print("How can I help you?")

def celcius_to_farenheit():
    """
    Translates from celcius to farenheit
    """
    temp = input("What temperature in Celcius would you like to translate into Fahrenheit? ")
    fahrenheit = round(float(temp) * 9/5 + 32, 2)
    print(str(temp) + " Celcius in Fahrenheit is " + str(fahrenheit))

def word_manipulation():
    """
    Multiplies words
    """
    word = input("What word would you like multiplied? ")
    times = int(input("How many times do you want that word multiplied? "))
    print("Okay, here are your words: ")
    print(multiply_str(word, times))

def sum_and_average():
    """
    Gives total and average of numbers
    """
    print("When you're done, just type 'done'")
    user_number = ""
    newnumber = 0
    timesnumber = 0
    while True:
        user_number = input("Give me a number: ")
        if user_number == "done":
            print("Your total is: " + str(newnumber) + " and the average is " 
            + str(round(newnumber / timesnumber, 2)))
            break
        elif user_number.isnumeric:
            newnumber = newnumber + float(user_number)
            timesnumber = timesnumber + 1
        else:
            print("That's not a valid number, please only use numbers")

def hyphen_string():
    """
    Shakes a word about
    """
    word_string = input("What word do you want me to mess up? ")
    new_word = ""
    times_new = 1
    for letter in word_string:
        concat_letter = ""
        for _ in range(times_new):
            concat_letter = concat_letter + letter
        new_word = new_word + concat_letter + "-"
        times_new = times_new + 1
    print(new_word[:-1])

def is_isogram():
    """
    Checks if input is an isogram
    """
    isoword = input("What word would you like me to check? ")
    is_iso = False
    check_string = ""
    for letter in isoword:
        if letter in check_string:
            is_iso = False
            break
        else:
            is_iso = True
        check_string = check_string + letter
    if is_iso:
        print("Match!")
    elif not is_iso:
        print("No match!")

def compare_numbers():
    """
    Compares numbers
    """
    print("Just put 'done' when you feel done.")
    first_number = input("Give me a number: ")
    second_number = input("Give me a second number: ")
    while second_number != "done":
        try:
            if int(first_number) > int(second_number):
                first_number = second_number
                print("smaller!")
            elif int(first_number) < int(second_number):
                first_number = second_number
                print("larger!")
            elif int(first_number) == int(second_number):
                first_number = second_number
                print("same!")
        except Exception:
            print("not a number!")
        second_number = input("Next number to check: ")

def randomize_string(word):
    """
    Randomizes a string
    """
    newWord = "".join(random.sample(word, len(word)))
    return word + " --> " + newWord

def get_acronym(name):
    """
    Makes an acronym
    """
    acronym = ""
    for letter in name:
        if letter.isupper():
            acronym = acronym + letter
    return acronym

def mask_string(stringToMask):
    """
    Masks a string
    """
    return multiply_str("#", len(stringToMask)-4) + stringToMask[-4:]


def find_all_indexes(wholeString, partString):
    """
    Finds all indexes
    """
    indexNumber = 0
    output = ""
    try:
        for i in range(len(wholeString)):
            if int(i) >= int(indexNumber):
                indexNumber = str(wholeString.index(partString, int(indexNumber)+len(partString)))
                output = output + indexNumber + ","
    except ValueError:
        return output[:-1]
    return output[:-1]

#Extras

def a1():
    """
    Checks if letters in word
    """
    string_one = input("Give me a word: ")
    string_two = input("Give me the letters you want me to check: ")
    same = False
    for letter in string_two:
        same = bool(letter in string_one)
        if same is False:
            break
    if same:
        print("Match!")
    else:
        print("No match!")

def a2():
    """
    Multiplies numbers until the contain all numbers
    """
    input_number = input("What number do you want to use? ")
    try_time = input("How many times should I try before I give up? ")
    exists = 0
    tries = 0
    while int(try_time) > 0 and exists < 10:
        try_time = int(try_time) -1
        exists = 0
        tries = tries + 1
        input_number = int(input_number) * 2
        for number in "0123456789":
            if number in str(input_number):
                exists = int(exists) + 1
    if exists != 10:
        tries = -1
    elif exists == 10 and tries == try_time:
        tries = 0
    print("Answer: " + str(tries) + " times")

def a3():
    """
    Replaces tabs with 3 spaces
    """
    string = input("Give me something with tabs in it: ")
    new_line = ""
    for char in string:
        if char == "\t":
            new_line = new_line + "   "
        else:
            new_line = new_line + char
    print(new_line)

def a4():
    """
    Makes shipnamnes
    """
    name_one = input("Give me a name: ")
    name_two = input("Give me another name: ")
    new_name1 = ""
    new_name2 = ""
    vowles = "aeiouy"
    count = 0
    for letter in name_one:
        if letter not in vowles:
            new_name1 = new_name1 + letter
        else:
            break
    for letter in name_two:
        if letter in vowles:
            new_name2 = name_two[count:len(name_two)]
            break
        count = count + 1
    print(new_name1 + new_name2)

def a5():
    """
    Counts points
    """
    input_string = input("Give me a string, every other character a letter and the next a number. ")
    letters = []
    points = []
    where = 0
    position = 0
    result = ""
    small_string = input_string.lower() #Make it small to match when searching
    for letter in small_string:
        where = where + 1 #Counter for index of points
        if letter.isalpha():
            point = input_string[where] #Gives the number after letter
            if input_string[where-1].isupper(): #If letter is capital change points
                point = 0 - int(point)
            if letter not in letters: #If bit isn't already in the lists
                letters.append(letter)
                points.append(point)
            else: #If the bit IS in the lists, add it
                position = int(letters.index(letter))
                points[position] = int(points[position]) + int(point)
    for i, _ in enumerate(letters): #Mix the two lists for result
        result = result + letters[i] + " " + str(points[i]) + ", "
    result = result[:-2]
    print(result)

def points_to_grade(maxPoints, points):
    """
    Turn points to a grade
    """
    grade = ""
    if int(points) >= ((int(maxPoints)/100)*90):
        grade = "A"
    elif int(points) >= ((int(maxPoints)/100)*80):
        grade = "B"
    elif int(points) >= ((int(maxPoints)/100)*70):
        grade = "C"
    elif int(points) >= ((int(maxPoints)/100)*60):
        grade = "D"
    elif int(points) <= ((int(maxPoints)/100)*60):
        grade = "F"
    return "score: " + grade

def has_strings(fullString, startString, middleString, endString):
    """
    Check if string contains strings
    """
    matches = "No match"
    if fullString.startswith(startString) and middleString in fullString and fullString.endswith(endString):
        matches = "Match"
    return matches
