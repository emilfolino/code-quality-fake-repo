#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Functions for text analyzing
"""

def get_all_lines_from_file(file_to_read):
    """
    returns a list with all lines from file
    """
    all_lines_in_file = []
    with open(file_to_read, "r") as file:
        for line in file:
            all_lines_in_file.append(line.translate({ord(i): None for i in ",.-¨'"}))
    return all_lines_in_file

def list_to_string(lst):
    """
    Converts a list to string 
    """
    as_a_string = "".join(lst)
    return as_a_string

def get_all_words(file_to_read):
    """
    Returns all words as a list
    """
    all_lines = get_all_lines_from_file(file_to_read)
    all_words = list_to_string(all_lines).split()
    return all_words

def get_total_words(file_to_read):
    """
    Returns number of words
    """
    total_number_words = len(get_all_words(file_to_read))
    return total_number_words

def get_all_letters(file_to_read):
    """
    Returns all letters
    """
    all_lines = get_all_lines_from_file(file_to_read)
    all_characters = list_to_string(all_lines)
    
    all_letters = all_characters.translate({ord(i): None for i in " \n"})
    return all_letters

def get_total_letters(file_to_read):
    """
    Returns number of letters
    """
    total_number_letters = len(get_all_letters(file_to_read))
    return total_number_letters

def to_dict(a_list):
    """
    Create a dict from a list of word where word is used as a key and
    value is number of times word in list
    """
    words = {}
    for word in a_list:
        words[word.lower()] = words.get(word.lower(), 0) + 1
    return words

def sort_dict_by_value(dictionary):
    """
    Returns a dict sorted by its value
    """
    #x: (x[1],x[0]), reverse=True)
    sorted_dict = sorted(dictionary.items() , key=lambda word_count: (word_count[1],word_count[0]), reverse=True)
    return sorted_dict

def print_frequency(sorted_list, total, text):
    """
    Prints the word/letter and number of times it is used in file
    """
    for i in range(7):
        word = sorted_list[i][0]
        count = sorted_list[i][1]
        percent = round(100 * count / total, 1)
        print(f"{word}: {count} | {percent}% of all {text}")
    print("")

def print_lines(file_to_read):
    """
    Counts number of non empty lines in file
    """
    all_lines = get_all_lines_from_file(file_to_read)
    total_number_of_lines = len(all_lines)
    print(f"Total number of lines in file: {total_number_of_lines}\n")
    
def print_words(file_to_read):
    """
    Counts number of words in file
    """
    total_number_of_words = get_total_words(file_to_read)
    print(f"Total number of words in file: {total_number_of_words}\n")

def print_letters(file_to_read):
    """
    Counts number of letters in file
    """
    total_numbers_of_letters = get_total_letters(file_to_read)
    print(f"Total number of letter in file: {total_numbers_of_letters}\n")

def print_word_frequency(file_to_read):
    """
    Filters out the 7 most used words and how many times they were used
    """
    all_words = get_all_words(file_to_read)
    words_dict = to_dict(all_words)
    sorted_list = sort_dict_by_value(words_dict)
    total_number_of_words = get_total_words(file_to_read)

    print_frequency(sorted_list, total_number_of_words, "words")

def print_letter_frequency(file_to_read):
    """
    Filters out the 7 most used letters and how many times they were used
    """
    all_letters = get_all_letters(file_to_read)
    letters_dict = to_dict(all_letters)
    sorted_list = sort_dict_by_value(letters_dict)
    total_number_of_letters = get_total_letters(file_to_read)

    print_frequency(sorted_list, total_number_of_letters, "letters")

def change():
    """
    Changes the file to read from
    """
    fileName = input("Enter a filename: ")
    return fileName

def print_all_info(file_to_read):
    """
    Runs all functions in module exept for change
    """
    print("\n")
    print_lines(file_to_read)
    print_words(file_to_read)
    print_letters(file_to_read)
    print_word_frequency(file_to_read)
    print_letter_frequency(file_to_read)

if __name__ == "__main__":
    pass
