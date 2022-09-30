#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
functions for marvin choices
"""
import random

def greet():
    """
    functions for marvin choices
    """
    name = input("What is your name? ")
    print("\nAzan says:\n")
    print("Hello %s - your awesomeness!" % name)
    print("What can i do for you?")


def celcius_to_farenheit():
    """
    functions for marvin choices
    """
    temp = (float(input("Input current temperature i Celsius and I'll convert it in Fahrenheit for you: ")))
    temp_2 = float(round(temp * 9 / 5 + 32, 2))
    print("\nAzan says:\n")
    print("On my planet that means it is %s in Fahrenheit" % temp_2)
    print("Wanna see what else I can do?!")

def multiply_str(_string, _int):
    """
    functions for marvin choices
    """
    word = _string
    num_1 = int(_int)
    new_word = ""

    for _ in range(num_1):
        try:
            new_word += word
        except ValueError:
            print("Not a number!")
        continue
    return new_word

def word_manipulation():
    """
    functions for marvin choices
    """
    _string = input("Enter a word: ")
    _int = int(input("Enter a number: "))
    print(multiply_str(_string, _int))


def sum_and_average():
    """
    functions for marvin choices
    """
    numbers = float(0)
    total = float(0)
    counter = float(0)

    while True:
        numbers = str(input("Enter a number, print done to quit: "))
        if numbers == "done":
            break

        try:
            if numbers != 'done':
                counter += 1
                total += float(numbers)
                Average = float(round(total / counter, 2))
        except ValueError:
            print("not a number!")
            continue

    print("\nAzan says:\n")
    print("The sum of all numbers are %s and the average is %s" %(total, Average))
    print("Wanna see what else I can do?!")


def hyphen_string():
    """
    functions for marvin choices
    """ 
    word = input("Enter a word and you'll see some magic: ")
    new_word = ""
    counter = 0
    for letter in word:
        counter += 1
        if counter <= 1:
            new_word += letter * counter
        else:
            new_word += "-" + letter * counter
        print(new_word)

    print("\nAzan says:\n")
    print("Hahahah didn't see that coming didn't you?")
    print("Wanna see what else I can do?!")


def is_isogram():
    """
    functions for marvin choices
    """
    string = input("Enter a word and I'll check if it's an isogram or not: ")

    for letter in string:
        string.count(letter)
        if string.count(letter) > 1:
            print("No match!")
            print("\nAzan says:\n")
            print("That was not an isogram!")
            break
    else:
        print("Match!") 
        print("\nAzan says:\n")
        print("You found an isogram")

def compare_numbers():
    """
    functions for marvin choices
    """
    while True:
        try:
            new_num = int(input("Enter a number: "))
            break
        except ValueError:
            print("not a number!")
            continue
    while True:
        try:
            num1 = input("Enter another number to compare, print done to quit: ")
            if num1 == "done":
                break

            counter = 0 + int(num1)	
            if int(num1) > new_num:
                print("larger!")
            elif int(num1) == new_num:
                print("same!")
            else:
                print("smaller!")
            new_num = counter

        except ValueError:
            print("not a number!")
            continue

def randomize_string(string1):
    """
    functions for marvin choices
    """
    random_string = ''.join(random.sample(string1, len(string1)))
    string = ("'{string} --> {random}'").format(
        string = string1,
        random = random_string
        )
    return string


def get_acronym(string):
    """
    functions for marvin choices
    """
    new_word = ""
    for letter in string:
        if letter.isupper():
            letter = new_word + letter
            new_word = letter
    return(new_word)

def mask_string(string):
    """
    functions for marvin choices
    """
    lenght = len(string) - 4
    num_of_mask = multiply_str("#", lenght)
    i = []
    result = ""
    for char in string:
        i.append(char)
    i[0:-4] = num_of_mask
    for letter in i:
        result += letter
    return result

def find_all_indexes(string, letter):
    """
    functions for marvin choices
    """
    counter1 = 0
    counter2 = 0
    i = ""
    try: 
        while counter2 < len(string) - 1:
            counter1 = string.index(letter, counter2, len(string))
            i += str(counter1) + ","
            counter2 = counter1 + len(letter)
    except ValueError:
        print("")
    i = i[:len(i) - 1]
    return i
