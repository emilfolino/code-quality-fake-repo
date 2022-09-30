#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Marvin with a simple menu to start up with.
Marvin doesnt do anything, just presents a menu with some choices.
You should add functinoality to Marvin.
"""
import random
turtle_image = r"""
                                       ___-------___
                                   _-~~             ~~-_
                                _-~                    /~-_
             /^\__/^\         /~  \                   /    \
           /| O ||O |        /      \_______________/        \
          | |___||__|      /       /                \          \
          |          \    /      /                    \          \
          |   (_______) /______/                        \_________ \
          |         / /         \                      /            \
           \         \^\         \                  /               \     /
             \         ||           \______________/      _-_       //\__//
               \       ||------_-~~-_ ------------- \ --/~   ~\    || __/
                 ~-----||====/~     |==================|       |/~~~~~
                  (_(__/  ./     /                    \_\      \.
                         (_(___/                         \_____)_)
"""

"""
Its an eternal loop, until q is pressed.
It should check the choice done by the user and call a appropriate
function.
"""
library = []
def  name():
    """Name function"""
    nume = input("Whom do i speak with? ")
    print("\n Wise turtle says:\n")
    print("Greatings %s " % nume)
    print("What can I do for you?")

def  farenheit():
    """Farenheit function"""
    print("\nMarvin says:\n")
    print("Let's see what Celsius is in Farenheit")
    user_input_string = input("Celcius -->")
    Farenheit = (float(user_input_string) * 9/5) + 32
    print("Farenheit: " + str(Farenheit))

def  multiplier():
    """Multiplier function"""
    print("\n wise turtle says: \n ")
    print("Let's multiply some words.") 
    user_imput_string = input("Enter a word ->")
    user_imput_string_2 = input("And how many times should we multiply it? ->")
    printed = 0
    while printed < int(user_imput_string_2):
        print(user_imput_string)
        printed += 1

def  math():
    """Math function"""
    input_number = []
    print("Go ahead and ask me?")
    while True:
        input_number.append(input("number -->"))
        if input_number[-1] == "done":
            del input_number[-1]
            break 
        change_input = [int(item) for item in input_number]
        print("sum: "+ str(sum(change_input)))
        print("Medel: "+str(sum(change_input)/len(change_input)))

def  worth():
    """Worth function"""
    input_number = []
    print("Give me numbers that I can kompare.")
    while True: 
        input_number.append(input("Number -->"))
        if input_number[-1] == "done":
            del input_number[-1]
            break
        if len(input_number) == 1:
            print("Please add one more number")
        else:
            if input_number[-1] > input_number[-2]:
                print("The resent number is greater than the one before")
            if input_number[-1] < input_number[-2]:
                print("The resent number is smaler than the one before")
            if input_number[-1] == input_number[-2]:
                print("The resent number is equal to the one before")
            if input_number[-1] == "done":
                del input_number[-1]
                break
def  expander():
    """Expander function"""
    y = 0 
    input_number = input("Word --> ")
    input_number = list(input_number)
    ANSWER = []
    for x in range(len(input_number)):
        result = ""
    if y == 0:
        result = input_number[0]
    else: 
        x += 1
        result = input_number[y] * x
        y += 1
        ANSWER.append(result)
    result = '-'.join(ANSWER)
    print(str(result))
def isogram():
    """Isogram function"""
    input_number = input("Word -->")
    input_number = input_number.lower()
    iso = []
    ANSWER = ""
    for letter in input_number: 
        if letter.isalpha():
            if letter in iso:
                ANSWER = "No match"
                print("No match")
            iso.append(letter)
    if ANSWER != "No match":
        ANSWER = "Match"
        print(ANSWER)
def suffle():
    """Suffle function"""
    input_suffle = input("word -->")
    input_random = list(input_suffle)
    random.shuffle(input_random)
    input_join = ''.join(input_random)
    print("The words letters got shuffled to " + input_join)
def anagram():
    """Anagram function"""
    input_anagram = input("First word -->")
    input_anagram2 = input("second word -->")
    if (sorted(input_anagram) == sorted(input_anagram2)):
        print("match")
    else:
        print("No match") 
def acronym(): 
    """Acronym function"""
    input_acronym = input("Give me a sentence that i can scan for acronyms -->")
    input_acrolist = list(input_acronym)
    answer = []
    for x in input_acrolist:
        if x.isupper():
            answer.append(x)
    if not answer:
        print("No acronyms found")
    else:
        print(str(answer))
def lister():
    """Lister function"""
    input_num = input("Give me numbers -->")
    input_numlist = input_num.split(',')
    diez = []
    for x in input_numlist:
        if int(x) > 10:
            diez.append(x)
    if not diez:
        print("No numbers are above 10")
    else:
        print(diez) 
def inv(cho):
    """Inv function"""
    print(library)
    print("items in library:", len(library))    
    if "inv pick" in cho:
        dd = cho.split()
        print(dd)
        try:
            if isinstance(int(dd[-1]), int):
                library.insert(int(dd[-1]), dd[-2])
            print(library)
            if int(dd[-1]) > len(library):
                print("index number was to high so the item was placed last in library.") 
        except ValueError:
            library.append(dd[-1])
            print(library)
    elif "inv drop" in cho:
        try:
            dd = cho.split()
            library.remove(dd[-1])
            print(library)
        except ValueError:
            print("Item not in library.")
    elif  "inv swap" in cho:
        try:
            dd = cho.split()
            vd = library.index(dd[-1])
            dv = library.index(dd[-2])
            library[vd], library[dv] = library[dv], library[vd]
        except ValueError:
            print("One of the items is not in the library.")

    
