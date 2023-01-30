#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Functions for analyzing text.
"""

from operator import itemgetter

def read_file(file_name):
    """
    Reads and returns a list of the file.
    """

    file_as_is = [] 

    try:
        with open(file_name) as fh:
            file_as_is = fh.readlines()
    except OSError as e:
        print(e)

    return file_as_is


def lines(file):
    """
    count lines. 
    """

    nr_of_lines = 0

    for line in file:
        if line:
            nr_of_lines += 1

    return nr_of_lines


def words(file):
    """
    count words.
    """

    nr_of_words = 0

    for line in file:
        nr_of_words += len(line.split())

    return nr_of_words


def letters(file):
    """
    count letters.
    """

    nr_of_letters = 0
    file_as_string = " ".join(file)
    
    for char in file_as_string:
        if char.isalnum():
            nr_of_letters += 1

    return nr_of_letters


def string_to_words(file):
    """
    Remove everything but the words and put them in a list.
    """

    file_as_string = " ".join(file)
    only_letters = file_as_string.replace(",", " ").replace(".", " ").replace("\n", " ")
    file_words = only_letters.split()

    for index, word in enumerate(file_words):
        no_whitespace = word.strip()
        file_words[index] = no_whitespace.lower()

    return file_words


def format_string(full_list, nr_of_words):
    """
    Format to correct output.
    """

    correct_output = ""

    for word, value in full_list[:7]:
        correct_output += f"{word}: {value} | {value/nr_of_words*100:.1f}%\n"

    return correct_output.rstrip()


def word_frequency(file):
    """
    count the frequency of words.
    """

    all_words = string_to_words(file)
    all_words.sort(reverse=True)
    frequency = {}

    for word in all_words:
        if word not in frequency:
            frequency[word] = 1
        else:
            frequency[word] += 1

    frequency_sorted = sorted(frequency.items(), key=itemgetter(1), reverse=True)

    return format_string(frequency_sorted, len(all_words))


def letter_frequency(file):
    """
    count the frequency of letters.
    """
    

    all_words = string_to_words(file)
    file_as_string = "".join(all_words)
    no_hyphen = file_as_string.replace("-", "")
    sorted_string = sorted(no_hyphen, reverse=True)
    frequency = {}

    for char in sorted_string:
        if char not in frequency:
            frequency[char] = 1
        else:
            frequency[char] += 1

    frequency_sorted = sorted(frequency.items(), key=itemgetter(1), reverse=True)
    
    return format_string(frequency_sorted, len(no_hyphen))
    
def do_all(file):
    """
    Print all menu choices.
    """

    output_string = f"{lines(file)}\n"
    output_string += f"{words(file)}\n"
    output_string += f"{letters(file)}\n"
    output_string += f"{word_frequency(file)}\n"
    output_string += f"{letter_frequency(file)}"
    
    return output_string
