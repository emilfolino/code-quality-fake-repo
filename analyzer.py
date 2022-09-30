"""
Here are all the methods for analyzing text.
"""

from operator import itemgetter

def change(file):
    """
    allows the user to change the file to be analysed
    """
    print("\nWhat file would you like to analyse?")
    userInput = input("--> ")
    try:
        with open(userInput) as filehandle:
            filehandle.close()
        file = userInput
    except FileNotFoundError:
        print("The file was not found. No changes have been saved.")
        print("The currently active file is {}".format(file))
    return file

def getString(file):
    """
    returns the file as a lowercase string with no line breaks
    """
    with open(file) as filehandle:
        content = filehandle.read() # save the content as a string
    
    contentLower = content.lower() # change the content to lowercase
    contentLower = contentLower.replace("\n", " ") # replace line breaks with spaces
    return contentLower

def spacesAndLetters(file):
    """
    returns the file as a lowercase string with just spaces and letters (no punctuation)
    """
    contentLower = getString(file)
    for char in contentLower:
        if char not in "qwertyuiopasdfghjklzxcvbnm ":
            contentLower = contentLower.replace(char, "") 
            # remove anything that's not a letter or a space
    return contentLower

def lettersOnly(file):
    """
    returns a string that contains only the letters, no spaces, no punctuation
    """
    strippedContent = spacesAndLetters(file) # a string with only spaces and letters
    strippedContent = strippedContent.replace(" ","") # remove all spaces
    return strippedContent

def lines(file):
    """
    returns the number of non-empty lines in the file
    """
    lines_count = 0
    with open(file) as filehandle:
        for line in filehandle:
            if line != "\n":
                lines_count += 1
    print(str(lines_count))
    return lines_count

def wordList(file):
    """
    returns a list with all the words
    """
    strippedContent = spacesAndLetters(file) # get a string with just spaces and letters
    listOfWords = strippedContent.split(" ") # turn the string into a list of words
    return listOfWords

def words(file):
    """
    returns the number of words in the file
    """
    listOfWords = wordList(file) # get all the words as a list
    numberOfWords = len(listOfWords)
    return numberOfWords

def letters(file):
    """
    returns the number of letters in the file
    """
    lettersString = lettersOnly(file)
    print(len(lettersString))
    return len(lettersString)

def sevenMostFrequent(listOfItems):
    """
    takes a list of items and returns a list of items sorted by occurrences
    """
    listOfItems.sort(reverse=True)
    dictionary = { listOfItems[0] : 1} 
    # create a dictionary where keys are words/letters and values are how many times they appear
    # add the first word/letter (counting only the first appearance)
    for i, element in enumerate(listOfItems):
        if i > 0: # we've already added the first word
            if listOfItems[i] == listOfItems[i-1]: # if the word is the same as the previous
                dictionary[element] += 1 # add one to the value
            else: # if it is a new word
                dictionary[element] = 1 # add it to the list with value 1
    dictAsList = dictionary.items() # make a list from the dictionary
    sorted_by_occurences = sorted(dictAsList, key=itemgetter(1), reverse=True) # sort by value
    return sorted_by_occurences

def word_frequency(file):
    """
    displays the 7 most frequently occurring words
    """
    listOfWords = wordList(file) # get all the words as a list
    byOccurences = sevenMostFrequent(listOfWords) # get words sorted by occurrences
    totalWords = words(file) # get total words
    for i, element in enumerate(byOccurences): 
        if i <= 6:
            print("{}: {} | {}%"
            .format(element[0], element[1], round(((element[1]/totalWords)*100),1)))

def letter_frequency(file):
    """
    displays the 7 most frequently used letters
    """
    allLetters = lettersOnly(file)
    listOfLetters = list(allLetters)
    byOccurences = sevenMostFrequent(listOfLetters) # get letters sorted by occurrences
    totalLetters = len(lettersOnly(file)) # get total letters
    for i, element in enumerate(byOccurences): 
        if i <= 6:
            print("{}: {} | {}%"
            .format(element[0], element[1], round(((element[1]/totalLetters)*100),1)))

def everything(file):
    """
    displays all the information together
    """
    lines(file)
    print(words(file))
    letters(file)
    word_frequency(file)
    letter_frequency(file)
