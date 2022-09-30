"""Worker code for analyzer"""
import os


def lines(file="phil.txt"):
    """Counts lines"""
    return len(getFile(file).split("\n"))


def words(file="phil.txt"):
    """Counts words"""
    data = getFile(file)
    fileWords = data.split()
    return len(fileWords)


def letters(file="phil.txt"):
    """Counts letters"""
    data = getFile(file)
    letterList = list(data)
    letterList = list(filter(lambda x: x.isalpha(), letterList))
    return len(letterList)


def word_frequency(file="phil.txt"):
    """word_frequency"""
    wordList = getFile(file).split()
    parsedData = freq(wordList)
    sortedDict = sorted(parsedData.items(), reverse=True,
                        key=lambda t: t[::-1])
    outString = ""
    for entry in sortedDict[:7]:
        amount = sortedDict[sortedDict.index(entry)][1]
        precent = round((amount/len(wordList)*100),1)
        outString += f"{entry[0]}: {amount} | {precent}%\n"
    return outString


def letter_frequency(file="phil.txt"):
    """letter_frequency"""
    data = getFile(file)
    letterList = list(data)
    letterList = list(filter(lambda x: x.isalpha(), letterList))
    parsedData = freq(letterList)
    sortedDict = sorted(parsedData.items(), reverse=True,
                        key=lambda t: t[::-1])
    outString = ""
    for entry in sortedDict[:7]:
        amount = sortedDict[sortedDict.index(entry)][1]
        precent = round((amount/len(letterList)*100),1)
        outString += f"{entry[0]}: {amount} | {precent}%\n"
    return outString


def getFile(name):
    """Reads file content"""
    pwd = os.path.dirname(os.path.abspath(__file__))
    with open(pwd + "/" + name, "r") as file:
        return file.read()


def freq(_list):
    """Makes a dict of data"""
    out = {}
    for _item in _list:
        item = _item.lower().replace(",","").replace(".","").replace(":","")
        try:
            out[item] += 1
        except KeyError:
            out[item] = 1
    return out
