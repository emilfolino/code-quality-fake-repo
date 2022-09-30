#!/usr/bin/env python3
"""
Functions for text analyzing
"""

def number_of_lines(filename):
    """
    Counts number of lines in text file.
    """
    with open(filename, "r") as filehandle:
        lines = filehandle.readlines()
        num_of_lines = len(lines)
    return num_of_lines

def number_of_words(filename):
    """
    Counts number of words in text file.
    """
    word_count = 0
    with open(filename, "r") as filehandle:
        for words in filehandle:
            word_count += len(words.split())
    return word_count

def number_of_letters(filename):
    """
    Counts number of letters in text file.
    """
    num_of_letters = 0
    with open(filename, "r") as filehandle:
        for line in filehandle:
            letters = [letter if letter.isalpha() else "" for letter in line]
            num_of_letters += len("".join(letters))
    return num_of_letters

def word_frequency(filename):
    """
    Prints 7 most common words in text file and their frequency in number
    and percent.
    """
    with open(filename, "r") as filehandle:
        text = filehandle.read()
    text = text.replace(",", "")
    text = text.replace(".", "")
    text = text.replace("-", "")
    text = text.replace("\n", " ")
    word_count = {}
    for word in text.split():
        low_word = word.lower()
        if low_word in word_count:
            word_count[low_word] += 1
        else:
            word_count[low_word] = 1
    total_words = 0
    ordered_words = []
    for word, number in word_count.items():
        ordered_words.append((number, word))
        total_words += number
    ordered_words.sort(reverse=True)
    for i in range(7):
        number, word = ordered_words[i]
        print(word + ": " + str(number) + " | " + \
            str(round(100*number/total_words,1)) + "%")

def letter_frequency(filename):
    """
    Prints 7 most common letters in text file and their frequency in number
    and percent.
    """
    with open(filename, "r") as filehandle:
        text = filehandle.read()
    letter_count = {}
    for letter in text:
        if letter.isalpha():
            low_letter = letter.lower()
            if low_letter in letter_count:
                letter_count[low_letter] += 1
            else:
                letter_count[low_letter] = 1
    total_letters = 0
    ordered_letters = []
    for letter, number in letter_count.items():
        ordered_letters.append((number, letter))
        total_letters += number
    ordered_letters.sort(reverse=True)
    for i in range(7):
        number, letter = ordered_letters[i]
        print(letter + ": " + str(number) + " | " + \
            str(round(100*number/total_letters,1)) + "%")

def all_funcs(filename):
    """
    Prints all functions in module analyzer.
    """
    print(number_of_lines(filename))
    print(number_of_words(filename))
    print(number_of_letters(filename))
    word_frequency(filename)
    letter_frequency(filename)
