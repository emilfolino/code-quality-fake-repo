"""Module for marvin"""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random


"""
Marvin with a simple menu to start up with.
Marvin doesnt do anything, just presents a menu with some choices.
You should add functinoality to Marvin.
"""

marvin_image = r"""
        _..._
      .'     '.
     / \     / \
    (  |     |  )
    (`"`  "  `"`)
     \         /
      \  ___  /
       '.___.'
"""


def goodbye():
    """goodbye """
    print("Bye, bye have a nice day!")


def menu():
    """main function """
    print(marvin_image)
    print("Hello, my name is Marvin. I dont know everything, but i'll do my best to help you.")
    print("1) Present yourself to Marvin.")
    print("2) Convert Celsius to Fahrenheit.")
    print("3) Word multiplication.")
    print("4) Sum & Average.")
    print("5) Comparing Numbers")
    print("6) Rebuilding string")
    print("7) Is isogram?")
    print("8) randomize_string.")
    print("9) get_acronym.")
    print("10) mask_string.")
    print("11) find_all_indexes.")
    print("q) Quit")


def greet():
    """ Greeting function """
    name = input("What is your name? ")
    print("\nMarvin says:\n")
    print("Hello ", name, " nice to meet you")


def celcius_to_farenheit():
    """ celcius_to_farenheit """

    print("\nMarvin says:\n")
    print("Present the temp in Celsius and i'll convert it for you")
    c = float(input("--> "))
    f = round((c * 9 / 5) + 32, 2)
    print("Your presented Celsius temp ",
          c, " is ", f, " in Farenheit")


def word_manipulation():
    """ word_manipulation """
    print("\nMarvin says:\n")
    word = input("Type a word please. ")
    number = input("Now type a number please. ")
    # val = ""
    # for i in range(int(number)):
    #     val += word
    print(multiply_str(word, int(number)))


def sum_and_average():
    """ sum_and_average """
    print("\nMarvin says:\n")
    print("Type numbers. I will do the calculations. When you dont want to enter more numbers type DONE \n\n")
    sum1 = float(0)
    times = 0

    while True:
        inP = input("Type number. \n")
        print("Detta är input:", inP)
        if str(inP) == "DONE" or str(inP) == "done":
            break
        elif (inP.isdigit() or isinstance(float(inP), float)):
            sum1 = float(sum1) + float(inP)
            times += 1
        else:
            continue
    print("The sum of your numbers is ", round(sum1, 2),
          " and the total average is ", round(sum1/times, 2))


def hyphen_string():
    """ hyphen_string """
    print("\nMarvin says:\n")
    inP = input("Type a word ")
    s = ""
    strLength = len(inP)

    for i in range(0, strLength):
        for _ in range(0, i+1):
            s += inP[i]
        s += '-'
    print(s)


def is_isogram():
    """ is_isogram """
    print("\nMarvin says:\n")
    inP = input("Type a word ")
    s = inP.lower()
    for letter in s:
        if s.count(letter) >= 2:
            print(inP, " No match!")
            break
    else:
        print(inP, " Match!")


def compare_numbers():
    """ compare_numbers """
    print("\nMarvin says:\n")
    print(
        "Type numbers. I will compare them. When you dont want to enter more numbers type DONE \n\n")
    number = ""
    while True:
        inP = input("Type number. (you can always quit with DONE) \n")
        try:
            if str(inP) == "DONE" or str(inP) == "done":
                break
            inP = int(inP)

        except ValueError:
            print("not a number!")
            continue
        if not isinstance(number, int):
            number = int(inP)
            print(
                "This was your first number, type another and I will compare it")
            continue

        if int(inP) > number:
            print("This numbers is larger! than your previous one.")

        elif int(inP) == number:
            print("This numbers is the same! as your previous one.")

        elif int(inP) < number:
            print("This numbers is smaller! than your previous one.")
        else:
            print("not a number!")
        number = int(inP)


def randomize_string(arg):
    """ randomize_string"""
    l = list(arg)
    random.shuffle(l)
    result = ''.join(l)
    return arg + " --> " + result


def get_acronym(arg):
    """ get_acronym"""
    retStr = ""
    strlen = len(arg)
    for i in range(0, strlen):
        if i == 0:
            retStr += arg[i]
        elif arg[i].isupper():
            retStr += arg[i]
        elif arg[i-1] == ' ':
            retStr += arg[i]
    return retStr.upper()


def mask_string(arg):
    """ mask_string"""

    returnStr = multiply_str("#", len(arg)-4) + arg[-4:]
    return returnStr


def multiply_str(argStr, argInt):
    """ multiply_str"""
    return argStr*argInt


def find_all_indexes(argStr1, argStr2):
    """ find_all_indexes"""
    foundIndexes = ""
    searchStart = 0
    while True:
        try:
            result = argStr1.index(argStr2, searchStart)
            if result >= 0:
                foundIndexes += str(result) + ','
                searchStart = result+1
        except ValueError:
            return foundIndexes[:-1]
