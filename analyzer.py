#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""File analyzer methods"""


########################################################
####                 Helper functions               ####
########################################################

def open_readlines(filename):
    """
    Opens the file in readmode and uses readlines to return file contents
    in a list
    """

    with open(filename, "r") as fd:

        return fd.readlines()


def open_read(filename):
    """Opens the file in readmode and returns the content in a string"""

    with open(filename, "r") as fd:

        return fd.read()


def words_to_list(content_string):
    """Returns input as words in a list, removes all non-letter chars"""

    content_list = [char for char in content_string]
    word_list = []
    word = ""
    compare = "abcdefghijklmnopqrstuvwxyz-"

    for i, char in enumerate(content_list):

        if char.lower() in compare:

            word += char

            if i == len(content_list) - 1:

                word_list.append(word)

        elif len(word) > 0:

            word_list.append(word)
            word = ""

    return word_list


def letters_to_list(content_string):
    """Returns a list of all the letters in the file"""

    compare = "abcdefghijklmnopqrstuvwxyz"
    letter_list = [char for char in content_string if char.lower() in compare]

    return letter_list


def times_in_list(item_list, check_item):
    """Finds and returns the number of times an item occurs in a list"""

    counter = 0

    for item in item_list:

        if item.lower() == check_item.lower():

            counter += 1

    return counter


def frequency(item_list):
    """
    Returns a dict with number of times an item occurs in a list
    Sorted by value as primary sort parameter and key as secondary
    Sorts in descending order
    """

    dataset = {}

    for item in item_list:

        if item.lower() not in dataset.keys():

            dataset[item.lower()] = times_in_list(item_list, item)

    return sorted(
        dataset.items(), key=lambda i: (i[1], i[0]), reverse=True)


########################################################
####              Main program functions            ####
########################################################


def count_lines(filename):
    """Returns the number of lines in a file"""

    content_list = open_readlines(filename)

    return len(content_list)


def count_words(filename):
    """Returns the number of words in a file"""

    word_list = words_to_list(open_read(filename))

    return len(word_list)


def count_letters(filename):
    """ Returns the number of letters in the file"""

    letter_list = letters_to_list(open_read(filename))

    return len(letter_list)


def word_frequency(filename):
    """Returns a string with the top 7 words lsited"""

    outstring = ""
    dataset = frequency(words_to_list(open_read(filename)))
    num_words = count_words(filename)

    for i in range(7):

        percent = round(dataset[i][1] / num_words * 100, 1)

        if i != 6:

            outstring += f"{dataset[i][0]}: {dataset[i][1]} | {percent}%\n"

        else:

            outstring += f"{dataset[i][0]}: {dataset[i][1]} | {percent}%"

    return outstring


def letter_frequency(filename):
    """Returns a string with the top 7 letters listed"""

    num_letters = count_letters(filename)
    dataset = frequency(letters_to_list(open_read(filename)))
    outstring = ""

    for i in range(7):

        percent = round(dataset[i][1] / num_letters * 100, 1)

        if i != 6:

            outstring += f"{dataset[i][0]}: {dataset[i][1]} | {percent}%\n"

        else:

            outstring += f"{dataset[i][0]}: {dataset[i][1]} | {percent}%"

    return outstring


def all_show(filename):
    """Runs all the analyzing functions and returns the result"""

    num_lines = count_lines(filename)
    num_words = count_words(filename)
    num_letters = count_letters(filename)
    word_freq = word_frequency(filename)
    letter_freq = letter_frequency(filename)

    return (f"{num_lines}\n" +
            f"{num_words}\n" +
            f"{num_letters}\n" +
            f"{word_freq}\n" +
            f"{letter_freq}")
