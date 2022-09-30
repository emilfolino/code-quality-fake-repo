#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Functions for marvin
"""
import random


def marvin_image():
    """returns ascii marvin"""
    return r"""
               _..-- `.`.   `.  `.  `.      --.._
              /    ___________\   \   \______    \
              |   |.-----------`.  `.  `.---.|   |
              |`. |'  \`.        \   \   \  '|   |
              |`. |'   \ `-._     `.  `.  `.'|   |
             /|   |'    `-._o)\  /(o\   \   \|   |\
           .' |   |'  `.     .'  '.  `.  `.  `.  | `.
          /  .|   |'    `.  (_.==._)   \   \   \ |.  \         _.--.
        .' .' |   |'      _.-======-._  `.  `.  `. `. `.    _.-_.-'\\
       /  /   |   |'    .'   |_||_|   `.  \   \   \  \  \ .'_.'     ||
      / .'    |`. |'   /_.-'========`-._\  `.  `-._`._`. \(.__      :|
     ( '      |`. |'.______________________.'\      _.) ` )`-._`-._/ /
      \\      |   '.------------------------.'`-._-'    //     `-._.'
      _\\_    \    | AMIGA  O O O O * * `.`.|    '     //
     (_  _)    '-._|________________________|_.-'|   _//_

"""
def read_float(toPrint = ""):
    """Reads and trycatches from commandline input(float)"""
    toReturn = None
    while(toReturn is None):
        try:
            toReturn = float(input(toPrint))
        except ValueError:
            print("Invalid input")
    return toReturn
def read_integer(toPrint = ""):
    """Reads and trycatches from commandline input(float)"""
    toReturn = None
    while(toReturn is None):
        try:
            toReturn = int(input(toPrint))
        except ValueError:
            print("Invalid input")

    return toReturn
def read_not_empty_string(toPrint =""):
    """Reads a string from the terminal. Forces user to not enter nothing"""
    cmdInput = ""
    while(cmdInput == ""):
        cmdInput = input(toPrint)
        if(cmdInput == ""):
            print("Not valid")

    return cmdInput

def c_to_f(celsius = 0.0):
    """Converts and returns fahrenheit from celsius(float)"""
    return (celsius * 1.8) + 32


def greet():
    """Menu for greeting the user"""
    name = input("What is your name? ")
    print("\nMarvin says:\n")
    print("Hello %s !" % name)
    print("How can i help you?")

def celcius_to_farenheit():
    """A menu for converting celsius to fahrenheit(void)"""
    celsius = read_float("Enter celsius: ")
    fahrenheit = c_to_f(celsius)
    print("Fahrenheit:", round(fahrenheit, 2))

def multiply_str(string_to_multiply, nr_of_times):
    """Multiplies strings.."""
    return string_to_multiply * nr_of_times

def word_manipulation():
    """A menu for multiplying word"""
    wordToMultiply = input("Enter string to multiply: ")
    multiplier = read_integer("Enter times to multiply: ")
    print(multiply_str(wordToMultiply, multiplier))

def hyphen_string():
    """Extends the number of letter based on their index"""
    cmdInput = input("Enter word to weirdly extend:")
    extendedString = ""
    for i, value in enumerate(cmdInput):
        for _ in range(i + 1):
            extendedString += value
        if i + 1 < len(cmdInput):
            extendedString += "-"
    print(extendedString)

def sum_and_average():
    """Sums and averages a list of floats"""
    toPrint = "Enter a number or type done:"
    cmdInput = input(toPrint)
    cmdInput = cmdInput.lower()
    numberList = []
    while(cmdInput != "done"):
        try:
            cmdInput = float(cmdInput)
            numberList.append(cmdInput)
        except ValueError:
            print("Invalid input")
        cmdInput = input(toPrint)

    if len(numberList) > 0:
        sumOfInputs = 0.0
        for i in numberList:
            sumOfInputs += i
        average = sumOfInputs / float(len(numberList))
        print("Average: ", round(average, 2), "Sum: ", round(sumOfInputs, 2))
    else:
        print("No inputs to calculate")

def isIsogram(wordToCheck = ""):
    """Checks if a word is an isogram"""

    wordToCheck = wordToCheck.lower()
    checkedLetters = []
    isDuplicate = False
    for letter in wordToCheck:
        for cLetter in checkedLetters:
            if letter == cLetter:
                isDuplicate = True
        if not isDuplicate:
            checkedLetters.append(letter)
    return not isDuplicate

def is_isogram():
    """Menu for checking if a word is an isogram"""
    wordToCheck = read_not_empty_string("Enter word to check if its an isogram: ")
    if isIsogram(wordToCheck):
        print("Match!")
    else:
        print("No match!")

def compare_numbers():
    """Checks if last number vs the new input"""
    current = 0.0
    previous = 0.0
    cmdInput = ""
    valid = False
    done = False

    while not valid:
        try:
            cmdInput = input("Enter number(or done): ")
            previous = float(cmdInput)
            valid = True
        except ValueError:
            print("Not valid")

    while not done:
        try:
            cmdInput = input("Enter number(or done): ")
            current = float(cmdInput)
            valid = True
        except ValueError:
            if cmdInput.lower() == "done":
                done = True
                valid = False
            else:
                print("not a number!")
                valid = False
        if not done and valid:
            if current > previous:
                print("larger!")
            elif current < previous:
                print("smaller!")
            else:
                print("same!")
        previous = current

def string_compare_menu():
    """Menu for checking if a string has the letters of another"""
    firstString = input("Enter the first string: ").lower()
    secondString = input("Enter the second string: ").lower()
    containingLetters = 0
    for i in secondString:
        for j in firstString:
            if j == i:
                containingLetters += 1
                break
    if len(secondString) == containingLetters:
        print("Match!")
    else:
        print("No match!")

def all_numbers_menu():
    """Checks if all numbers are in a thing"""
    nrToMultiply = read_integer("Enter number to multiply: ")
    nrOfTimes = read_integer("Enter nr of times to try: ")
    allNumbersExist = False
    counter = 0
    while(not allNumbersExist and counter < nrOfTimes):
        firstString = str(nrToMultiply)
        secondString = "0123456789"
        containingLetters = 0
        for i in secondString:
            for j in firstString:
                if j == i:
                    containingLetters += 1
                    break
        if len(secondString) == containingLetters:
            allNumbersExist = True
        else:
            counter += 1
            nrToMultiply *= 2
    if not allNumbersExist:
        counter = -1
    print("Answer:", counter, "times")
    print(nrToMultiply)

def tab_shortener_menu():
    """Menu for replacing tabs with 3 spaces"""
    textToShorten = input("Enter text with tabs in it: ")
    textToShorten = textToShorten.replace("\t", "   ")
    print(textToShorten)

def word_combiner_menu():
    """Combines 2 words into one"""
    firstName = input("Enter the first name: ").lower()
    secondName = input("Enter the second name: ").lower()
    VOWELS = "aeiouy"
    for i, val in enumerate(firstName):
        print(val)
        if val in VOWELS:
            firstName = firstName[:i]
            break
    for i, val in enumerate(secondName):
        print(val)
        if val in VOWELS:
            secondName = secondName[i:]
            break
    combinedName = firstName + secondName
    print(combinedName)

def point_calculator_menu():
    """A menu for calculating points from string"""
    playerNames = []
    playerPoints = []
    infoString = input("Input the string: ")
    printString = ""
    for i, val in enumerate(infoString):
        if not val.isdigit():
            if val.lower() in playerNames:
                if val.isupper():
                    playerPoints[playerNames.index(val.lower())] -= int(infoString[i + 1])
                else:
                    playerPoints[playerNames.index(val.lower())] += int(infoString[i + 1])
            else:
                playerNames.append(val.lower())
                playerPoints.append(0)
                if val.isupper():
                    playerPoints[playerNames.index(val.lower())] -= int(infoString[i + 1])
                else:
                    playerPoints[playerNames.index(val.lower())] += int(infoString[i + 1])
    for i, val in enumerate(playerNames):
        if(i < len(playerNames) - 1):
            printString += val + " " + str(playerPoints[i]) + ", "
        else:
            printString += val + " " + str(playerPoints[i])
    print(printString)

def randomize_string(string_to_randomize):
    """Returns randomized string"""
    randomized_string = "".join(random.sample(string_to_randomize, len(string_to_randomize)))
    return f"{string_to_randomize} --> {randomized_string}"

def get_acronym(to_acronymize):
    """Returns the uppercase letters"""
    acronym = ""
    for i in to_acronymize:
        if i.isupper():
            acronym += i
    return acronym

def string_to_char_list(string_to_convert):
    """Converts string to list of chars"""
    list_of_chars = []
    for i in string_to_convert:
        list_of_chars.append(i)
    return list_of_chars

def mask_string(to_mask):
    """Returns a masked string of all but the four last characters"""
    amount = len(to_mask) - 4
    last_four = to_mask[len(to_mask) - 4:len(to_mask)]
    return multiply_str("#", amount) + last_four

def find_all_indexes(string_to_search, key):
    """Finds and returns list of all indexes"""
    i = 0
    list_of_indexes = []
    while i < len(string_to_search):
        try:
            i = string_to_search.index(key, i)
            list_of_indexes.append(i)
            i += 1
        except ValueError:
            i = len(string_to_search)#Nothing found in substring.
    return str(list_of_indexes).replace("[", "").replace("]", "").replace(" ", "")#yes


def points_to_grade(maxpoints, points):
    """Returns grade from F-A"""
    percentage = float(points) / float(maxpoints)
    grade = "F"
    if percentage >= 0.9:
        grade = "A"
    elif percentage >= 0.8:
        grade = "B"
    elif percentage >= 0.7:
        grade = "C"
    elif percentage >= 0.6:
        grade = "D"
    return "score: " + grade

def has_strings(full_string, start_string, contains_string, end_string):
    """Checks how first string compares"""
    all_true = True
    if not full_string.startswith(start_string):
        all_true = False
    elif not contains_string in full_string:
        all_true = False
    elif not full_string.endswith(end_string):
        all_true = False
    if all_true:
        return "Match"
    return "No match"
