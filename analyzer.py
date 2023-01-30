#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Contains all funtionality for analyzing the files..
"""

def lines(filename):
    """
    Counts the number of lines in the file.
    """

    with open(filename) as fhand:
        line_count = 0
        for line in fhand:
            if line != "\n":
                line_count += 1

    return line_count

def words(filename):
    """
    Counts the number of words in the file.
    """

    with open(filename) as fhand:
        file = fhand.read()
        file = file.split()
        word_count = len(file)

    return word_count

def letters(filename):
    """
    Counts the number of letters in the file.
    """
    file_as_chr = ""
    with open(filename) as fhand:
        file = fhand.read()
        file = "".join(file.split())
        for letter in file:
            if letter.isalpha():
                file_as_chr += letter
        letter_count = len(file_as_chr)

    return letter_count

def word_frequency(filename):
    """
    Checks the frequency of words and compare it to the total number of words.
    """
    frequency_of_words = {}
    with open(filename) as fhand:
        file = fhand.read()
        file = file.split()
        
        for word in file:
            word = word.strip(".,").lower()
            if word not in frequency_of_words:
                frequency_of_words[word] = 0
            frequency_of_words[word] += 1
    
    nr_of_words = words(filename)
    
    words_sorted_by_value = sorted(frequency_of_words.items(), key=lambda x: (x[1], x[0]), reverse=True)
    
    print_frequency(words_sorted_by_value, nr_of_words)

def letter_frequency(filename):
    """
    Checks the frequency of letters and compare it to the total number of words.
    """
    frequency_of_letters = {}
    with open(filename) as fhand:
        file = fhand.read()
        file = "".join(file.split()).lower()
        for letter in file:
            if not letter.isalpha():
                continue
            if letter not in frequency_of_letters:
                frequency_of_letters[letter] = 0
            frequency_of_letters[letter] += 1
    
    nr_of_letters = letters(filename)
    
    letters_sorted_by_value = sorted(frequency_of_letters.items(), key=lambda x: (x[1], x[0]), reverse=True)
    
    print_frequency(letters_sorted_by_value, nr_of_letters)

def print_frequency(tuplesorted_by_value, total_number_of):
    """
    Prints the 7 most frequent used from tuple
    """
    
    counter = 0
    for key, value in tuplesorted_by_value:
        percent = round((value / total_number_of) * 100, 1)
        print("{0}: {1} | {2}%".format(key, value, percent))
        if counter >= 6:
            break
        counter += 1
