#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Functions for analyzer program
"""
def count_lines(filename):
    """
    counts number of lines in given text file
    """
    with open(filename, "r") as f:
        lines = f.readlines()
        return len(lines)

def word_count(filename):
    """
    Counts number of words in a given text file
    """
    with open(filename, "r") as f:
        data = f.read()
        words = len(data.split())
        return words

def letter_count(filename, space = True):
    """
    Counts number of letters in a given text file
    """
    with open(filename, "r") as f:
        data = f.read().replace("\n", " ").lower()
        letters = ""
        invalid_characters = ['.', ',', '-']

        if space:
            invalid_characters.append(' ')

        for char in data:
            if char not in invalid_characters:
                letters = letters + char
        return letters


def prepare_string(top_items, item_dictionary):
    """
    Prepares a string for output
    """
    top_seven = top_items
    sorted_dict = item_dictionary

    output_string = ""

    for item in top_seven:
        output_string = output_string + f"{item}: {sorted_dict[item][0]} | {sorted_dict[item][1]}%\n"
    return output_string

def count_unique(items, sorted_list, no_of_items):
    """
    Counts number of unique items in a list
    """
    item_dict = {}
    for unique in sorted_list:
        counter = 0
        for item in items:
            if item == unique:
                counter += 1
        item_dict[unique] = (counter, round(((counter / no_of_items) * 100), 1))
    sorted_dict = dict(sorted(item_dict.items(), key=lambda item: item[1], reverse=True))
    return sorted_dict

def unique_list(items):
    """
    Creates a list without duplicates
    """
    item_list = []
    for item in items:
        if item not in item_list:
            item_list.append(item)
    return item_list

def word_frequency(filename):
    """
    Returns the most frequently used words
    """
    words = list(letter_count(filename, False).split(" "))
    no_of_words = len(words)

    word_list = unique_list(words)

    sorted_word_list = sorted(word_list, reverse=True)

    # sorts dictionary by letter frequency
    sorted_dict = count_unique(words, sorted_word_list, no_of_words)


    # retrieves top seven words from the sorted dictionary

    top_seven = list(sorted_dict)[:7]

    return prepare_string(top_seven, sorted_dict)

def letter_frequency(filename):
    """
    Returns the most frequenly used letters
    """
    letters = list(letter_count(filename))
    no_of_letters = len(letters)

    letter_list = unique_list(letters)

    sorted_letter_list = sorted(letter_list, reverse=True)

    sorted_dict = count_unique(letters, sorted_letter_list, no_of_letters)

    top_seven = list(sorted_dict)[:7]

    return prepare_string(top_seven, sorted_dict)

def all_functions(filename):
    """
    Returns all analyze functions
    """
    print_dict = {}

    print_dict[0] = count_lines(filename)
    print_dict[1] = word_count(filename)
    print_dict[2] = len(letter_count(filename))
    print_dict[3] = word_frequency(filename)
    print_dict[4] = letter_frequency(filename)

    for item in print_dict.items():
        print(item[1])

def change():
    """
    Changes the text file that the program analyzes
    """
    user_input = input("File path for the text that you want to analyze: ")
    change_text = "text/" + user_input
    return change_text
