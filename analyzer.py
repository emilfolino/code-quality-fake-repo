#!/usr/bin/env python3

"""
Functions for text analyzer
"""

def get_lines(file_name):
    """
    Get non-empty lines from a file
    """
    with open(file_name, "r") as file:
        lines = file.read().split("\n")
    while "" in lines:
        lines.remove("")
    return lines

def count_lines(file_name):
    """
    Counts number of lines in a file
    """
    return len(get_lines(file_name))

def count_words(file_name):
    """
    Counts number of words in a file
    """
    lines = get_lines(file_name)
    words = []
    for line in lines:
        words[:0] = line.split(" ")
    return len(words)

def count_letters(file_name):
    """
    Counts number of letters in a file
    """
    with open(file_name, "r") as file:
        string = file.read().lower()
    letters = 0
    for character in string:
        if character in "abcdefghijklmnopqrstuvwxyz":
            letters += 1
    return letters

def item_value(item):
    """
    Calculates the value an item should have when sorted
    """
    value = list("0" * 99)
    item_number = list(str(item[1]))
    value[-len(item_number):] = item_number
    value.append(item[0])
    return "".join(value)

def seven_most_frequent(dictionary, total):
    """
    Sorts dictionary and returns string with 7 most frequent items
    """
    items = []
    for index, item in enumerate(sorted(dictionary.items(), key = item_value, reverse = True)):
        if index > 6:
            break
        items.append(f"{item[0]}: {item[1]} | {round((item[1] / total) * 100, 1)}%")
    return "\n".join(items)

def frequent_words(file_name):
    """
    Get the 7 most frequent words in a file
    """
    lines = get_lines(file_name)
    word_list = []
    for line in lines:
        word_list[:0] = line.split(" ")
    words = {}
    for word in word_list:
        word = word.lower().strip(".,")
        if word in words:
            words[word] += 1
        else:
            words[word] = 1
    return seven_most_frequent(words, len(word_list))

def frequent_letters(file_name):
    """
    Get the 7 most frequent letters in a file
    """
    with open(file_name, "r") as file:
        string = file.read().lower()
    letters = {}
    letter_count = 0
    for character in string:
        if character in "abcdefghijklmnopqrstuvwxyz":
            letter_count += 1
            if character in letters:
                letters[character] += 1
            else:
                letters[character] = 1
    return seven_most_frequent(letters, letter_count)
