#!/usr/bin/env python3
"""
Functions for analyzer
"""
#Import itemgetter from operator
from operator import itemgetter

def count_lines(filename):
    """
    Calculates and returns number
    of non-empty lines in a file
    """

    nr_of_lines = 0

    #Get the lines of the file (without newlines) in a list
    try:
        line_list = get_lines(filename)
    except FileNotFoundError as e:
        raise e
    except ValueError as e:
        raise e

    #Loop through the lines, count all lines
    #that are not empty
    for line in line_list:
        if line != "":
            nr_of_lines += 1

    return nr_of_lines

def count_words(filename):
    """
    Calculates and returns number
    of words in a file
    """
    #Get a list with the words of the file
    try:
        word_list = get_words(filename)
    except FileNotFoundError as e:
        raise e
    except ValueError as e:
        raise e

    #Calculate nr of words
    nr_of_words = len(word_list)

    return nr_of_words

def count_letters(filename):
    """
    Calculates and returns number
    of letters in a file
    """

    #Get the letters of the file as a string
    try:
        letter_string = get_letters(filename)
    except FileNotFoundError as e:
        raise e
    except ValueError as e:
        raise e

    #Get the length of the string
    nr_of_letters = len(letter_string)

    return nr_of_letters

def word_frequency(filename):
    """
    Calculates and returns the seven
    most frequent words in a file
    """
    #Get a list with the words of the file
    try:
        word_list = get_words(filename)
    except FileNotFoundError as e:
        raise e
    except ValueError as e:
        raise e

    #Get the total nr of words in the file
    try:
        nr_of_words = count_words(filename)
    except FileNotFoundError as e:
        raise e
    except ValueError as e:
        raise e

    #Get and return frequency list
    return get_frequency_list(word_list, nr_of_words)

def letter_frequency(filename):
    """
    Calculates and returns the seven
    most frequent letters in a file
    """
    #Get letter string
    try:
        letter_string = get_letters(filename)
    except FileNotFoundError as e:
        raise e
    except ValueError as e:
        raise e

    #Get total amount of letters
    try:
        nr_of_letters = count_letters(filename)
    except FileNotFoundError as e:
        raise e
    except ValueError as e:
        raise e

    #Get and return frequency list
    return get_frequency_list(letter_string, nr_of_letters)

def analyze_everything(filename):
    """
    Runs all analyzer functions
    and stores their results in a dict
    returns the dict
    """
    #Get all values
    try:
        nr_of_lines = count_lines(filename)
        nr_of_words = count_words(filename)
        nr_of_letters = count_letters(filename)
        word_frequency_list = word_frequency(filename)
        letter_frequency_list = letter_frequency(filename)
    except FileNotFoundError as e:
        raise e
    except ValueError as e:
        raise e

    data = {
        'total_lines': nr_of_lines,
        'total_words': nr_of_words,
        'total_letters': nr_of_letters,
        'word_frequency': word_frequency_list,
        'letter_frequency': letter_frequency_list
        }

    return data

def analyzer_data_as_string(analyzer_data):
    """
    Takes a dict with analyzer data converts it to a string, returns the string
    """
    #Get the data as strings
    line_string = str(analyzer_data.get('total_lines')) + "\n"
    word_string = str(analyzer_data.get('total_words')) + "\n"
    letter_string = str(analyzer_data.get('total_letters')) + "\n"
    word_frequency_string = frequency_result_to_string(analyzer_data.get('word_frequency'))
    letter_frequency_string = frequency_result_to_string(analyzer_data.get('letter_frequency'))

    #Concatenate the strings
    data_string = line_string + word_string + letter_string + word_frequency_string + letter_frequency_string

    #Return the resulting string
    return data_string

def change():
    """
    Lets the user change which file to analyze
    """
    filename = input("Please enter the name of the file: ")

    print(f"New file to analyze is: {filename}")

    return filename

def read_file(filename):
    """
    Reads a file and returns
    it's content as a lower case string
    """
    #Open and read the file using with open-as
    #to close it automatically, assign
    #file contents to variable content
    try:
        with open(filename, "r", encoding='utf-8') as filehandle:
            content = filehandle.read()
    except FileNotFoundError as e:
        raise FileNotFoundError("Error file does not exist!") from e

    if content == "":
        raise ValueError("Error, file is empty")

    content = content.lower()

    return content

def get_lines(filename):
    """
    Gets and returns the lines of a file as a list without newlines
    """
    #Get the content of the file
    try:
        content = read_file(filename)
    except FileNotFoundError as e:
        raise e
    except ValueError as e:
        raise e

    #Split the content at newlines
    content_list = content.split("\n")

    return content_list

def get_words(filename):
    """
    Gets and returns the words of a file as a list
    """
    #Get a list of the lines of the file
    try:
        line_list = get_lines(filename)
    except FileNotFoundError as e:
        raise e
    except ValueError as e:
        raise e

    #Create a string of the list with spaces between words
    word_string = " ".join(line_list)

    #Remove all punctuation from the string
    word_string = remove_punctuation(word_string)

    #Split the string at spaces to obtain a list with words
    word_list = word_string.split(" ")

    return word_list

def get_letters(filename):
    """
    Gets and returns the letters of a file as a string
    """
    #Get a list of the lines of the file
    try:
        line_list = get_lines(filename)
    except FileNotFoundError as e:
        raise e
    except ValueError as e:
        raise e

    #Join the lines into a string
    letter_string = "".join(line_list)

    #Remove all whitespace from the string
    letter_string = letter_string.replace(" ", "")

    #Remove all punctuation from the string
    letter_string = remove_punctuation(letter_string)

    return letter_string

def get_frequency_list(items, total_amount):
    """
    Takes an interable (in this case list or string) and an int value
    of total number of items (words or letters in this case)
    and calculates the frequency of an item in both total amount and percentage
    Returns a list of tuples with (item, amount, %) with the seven most
    frequent items sorted on largest first
    """

    #Dict to keep track of the frequency (values) of the items (keys)
    item_dict = {}

    #Loop through the string or list of items, for each item (key) assign a value
    #by using get to get the value at the item (key) or else assign
    #value 0 to the word, then add 1
    for item in items:
        item_dict[item] = item_dict.get(item, 0) + 1

    #List to hold tuples with item, frequency and percentage
    items_by_frequency = []

    #Loop through the dict items, for each pass calculate
    #the frequency in percentage of total words in the file
    #append word, count, percentage as a tuple in words_by_frequency
    for item, count in item_dict.items():
        percentage = round((count/total_amount) * 100, 1)
        items_by_frequency.append((item, count, percentage))

    #Sort items by frequency on count and thereafter item, largest first, using itemgetter
    items_by_frequency = sorted(items_by_frequency, key=itemgetter(1, 0), reverse=True)

    #Get the seven most frequent items by slicing items_by_frequency
    items_by_frequency_top_seven = items_by_frequency[0:7]

    return items_by_frequency_top_seven

def frequency_result_to_string(frequency_list):
    """
    Prints the result of the frequency functions,
    takes a list with tuples with (word/letter, number, %)
    and prints it
    """
    result_string = ""
    #Loop through the list and make a string
    for value in frequency_list:
        result_string += value[0] + ": " + str(value[1]) + " | " + str(value[2]) + "%" +"\n"

    return result_string

def remove_punctuation(string_to_change):
    """
    Removes certain punctuation from a string,
    returns the modified string
    """
    #Punctuation chars
    punctuation = '!"#%&\'()*+,-./:;<=>?@[\\]^_{|}~'

    #Loop through the punctuation chars, if they
    #are detected in the string remove them from it
    for char in punctuation:
        if char in string_to_change:
            string_to_change = string_to_change.replace(char, "")

    return string_to_change
