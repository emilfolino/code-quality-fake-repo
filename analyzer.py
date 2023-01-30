"""Analyze functions"""
fileName = "phil.txt"

def ChangeFile(name):
    """Changing filename"""
    global fileName
    fileName = name
    

def all_Analyzes():
    """Full output of analyze"""
    lines = AmountLines(ReadFile())
    words = len(AmountWordFromString(ReadFile()))
    letters = CountLettersInList(ListOfChars(ReadFile()))
    list1 = [lines, words, letters]
    list1.sort()
    out = str(list1[0]) + '\n' + str(list1[1]) + '\n' + str(list1[2])
    out += '\n' + word_frequency() + letter_frequency()
    return out

def letter_frequency():
    """Return letter freq"""
    listVar = SortList(LetterFreqDict(ReadFile()))
    outString = ""
    for i in range(7):
        if len(listVar) - 1 < i:
            break
        outString += listVar[i][0] + ": "
        outString += str(listVar[i][1][0]) + " | "
        outString += str(listVar[i][1][1]) + "%\n"
    return outString

def word_frequency():
    """Return word freq"""
    listVar1 = SortList(WordFreqDict(ListOfWords(ReadFile())))
    outString = ""
    for i in range(7):
        if len(listVar1) - 1 < i:
            break
        outString += listVar1[i][0] + ": "
        outString += str(listVar1[i][1][0]) + " | "
        outString += str(listVar1[i][1][1]) + "%\n"
    return outString

def ReadFile():
    """Reading the file"""
    fileData = ""
    with open(fileName, 'r') as file:
        fileData = file.read()
    return fileData

def CountLettersInList(listOfChars):
    """count letters in list"""
    count = 0
    for item in listOfChars:
        if item in (' ', ',', '.', '\n', '-') :
            count += 1
    return len(listOfChars)-count

def ListOfChars(string):
    """Returning list of char"""
    return [char for char in string]

def StrToLower(listArg):
    """All chars to lowercase"""
    return str(listArg).lower()

def AmountLines(listArg):
    """Counting amount lines"""
    count = 1
    stringLength = len(listArg)
    for i in range(stringLength):
        if listArg[i] == '\n':
            count += 1
    return count

def ListOfWords(rawString):
    """Return list of words from string"""
    rawString = rawString.replace(',', '')
    rawString = rawString.replace('.', '')
    rawString = rawString.lower()
    wordList = rawString.split()
    return wordList

def AmountWordFromString(rawString):
    """Return list of words from string"""
    rawString = rawString.lower()
    wordList = rawString.split()
    return wordList


def LetterFreqDict(list44):
    """Creating dictionary with Letter with frequency"""
    counter = 0
    dictionay = dict({})

    for word in list44:
        if word in (' ', ',', '.', '\n', '-'):
            continue
        if word.lower() in dictionay:
            dictionay[word.lower()][0] += 1
            dictionay[word.lower()][1] = 1
        else:
            dictionay[word.lower()] = [1, 0]
        counter += 1

    for item in dictionay:
        dictionay[item.lower()][1] = round(
            (dictionay[item.lower()][0]/counter)*100, 1)
    return dictionay


def WordFreqDict(listArg):
    """Creating dictionary with Letter with frequency"""
    counter = 0
    dictionay = dict({})
    for word in listArg:
        counter += 1
        if word.lower() in dictionay:
            dictionay[word.lower()][0] += 1
            dictionay[word.lower()][1] = 1
        else:
            dictionay[word.lower()] = [1, 0]

    for item in dictionay:
        dictionay[item.lower()][1] = round(
            (dictionay[item.lower()][0]/counter)*100, 1)
    return dictionay

def SortList(listArg):
    """Returns sorted list value > key"""
    return sorted(listArg.items(), key=lambda x: (x[1], x[0]), reverse=True)
