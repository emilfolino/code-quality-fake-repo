#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Functions for text analysis"""

def load_file(filename):
    """Load file"""
    with open(filename, "r") as fd:
        content = fd.read()
    return content

def lines_analysis(filename):
    """Count amount of lines"""
    content = load_file(filename)

    line_count = 0
    for i in content:
        if i == "\n":
            line_count += 1
    line_count += 1
    return line_count

def words_analyzer(filename):
    """Count amount of words"""
    content = load_file(filename)

    content_clean = content
    for i in "\n":
        content_clean = content_clean.replace(i, " ")
    content_split = content_clean.split(" ")
    word_count = len(content_split)
    return word_count

def letters_analyzer(filename):
    """Count amount of letters"""
    content = load_file(filename)
    
    content_clean = content
    for i in "-., \n":
        content_clean = content_clean.replace(i, "")
    letter_count = len(content_clean)
    return letter_count

def calc_frequence(filename, content, analyzer):
    """Calculate character frequency"""
    freq_dict = {}
    for word in content:
        value = content.get(word)
        total_chars = analyzer(filename)
        word_freq = (value / total_chars)  * 100
        round(word_freq, 2)
        freq_dict[word] = round(word_freq, 1)
    return freq_dict

def create_dict(content):
    """Create character dictionary"""
    char_dict = {}
    for char in content:
        if char not in char_dict:
            char_dict[char] = 1
        else:
            char_dict[char] += 1
    return char_dict

def word_frequency(filename):
    """Count word frequency"""
    content = load_file(filename)
    
    content_clean = content
    for i in "\n":
        content_clean = content_clean.replace(i, " ")
    for i in "-.,":
        content_clean = content_clean.replace(i, "")
    content_lowercase = content_clean.lower()

    content_split = content_lowercase.split()
    word_dict = create_dict(content_split)
    word_sorted = dict(sorted(word_dict.items(), key=lambda x: (x[1],x[0]), reverse=True))
    freq_dict = calc_frequence(filename, word_sorted, words_analyzer)

    counter = 0
    for word in word_sorted:
        if counter < 7:
            print(word + ": " + str(word_sorted[word]) + " | " + str(freq_dict[word]) + "%")
            counter += 1

def letter_frequency(filename):
    """Count letter frequency"""
    content = load_file(filename)
    
    content_clean = content
    for i in "-., ":
        content_clean = content_clean.replace(i, "")
    content_lowercase = content_clean.lower()

    letter_dict = create_dict(content_lowercase)
    letter_sorted = dict(sorted(letter_dict.items(), key=lambda item: item[1], reverse=True))
    freq_dict = calc_frequence(filename, letter_sorted, letters_analyzer)

    counter = 0
    for word in letter_sorted:
        if counter < 7:
            print(word + ": " + str(letter_sorted[word]) + " | " + str(freq_dict[word]) + "%")
            counter += 1
