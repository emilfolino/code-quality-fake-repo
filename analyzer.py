#!/usr/bin/env python3

"""
Functions for analyzing text
"""

def read_file(filename):
    """Read a text file"""
    with open(filename) as fh:
        content = fh.read()
    return content

def count_lines(text):
    """Count the number of lines in a text."""
    number_of_lines = 0
    split_text = text.split("\n")
    for line in split_text:
        if line != "":
            number_of_lines += 1
    return number_of_lines

def count_words(text):
    """Count the number of words in a text"""
    number_of_words = 0
    split_text = text.split("\n")
    word_list = []
    for line in split_text:
        word_list.append(line.split())
    for line in word_list:
        number_of_words += len(line)
    return number_of_words

def count_letters(text):
    """Count the number of letters in a text"""
    number_of_letters = len(text) - text.count(" ") - text.count(
        ".") - text.count(",") - text.count("-") - text.count("\n")
    print(number_of_letters)
    return number_of_letters

def get_word_frequency_dict(text):
    """Check the word frequency in a text"""
    word_frequencies = {}
    text = text.replace("-", " ")
    text = text.replace(",", " ")
    text = text.replace(".", " ")
    split_text = text.split("\n")
    word_list = []
    for line in split_text:
        word_list.append(line.split())
    for line in word_list:
        for word in line:
            word = word.lower()
            if word in word_frequencies:
                word_frequencies[word] += 1
            else:
                word_frequencies[word] = 1
    return word_frequencies

def word_frequency(text):
    """Print the most frequent words in a text"""
    word_frequencies = get_word_frequency_dict(text)
    sorted_word_freq = sorted(word_frequencies.items(),
    key = lambda x: (x[1], x[0]), reverse = True)
    words = count_words(text)
    for word, freq in sorted_word_freq[0:7]:
        percent = round(100 * freq / words, 1)
        print(f"{word}: {freq} | {percent}%")

def get_letter_frequency_dict(text):
    """Check the letter frequency of a text"""
    letter_frequencies = {}
    text = text.replace("-", "")
    text = text.replace(",", "")
    text = text.replace(".", "")
    text = text.replace("\n", "")
    text = text.replace(" ", "")
    for letter in text:
        letter = letter.lower()
        if letter in letter_frequencies:
            letter_frequencies[letter] += 1
        else:
            letter_frequencies[letter] = 1
    return letter_frequencies

def letter_frequency(text):
    """Print the most frequent letters in a text"""
    letter_frequencies = get_letter_frequency_dict(text)
    sorted_letter_freq = sorted(letter_frequencies.items(),
    key = lambda x: (x[1], x[0]), reverse = True)
    letters = count_letters(text)
    for letter, freq in sorted_letter_freq[0:7]:
        percent = round(100 * freq / letters, 1)
        print(f"{letter}: {freq} | {percent}%")

if __name__ == "__main__":
    pass
