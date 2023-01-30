" Module for analyzing text "

import os.path


def lines():
    """
    Return number of lines in the selected file.
    """
    n_lines = len(CONTENT.split("\n"))
    return n_lines


def words():
    """
    Return number of words in the selected file.
    """
    n_words = len(CONTENT.replace("\n", " ").split(" "))
    return n_words


def letters():
    """
    Return number of letters in the selected file.
    """
    counter = 0
    for c in CONTENT:
        if c.isalpha():
            counter += 1
    return counter


def word_frequency():
    """
    Print the top 7 most occuring words in the file, sorted descending by word.
    """
    word_dict = {}
    words_without_period_and_comma = (
        CONTENT.lower().replace("\n", " ").replace(".", "").replace(",", "").split(" ")
    )
    for word in words_without_period_and_comma:
        if word not in word_dict:
            word_dict[word] = 1
        else:
            word_dict[word] += 1
    sorted_dict = sort_dict_descending_by_frequency_and_key(word_dict)
    print_top_n(sorted_dict, 7, words())


def letter_frequency():
    """
    Print the top 7 most occuring words in the file, sorted descending by letter.
    """
    letter_dict = {}
    for letter in CONTENT.lower():
        if letter.isalpha():
            if letter not in letter_dict:
                letter_dict[letter] = 1
            else:
                letter_dict[letter] += 1
    sorted_dict = sort_dict_descending_by_frequency_and_key(letter_dict)
    print_top_n(sorted_dict, 7, letters())


def sort_dict_descending_by_frequency_and_key(dict_):
    """
    Sorts a disctionary descending by value, and if ties, descending by characters in key.
    """
    dict_sorted_by_key = {}
    for key in sorted(dict_, reverse=True):
        dict_sorted_by_key[key] = dict_[key]
    dict_sorted_by_freq = {}
    for key in sorted(dict_sorted_by_key, key=dict_sorted_by_key.get, reverse=True):
        dict_sorted_by_freq[key] = dict_sorted_by_key[key]
    return dict_sorted_by_freq


def print_top_n(dict_, n, total_amount):
    """
    Prints the first n values of a dictionary, as well as the ratio between
    the value and the total_amount.
    """
    for i, key in enumerate(dict_):
        if i == n:
            break
        freq = dict_[key]
        print(f"{key}: {freq} | {round(freq/total_amount*100, 1)}%")


def all():  # pylint: disable=redefined-builtin
    """
    Runs all text analysis functions for the selected file.
    """
    print(lines())
    print(words())
    print(letters())
    word_frequency()
    letter_frequency()


def change():
    """
    Select file based on input
    """
    global FILE
    file = input("What file would you like to read:\n--> ")
    if os.path.isfile(file):
        FILE = file
    else:
        print(f"{file} not found")
    read_file()
    print(f"FILE selected: {FILE}")


def read_file():
    """
    Sets the global variable CONTENT to the content of the currently selected file.
    """
    global CONTENT
    global FILE
    script_dir = os.path.dirname(__file__)
    with open(os.path.join(script_dir, FILE), "r") as f:
        CONTENT = f.read()


FILE = "phil.txt"
CONTENT = ""
read_file()
