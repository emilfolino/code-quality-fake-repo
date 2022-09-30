"""
This module contains functions for analyzing text.
"""


current_file = "phil.txt"

def swapfile():
    """
    Swaps the file that is being analyzed
    """
    global current_file
    current_file = input("What file would you want to swap to?")

def countLines():
    """
    counts lines in current file
    """
    with open(current_file) as file:
        text = file.read().split("\n")
    count = 0
    for line in text:
        if line != "":
            count += 1
    return count

def countWords():
    """
    counts words in current file
    """
    with open(current_file) as file:
        text = file.read().split("\n")
    count = 0
    for line in text:
        for _ in line.split(" "):
            count +=1
    return count

def countLetters():
    """
    counts letters in current file
    """
    with open(current_file) as file:
        text = file.read().split("\n")
    count = 0
    for line in text:
        for letter in line:
            if letter.isalpha():
                count +=1
    return count

def wordAnalyzer():
    """
    analyzes word frequency
    """
    with open(current_file) as file:
        text = file.read().split("\n")
    words = {}
    for word in " ".join(text).replace(",", "").replace(".", "").lower().split(" "):
        if word in words:
            words[word] += 1
        else:
            words[word] = 1
    words = dict(sorted(words.items(), key=lambda item: (item[1], item[0]), reverse = True))
    wordCount = countWords()
    for i in range(0,7):
        print(f"{list(words.keys())[i]}: {list(words.values())[i]} | {round(list(words.values())[i]/wordCount*100,1)}%")

def letterAnalyzer():
    """
    analyzes word frequency
    """
    with open(current_file) as file:
        text = file.read().split("\n")
    letters = {}
    for letter in " ".join(text).replace(",", "").replace(".", "").replace(" ", "").lower():
        if letter in letters:
            letters[letter] += 1
        else:
            letters[letter] = 1
    letters = dict(sorted(letters.items(), key=lambda item: (item[1], item[0]), reverse = True))
    letterCount = countLetters()
    for i in range(0,7):
        print(f"{list(letters.keys())[i]}: {list(letters.values())[i]} "+
        f"| {round(list(letters.values())[i]/letterCount*100,1)}%")

def collectAllData():
    """
    collects all data and prints out.
    """
    print(countLines())
    print(countWords())
    print(countLetters())
    wordAnalyzer()
    letterAnalyzer()
