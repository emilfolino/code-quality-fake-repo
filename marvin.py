
"""
A gathering of all functions for the main.py file
"""

import random


def greet():
    """
    Greets the user with an input- and a print- function
    """
    name = input("What is your name? ")
    print("\nCube says:\n")
    print("Hello %s - you none-cube." % name)
    print("Don't waste my time!")


def celcius_to_farenheit():
    """
    Converts celcius to fahrenheit with a input, math and print
    """
    print("I - Anna - know more than you. Tell me the celsius ")
    celsius = input("--> ")
    fahrenheit = (float(celsius) * (9/5) + 32)
    print("Your awnser is: {}".format(round(fahrenheit, 2)))
    print("Don't waste my time!")


def word_manipulation():
    """
    Reapets the same word x amount of times, after requesting an amount through an input
    """
    print("I - Anna - shall not repeat myself more than needed ")
    print("Tell I - Anna - your word")
    word = input("--> ")
    print("Tell I - Anna - the amount of times you need your word repeated")
    amount = input("--> ")
    word_return = multiply_str(word, amount)
    print("Your word: ")
    print(word_return)
    print("Don't waste my time!")


def sum_and_average():
    """
    Prints the average of multiple number inputs
    """
    print("I - Anna - am confused over how you can't do something so simple ")
    print("Tell I - Anna - the numbers you need the average of ")
    print("Tell I - Anna - when you are DONE")
    finnish = 0
    times = 0
    while True:
        part = ""
        part = input("--> ")
        if "done" in part:
            if finnish == 0:
                print("You are a waste of air")
                print("DO NOT WASTE MY TIME!")
                break
            else:
                result = finnish / times
                print("Your sum is {}".format(round(finnish, 2)))
                print("Your average is {}".format(round(result, 2)))
                break
        else:
            times += 1
            finnish = finnish + float(part)


def hyphen_string():
    """
    Prints a stuttering version of a sentence placed in an input
    """
    print("I - Anna - do not see the purpose of your request")
    print("I - Anna - need you to say the word you need repeated back")
    spellword = input("--> ")
    returnspellword = ""
    spellnumber = 0
    for i in spellword:
        spellnumber += 1
        if spellnumber == 1:
            returnspellword = i
        else:
            returnspellword = returnspellword + "-" + (i * spellnumber)
    print("Your word: ")
    print(returnspellword)
    print("Don't waste my time!")


def is_isogram():
    """
    Does a isogram(?)
    """
    print("I - Anna - laugh at your simple request")
    print("Tell I - Anna - your selected word")
    isogram = input("--> ")
    isolean = True
    for x in isogram:
        isonumber = 0
        for y in isogram:
            if x == y:
                isonumber += 1
                if isonumber >= 2:
                    isolean = False
    print("Your word:")
    if not isolean:
        print("No match!")
    if isolean:
        print("Match!")
    print("Don't waste my time!")


def compare_numbers():
    """
    Compares numbers and returns the two last inputed numbers
    """
    print("At this point, you are either 12, a robot or dumb as fuck")
    print("But I - Anna - will teach you the bascis of numbers")
    print("Enter two numbers")
    numone = input("--> ")
    numcount = 1
    while True:
        if (numcount % 2) == 1:
            try:
                numtwo = input("--> ")
                if numtwo == "done":
                    break
                elif float(numone) == float(numtwo):
                    print("same!")
                    numcount += 1
                elif float(numtwo) < float(numone):
                    print("smaller!")
                    numcount += 1
                elif float(numtwo) > float(numone):
                    print("larger!")
                    numcount += 1
            except ValueError:
                print("not a number!")
        elif (numcount % 2) == 0:
            try:
                numone = input("--> ")
                if numone == "done":
                    break
                elif float(numone) == float(numtwo):
                    print("same!")
                    numcount += 1
                elif float(numone) > float(numtwo):
                    print("larger!")
                    numcount += 1
                elif float(numone) < float(numtwo):
                    print("smaller!")
                    numcount += 1
            except ValueError:
                print("not a number!")


"""
Every function following this section is NOT featured in the marvin1 exercise.
"""


def randomize_string(input_a):
    """
    Randomizes the characters in a sentence, that is placed as an input
    """
    new_word = ""
    old_word = input_a
    i_length = len(input_a)
    current_num = 0
    while current_num < i_length:
        current_num += 1
        random_num = random.randrange(len(input_a))
        new_word = new_word + input_a[random_num]
        input_a = input_a[0: random_num:] + \
            input_a[random_num + 1: len(input_a):]
    return f"{old_word} --> {new_word}"


def get_acronym(input_b):
    """
    Creats acronyms from big letters
    """
    acronym = ""
    for i in input_b:
        if i.isupper():
            acronym = acronym + i
    return acronym


def mask_string(input_c):
    """
    Will replace all but the last 4 characters in a string, with: #
    """
    till = len(input_c) - 4
    number = 0
    masked = ""
    masked = multiply_str("#", till)
    for i in input_c:
        if number >= till:
            masked = masked + i
        number += 1
    return masked


def multiply_str(input_str, input_num):
    """
    Multiplies an input depending on input
    """
    output = input_str * input_num
    return output


def find_all_indexes(input_d, input_e):
    """
    Finds the indexes of all instances of input_e in input_d
    """
    number = 0
    ondex_output = ""
    while number < len(input_d):
        try:
            ondex = input_d.index(input_e, number, len(input_d))
            if ondex_output == "":
                ondex_output = ondex
            else:
                ondex_output = str(ondex_output) + "," + str(ondex)
            number = ondex + 1
        except ValueError:
            break
    return ondex_output
