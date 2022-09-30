"""Module that holds all the functions that analyze a text"""
name = "phil.txt"

def readText():
    """Reads the text"""
    with open(name) as f:
        text = f.read()
    return text

def correctText(text):
    """Gets rid of all unwanted characters"""
    text = text.replace("\n", " ")
    text = text.replace(",", "")
    text = text.replace(".", "")
    text = text.lower()
    return text

def lines():
    """Counts the number of lines in a text file"""
    with open(name) as f:
        lineList = f.readlines()
    for i in lineList:
        i.rstrip("\n")
        if i == "":
            lineList.remove(i)
    return len(lineList)

def words():
    """Counts the number of words in a text file"""
    text = readText()
    text = text.replace("\n", " ")
    wordList = text.split()
    wordCount = len(wordList)
    return wordCount

def letters():
    """Counts the number of letters in a text file"""
    letterCount = 0
    for letter in readText():
        if letter.isalpha():
            letterCount += 1
    return(letterCount)

def freq(stri):
    """Counts the frequency of letters or words"""
    returnDict = {}
    if len(stri.split()) <= 1:
        letterList = list(stri)
        existingLetters = []

        for i in letterList:
            if i not in existingLetters:
                existingLetters.append(i)
        for i, _ in enumerate(existingLetters):
            total = letters()
            percentage = round((letterList.count(existingLetters[i]) / total) * 100, 1)
            returnDict[existingLetters[i]] = [letterList.count(existingLetters[i]), percentage]
    else:
        wordList = stri.split()
        existingWords = []
        total = 0
        for i in wordList:
            if i not in existingWords:
                existingWords.append(i)
        for i, _ in enumerate(existingWords):
            total = words()
            percentage = round((wordList.count(existingWords[i]) / total) * 100, 1)
            returnDict[existingWords[i]] = [wordList.count(existingWords[i]), percentage]
    return returnDict

def word_frequency():
    """prints the frequency of words"""
    frequency = freq(correctText(readText()))
    frequency = sorted(frequency.items(), key=lambda item: (item[1][0], item[0]), reverse=True)
    for key, value in frequency[0:7]:
        print(f"{key}: {value[0]} | {value[1]}%")

def letter_frequency():
    """prints the frequency of letters"""
    text = correctText(readText())
    Lstr = ""
    splittext = "".join(text.split())
    for letter in splittext:
        Lstr += letter
    #print(Lstr)
    frequency = freq(Lstr)
    #print(frequency)
    frequency = sorted(frequency.items(), key=lambda item: (item[1][0], item[0]), reverse=True)
    for key, value in frequency[0:7]:
        print(f"{key}: {value[0]} | {value[1]}%")

def all_functions():
    """uses all functions"""
    print(lines())
    print(words())
    print(letters())
    word_frequency()
    letter_frequency()

def change(fileName):
    """Changes the filename"""
    global name
    name = fileName
