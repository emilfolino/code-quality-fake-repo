#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Analyzer functions
"""

def lines(file):
    """Returns number of lines of the content in a text file"""
    counter = 0
    with open(file) as fhand:
        for line in fhand:
            if line != "":
                counter += 1
    return counter                

def words(file):
    """Returns number of words of the content in a text file"""
    with open(file) as fhand:
        content = fhand.readlines() # ger array

        all_words = 0
        for line in content:
            word = len(line.split(" "))
            all_words += word
        return all_words

def letters(file):
    """Returns number of letters of the content in a text file"""
    with open(file) as fhand:
        content = fhand.readlines() # ger array med en hel rad som element

    total_length = 0
    for line in content:
        for letter in line:
            if (letter.isalpha()):
                total_length += len(letter)

    return total_length


def word_frequency(file):
    """Prints word frequencies of the content in a text file"""
    with open(file) as fhand:
        data_list = fhand.readlines() # array med varje rad som ett element

    all_words = []
    for line in data_list: # line är en sträng
        line = line.split(" ") # line är en list
        for word in line:
            word = word.replace(",", "")
            word = word.replace(".", "")
            all_words.append(word.strip().lower())

    word_dict = {}
    counter = 1
    for word in all_words:
        if (word not in word_dict):
            word_dict[word] = counter
        else:
            word_dict[word] += 1

    #Sortera word_dict
    word_dict_sorted = dict(sorted(word_dict.items(), key=lambda item: (item[1], item[0]), reverse=True))

    word_counter = 0
    for key, value in word_dict_sorted.items():
        print(key + ": " + str(value) + " | " + str(round((value/len(all_words)*100), 1)) + "%")
        word_counter += 1
        if (word_counter == 7):
            break

def letter_frequency(file):
    """Prints letter frequencies of the content in a text file"""
    letter_dict = {}
    counter = 1
    with open(file) as fhand:
        data_list = fhand.readlines() # array med varje rad som ett element

    letter_counter = 0
    for line in data_list: # line är en sträng
        for letter in line:
            if (letter.isalpha()):
                letter_counter += 1
                if (letter.lower() not in letter_dict):
                    letter_dict[letter.lower()] = counter
                else:
                    letter_dict[letter.lower()] += 1

    #Sortera letter_dict
    letter_dict_sorted = dict(sorted(letter_dict.items(), key=lambda item: (item[1], item[0]), reverse=True))

    counter = 0
    for key, value in letter_dict_sorted.items():
        print(key + ": " + str(value) + " | " + str(round((value/letter_counter*100), 1)) + "%")
        counter += 1
        if (counter == 7):
            break

def all_functions(file):
    """Performs all functions in the analyzer meny"""
    print(lines(file))
    print(words(file))
    print(letters(file))
    word_frequency(file)
    letter_frequency(file)

def change(file):
    """Changes text file to use in all analyzer functions"""
    inp = input("Which file should I use instead? ")
    try: # Om kraschar används inte nästa kodrad
        with open(inp):
            print("I now use the file " + inp + ".")
            return inp
    except FileNotFoundError:
        print("File is not changed. Could not find file: " + inp + "." )
        return file
