#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" Methods for marvin the chat bot """


def choice_q():
    """Quit method"""
    print("Bye, bye - and welcome back anytime!")

def lines(file):
    """Print number of non empty lines in txt file"""
    emptyList = []
    for i, j in enumerate(file):
        if j == '\n':
            emptyList.append(i)

    indexes = emptyList
    for index in sorted(indexes, reverse=True):
        del file[index]

    return len(file)

def words(file):
    """Print number of words in txt file"""
    numWords = 0
    for linesInFile in file:
        wordList = linesInFile.split()
        lengthWordList = len(wordList)
        numWords += lengthWordList

    return numWords

def letters(file):
    """Print number of words in txt file"""
    numLetters = 0
    for linesInFile in file:
        wordList = linesInFile.split()
        for wordsInWordList in wordList:
            characterList = list(filter(str.isalpha, wordsInWordList))
            numLetters += len(characterList)

    return numLetters

def word_frequency(file):
    """Print number frequency of words"""
    wordList = []
    txtPiece = ""
    txtPiece = ''.join(file)

    txtPiece = removeSpecialChar(txtPiece)

    txtPiece = txtPiece.replace("\n", " ")
    txtPiece = txtPiece.lower()

    wordList += txtPiece.split(" ")

    counts = {}
    for word in wordList:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    """I had to sort dictionary keys alpabetically to pass validation on lorum.txt"""
    countsSort = sorted(counts.keys(), reverse=True)
    newDict = {}
    for keys in countsSort:
        newDict[keys] = counts[keys]

    sortedList = sorted(newDict, key=newDict.get, reverse=True)

    txtResult = ""
    for w in sortedList[0:7]:
        txtResult += "{word}: {frequency} | {percFreq}%\n".format(word = w,
              frequency = counts[w], percFreq = round((counts[w]/words(file))*100, 1))

    return txtResult


def letter_frequency(file):
    """Print number frequency of letters"""
    txtPiece = ''.join(file)

    txtPiece = removeSpecialChar(txtPiece)

    txtPiece = txtPiece.replace("\n", " ")
    txtPiece = txtPiece.replace(" ", "")
    txtPiece = txtPiece.lower()

    counts = {}
    for letter in txtPiece:
        if letter in counts:
            counts[letter] += 1
        else:
            counts[letter] = 1

    sortedList = sorted(counts, key=counts.get, reverse=True)

    txtResult = ""
    for i in sortedList[0:7]:
        txtResult += "{letter}: {frequency} | {percFreq}%\n".format(letter = i,
              frequency = counts[i], percFreq = round(counts[i]/sum(counts.values())*100, 1))

    return txtResult

def allFunc(file):
    """Run all the above functions in one"""
    allResults = {}
    allResults["lines"] = str(lines(file)) + "\n"
    allResults["words"] = str(words(file)) + "\n"
    allResults["letters"] = str(letters(file)) + "\n"
    allResults["wordFreq"] = word_frequency(file)
    allResults["letterFreq"] = letter_frequency(file)

    txtResult = ""
    for content in allResults.items():
        txtResult += content[1]

    return txtResult

def change(phil):
    """Run all the above functions in one"""
    name = input("Input filename of txt file to be analysed: ")
    filename = name
    try:
        with open(filename) as filehandle:
            phil = filehandle.readlines()
    except FileNotFoundError:
        print("\nFile doesn't exist, deafult file *phil.txt* is analysed")

    return phil


def not_valid():
    """Not valid statement"""
    print("That is not a valid choice. You can only choose from the menu.")

def continue_func():
    """Continue method"""
    input("\nPress enter to continue...")

def removeSpecialChar(text):
    """Removing special characters from string method"""
    chars = "\\*_{}[]()>#+-.!$,:;"
    for c in chars:
        text = text.replace(c, '')

    return text
