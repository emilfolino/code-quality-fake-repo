"""
All functions for analysing a text file
"""

SELECTED_FILE = "phil.txt"



def createOutput(arg):
    """
    Create an output for word_frequency and letters_frequency functions
    """
    output = ""
    for key, value in arg:
        output += f"\r{key}: {value[0]} | {value[1]}% \n"
    return output


def countPercentage(arg):
    """
    Count the precentage word and letter repeatation (for word_frequency and letters_frequency funcions)
    """
    totalNumber = 0
    for num in arg.values():
        totalNumber += num
    words = []
    for item in arg.items():
        percentageRepeat = item[1] / totalNumber * 100
        percentageRepeat = round( percentageRepeat, 1)
        words.append((item[0], ( item[1] ,percentageRepeat)))
        
    words.sort(key=lambda item: (item[1][0], item[0]), reverse=True)
    return words[0:7]


def readTheFile(readLines=False):
    """
    Read SELECTED_FILE
    """
    with open(SELECTED_FILE, 'r')  as file:
        if not readLines:
            return file.read().strip()
        return file.readlines()

def count_lines():
    """
    Count lines, empty lines aren't included
    """
    lines = readTheFile(readLines=True)
    while '\n' in lines:
        lines.remove('\n')
    return len(lines)

def count_words():
    """
    Count how many words the SELECTED_FILE content contains
    """
    text = readTheFile()
    text = text.replace("\n", " ")
    words = text.split(" ")
    return len(words)

def count_letters():
    """
    Count the number of letters in the SELECTED_FILE
    """
    text = readTheFile()
    countOfLetters = 0
    for letter in text:
        if letter.isalpha():
            countOfLetters += 1
    return countOfLetters

def word_frequency():
    """
    Find Seven most common words in the SELECTED_FILE
    """
    text = readTheFile().lower()
    for char in [',','.','\n']:
        text = text.replace(char, " ")
    words = text.split(" ")
    while '' in words:
        words.remove('')
    validWords = {}
    for word in words:
        if word in validWords:
            validWords[word] += 1
        else:
            validWords[word] = 1
    output = createOutput(countPercentage(validWords))
    return output
    

def letters_frequency():
    """
    Find Seven most common letters in the SELECTED_FILE
    """
    text = readTheFile().lower()
    letters = {}
    for letter in text:
        if letter.isalpha():
            if letter in letters:
                letters[letter] += 1
            else: 
                letters[letter] = 1
    output = createOutput(countPercentage(letters))
    return output


def all_analyses():
    """
    Do all analyses
    """
    output = f"""
    {count_lines()}
    {count_words()}
    {count_letters()}
    {word_frequency()}
    {letters_frequency()}
    """
    return output

def changeSelectedFile(newFile):
    """
    Change SELECTED_FILE to newFile
    """
    global SELECTED_FILE
    try:
        with open(newFile,'r') as file:
            file.read()
        SELECTED_FILE = newFile
        print(f"Now the file is: {SELECTED_FILE}")
    except FileNotFoundError:
        print("File doesn't exist!")
