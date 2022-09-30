#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""This module is for the random method"""
import random

"""
Marvin with a simple menu to start up with.
Marvin doesnt do anything, just presents a menu with some choices.
You should add functinoality to Marvin.
"""

marvin_image = r"""
         _____
     _-~~     ~~-_//
   /~             ~\
  |              _  |_
 |         _--~~~ )~~ )___
\|        /   ___   _-~   ~-_
\          _-~   ~-_         \
|         /         \         |
|        |           |     (O  |
 |      |             |        |
 |      |   O)        |       |
 /|      |           |       /
 / \ _--_ \         /-_   _-~)
   /~    \ ~-_   _-~   ~~~__/
  |   |\  ~-_ ~~~ _-~~---~  \
  |   | |    ~--~~  / \      ~-_
   |   \ |                      ~-_
    \   ~-|                        ~~--__ _-~~-,
     ~-_   |                             /     |
        ~~--|                                 /
          |  |                               /
          |   |              _            _-~
          |  /~~--_   __---~~          _-~
          |  \                   __--~~
          |  |~~--__     ___---~~
          |  |      ~~~~~
          |  |
"""


def printMenu():
    """
    Den här metoden printar menyn
    """
    print(chr(27) + "[2J" + chr(27) + "[;H")
    print(marvin_image)
    print("Hi, I'm Marvin. I know it all. What can I do you for?")
    print("1) Present yourself to Marvin.")
    print("2) Celsius to fahrenheit")
    print("3) Let's play parrot! You say it, ill repeat it.")
    print("4) Sure i can do you math for you!")
    print("5) Repeat letters in word?")
    print("6) Isogram")
    print("7) Is smaller, bigger or equal")
    print("8) Shuffle a word")
    print("9) Create acronym")
    print("10) Mask characters")
    print("11) Find all indexes")
    print("12) Search for country")
    print("13) Show emission change for a country")
    print("14) Show all data for a country")
    print("q) Quit.")


def menu():
    """
    This function will show the start menu, and ask the user for a choice.
    :return: The choice from the menu.
    """
    choices = "1234567891011121314q"
    while True:
        printMenu()

        choice = input("--> ")

        if choice in choices:
            return choice

        print("That is not a valid choice. You can only choose from the menu.")


def choiceIsApplicable(choice: str):
    """
    Checks if the choice is applicable
    """
    choices = "1234567891011121314"
    return choice in choices


def quit_program():
    """
    This method executes the quit command
    :return: False
    """
    print("Bye, bye - and welcome back anytime!")
    return False


def greet():
    """
    This method executes the greet command
    """
    name = input("What is your name? ")
    print("\nMarvin says:\n")
    print("Hello %s - I like you!" % name)
    print("What can I do you for?!")


def celcius_to_farenheit():
    """
    This method executes the celsius to farenheit command
    """
    goodInput = True
    while goodInput:
        try:
            celsius = float(input("What is you temperature in celsius? "))
            fahrenheit = round(celsius * 9 / 5 + 32, 2)
            print("Your temperature in fahrenheit is: " + str(fahrenheit))
            goodInput = False
        except Exception:
            print("That was not a temperature number, please try again.")
            input("\nPress enter to continue...")


def word_manipulation():
    """
    This method executes the word manipulation command
    """
    ord1 = input("Ge mig ett ord: ")
    goodInput = True
    while goodInput:
        try:
            siffra = int(input("Ge mig en integer: "))
            for _ in range(siffra):
                print(ord1, end='')
            goodInput = False
        except Exception:
            print("That was not integer, please try again.")
            input("\nPress enter to continue...")


def sum_and_average():
    """
    This method executes the sum and average command
    """
    numberOfAnswers = 0
    sumOfNumbers = 0
    while True:
        answer = input(": ")
        if answer == "done":
            break
        try:
            sumOfNumbers += float(answer)
            numberOfAnswers += 1
        except Exception:
            print("That was not number, please try again.")

    mean = sumOfNumbers / numberOfAnswers
    print("The sum of all numbers are " + str(round(sumOfNumbers, 2)) + " and the average is " +
          str(round(mean, 2)))


def hyphen_string():
    """
    This method executs the hyphen string command
    """
    word = input("Say something: ")
    string = ""
    lengthOfString = len(word)
    for i in range(lengthOfString):
        if i != 0:
            string += "-"
        for _ in range(i + 1):
            string += word[i]
    print(string)


def is_isogram():
    """
    This method executes the is isogram command
    """
    word1 = input("Word: ")
    numberOfLetters = range(len(word1))
    isNotIsogram = True
    for i in numberOfLetters:
        char = word1[i]
        for j in numberOfLetters:
            if i == j:
                continue
            if char == word1[j]:
                isNotIsogram = False
    if isNotIsogram:
        print("Match!")
    else:
        print("No match!")


def compare_numbers():
    """
    This method executes the compare numbers command
    """
    current = 0
    while True:
        answer = input(": ")
        if answer == "done":
            break
        try:
            current = float(answer)
            break
        except Exception:
            print("That was not number, please try again.")

    while True:
        answer = input(": ")
        if answer == "done":
            break
        try:
            num = float(answer)
            if num > current:
                print("larger!")
            elif num == current:
                print("same!")
            else:
                print("smaller!")
            current = num
        except Exception:
            print("not a number!")


def randomize_string(string: str):
    """
    This method executes the randomize string command
    """
    randomString = string
    listOfIndex = list(range(0, len(string)))
    for char in string:
        index = random.choice(listOfIndex)
        listOfIndex.remove(index)
        randomString = randomString[:index] + char + randomString[index + 1:]
    return string + " --> " + randomString


def get_acronym(string: str):
    """
    This method executes the get acronym command
    """
    acronym = ""
    for char in string:
        if char.isupper():
            acronym = acronym + char
    return acronym


def mask_string(string: str):
    """
    This method executes the mask string command
    """
    masked_string = multiply_str("#", len(string) - 4)
    for index in range(len(string) - 4, len(string)):
        masked_string = masked_string + string[index]
    return masked_string


def multiply_str(string: str, integer: int):
    """
    A method that was needed, to not fail validation.
    """
    return string * integer


def find_all_indexes(string: str, sub_string: str):
    """
    This method executes the find all indexes command
    """
    index = 0
    location_string = ""
    run = True
    while run:
        try:
            location = string.index(sub_string, index)
            index = location + 1
            if len(location_string) != 0:
                location_string = location_string + ","
            location_string = location_string + str(location)
        except ValueError:
            run = False
    return location_string
