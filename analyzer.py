"""
The functions for the text analyzer.
"""

from operator import itemgetter


def count_lines(analyzing_file):
    """
    Counts the amount of lines in a text file.
    """
    with open(analyzing_file, "r") as text_file:
        line_count = 0

        text_lines = text_file.readlines()
        
        for lines in text_lines:
            if lines:
                line_count += 1
        
        print("Number of lines:", line_count, "\n")

def count_words(analyzing_file):
    """
    Counts the amount of words in a text file.
    """
    with open(analyzing_file, "r") as text_file:
        analyzing_text = text_file.read()
        words = analyzing_text.split()

        print("Number of words: ", len(words), "\n")

def count_letters(analyzing_file):
    """
    Counts the amount of letters in a text file.
    """
    total_letters = letter_counter(analyzing_file)
    print("Number of letters: ", total_letters, "\n")

def word_frequency(analyzing_file):
    """
    A function that finds the 7 most used words in the text file.
    """

    word_dict = {}

    with open(analyzing_file, "r") as text_file:
        analyzing_text = text_file.read().replace(",", " ").replace(".", " ")
        words = analyzing_text.split()
        lower_case_words_list = convert_list_to_lowercase(words)
        sorted_words_list = sorted(lower_case_words_list, reverse = True)
        for word in sorted_words_list:
            if word.lower() in word_dict:
                word_dict[word.lower()] += 1
            else: 
                word_dict[word.lower()] = 1
        seven_most_used = {}
        seven_most_used = sorted(word_dict.items(), key = itemgetter(1), reverse = True)
        percent_dict = {}
        for value in seven_most_used[:7]:
            percent_dict[value[0]] = round((value[1]/len(words))*100, 1)
        
        for values in seven_most_used[:7]:
            print(values[0] + ": " + str(values[1]) + " | " + str(percent_dict[values[0]]) + "%")


def letter_frequency(analyzing_file):
    """
    A function that finds the 7 most used words in the text file.
    """

    letter_dict = {}

    with open(analyzing_file, "r") as text_file:
        analyzing_text = text_file.read().replace(",", " ").replace(".", " ")
        lower_case_letter_list = convert_list_to_lowercase(analyzing_text)
        sorted_letter_list = sorted(lower_case_letter_list, reverse = True)
        for letter in sorted_letter_list:
            if letter.isalpha():
                if letter.lower() in letter_dict:
                    letter_dict[letter.lower()] += 1
                else: 
                    letter_dict[letter.lower()] = 1

        seven_most_used = {}
        seven_most_used = sorted(letter_dict.items(), key = itemgetter(1), reverse = True)
        percent_dict = {}
        total_letters = letter_counter(analyzing_file)
        for value in seven_most_used[:7]:
            percent_dict[value[0]] = round((value[1]/total_letters)*100, 1)
        
        for values in seven_most_used[:7]:
            print(values[0] + ": " + str(values[1]) + " | " + str(percent_dict[values[0]]) + "%")


def everything(analyzing_file):
    """
    A function that does every menu choice that is possible.
    """
    count_lines(analyzing_file)
    count_words(analyzing_file)
    count_letters(analyzing_file)
    word_frequency(analyzing_file)
    letter_frequency(analyzing_file)

def change_file():
    """
    Changes the file that the analyzer is using
    """
    filename = input("Enter filename: ")

    analyzing_file = filename

    return analyzing_file
    
def convert_list_to_lowercase(chosen_list):
    """
    Converts a list in to only lowercase strings.
    """
    lower_case = [x.lower() for x in chosen_list]

    return lower_case

def letter_counter(analyzing_file):
    """
    Counts the total amounts of letters in a text file.
    """
    with open(analyzing_file, "r") as text_file:
        counter = 0
        analyzing_text = text_file.read()
        for char in analyzing_text:
            if char.isalpha():
                counter += 1
        return counter
    
