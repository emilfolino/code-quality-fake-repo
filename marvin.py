#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" Methods for marvin the chat bot """
from random import sample


def asci_image():
    """Creating introduction asci-image dilbert"""
    dilbert_image = r"""
                        (`'`'`'`'`)
                         |       |
                         |       |
                         |       |
        -----..        (()----   |
       |        ||     (_        |
       |        ||       |       |
       |        ||       |       |
       |        ||       /\   ..--
       '--------''   /\  ||-''    \
          /   \      \ \//   ,,   \---.
       .---------.    \./ |~| /__\  \  |
    ___|_________|__|""-.___ / ||   |  |
    |               | .-----'  ||   |  |
    |               |CC.-----.      |  |
    |               |  '-----'      |  |
                                    |  |

    """
    return dilbert_image

def menu_choice():
    """Printing menu method"""
    print(chr(27) + "[2J" + chr(27) + "[;H")
    print(asci_image())
    print("Dilbert: \"okay finished creating a chat-bot in programming " + \
    "introduction course,\n I'm sure it is going to outsmart Siri in no time\"")
    print("\n--Dilbert runs chat-bot--\n")
    print("Hi, I'm Iris, what can I do for you?:")
    print("1) Introduce yourself")
    print("2) Convert Celsius to Fahrenheit")
    print("3) Do word multiplification")
    print("4) Sum and mean calculator")
    print("5) Word prolongation")
    print("6) Check if word is an isogram")
    print("7) Play the larger, smaller and same game")
    print("8) Randomize string")
    print("9) Get acronym")
    print("10) Mask string")
    print("11) Find index of search item")
    print("12) Search for country in emission data")
    print("13) Show emission change for a country")
    print("14) Show all data for a country")
    print("q) Quit.")
    print("")
    print("")
    print("")

    print("Try out my \"inv\" commands!")
    print("--------------------------")

    choiceInput = input("--> ")
    return choiceInput

def choice_q():
    """Quit method"""
    print("Bye, bye - and welcome back anytime!")

def greet():
    """Introduce yourself method"""
    name = input("What is your name? ")
    print("\n Iris says:\n")
    print("Hello %s - your awesomeness!" % name)
    print("What can I do you for?!")

def celcius_to_farenheit():
    """Convert celcius to fahrenheit method"""
    print("\n Iris says:")
    print("I can help you convert Celcius to Fahrenheit, " +
          "just input temperature value in Celcius:")
    temperatureCelcius = input("Celcius value: ")

    try:
        float(temperatureCelcius)
    except ValueError:
        print("\n That's not a number!")
    else:
        temperatureFahrenheit = round(float(temperatureCelcius) * 9/5 + 32, 2)
        print("\n {tempC} [°C] is equal to {tempF} [°F]".\
        format(tempC=temperatureCelcius, tempF=temperatureFahrenheit))

def word_manipulation():
    """Word multiplification method"""
    print("\nI can help you with word multiplification." +
          " Not sure what it is good for \nbut hey why don't you try it." +
          " Type a word and how many times you want it multiplied:\n")
    inputWord = input("Word: ")
    inputTimes = input("Number of multiplifications: ")

    try:
        int(inputTimes)
    except ValueError:
        print("\nYou decide what is a word, but 'Number of multiplifications' is not an integer number!")
    else:
        wordXTimes = multiply_str(inputWord, int(inputTimes))

        print("\n This is {word} {number} times\n\n {xword}".\
        format(word=inputWord, number=inputTimes, xword=wordXTimes))

def sum_and_average():
    """Sum and mean method"""
    print("\nTry my sum and mean calculator: \n")

    inputNumber = 0
    count = 0
    vec = []
    while inputNumber != "done":
        count += 1
        inputNumber = input("Number {count}: ".format(count=count))

        if inputNumber != "done":
            try:
                float(inputNumber)
            except ValueError:
                print("\nInput is not a number or done!\n")
            else:
                vec.append(float(inputNumber))

    vec_sum = sum(vec)
    vec_mean = round(vec_sum/len(vec), 2)
    vec_sum = round(sum(vec), 2)

    print("The sum of all numbers is {sum} and the average is {mean}".\
    format(sum=vec_sum, mean=vec_mean))

def hyphen_string():
    """Letter dasher method"""
    print("\nWelcome to the letter dasher\n")

    word = input("Please input a word: ")
    count = 1
    new_word = ""
    for i in word:
        new_word = new_word + (i*count) + "-"
        count += 1

    print(new_word[:-1])

def is_isogram():
    """Isogram tester method"""
    print("\nIs it an isogram tester: \n")

    word = input("Input word: ")
    count = 0
    a = "Match!"
    for i in word[:-1]:

        count += 1
        try:
            1/(True - bool(i in word[count:]))
        except ZeroDivisionError:
            a = "No match!"

    print(a)

def compare_numbers():
    """Smaller, same, larger method"""
    print("\nWelcome to smaller, same or larger \n")

    inputNumber1 = input("Input number: ")

    while inputNumber1 != "done":
        inputNumber2 = input("Input Number: ")

        if inputNumber1 != "done" and inputNumber2 != "done":
            try:
                float(inputNumber1) + float(inputNumber2)
            except ValueError:
                print("not a number!")
                inputNumber2 = inputNumber1
            else:
                compare = float(inputNumber1) - float(inputNumber2)

                if compare > 0:
                    print("smaller!")
                elif compare == 0:
                    print("same!")
                else:
                    print("larger!")

        inputNumber1 = inputNumber2

def randomize_string(inputString):
    """randomize string method"""
    totalLength = len(inputString)
    listcharacters = range(0, totalLength)

    randomIndex = listcharacters
    while list(randomIndex) == list(listcharacters):
        randomIndex = sample(listcharacters, totalLength)

    randomString = ""
    for i in randomIndex:
        randomString = randomString + inputString[i]

    return (inputString + " --> " + randomString)

def get_acronym(inputString):
    """acronym string method"""

    acronym = ""
    for i in inputString:

        if i.isupper():
            acronym = acronym + i

    if acronym == "":
        acronym = "No upper case letters exists in input string"

    return acronym

def mask_string(inputString):
    """mask string method"""
    numberOfMasked = len(inputString)-4

    remainingString = ""
    for index, value in enumerate(inputString):
        if index > numberOfMasked - 1:
            remainingString = remainingString + value

    replacementChar = "#"

    return (multiply_str(replacementChar, numberOfMasked) + remainingString)

def multiply_str(stringName, numberOfTimes):
    """multiply string input"""
    multipliedString = stringName * numberOfTimes
    return multipliedString

def find_all_indexes(inputString1, inputString2):
    """find all indexes of input"""
    foundIndex = 0
    nextIndex = 0
    foundIndexString = ""

    count = 0
    while count < len(inputString1):
        count += 1

        try:
            inputString1.index(inputString2, nextIndex, len(inputString1))
        except ValueError:
            print("Done searching")
            break
        else:
            foundIndex = inputString1.index(inputString2, nextIndex, len(inputString1))
            nextIndex = foundIndex + len(inputString2)
            foundIndexString = foundIndexString + str(foundIndex) + ","

    return foundIndexString[:-1]

def not_valid():
    """Not valid statement"""
    print("That is not a valid choice. You can only choose from the menu.")

def continue_func():
    """Continue method"""
    input("\nPress enter to continue...")
