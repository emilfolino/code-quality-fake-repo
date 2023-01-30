#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
The functions defined for the program Marvin main.py
"""
import random

def almost(arg, start, stop):
    """
    Returning a value that is almost the same as the input
    """
    rand = random.randint(start, stop)
    return (arg + rand)

def isnumber(arg):
    """
    Checking if input is a number
    """
    try:
        float(arg)
        return True
    except Exception:
        return False

def multiply_str(string, integer):
    """
    Returns a given string multiplied with the given integer.
    """
    return string * integer

def greet():
    """
    Demon Cat almost knows your name and greets you.
    """
    print("\nDemon Cat says:\n")
    name = input("What is your name? ")
    almost_name = ""
    vowels = "aeiou"
    for i in name:
        new_i = i
        if new_i in vowels:
            while True:
                index = random.randint(0, 4)
                if new_i == vowels[index]:
                    continue
                new_i = vowels[index]
                break
        almost_name += new_i
    print("No, wait don't tell me! \nI already know your name. It's %s.\n Impressive isn't it?" %almost_name)
    print("...or was it %s... ah whatever!" %name)
    print("So %s, what aproximate knowledge do you seek?" %almost_name)
    #input("\nPress enter to continue...")

def celcius_to_farenheit():
    """
    Demon Cat converts Celsious to Farenheit, at the best of his knowledge...
    """
    print("\nDemon Cat says:\n")
    print("One of many things I almost know is how to convert Celsius to Farenheit.\n"
          "Try me, how many degrees C do you want me to convert? \n")
    while True:
        celsius = input("")
        try:
            celsius = float(celsius)
            break
        except Exception:
            print("I'm quite sure that's not a number. Right? \nGive it another shot: \n")

    farenheit = round((celsius) * 9 / 5 + 32, 2)
    print("That is {f_degrees} Farenheit! \n".format(f_degrees=almost(farenheit, -5, 5)))
    print(("Or I mean {f_degrees}! No wait... maybe closer to {f_degrees2}?"
           .format(f_degrees=almost(farenheit, -5, 5)
                   , f_degrees2=almost(farenheit, -5, 5))))
    print("No, I know now. It is definately {farenheit}... Give or take.".format(farenheit=round(farenheit, 2)))
    #input("\nPress enter to continue...")

def word_manipulation():
    """
    Demon Cat asks you for a word and repeats it how many times you want.
    """
    print("\nDemon Cat says:\n")
    word = input("Give me a word:\n")
    while True:
        times = input("Now give me an integer:\n")
        if isinstance(times, int):
            break
        else:
            print("That's not an integer")

    print(multiply_str(word, times))
    #input("\nPress enter to continue...")

def sum_and_average():
    """
    Demon Cat asks you for a bunch of numbers and gives you the sum and average.
    """
    print("\nDemon Cat says:\n")
    total = 0
    count = 0
    while True:
        number = input("Give me a number:\n")
        if number.casefold() == "done":
            break
        if not isnumber(number):
            print("that's not a number...")
            continue
        total += float(number)
        count += 1
    average = total/count
    print(("The sum of all numbers are {total} and the average is {average}"
           .format(total=total, average=round(average, 2))))
    #input("\nPress enter to continue...")

def hyphen_string():
    """
    Demon Cat asks you for a string and says it back to you with an
    increasing amount of letters.
    """
    print("\nDemon Cat says:\n")
    word = input("Tell me a word: \n")
    demon_word = ""
    index = 1
    for i in word:
        demon_word += i * index
        index += 1
        demon_word += "-"
    print("Did you mean: {demon_word}".format(demon_word=demon_word))
    #input("\nPress enter to continue...")

def is_isogram():
    """
    Demon cats tell you if the string given is an isogram.
    That means no one letter twice.
    """
    print("\nDemon Cat says:\n")
    word = input("Tell me a word: \n")
    letters = ""
    var = False
    for i in word:
        if i in letters:
            var = True
        letters += i
    if var:
        print("No match!")
    else:
        print("Match!")
    #input("\nPress enter to continue...")

def compare_numbers():
    """
    Demon Cats tells you if a number is bigger or smaller than the
    preceding number.
    """

    # Jag valde att inte ändra här då jag misstänker att en detalj blev missad.
    # Funktionen isnumber() är en funktion jag skrev själv och den är definierad högst upp.
    # I den så använder jag mig av tr/except för att kolla input och
    # jag återanvänder den vid alla numeric inputs i uppgiften.
    # Om det inte uppfyller kraven i uppgiften så ändrar jag gladeligen till try/catch direkt härunder.

    print("\nDemon Cat says:\n")
    number1 = None
    while True:
        number1 = input("Give me a number:\n")
        if number1.casefold() == "done":
            break
        if not isnumber(number1):

            # Förklaring ovan!

            print("that's not a number...")
            continue
        break
    while True:
        number2 = input("Give me another number:\n")
        if number2.casefold() == "done":
            break
        if not isnumber(number2):
            print("not a number!")
            continue
        number1 = float(number1)
        number2 = float(number2)
        if number2 > number1:
            print("larger!")
        elif number2 < number1:
            print("smaller!")
        else:
            print("same!")
        number1 = number2
    #input("\nPress enter to continue...")

def randomize_string(old_string):
    """
    Demon Cat asks for a string that he randomizes and says back to you.
    """

    text = old_string
    only_letters = ""
    for i in text:
        if i.isalpha():
            only_letters += i
    temp_text = list(only_letters)
    new_text = ""
    length = len(only_letters)

    for i in text:
        if not i.isalpha():
            new_text += i
        else:
            rand = random.randint(0, length-1)
            new_text += temp_text[rand]
            temp_text.remove(temp_text[rand])
            length -= 1
    return old_string + " --> " + new_text

def get_acronym(old_string):
    """
    Returns an acronym made up from the upper case letters in the word
    """
    new_string = ""
    for i in old_string:
        if i.isupper():
            new_string += i
    return new_string

def mask_string(old_string):
    """
    Masks all characters except the last four ones
    """
    new_string = ""
    length = len(old_string)
    new_string = multiply_str("#", length - 4)
    new_string += old_string[-4:]
    return new_string

def find_all_indexes(string1, string2):
    """
    Finds allt he indexes of a substring in a string.
    """

    new_string = ""
    while True:
        try:
            if new_string == "":
                temp_index = string1.index(string2)
                new_string = str(temp_index)
            else:
                temp_index = string1.index(string2, temp_index +1)
                new_string += "," + str(temp_index)
        except ValueError:
            return new_string

def letters_in_word():
    """
    Demon Cat asks you for two strings and tells you if the letters
    in the second string are all in the first.
    """
    print("\nDemon Cat says:\n")
    word = input("Tell me a word: \n")
    word2 = input("And a bunch of letters I'll match with the first word: \n")
    var = True
    for i in word2:
        if i.casefold() not in word.casefold():
            var = False
            break
    if var:
        print("Match!")
    else:
        print("No match!")
    input("\nPress enter to continue...")

def multiply_to_find():
    """
    Demon Cat asks you for two numbers. One that is to be multiplied with 2
    and one which is the uppe limit of how many times that is to be done
    trying to achieve a number that contains all ten digits 0-9.
    """
    print("\nDemon Cat says:\n")
    all_digits = "0123456789"
    number1 = None
    number2 = None
    while True:
        number1 = input("Give me an integer: \n")
        if not isnumber(number1):
            print("that's not a number...")
            continue
        number1 = int(number1)
        break
    while True:
        number2 = input("How many times should I try to multiply that number?: \n")
        if not isnumber(number2):
            print("that's not a number...")
            continue
        number2 = int(number2)
        break
    var = True
    count = 0
    for _ in range(0, number2):
        for n in str(all_digits):
            if n not in str(number1):
                var = False
                break
            var = True
        if var:
            break
        number1 *= 2
        count += 1
    if not var:
        count = "-1"
        print("Answer: -1 times")
    else:
        print(("Answer: {count} times and you'll have {number1}"
               .format(count=count, number1=number1)))
    input("\nPress enter to continue...")

def tab_is_space():
    """
    Demon Cat asks you for a string with tabs and returns it with those
    tabs changed into 4 spaces.
    One of Demon Cats many very impressive skills.
    """
    print("\nDemon Cat says:\n")
    word = input("Tell me a word: \n")
    new_word = ""
    for i in word:
        if i == "\t":
            i = "   "
        new_word += i
    print(new_word)
    input("\nPress enter to continue...")

def brangelina():
    """
    Demon Cat asks you for two names and concatinatesthem,
    Brangelina style!
    """
    print("\nDemon Cat says:\n")
    name1 = input("Tell me a name: \n")
    name2 = input("Tell me another name: \n")
    new_name1 = ""
    new_name2 = ""
    vowels = "aeiouy"
    var = False
    for i in name1:
        if i in vowels:
            break
        new_name1 += i
    for i in name2:
        if i in vowels:
            var = True
        if var:
            new_name2 += i
    print(new_name1 + new_name2)
    input("\nPress enter to continue...")

def points():
    """
    Demon Cat tells you how many points each player has from a complicated
    string system with upper and lower case letters and points.
    """
    score = input("tell me the scores")
    players = {}
    for i in range(0, len(score), 2):
        if score[i].casefold() not in players:
            players[score[i].casefold()] = int(0)
        if score[i].isupper():
            players[score[i].casefold()] -= int(score[i + 1])
        else:
            players[score[i].casefold()] += int(score[i + 1])

    values = list(players.values())
    keys = list(players.keys())

    formated = ""
    for i in range(len(players)):
        formated += str(keys[i]) + " " + str(values[i]) + ", "
    print(formated)
    input("\nPress enter to continue...")

def points_to_grade(max_points, own_points):
    """
    2 inputs, first is max score, second one is graded on the first one.
    """
    max_points = int(max_points)
    own_points = int(own_points)
    if own_points >= max_points * 0.9:
        return "score: A"
    if own_points >= max_points * 0.8:
        return "score: B"
    if own_points >= max_points * 0.7:
        return "score: C"
    if own_points >= max_points * 0.6:
        return "score: D"

    return "score: F"

def has_strings(string1, string2, string3, string4):
    """
    Checks if string1 starts with string2, contains string3
    and ends with string4.
    """
    starts_with = string1.startswith(string2)
    contains = (string3 in string1)
    ends_with = string1.endswith(string4)
    match_no_match = ""
    if starts_with and ends_with and contains:
        match_no_match = "Match"
    else:
        match_no_match = "No match"
    return match_no_match
