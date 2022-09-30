#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""This program holds functions for main.py"""


import random
import re

def greet():
    """this function greets the user"""
    print("Batbot says:\n")
    name = input("What is your name?: ")
    print("Hello %s - you are just as scary as I am!" % name)
    print("Anything else I can do for you?")

def celcius_to_farenheit():
    """this functions convert celcius to farenheit"""
    print("I will now convert celcius to farenheit. ")
    celcius = (float(input("What is the temperature in Celcius? ")))
    farenheit = celcius * 9 / 5 + 32
    farenheit = round(farenheit, 2)
    print(str(farenheit))

def word_manipulation():
    """this function manipulates the word"""
    word = str(input("Type your word. "))
    print("Excellent choice. ")
    numb = (int(input("Type how many times I shall sing it for you. ")))
    svar = multiply_str(word, numb)
    print(svar)

def sum_and_average():
    """this function sum and average the ints"""
    print("Type the numbers you want the sum and average of. type done to get result")
    sum4 = 0
    medel = 0
    i = 0
    numb = input("What number? ")
    while numb != "done":
        i = i + 1
        sum4 += float(numb)
        numb = (input("What number? "))
    medel = sum4 / i
    print("The sum of all numbers are " + str(round(sum4, 2)) + " and the average is " + str(round(medel, 2)))

def hyphen_string():
    """this is a hyphening function"""
    word = input("Type your word for adding letters ")
    ord5 = ""
    num = 0

    for i in word:
        num = num + 1
        ord5 = ord5 + "-"

        for _ in range(num):
            ord5 = ord5 + i

    print("your word with more letters: " + ord5[1:])

def is_isogram():
    """this function checks if it the word is a isogram"""
    word = input("Type your word here to check if it is a isogram ")

    for i in word:
        word = word[1:]
        if i in word:
            svar = "No match!"
            break
        else:
            svar = "Match!"

    print(svar)

def compare_numbers():
    """this function compare numbers"""
    print("Type two numbers, when you are finished type done to end program.")
    num1 = ""

    while True:
        try:
            if num1 == "done":
                break
            num1 = input("Type a number: ")
            if num1 == "done":
                break
            num1 = int(num1)

            while True:
                try:
                    num2 = input("Type a number: ")
                    if num2 == "done":
                        num1 = num2
                        break
                    num2 = int(num2)

                    if num1 < num2:
                        print("larger!")
                    if num1 == num2:
                        print("same!")
                    if num1 > num2:
                        print("smaller!")

                    num1 = num2

                except ValueError:
                    print("not a number!")

        except ValueError:
            print("not a number!")

def randomize_string(string):
    """this function randomize the string"""
    string1 = ""
    string2 = ""
    string3 = ""
    for i in string:
        if i not in "1234567890":
            string2 += i
    string2 = list(string2)
    random.shuffle(string2)
    string2 = "".join(string2)
    for i in string:
        if i in "0123456789":
            string1 += i
    string3 = string2 + string1

    string = string + " --> " + string3

    return string


def get_acronym(string):
    """this function gets a acronym for the user"""
    sum10 = ""
    for i in string:
        if i.isupper():
            sum10 += i
    return sum10

def mask_string(string):
    """this function masks the string"""
    counter = 0
    for _ in string:
        counter = counter + 1
    counter = counter - 4

    string = multiply_str("#", counter) + string[(counter):]
    return string


def multiply_str(string, counter):
    """this function multiplies the string"""
    sum11 = ""
    for _ in range(counter):
        sum11 += string
    return sum11


def find_all_indexes(string1, string2):
    """this function finds all the indexes"""
    counter = 0
    counter2 = 0
    sum12 = ""
    tot = ""

    for _ in string1:
        counter2 = counter2 + 1

    try:
        for _ in string1:
            if counter < counter2:
                sum12 = (string1[counter:].index(string2),counter)
                if sum12 == (0, counter):
                    tot += str(sum12[1:])
                counter = counter + 1

    except ValueError:
        ""
    tot = re.sub(r"[\([{})\]]", "", tot)

    counter = 0
    for _ in tot:
        counter = counter + 1
    counter = counter - 1
    tot = tot[:counter]

    return tot
