"""
Functions for text analyzis
"""

def openFile(file):
    """
    Reads file
    """
    with open(file, "r" , encoding="UTF-8") as theFile:
        item = theFile.readlines()
    return item

def cleanWords(base):
    """
    Clean from not-letters
    """
    base = " ".join(base)
    clean = ""
    for letter in base:
        if letter.isalnum() or letter.isspace():
            clean = clean + letter.strip("\n")
    return clean

def countLines(item):
    """
    Counts how many lines
    """
    count = 0
    for row in item:
        if row == "\n":
            count = count + 1
    return len(item) - count

def countWords(item):
    """
    Counts how many words
    """
    item = cleanWords(item)
    item = item.split(" ")
    return len(item)

def countLetters(item):
    """
    Counts how many letters
    """
    item = cleanWords(item)
    item = item.replace(" ", "")
    return len(item)

def frequency(item, total): #give string of words/letters and totalWords/Letters
    """
    Calculates the frequency of something
    """
    counter = {}
    output = ""
    #make a dictionary with the item and amount of times it appears
    for wl in item: #wl = word/letter
        if wl.lower() not in counter:
            counter[wl.lower()] = 1
        elif wl.lower() in counter:
            counter[wl.lower()] = int(counter[wl.lower()]) + 1
    sortedDict = sorted(counter.items(), key=lambda x: x[1], reverse=True)
    sortedDict = sortedDict[:7] #the 7 rows
    for i in sortedDict: #figure out percentage and the string
        wl = i[0] #new word/letter
        amount = i[1] #amount of times it appears
        percentage = round(amount / total * 100, 1) #calc percentage
        output = output + wl + ": " + str(amount) + " | " + str(percentage) + "%\n"
    return output

def wordFrequency(file):
    """
    Calculates the frequency of words
    """
    words = cleanWords(file)
    words = words.lower()
    words = words.split(" ")
    words = sorted(words, reverse=True)
    totalWords = countWords(file)
    output = frequency(words, totalWords)
    return output

def letterFrequency(file):
    """
    Calculates the frequency of letters
    """
    letters = cleanWords(file)
    letters = letters.replace(" ", "")
    letters = sorted(letters)
    totalLetters = countLetters(file)
    output = frequency(letters, totalLetters)
    return output

def runAll(file):
    """
    Runs all analyzing functions
    """
    print(countLines(file))
    print(countWords(file))
    print(countLetters(file))
    print(wordFrequency(file))
    print(letterFrequency(file))
