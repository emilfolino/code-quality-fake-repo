"""
This module contains all functions used in the menu options in main.py.
The functions are all relevant to the topic of analyzing frequency of letters, lines and letters in a text file.
"""
from operator import itemgetter

def lines(file):
    """
    This function uses the file from the argument and registers every line that is not empty as a real line.
    Returns the non-empty line count.
    """
    linecount = 0
    with open(file) as fh:
        fhList = fh.readlines()
        for i in fhList:
            if i != "\n":
                linecount += 1
    return linecount

def words(file):
    """
    Reads the argumented file and returns a list with all of the words, without blankspaces.
    """
    with open(file) as fh:
        fhStr = fh.read()
        newStr = ""
        for i in fhStr:
            if i == "\n":
                i = " "
            newStr += i.lower()
        fhList = newStr.split(" ")
    return fhList

def letters(file):
    """
    Reads the argumented file and returns a string with all letters from the file, 
    without any special characters, newlines or spaces.
    """
    with open(file) as fh:
        fhStr = fh.read()
        newStr = ""
    for i in fhStr:
        if i in (" ", "\n", ",", ".", "-", "'", ":", "<", ">", "+", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"):
            i = ""
        newStr += i
    return newStr.lower()

def word_frequency(file):
    """
    Returns a string with the 7 most frequently used words in the argumented file, 
    with linebreaks between every new word.
    Every line contains the aforementioned word, it's frequency and how many percent the word covers the file's text,
    with a colon between the word and the frequency, and a '|' between the frequency and the percentage.
    """
    with open(file) as fh:
        fhStr = fh.read()

        newStr = ""
        for i in fhStr:
            if i == "\n":
                i = " "
            if i in (",", "."):
                i = ""
            newStr += i.lower()
        fhList = newStr.split(" ")
        fhDict = {}
        for word in fhList:
            try:
                fhDict[word] += 1
            except KeyError:
                fhDict[word] = 1
        fhDictList = sorted(fhDict.items(), reverse=True)
        fhDictListSorted = sorted(fhDictList, key=itemgetter(1), reverse=True)
        utskrift = ""
        for i in fhDictListSorted[0:7]:
            utskrift += i[0] + ": " + str(i[1]) + " | " + str(round(100*i[1]/len(words(file)), 1)) + "%" +"\n"
    return utskrift.rstrip()

def letter_frequency(file):
    """
    Returns a string with the 7 most frequently used letters in the argumented file, 
    with linebreaks between every new letter.
    Every line contains the aforementioned letter, it's frequency and the percentage of how many letters
    in the file are that letter.
    """
    lettersStr = letters(file)
    fhDict = {}
    for letter in lettersStr:
        try:
            fhDict[letter] += 1
        except KeyError:
            fhDict[letter] = 1
    fhDictList = sorted(fhDict.items(), reverse=True)
    fhDictListSorted = sorted(fhDictList, key=itemgetter(1), reverse=True)
    utskrift = ""
    for i in fhDictListSorted[0:7]:
        utskrift += i[0] + ": " + str(i[1]) + " | " + str(round(100*i[1]/len(letters(file)), 1)) + "%" +"\n"
    return utskrift.rstrip()

def alloftheabove(file):
    """
    Returns a dictionary with the names of the functions defined above with the function name as the keys,
    and the returned value from the function as the dictionary value.
    """
    alldict = {
    "lines" : lines(file),
    "words" : len(words(file)),
    "letters" : len(letters(file)),
    "word_frequency" : word_frequency(file),
    "letter_frequency" : letter_frequency(file)
    }
    return alldict
    