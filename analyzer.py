"""
Functions for analyze text
"""

from operator import itemgetter

def lines(content):
    """
    get amount of lines
    """
    return len(content)

def words(content):
    """
    Get amount of words
    """
    count = 0
    temp = []
    for e in content:
        temp = e.split()
        count += len(temp)
    return count

def letters(content):
    """
    Get amount of letters
    """
    count = 0
    for e in content:
        for c in e:
            if c.lower() in "abcdefghijklmnopqrstuvwxyz":
                count += 1
    return count

def frequency(d, total):
    """
    Get frequency
    """
    count = 0
    for key, value in d.items():
        if count < 7:
            percentage = round(value/total*100, 1)
            print(key + ": " + str(value) + " | " + str(percentage) + "%")
            count += 1

def sort_dict(d):
    """
    Sort dictionary by key in decending order then by value
    """
    sorted_dict = sorted(d.items(), reverse=True)
    return sorted(sorted_dict, key=itemgetter(1), reverse=True)

def list_to_dict(l):
    """
    Convert list to dictionary
    """
    temp = {}
    for e in l:
        temp[e[0]] = e[1] 
    return temp
        

def word_frequency(content):
    """
    Get frequency of the 7 most used words
    """
    common_words = {}
    temp = []
    for e in content:
        temp = e.split()
        for word in temp:
            if word[-1] not in "abcdefghijklmnopqrstuvwxyz":
                word = word[:-1]
            if word.lower() in common_words:
                common_words[word.lower()] += 1
            else:
                common_words[word.lower()] = 1
    sorted_words = sort_dict(common_words)
    common_words = list_to_dict(sorted_words)
    frequency(common_words, words(content))

def letter_frequency(content):
    """
    Get frequency of the 7 most used letters
    """
    common_letters = {}
    for e in content:
        for c in e:
            if c.lower() in "abcdefghijklmnopqrstuvwxyz":
                if c.lower() in common_letters:
                    common_letters[c.lower()] += 1
                else:
                    common_letters[c.lower()] = 1
    sorted_letters = sort_dict(common_letters)
    common_letters = list_to_dict(sorted_letters)
    frequency(common_letters, letters(content))

def show_all(content):
    """
    Runs all functions
    """
    print(lines(content))
    print(words(content))
    print(letters(content))
    word_frequency(content)
    letter_frequency(content)

def change():
    """
    Change file to read from
    """
    new_file = input("Enter filename: ")
    return new_file
