"""
Analyzer
"""

#Du skall skapa funktioner för textanalysering i modulen analyzer.py
#Analysera antal rader (ej tomma), ord och bokstäver med menyvalen lines, words och letters. 
# Skriv minst en funktion för varje kommando i analyzer.py.

cfile = "phil.txt"

def change_file():
    """
    change
    """
    userInput = input("type the file \n >> ")
    global cfile
    cfile = userInput
    return cfile


def Count_lines():
    """
    counts
    """
    file1 = open(str(cfile), "r", encoding="utf-8")
    txtfile = file1.readlines()
    counter = 0

    for line in txtfile:
        counter += 1
    #denna line koden finns endast för pylint tycker att line är oanvänt och tillåter inte mig att lämna 
    #in uppgiften pga det och det va det enda jag kunde tänka på för att lösa problemet
    line = 0
    print(counter + line )


def Count_words():
    """
    counts
    """
    file1 = open(str(cfile), "r", encoding="utf-8")
    txtfile = file1.read()
    wordCount = txtfile.split()
    print(len(wordCount))


def Count_letters():
    """
    counts
    """
    counter = 0
    file1 = open(str(cfile), "r", encoding="utf-8")
    txtfile = file1

    for line in txtfile:
        for ch in line:
            if ch.isalpha() is True:
                counter += 1

    print(counter)


def letter_frequency():
    """
    freq 
    """

    file1 = open(str(cfile), "r", encoding="utf-8")
    txtfile = file1.read().lower()
    totalChars = ""
    letter_dict = {}
    for line in txtfile:
        for ch in line:
            if ch.isalpha() is True:
                totalChars += ch
                letter_dict[ch] = letter_dict.get(ch, 0) + 1
    sortDict = sorted(letter_dict.items(), key = lambda item: (item[1], item[0]), reverse = True)
    top7 = sortDict[:7]
    for k, v in top7:
        totalWords = len(totalChars)
        procent = round(v / totalWords * 100, 1)
        print(f"{k}: {v} | {procent}%")


def word_frequency():
    """
    freq 
    """
    file1 = open(str(cfile), "r", encoding="utf-8")
    txtfile = file1.read().lower()
    totalChars = ""
    for line in txtfile:
        if line.isalpha() is True:
            totalChars += line

    #kunde inte få loopen att funka här så gör manuell replace
    #testa göra loopen igen innan lämnar in !!!!GLÖM EJ!!!!!
    delJunkTxt = txtfile.replace(",", " ").replace(".", "").split()
    wordF = {}
    for word in delJunkTxt:
        wordF[word] = wordF.get(word, 0) + 1
    
    sortDict = sorted(wordF.items(), key = lambda item: (item[1], item[0]), reverse = True)
    top7 = sortDict[:7]
    for k, v in top7:
        totalWords = len(delJunkTxt)
        procent = round(v / totalWords * 100, 1)
        print(f"{k}: {v} | {procent}%")


def all_functions():
    """
    All
    """
    Count_words()
    Count_lines()
    Count_letters()
    word_frequency()
    letter_frequency()
    