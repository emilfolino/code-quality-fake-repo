#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Module containing function to display the menu
"""
import re
from operator import itemgetter

##Helper functions ======================================

def lineToWords(lineToAnalyze):
    """
    Helper function which splits the stirng into a list of words
    returns the word list when emty strings have been removed
    """
    lineToAnalyze = str(lineToAnalyze).lower()
    wordList = re.split(r", |\. | |\! |\? |\n|\: |; |\- |\.|\,", lineToAnalyze)
    wordListNoEmptyElems = []
    for word in wordList:
        if word != "":
            wordListNoEmptyElems.append(word)
    return wordListNoEmptyElems

def wordsToLetters(wordsList):
    """
    Helper function which takes a list of words and separates them into a 
    list of letters. returns the list of letters
    """
    listOfLetters = []
    for word in list(wordsList):
        for letter in word:
            if letter != "-":
                listOfLetters.append(letter)
    return listOfLetters

def getFrequency(occurances, total):
    """
    Helper function which takes to values and calculates the frequency.
    returns the frequency after rounding to two decimals
    """
    frequency = occurances / total
    frequency = frequency * 1000
    frequency = round(frequency)
    return frequency / 10

def getSevenMostCommon(dictionary, totalElementCount):
    """
    Helper function which takes a dictionary and the total amount of the corresponding 
    element. Then the functions creates a reverse dictionary, to be able to sort the elements
    with the same amount of occurances. 
    
    first: {element : occurances} 
    later: {occurance : [element, element]}

    Then the function sorts by occurances and then sorts the list of elements to each occurance.
    A list then appends every word with the corresponding occurance.

    Now there are a list with both sorted occurances and elements.
    The first seven elements of the list are put in a dictionary to be returned.
    The returned dictionary is of type: {element : occurance, frequency}
    """

    dictByValue = {}
    sevenMostCommon = {}

    for element in dict(dictionary).items():
        if element[1] not in dictByValue:
            dictByValue[element[1]] = []
            
        dictByValue[element[1]].append(element[0])

    dictByValueList = dictByValue.items()

    dictByValueList = sorted(dictByValueList, key=itemgetter(0), reverse=True)

    sortedwordList = []

    for wordList in dictByValueList:
        for word in sorted(wordList[1], reverse= True):
            sortedwordList.append((word, wordList[0]))

    for word in sortedwordList[:7]:
        sevenMostCommon[word[0]] = (word[1], getFrequency(word[1], totalElementCount))

    return sevenMostCommon

def printFrequencyDictionary(dictionary):
    """
    A helper function to print dictionarys like the ones returned from getSevenMostCommon funtion.
    """
    dictionaryList = dict(dictionary).items()
    for element in dictionaryList:
        print(str(element[0]) + ": " + str(element[1][0]) + " | " + str(element[1][1]) + "%")


##Functions used in main.py =============================

def linesAnalyzer(fileName):
    """
    Function to calculate the number of lines in file.
    returns the amount of lines.
    """
    lineCounter = 0    
    with open(fileName, "r") as fileHandler:
        for line in fileHandler:            
            if line != "\n":
                lineCounter += 1
    return lineCounter

def wordsAnalyzer(fileName):
    """
    Function to calculate the amount of words in file.
    Calls the function lineToWords for each line in file to get a list of words in that line.
    returns the amount of words.
    """
    wordCounter = 0
    with open(fileName, "r") as fileHandler:
        for line in fileHandler:
            wordCounter += len(lineToWords(line))
    return wordCounter

def lettersAnalyzer(fileName):
    """
    Function to calculate the amount of letters in file.
    Calls lineToWords and then wordsToLetters for every line to get a list of the letters in that line.
    returns the amount of letters. 
    """
    letterCounter = 0
    with open(fileName, "r") as fileHandler:
        for line in fileHandler:
            letterCounter += len(wordsToLetters(lineToWords(line)))
    return letterCounter

def wordFrequencyAnalyzer(fileName):
    """
    Function that gets all the words of every line and puts them in a list.
    Then a dictionary is created to store all the words and amount of times that they occure.
    Calls printFrequencyDictionary with getSevenMostCommon with wordsAnalyzer to get and print 
    the seven most common words with occurances and frequency.
    """
    wordsList = []
    with open(fileName, "r") as fileHandler:
        for line in fileHandler:
            for word in lineToWords(line):
                wordsList.append(word)
    wordDict = {}
    for word in wordsList:
        if word in wordDict:
            wordDict[word] += 1
        else:
            wordDict[word] = 1

    printFrequencyDictionary(getSevenMostCommon(wordDict, wordsAnalyzer(fileName)))

def letterFrequencyAnalyzer(fileName):
    """
    Function that gets all the letters of every line and puts them in a list.
    Then a dictionary is created to store all the letters and amount of times that they occure.
    Calls printFrequencyDictionary with getSevenMostCommon with lettersAnalyzer to get and print 
    the seven most common letters with occurances and frequency.
    """
    wordList = []
    with open(fileName, "r") as fileHandler:
        for line in fileHandler:
            for word in lineToWords(line):
                wordList.append(word)
    lettersList = wordsToLetters(wordList)
    letterDict = {}
    for letter in lettersList:
        if letter in letterDict:
            letterDict[letter] += 1
        else:
            letterDict[letter] = 1

    printFrequencyDictionary(getSevenMostCommon(letterDict, lettersAnalyzer(fileName)))

def allAnalyzer(fileName):
    """
    Function that calls and prints all the analyzies of the file.
    """
    print(linesAnalyzer(fileName))
    print(wordsAnalyzer(fileName))
    print(lettersAnalyzer(fileName))
    wordFrequencyAnalyzer(fileName)
    letterFrequencyAnalyzer(fileName)

def changeFile(currentFile):
    """
    Function to change the file to be analyzed.
    The currently analyzed files name is tored in main.
    The value of that variable is set by this function.
    If the file enetered exists it returns the new filename.
    else it returns the old filename
    """
    inputLine = input("Name the file to analyze: ")
    try:
        with open(inputLine, "r"):
            print("File changed!")
        return inputLine
    except FileNotFoundError:
        print("File not found!")
        return currentFile
