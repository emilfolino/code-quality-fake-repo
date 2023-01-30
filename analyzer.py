#pylint: disable-all
"""
alla funktioner finns här
"""
import collections


def countLines(fileName):
    """
    Räknar antal rader
    """
    sumLines = 0
    for line in open(fileName):
        if line != "\n":
            sumLines += 1
    return sumLines

def countWords(fileName):
    """
    Räknar antal ord
    """
    file = open(fileName)
    words = file.read().split()
    return len(words)

def countLetters(fileName):
    """
    Räknar antal bokstäver
    """
    file = open(fileName)
    letters = file.read()
    sumLetters = 0
    for letter in letters:
        if letter != "\n" and letter != " " and letter != "." and letter != "," and letter != "-":
            sumLetters += 1

    return sumLetters

def word_frequency(fileName):
    """
    Räknar frekvens ord
    """
    file = open(fileName)
    text = file.read().split()
    listWords = {}
    for word in text:
        if "," in word:
            word = word[:-1]
        if "." in word:
            word = word[:-1]
        if word.lower() not in listWords:
            listWords[word.lower()] = 1
        else:
            listWords[word.lower()] += 1
    
    listWords = collections.OrderedDict(sorted(listWords.items(), reverse=True))
    listWords = sorted(listWords.items(), key=lambda x: x[1], reverse=True)
    amountPrinted = 0
    sumWords = countWords(fileName)
    for word in listWords:
        if amountPrinted < 7:
            percent = (word[1] / sumWords) * 100
            print(word[0] + ": " + str(word[1]) + " | " + str(round(percent, 1)) + "%" )
            amountPrinted += 1
        else:
            break
    

def letter_frequency(fileName):
    """
    Räknar frekvens bokstäver
    """
    file = open(fileName)
    text = file.read()
    listLetters = {}
    for letter in text:
        if letter.lower() not in listLetters:
            if letter != "\n" and letter != " ":
                listLetters[letter.lower()] = 1
        else:
            if letter.lower() != "\n" and letter != " ":
                listLetters[letter.lower()] += 1
    
    listLetters = sorted(listLetters.items(), key=lambda x: x[1], reverse=True)
    amountPrinted = 0
    sumLetter = countLetters(fileName)
    for letter in listLetters:
        if amountPrinted < 7: 
            percent = (letter[1] / sumLetter) * 100
            print(letter[0] + ": " + str(letter[1]) + " | " + str(round(percent, 1)) + "%")
            amountPrinted += 1
        else:
            break
