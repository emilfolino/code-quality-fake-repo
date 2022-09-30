#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Marvin with a simple menu to start up with.
Marvin doesnt do anything, just presents a menu with some choices.
You should add functinoality to Marvin.
"""

import random

#Name option
def greet():
    """ greets user """
    name = input("What is your name? ")
    print("\nGroos says:\n")
    print("Hello %s - I'm your assistant today!" % name)
    print("What can I do you for?!")

#Celsius option
def celcius_to_farenheit():
    """ converts celsius to farenheit """
    numm = input("Input amount of Celsius: ")
    numm = round(float(numm) * 1.8 + 32, 2)
    print(str(numm) + " Farenheit")

#Parrot option
def word_manipulation():
    """ word_manipulation """
    numm = input("What word should i say?: ")
    numm2 = input(f"How many times should i say '{numm}': ")
    print(multiply_str(numm,numm2))

#Math option
def sum_and_average():
    """ sum_and_average """
    total = 0
    repeated = 0
    print("Im gonna ask for numbers, when youre done, type 'done'")

    #input numbers loop
    while (True):
        numm = input("#: ")
        if numm == "done":
            #exit loop
            break
        else:
            #add number to total
            total += float(numm)
            repeated += 1

    print("The sum of those numbers is: " + str(round(total , 2)) )
    print("The average of those numbers is: " + str(round( total / repeated , 2)) )

#Character thing option
def hyphen_string():
    """ hyphen_string """
    total = ""
    string = input("Write a word: ")
    length = len(string)

    for x in range(length):
        total += string[x] * int(x+1)
        if x != len(string)-1:
            total += "-"

    print(total)

#Isogram option
def is_isogram():
    """ checks if string is isogram """
    print("An isogram is a word that doesn't reuse a single letter")
    string = input("Gimme a word: ")
    char_list = []
    result = False

    #Gå Genom Char_list arrayn, om bokstaven inte finns läggs den till
    for x in string:
        if x not in char_list:
            #Bokstaven finns inte och läggs till
            result = True
            char_list.append(x)
        else:
            #Bokstaven finns i char_list
            result = False
            break

    if result:
        print("Match!")
    else:
        print("No match!")

#smaller bigger option
def compare_numbers():
    """ compare_numbers """
    print("Welcome to 'Smaller, The Same or Bigger?', to exit, write 'done'")
    nummOLD = input("Write a number: ")

    while (True):
        nummNEW = input("Again: ")

        if nummNEW == "done":
            break

        #test if variable is string
        try:
            nummNEW = float(nummNEW)
            nummOLD = float(nummOLD)
        except ValueError:
            print("not a number!")
            continue

        #Check which variable is larger
        if nummNEW > nummOLD:
            print("larger!")
            nummOLD = nummNEW

        elif nummNEW == nummOLD:
            print("same!")
            nummOLD = nummNEW

        elif nummNEW < nummOLD:
            print("smaller!")
            nummOLD = nummNEW

#MARVIN 2 !!___________________

#menyval 8
def randomize_string(s):
    """ randomize_string """
    #string behöver bli list för shuffle functionen
    l = list(s)
    random.shuffle(l)
    #join sätter ihop string listan med '' (eller inget) mellan chars-en
    return s + " --> " + ''.join(l)

#menyval 9
def get_acronym(s):
    """ get acronym from a string """
    new = ""
    #gå genom stringen och lägg till char-en som är Uppercase
    for i in s:
        if i.isupper():
            new += i

    return new

#menyval 10
def multiply_str(s,s2):
    """ multiply_str """
    return str(s * int(s2))

def mask_string(s):
    """ makes all characters '#' except the last 4 """
    if len(s) > 3:
        #save the last 4 chars
        result = s[-4]+s[-3]+s[-2]+s[-1]
    else:
        #incase the string wasnt longer than 3
        result = s

    return multiply_str("#",len(s)-4)+result

#menyval 11
def find_all_indexes(s,s2):
    """ finds all indexes in a string """
    indx = []
    le = len(s)
    i = 0

    while i <= le:
        try:
            i = s.index(s2,i)
            indx.append(str(s.index(s2,i)))
            i += 1
        except ValueError:
            indx = ','.join(indx)
            return indx

    #ifall except inte körs
    indx = ','.join(indx)
    return indx
