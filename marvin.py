#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Marvin with a simple menu to start up with.
Marvin doesnt do anything, just presents a menu with some choices.
You should add functinoality to Marvin.
"""
from random import shuffle

botname = "Donald"

"""
Its an eternal loop, until q is pressed.
It should check the choice done by the user and call a appropriate
function.
"""

def greet():
    """A short greeting"""
    name = input("What is your name, user? ")
    print("Hi %s! My name is Påhl, I'm the creator of this bot. I hope you like it" % name)

def celcius_to_farenheit():
    """Converts between celcius and farenheit"""
    temperature = float(input("Temperature in Celsius: "))
    temperature = round((temperature * 1.8) + 32, 2) #Convert to Fahrenheit

    print("\n%s says:\n" % botname)
    print("The value in Fahrenheit is: " + str(temperature))

def word_manipulation():
    """Repeats a word"""
    word = input("Enter a word: ")
    number = int(input("Enter a number: "))
    print(multiply_str(word, number))

def sum_and_average():
    """Calculates sum and average"""
    x = 0
    i = 0
    while True:
        inputString = input("\nEnter a number to add to the sum, write 'done' when you are done. \n")
        if inputString == "done":
            break
        else:
            x = x + float(inputString)
            i += 1
    print("The sum of all numbers are: " + str(round(x, 2)) + " and the average is " + str(round((x/i), 2)))

def hyphen_string():
    """Puts a hypen between words"""
    word = input("Enter a word: ")
    output = ""
    repeat = 1
    for x in word:
        y = 0
        while y < repeat:
            y += 1
            output = output + x
        if len(word) > repeat:
            output = output + "-"
        repeat += 1
    print(output)

def is_isogram():
    """Checks if a word is an isogram"""
    word = input("Enter a word: ")
    
    output = "Match!"
    for i, x in enumerate(word): #Gives each char in 'x' while also giving me a position number in the int 'i'
        for y in word[(i+1):]: #Iterates from next character until the end of 'word' s[start:stop]
            if (x == y):
                output = "No match!"
    print(output)

def compare_numbers():
    """Compare numbers"""
    previousNumber = input("Enter the first number: ")
    while True:
        try:
            currentNumber = input("Enter another number: ")
            if currentNumber == "done":
                break
            elif (int(currentNumber) > int(previousNumber)):
                print(currentNumber + " : " + previousNumber + " larger!")
            elif (int(currentNumber) < int(previousNumber)):
                print("smaller!")
            else:
                print("same!")
            previousNumber = currentNumber
        except ValueError:
            print("not a number!")

def randomize_string(string:str):
    """Randomizes a given string"""
    l = list(string) #Makes a list of the string
    shuffle(l) #Shuffles the list. (Import up top)
    shuffledString = "".join(l) #Concatenates the list to a string. (ie. makes it a string again)
    return string + " --> " + shuffledString #return original and result

def get_acronym(string:str):
    """Returns only the uppercase letters of a string"""
    newString = ""
    for char in string:
        if char.isupper():
            newString = newString + char
    return newString

def mask_string(string:str):
    """Masks all but the last 4 characters in a string"""
    mask = multiply_str("#", (len(string) - 4))
    newString = mask + string[-4:]
    return newString

def multiply_str(string:str, multiplyBy:int):
    """Returns a given string, repeated multiplyBy times"""
    newString = ""
    for _ in range(multiplyBy):
        newString = newString + string
    return newString

def find_all_indexes(string:str, substring:str):
    """Returns a string with all indexes at which substring exists in string"""
    returnString = ""
    index = 0
    #Run until index() gives ValueError, meaning there are no more found instances of substring
    try:
        while True:
            index = string.index(substring, index + 1) #Look for next index, starting at current index + 1
            returnString = returnString + str(index) + "," #Concatenate found index into our string of indexes
    except ValueError:
        return returnString.strip(",")

def points_to_grade(maxPoints:int, points:int):
    """Grades points. Returns string with result"""
    if points <= maxPoints:
        grade = "score: "
        percentage = (int(points) / int(maxPoints)) * 100
        if percentage >= 90:
            grade = grade + "A"
        elif percentage >= 80:
            grade = grade + "B"
        elif percentage >= 70:
            grade = grade + "C"
        elif percentage >= 60:
            grade = grade + "D"
        else:
            grade = grade + "F"
    else:
        grade = "Points earned can not be higher than the maximum possible points!"
    return grade

def has_strings(string:str, prefix:str, middle:str, end:str):
    """Checks if string is made out of substrings 1,2 and 3"""
    if string.startswith(prefix):
        if middle in string:
            if string.endswith(end):
                return "Match"
    return "No match"
