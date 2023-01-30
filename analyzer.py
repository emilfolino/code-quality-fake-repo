"""Functions for the analyzer program."""

def lines(filename):
    '''Counts the number of lines in a textfile.'''
    with open(filename) as filehandle:
        contentLines = filehandle.readlines()
    numberOfLines = len(contentLines)
    return numberOfLines

def create_word_list(filename):
    '''Creates a lowercase list of all words in a textfile'''
    with open(filename) as filehandle:
        content = filehandle.read()

    content = content.replace("\n", " ")
    content = content.replace(".", "")
    content = content.replace(",", "")
    wordList = content.split(" ")
    for i, _ in enumerate(wordList):
        wordList[i] = wordList[i].lower()
    return wordList

def create_letter_list(filename):
    '''Creates a lowercase list of all letters in a textfile.'''
    with open(filename) as filehandle:
        content = filehandle.read()

    # Remove newlines.
    content = content.replace("\n","")
    # Remove spaces, periods, commas.
    content = content.replace(" ","")
    content = content.replace(".","")
    content = content.replace(",","")
    content = content.replace("-","")
    content = content.lower()
    letterList = list(content)
    return letterList

def words(filename):
    '''Counts the number of words in a textfile.'''
    numberOfWords = len(create_word_list(filename))
    return numberOfWords

def letters(filename):
    '''Counts the number of letter (a-z) in a textfile.'''
    letterList = create_letter_list(filename)
    numberOfLetters = len(letterList)
    return numberOfLetters

def word_frequency(filename):
    '''Counts the frequency of words in file, and returns the top 7.'''
    wordList = create_word_list(filename)
    wordList.sort()
    wordFrequencyDict = calculate_frequency(wordList)
    print_frequency(wordFrequencyDict, 7, words(filename))

def letter_frequency(filename):
    '''Counts the frequency of letters in file, and returns the top 7.'''
    letterList = create_letter_list(filename)
    letterList.sort()
    letterFrequencyDict = calculate_frequency(letterList)
    print_frequency(letterFrequencyDict, 7, letters(filename))

def calculate_frequency(sortedListOfItems):
    '''Create a dictionary with every word or letter + its count as a value.'''
    wordCount = 0 
    currentWord = sortedListOfItems[0]
    resultDict = {}
    loopCount = 0
    for word in sortedListOfItems:
        loopCount += 1
        # Checks if it's the last word - if so adds it. Otherwise it's added in the next loop.
        if loopCount == len(sortedListOfItems):
            if word == currentWord:
                wordCount += 1  
                resultDict[currentWord] = wordCount
            else:
                resultDict[currentWord] = wordCount
                resultDict[word] = 1
        else:
            if word == currentWord:
                wordCount += 1            
            else:  
                resultDict[currentWord] = wordCount
                currentWord = word
                wordCount = 1
    
    
    sortedByValue = {k: v for k, v in sorted(resultDict.items(), key=lambda x: x[1])}
    return sortedByValue

def print_frequency(frequencyDict, amount, totalwords):
    '''Prints a dictionary of the frequency of words or letters'''
    frequencyList = list(frequencyDict.items())
    for i in range(1,amount+1):
        word = frequencyList[-i][0]
        count = frequencyList[-i][1]
        percentage = round(count / totalwords * 100,1)
        print(word + ": " + str(count) + " | " + str(percentage) + "%")

def print_all(filename):
    '''Prints the result of every other option'''
    print(lines(filename))
    print(words(filename))
    print(letters(filename))
    word_frequency(filename)
    letter_frequency(filename)
