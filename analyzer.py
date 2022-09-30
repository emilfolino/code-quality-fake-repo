"""
Analyzer Function
"""

PhilText = 'phil.txt'
LoremText = 'lorum.txt'


FileName = PhilText

def ChangeFile(Name):
    """
    ChangeFile Function
    """
    global FileName
    FileName  = Name

def LineCount ():
    """
    Counting Lines In TextFile
    """
    with open(FileName, 'r') as Lines:
        print(len(Lines.readlines()))

def WordCount():
    """
    Counting Words In A TextFile
    """
    
    with open(FileName, 'r') as Words:
        data = Words.read()
        words = data.split()
    print(len(words))

def LetterCount ():
    """
    Counting Letters In A TextFile
    """
    count = 0
    
    with open(FileName, "r") as Letters:
        for char in Letters.read():
            if (char.isalpha()):
                count += 1
    print(count)


def letter_frequency ():
    """
    Counting Letter Frequency In A TextFile
    """
    
    counts = {}
    nums = 0
    with open(FileName, "r") as LetterFreq:
        LetterFreq = LetterFreq.read()
        
        # beräkna bokstäver totalt
        TotalLetterCount = sum([char.isalpha() for char in LetterFreq])
        

        for name in LetterFreq:
            counts[name.lower()] = counts.get(name.lower(), 0) + 1

        SortLetters = sorted(counts.items(), key=lambda x: (x[1], x[0]), reverse=True)
        for _, value in enumerate(SortLetters):
            if (not value[0].isalpha() or nums > 6):
                continue
            print(f"{value[0]}: {value[1]} |{value[1] / TotalLetterCount * 100: .1f}%")
            nums += 1


def word_frequency ():
    """
    Counting Words Frequency In A TextFile
    """
    counts = {}
    nums = 0
    
    
    with open(FileName, "r") as WordFreq:
        WordCounting = "".join(WordFreq.readlines())
        WordCounting = WordCounting.split()
        l_out = [''.join(e for e in string if e.isalnum()) for string in WordCounting]

        WordCounting = l_out 
        for word in WordCounting:
            counts[word.lower()] = counts.get(word.lower(), 0) + 1

        TotalWordcount = len(l_out)

        SortWords = sorted(counts.items(), key=lambda x: (x[1], x[0]), reverse=True)
        for _, value in enumerate(SortWords):
            if(not value[0].isalnum() or nums > 6):
                continue
            print(f"{value[0]}: {value[1]} |{value[1] / TotalWordcount * 100: .1f}%")
            nums += 1

def AllData():
    """
    Prints All Information
    """
    return LineCount(), WordCount(), LetterCount(), word_frequency(), letter_frequency()
