#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
functions for marvin choices
"""
import random

def greet():
    """
    greet function
    """
    name = input("What is your name? ")
    print("\nMarvin says:\n")
    print("Hello %s, drinker of water!" % name)
    print("What can I do you for?!")
    

def celcius_to_farenheit():
    """
    converts °C to °F
    """
    print("\nMarvin says:\n")
    temp_c = input("Enter a temperature in °C, and press enter: ") 
    try:
        temp_f = round(float(temp_c) * 9 / 5 + 32, 2) 
        print("\nMarvin says:\n")
        print("%s °C is equivalent to %.2f °F" % (temp_c, temp_f)) 
    except ValueError:
        print("That was not a number.")
    print("What can I do you for?!")


def word_manipulation():
    """
    multiplies a word a number of times
    """
    word = input("Enter a word, press enter: ")
    number = input("Enter a number: ")
    print("\nMarvin says:\n")
    print("You entered %s and %s. That makes: " % (word, number))
    print(multiply_str(word, number))
    print("What can I do you for?!")


def sum_and_average():
    """
    calculates the sum and an average
    """
    total_sum = 0
    counter = 0

    while True:
        text = input("Enter a number or 'done': ")

        if text == "done":
            break
        else:
            number = float(text)
            total_sum += number
            counter += 1
    try:
        print("Total sum is: ", total_sum)
        print("Mean value is: ", round(total_sum / counter, 2))
    except ZeroDivisionError:
        print("Don't you love maths?")
        #break
    

def hyphen_string():
    """
    something something hyphenates a word
    """
    word = input("Enter a word, press enter: ")
    new_word = ""
    for index, letter in enumerate(word):
        new_word = new_word + letter * (index + 1) + "-"
    print(new_word.rstrip("-"))

def is_isogram():
    """
    checks if a word is an isogram
    """
    word = input("Enter a word: ")  
    new_word = ""
    match = True
    for letter in word:
        if letter not in new_word:
            new_word += letter
        else: 
            match = False
            break
    if match:
        print ("Match!")
    else:
        print("No match!")
    
def compare_numbers():
    """
    compares two numbers
    """
    previous = -9999
    current = 0

    while True:
        text = input("Enter an integer or 'done': ")
        try: 
            if text == "done":
                break
            else:
                current = int(text)
                if previous > -9999:
                    if current > previous:
                        print("larger!")
                    elif current < previous:
                        print("smaller!")
                    else:
                        print("same!")

            previous = current
        except ValueError:
            print("not a number!")


def randomize_string(string):
    """
    randomizes a string
    """
    in_str = string
    str1 = list(string)
    result = ""
    random.shuffle(str1)
    for letter in str1:
        result += letter
    return in_str + " --> " + result


def get_acronym(string):
    """
    creates an acronym
    """
    str1 = ""
    for letter in string:
        if letter.isupper():
            str1 += letter
    return str1


def multiply_str(word, number):
    """
    multiplies a word a number of times
    """
    return int(number) * word


def mask_string(string):
    """
    masks all but the last four characters
    """
    str1 = string
    number = 0
    number = len(str1) - 4 
    masked_str = multiply_str("#", number) 

    return masked_str + str1[number:]


def find_all_indexes(string, part):
    """
    finds all indexes
    """
    try:
        str1 = string
        part1 = part
        str_answer = ""
        found = - 1

        while found < len(str1):
            found = str1.index(part1, found + 1)
            str_answer += str(found) + ','

    except ValueError:
        return str_answer.rstrip(",")



def check_strings(str1, str2):
    """
    checks if str2 is in str1
    """
    match = True
    for letter in str2:
        if letter not in str1:
            match = False
        if match:
            return "Match!"
        return "No match!"


def number_doubler(tal, tal_tries):
    """
    doubles a number for a number of times, until resulting number contrains all digits 0-9
    """   
    for x in range(0, tal_tries):
        test_tal = tal * (2**x) 
        str_tal = str(test_tal)
        digits = ""
        for digit in str_tal:
            if digit not in digits:
                digits = digits + digit

        if len(digits) == 10:
            #print(x)
            return "%s times" % (x)

    return "-1 times"


def tab_space(string1):
    """
    replaces tab with spaces
    """
    string2 = string1.replace('\t', '   ')
    return string2

        
def ship_names(word1, word2):
    """
    ships to words (adds names)
    """
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    for letter1 in word1:
        if letter1 in vowels:
            end1vowel = word1.find(letter1)
            break
    for letter2 in word2:
        if letter2 in vowels:
            begin2 = word2.find(letter2) 
            break
    ship = word1[:end1vowel] + word2[begin2:]
    return ship


def calc_points(playerpoints):
    """
    calculates points
    """
    players = ""
    for letter in playerpoints:
        if letter.isalpha(): # det är en spelare
            if letter.lower() not in players:
                players = players + letter.lower()
    result = ""
    for player in players:
        score = 0
        for index, letter in enumerate(playerpoints):
            if letter == player:
                score += int(playerpoints[index+1])
            elif letter == player.upper():
                score -= int(playerpoints[index+1])
        result = result + player + " " + str(score) + ", "
    result = result.rstrip(", ")
    return result


def points_to_grade(score_max, score): 
    """
    calculates a grade from points
    """
    score_max1 = float(score_max)
    score1 = float(score)

    grade = 100 * score1 / score_max1
    a = ""

    if grade < 60:
        a = "F"
    elif 60 <= grade < 70:
        a = "D"
    elif 70 <= grade < 80:
        a =  "C"
    elif 80 <= grade < 90:
        a =  "B"
    elif 90 <= grade <= 100:
        a =  "A"

    return ("score: " + a)


def has_strings(a, b, c, d):
    """
    compares strings
    """
    match_2 = False
    match_3 = False
    match_4 = False
    str1 = a

    if str1.startswith(b):
        match_2 = True
    if c in str1:
        match_3 = True
    if str1.endswith(d):
        match_4 = True
    
    if match_2 is match_3 is match_4 == True:
        return "Match!"
    return "No match"
    
if __name__ == "__main__":
    print("Hello from marvin.py")
