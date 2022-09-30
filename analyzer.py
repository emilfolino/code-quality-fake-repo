"""---"""

def openFile(chosenFile):
    """---"""
    try:
        with open(chosenFile) as cf:
            content = cf.readlines()
            return content
    except FileNotFoundError:
        print("There is no file")
        return False
        

def linesCount(cfile):
    """---"""
    content = openFile(cfile)
    countL = 0

    for line in content:
        if line != "\n":
            countL += 1

    return countL

def wordsCount(cfile):
    """---"""
    content = openFile(cfile)
    countW = 0

    for line in content:
        words = line.split()
        countW += len(words)

    return countW


def lettersCount(cfile):
    """---"""
    content = openFile(cfile)
    char = 0
    for line in content:
        for x in line:
            if x.isalpha():
                char += 1        

    return char

    
def word_frequency(cfile):
    """---"""
    with open(cfile) as cf:
        content = cf.read().lower()
    words = content.replace(",", " ").replace(".", " ").replace("\n", " ").replace("-", " ")
    words = words.split()
    dex = {}
    for word in words:
        dex[word] = dex.get(word, 0) + 1

    list1 = [(v, k) for k, v in dex.items()]

    sortList = list1

    sort = sorted(sortList, key = lambda x: (x[0],x[1]), reverse = True ) 

    for keys, values in sort[:7]:
        tw = len(words)
        percentage = round( keys / tw * 100, 1)
        print_statement =  "{}: {} | {}%".format(values, keys, percentage)
        print(print_statement)

#word_frequency2("lorum.txt")

def letter_frequency(cfile):
    """---"""
    with open(cfile) as cf:
        ltrs = cf.read().lower()
    words = ltrs.replace(",", " ").replace(".", " ").replace("\n", "").replace("-", "")
    dexL = {}

    for ltr in words:
        if ltr.isalpha():  
            dexL[ltr] = dexL.get(ltr, 0) + 1

    sort = sorted(dexL.items(), key = lambda x: x[1], reverse = True)
    
    words = words.replace(" ", "")
    for keys, values in sort[:7]:
        tl = len(words)
        percentage = round( values / tl * 100, 1)
        print_statement =  "{}: {} | {}%".format(keys, values, percentage)
        print(print_statement)


def printAll(cfile):
    """---"""
    print(linesCount(cfile))
    print(wordsCount(cfile))
    print(lettersCount(cfile))
    word_frequency(cfile)
    letter_frequency(cfile)
