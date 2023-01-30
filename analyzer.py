"""
Docstring
"""

from operator import itemgetter


def line_count(doc):
    """
    it opens the file
    for every line in the file
    it increments the linecount and returns it
    """
    with open(doc, 'r') as file:
        lineCount = 0
        for line in file.readlines():
            if line != "\n":
                lineCount += 1
    return lineCount

def words_count(doc):
    """
    it opens the file
    and iterates through each word in file
    and increments the wordcount and returns it
    """
    with open(doc, 'r') as file:
        wordCount = 0
        # textStr = file.read().lower()

        textStr = file.read().lower().rsplit()
        for word in textStr:
            if word.isalpha() or "-" in word or "." in word or "," in word:
                wordCount += 1


        # matchPattern = re.findall(r'\b[a-z-]{1,50}\b', textStr)
        # for word in matchPattern:
        #     wordCount += 1
        
    return wordCount

def letters_count(doc):
    """
    it opens the file
    and iterates through each word in file
    and then each character in each word
    and increments the lettercount and returns it
    """
    with open(doc, 'r') as file:
        letterCount = 0
        words = file.read().rsplit() # list of words/strings
        for word in words:
            for char in word:
                if char.isalpha():
                    letterCount += 1
    return letterCount

            
        
def word_frequency(doc):
    """
    print de 7 mest förekommande orden/bokstäverna
    Creates a new dictionary
    finds all words and for each word, it assigns the number of times
    it exists to its value
    it then sorts the list based on value/also calculates the total number of
    values in the new dictionary to find the word frequency
    """
    wordFreq = {}
    file = open(doc,'r')
    textStr = file.read().lower().rsplit()
    for word in textStr:
        if word.endswith(","):
            wordx = word.replace(",","")
            if wordx.isalpha():
                total = wordFreq.get(wordx, 0)
                wordFreq[wordx] = total + 1
        if word.endswith("."):
            wordx = word.replace(".","")
            if wordx.isalpha():
                total = wordFreq.get(wordx, 0)
                wordFreq[wordx] = total + 1
        if word.isalpha() or "-" in word :
            total = wordFreq.get(word, 0)
            wordFreq[word] = total + 1


    # with open(doc, 'r') as file:
    #     # textStr = file.read().lower()
    #     # matchPattern = re.findall(r'\b[a-z-]{1,50}\b', textStr)
    #     # for word in matchPattern:
    #     #     total = wordFreq.get(word, 0)
    #     #     wordFreq[word] = total + 1
        
        # textStr = file.read().lower().rsplit()
        # for word in textStr:
        #     if word.isalpha() or "-" in word :
        #         word = word.replace(",","")
        #         word = word.replace(".","")
        #         total = wordFreq.get(word, 0)
        #         wordFreq[word] = total + 1

        freqlList = wordFreq.items()
        freqListSorted = sorted(freqlList, key = lambda x:(x[1],x[0]), reverse=True ) #list of tuples
        yCount = 0 
        newDict = dict(freqListSorted) # converted back to dict
        
       
        for y in newDict.values():
            yCount += y
        # for x, y in freqListSorted: 
        #     yCount += y
        listem = []

        for key, val in freqListSorted[:7]:
            listem.append(str(key) + ": " + str(val) + " | " + str(round((val/yCount) * 100,1)) + "%")
        
                
    file.close()
    return listem

    #dicti = {}
    #for key, val in freqListSorted[:7]:
        #dicti[key] = str(val) + " | " + str(round((val/yCount) * 100,1)) + "%"
    

def letter_frequency(doc):
    """
    opens the file
    strips the white character and holds all words in a list
    for each element in the list
    for each letter in each element
    it incremeents the value of each letter (if not found, 0) in the dictionary
    sorts the dictionary based on values
    and for every items (key,val) it appends the key to the list
    and returns the first 7 elements
    """
    letterDict = {}
    with open(doc, 'r') as file:
        words = file.read().lower().rsplit() # list of words/strings [word1, word2, etc]
        for word in words:
            for letter in word:
                total = letterDict.get(letter, 0)
                letterDict[letter] = total + 1
        letterSorted = sorted(letterDict.items(), key=itemgetter(1), reverse=True)
        listem = []
        for key, val in letterSorted[:7]:
            listem.append(str(key) + ": " + str(val) + " | " + str(round((val/letters_count(doc)) * 100,1)) + "%")
    return listem

def allx(doc):
    """
    it calls all defined functions
    and adds their return values as dictionary values
    and prints them
    """
    x = line_count(doc)
    y = words_count(doc)
    z = letters_count(doc)
    h = word_frequency(doc)
    j = letter_frequency(doc)
    dicti = {0:x, 1:y, 2:z, 3:h, 4:j}
    for y in dicti.values():
        print(y)

def change():
    """
    it changes the argument of main function with the input
    """
    newDoc = input("Enter a file name: ")
    return newDoc
