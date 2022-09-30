
"""
File that contains  all the functions for our analyzer
"""
from operator import itemgetter
import string


def strip_punctuations(line):
    """
    function that gets rid of all punctuation characters
    """
    for character in string.punctuation:
        line = line.replace(character, "")
    return line

def letters(text_file):
    """
    Counting amount of letters in a text file
    """
    with open(text_file, "r") as filehandle:

        letters_data = filehandle.read()
        count = 0
        for letter in letters_data.lower():
            if letter.isalpha():
                count += 1
        return count

def words(text_file):
    """
    Counting amount of words in a text file
    """
    with open(text_file, "r") as filehandle:
        words_data = filehandle.read()
        words_to_count = words_data.split()
        number_of_words = len(words_to_count)
    return number_of_words

def lines(text_file):
    """
    Counting number of lines in a file text
    """
    with open(text_file, "r") as filehandle:
        line_count = 0
        for line in filehandle:
            if line != "\n":
                line_count += 1
        return line_count



def dictionary_frequency(this_file, total_items):
    """
    Make a dictionary out of list, with frequency as number
    """
    di = {}

    for w in this_file:
        if w in di:
            di[w] += 1
        else:
            di[w] = 1
    di_percent = dictionary_percent(di, total_items)
    return di_percent




def word_frequency(text_file, total_words):
    """
    Print out word frequency of text file in number and percent
    """
    words_list = []
    with open(text_file, 'r') as fi:
        for line in fi:
            line = strip_punctuations(line)
            line = line.lower()
            words_list += line.split()
        dict_as_percent = dictionary_frequency(words_list, total_words)
        return print_frequency(dict_as_percent)

def letter_frequency(text_file, total_letters):
    """
    Print out word frequency of text file in number and percent
    """
    letters_list = []
    with open(text_file, 'r') as fi:
        for line in fi:
            line = strip_punctuations(line)
            line = line.strip()
            line = line.lower()
            new_items = list(line)
            remove_space = [x.strip(' ') for x in new_items]
            delete_empty = [ele for ele in remove_space if ele.strip()]
            letters_list.extend(delete_empty)
    dict_as_percent = dictionary_frequency(letters_list, total_letters)
    return print_frequency(dict_as_percent)

def dictionary_percent(this_dictionary, total_items):
    """
    Takes dictionary as an argument, then counts items in percentage
    """
    frequency_sorted = {}
    for key in sorted(this_dictionary, reverse=True):
        frequency_sorted[key] = this_dictionary[key]

    frequency_percent = {}
    for key, value in sorted(frequency_sorted.items(), key=itemgetter(1), reverse=True):

        frequency_percent[key] = (value, round((value * 100) / total_items, 1))

    return frequency_percent



def print_frequency(this_file):
    """
    Uses dictionary with a percentage and prints out graph
    """
    stepper = 7
    count = 0
    final_graph = ""
    for key, value in this_file.items():
        if count == stepper:
            break
        else:
            final_graph += f"{key}: {value[0]} | {value[1]}%\n"
            count += 1
    final_graph = final_graph.rstrip("\n")
    return final_graph
