#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Gunnar with a simple menu to start up with.
Gunnar doesnt do anything, just presents a menu with some choices.
You should add functinoality to Gunnar.
"""

from random import randint
Gunnar_image = r"""
       _       _
     (_\     /_)
       ))   ((
   .-''''''''''''-.  
 /^\/  _.   _.  \/^\
 \(   /__\ /__\   )/
  \,  \o_/_\o_/  ,/
    \    (_)    /
     `-.'==='.-'
      __) - (__   
     /  `~~~`  \
    /  /     \  \
    \ :       ; /
     \|==(*)==|/
      :       :
       \  |  /
     ___)=|=(___
    {____/ \____}
"""


def menu():
    '''Prints menu'''
    print(chr(27) + "[2J" + chr(27) + "[;H")
    print(Gunnar_image)
    print("Tjofräs, I'm Gunnar. I am all powerful. What can I do you for?")
    print("1) Present yourself to Gunnar.")
    print("2) Celcius to Farenheit")
    print("3) Word multiplication")
    print("4) Sum and average")
    print("5) Letter multiplication")
    print("6) ISOGram?")
    print("7) Messy strings")
    print("8) Randomize strings")
    print("9) Get acronym")
    print("10) Mask string")
    print("11) Find all indexes")
    print("12) Word search")
    print("13) Diffrance in emission")
    print("14) Find all indexes")

    print("EXTRA ============")
    print("A1) String contains chars")
    print("A2) Double until all numbers")
    print("A3) Replace tabs")
    print("A4) Merge names")
    print("A5) Score counter")
    print("q) Quit.")


def cTof(temp: float):
    '''converts c to f'''
    return temp * 9 / 5 + 32


def printExit():
    '''Prints quit message'''
    print("Bye, bye - and welcome back anytime!")


def greet():
    '''Prints greeting'''
    name = input("What is your name? ")
    print("\nGunnar says:\n")
    print("Hello %s - your awesomeness!" % name)
    print("What can I do you for?!")


def celcius_to_farenheit():
    '''Converts c to f'''
    c = float(input("Enter celcius:"))
    print(f"{round(cTof(c),2)} Farenheit")


def word_manipulation():
    '''Manipulates wordsF'''
    word = input("pls give word")
    times = int(input("how manny times"))
    print(multiply_str(word, times))


def sum_and_average():
    '''Prints sum and average'''
    thesum = 0
    count = 0
    while True:
        num = input("Enter number or done")
        if(num == "done"):
            break
        thesum += float(num)
        count += 1
    print(round(thesum, 2))
    print(round(thesum/count, 2))


def hyphen_string():
    '''Makes a hyphen string from string'''
    word = input("give The Word")
    count = 1
    string = ""
    for letter in word:
        string += letter*count + "-"
        count += 1
    print(string[:-1])


def is_isogram():
    '''Checks if word is an isogram'''
    word = input("gimme a word pls pls")
    used = []
    dupe = False
    for char in word:
        if char not in used:
            used.append(char)
        else:
            dupe = True
    if(dupe):
        print("No match!")
    else:
        print("Match!")


def compare_numbers():
    '''Compares numbers'''
    history = []
    num = None
    while True:
        userInput = input("Give me number")
        try:
            num = float(userInput)
        except ValueError:
            if(userInput == "done"):
                break
            print("not a number!")
            continue
        if(len(history) == 0):
            history.append(num)
            print("First time")
        else:
            lastElement = history[len(history) - 1]
            if(lastElement < num):
                print("larger!")
            elif(lastElement > num):
                print("smaller!")
            else:
                print("same!")
            history.append(num)


def wordMatchA1():
    '''Wordmatch function'''
    in1 = input("Input 1").lower()
    in2 = input("Input 2").lower()
    notIn = False
    for char in in2:
        if char not in in1:
            notIn = True
    if(notIn):
        print("No match!")
    else:
        print("Match!")


def howManyTimesForAllNumbersAtleastOnce():
    '''Checks how many times you need to multiply with 2 to find all numbers in a number'''
    in1 = int(input("Input 1"))
    in2 = int(input("Input 2"))
    counter = 0
    number = in1
    while True:
        if(counter > in2):
            print("Answer: -1 times")
            break
        strNumber = str(number)
        hasAllNums = True
        for char in "0123456789":
            if char not in strNumber:
                hasAllNums = False
        if(hasAllNums):
            print(f"Answer: {counter} times")
            break
        else:
            counter += 1
            number *= 2


def replaceTabs():
    '''Replaces tabs'''
    in1 = input("Input 1")
    out = ""
    for letter in in1:
        if ord(letter) == 9:
            out += "   "
        else:
            out += letter
    print(out)


def nameGenerator():
    '''Makes a new name'''
    splitLetters = "aeiouy"
    name1 = input("Name1")
    name2 = input("Name2")

    out = ""
    for char in name1:
        if char not in splitLetters:
            out += char
        else:
            break
    foundSplitter = False
    # Dirty hack, works here tho
    for char in name2:
        if char in splitLetters:
            foundSplitter = True
        if(foundSplitter):
            out += char
    print(out)


def pointCounter():
    '''Counts points'''
    i = 0
    in1 = input("Name1")
    scoreMap = {}
    while(i < len(in1)):
        player = in1[i].lower()
        lostPoints = in1[i].lower() != in1[i]
        if player not in scoreMap:
            scoreMap[player] = 0
        if(lostPoints):
            scoreMap[player] -= int(in1[i+1])
        else:
            scoreMap[player] += int(in1[i+1])
        i += 2
    out = ""
    # Disabling here since i need keys aswell as value in this case
    # pylint: disable=consider-using-dict-items
    for player in scoreMap:
        out += f"{player} {scoreMap[player]}, "
    print(out[: - 2])


def randomize_string(stringToRandomize: str):
    '''Shuffles a string'''
    outString = split(stringToRandomize)
    # Need index here so i dont want to use enumerate
    # pylint: disable=consider-using-enumerate
    for i in range(len(outString)):
        randomIndex = randint(0, len(outString)-1)
        tmp = outString[randomIndex]
        outString[randomIndex] = outString[i]
        outString[i] = tmp
    return(f"{stringToRandomize} --> {''.join(outString)}")


def get_acronym(inputString: str):
    '''Makes a new acronym'''
    out = ""
    for letter in inputString:
        if(letter.isupper()):
            out += letter
    return out


def mask_string(inputString):
    '''Masks a string'''
    mask = inputString[:-4]
    return multiply_str("#", len(mask)) + inputString[-4:]


def find_all_indexes(inputString: str, substring: str):
    """Finds all indexes"""
    indexes = []
    counter = 0
    try:
        while True:
            index = inputString.index(substring, counter)
            indexes.append(f"{index}")
            counter = index + len(substring)
    except ValueError:
        return ",".join(indexes)


def multiply_str(s, l):
    """Multiplies a string"""
    return s*l


def split(word):
    """Splits a string into chars"""
    return [char for char in word]


def points_to_grade(maxScore, score):
    """Gets grade"""
    precent = (float(score) / float(maxScore)) * 100
    if precent >= 90:
        return "score: A"
    if precent >= 80:
        return "score: B"
    if precent >= 70:
        return "score: C"
    if precent >= 60:
        return "score: D"
    if precent < 60:
        return "score: F"
    return "N/A"


def has_strings(whole: str, start: str, mid: str, end: str):
    """Cehcks if string is in sing"""
    startBool = whole.startswith(start)
    midBool = mid in whole
    endBool = whole.endswith(end)
    return "Match" if startBool and midBool and endBool else "No match"
