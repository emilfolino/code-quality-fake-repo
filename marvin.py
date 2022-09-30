#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Contains all the functions called for from main.py"""

from random import shuffle

def greet():
    """Inputs a name and replies with the name"""
    name = input("What is your name? ")
    print("\nColossus says:\n")
    print("Hello %s - your awesomeness!" % name)
    print("What can I do you for?!")

def celcius_to_farenheit():
    """Converts celsius to fahrenheit"""
    celsius = input("Temperature in Celsius: ")
    fahrenheit = float(celsius) * (9/5) + 32
    fahrenheit = round(fahrenheit, 2)
    text = ("Temperature in Fahrenheit: " + str(fahrenheit))
    print(text)

def word_manipulation():
    """Asks for a word and a number, then prints the word x times"""
    word = input("Type a word: ")
    number = input("Enter a number: ")
    print(multiply_str(word, number))

def sum_and_average():
    """Continuously asks for a number until users enters "done", 
    then it prints the sum and avg of the numbers"""
    sum1 = 0
    num = 0
    each = 0
    avg = 0
    while num != "done":
        num = input("Enter a number: ")
        if num == "done":
            break
        else:
            each = each + 1
            sum1 = round(sum1 + float(num), 2)
    avg = round(sum1 / each, 2)
    text = ("The sum of all numbers are " + str(sum1) + " and the average is " + str(avg))
    print(text)

def hyphen_string():
    """Asks for a string and prints a new string where 
    every character is increased by +1 and separated by "-" """
    word = input("Enter a word: ")
    seq = 1
    step2 = ""
    for i in word:
        step1 = i * seq + "-"
        seq = seq + 1
        step2 = str(step2) + str(step1)
    text = step2[:-1]
    print(text)

def is_isogram():
    """Checks if a word is an isogram"""
    word = input("Enter a word: ")
    for i in word:
        if word.count(i) > 1:
            print("No match!")
    print("Match!")

def compare_numbers():
    """Inputs two numbers then compare the last with the previous 
    and returns with smaller, larger och same."""
    num1 = None #first number to compare
    num2 = None #second number to compare
    while num1 is None:
        input_error = True #loops until the input number is valid
        while input_error is True:
            num1 = input("Enter a number: ")
            if num1 == "done":
                break
            try:
                num1 = int(num1)
            except ValueError:
                print("That's not a valid number!")
                input_error = True
                num1 = 0
                break
            input_error = False
    while num2 != "done":
        if num1 == "done":
            break
        input_error = True
        while input_error is True:
            num2 = input("Enter another number: ")
            if num2 == "done":
                break
            try:
                num2 = int(num2)
            except ValueError:
                print("not a number!")
                input_error = True
                break
            input_error = False
        else:
            if num2 == "done":
                break
            if input_error is False:
                if num2 > num1:
                    num1 = num2
                    print("larger!")
                if num2 == num1:
                    num1 = num2
                    print("same!")
                if num2 < num1:
                    num1 = num2
                    print("smaller!")

def randomize_string(word):
    """Takes a word, randomizes it and then print it with 
    original string --> randomized string"""
    scrambled_word = word
    scrambled_word = list(scrambled_word)
    shuffle(scrambled_word)
    return word + " --> " + ''.join(scrambled_word)

def get_acronym(word):
    """Takes a string and returns the acronym of that word as a single string"""
    acronym = ""
    for i in word:
        if i.isupper():
            acronym = acronym + i
        else:
            continue
    return acronym

def multiply_str(string, integer):
    """Multiplies a string with an integer and returns the result"""
    resulting_string = string * int(integer)
    return resulting_string

def mask_string(word):
    """Takes a string a replaces all but the four last characters with "#" """
    masked_string = multiply_str("#", len(word)-4) + word[-4:]
    return masked_string

def find_all_indexes(word, part_of_word):
    """Takes two strings where the second one is compared with the first one 
    and replies with all the index positions where it is found"""
    count = 0
    indexes = ""
    while count < len(word):
        try:
            last_index = (word.index(part_of_word, count, len(word)))
            indexes = indexes + "," + str(last_index)
            count = last_index + 1
        except ValueError:
            break
    clean_index = indexes[1:]
    return clean_index
