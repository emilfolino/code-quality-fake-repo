"""
Functions for text analyses
"""
import os

# import pprint

def read_file(filename, mode):
    """
    Opens up the access point to the contents of a file.
    mode, in this case, indicates if readlines (rls), read(r), 
    or readline(rl) will be used
    """
    if mode == "r":
        with open(filename, "r") as fd:
            contents = fd.read()
    elif mode == "rl":
        with open(filename, "r") as fd:
            contents = fd.readline()
    elif mode == "rls":
        with open(filename, "r") as fd:
            contents = fd.readlines()
    return contents

# menu choice == "lines"
def analyze_lines(filename):
    """
    Prints the amount of not empty lines there are in a file.
    """
    contents = read_file(filename, "rls")
    amount_of_lines = 0
    for lines in contents:
        if lines != "":
            amount_of_lines += 1
    return amount_of_lines
    # print() done in main.py

# Menu choice == "words"
def analyze_words(filename):
    """
    Prints out the amount of words found in a file.
    Returns the amount of words in file.
    """
    list_of_words = list_words(filename)
    return len(list_of_words)
    # print() done in main.py

# Menu choice == "letters"
def analyze_letters(filename):
    """
    Prints out the amount of letters in the file.
    """
    letters = "abcdefghijklmnopqrstuvwxyz"
    amount_of_letters = 0
    list_of_words = list_words(filename)
    for word in list_of_words:
        for char in word:
            if char in letters:
                amount_of_letters += 1
    return amount_of_letters
    # print() done in main.py


##############################################################
# Functions used mostly for menu choices == "word_frequency" 
# and "letter_frequency"


def list_words(filename):
    """
    Creates a list containing all the words in the file. 
    Splits the lines into words and replaces the punctuations:
    ".," with ""

    Returns that list with lower-case letters.
    """
    contents_list = read_file(filename, "rls")
    list_of_words_in_content = []
    for line in contents_list:
        if line != "":
            line_to_list_of_words = line.lower().strip().split(" ")
            list_of_words_in_content.extend(line_to_list_of_words)
    strip_words_of_punctuations(list_of_words_in_content)
    return list_of_words_in_content

# used in list_words() function
def strip_words_of_punctuations(list_of_words):
    """
    Strips the words in a given list of the punctuations:
    ",."
    """
    for i, word in enumerate(list_of_words):
        if "." in word:
            list_of_words[i] = word.replace(".", "")
        elif "," in word:
            list_of_words[i] = word.replace(",", "")
    # pprint.pprint(list_of_words)

def list_letters(filename):
    """
    Creates a list containing all the letters in the file. 
    Returns the list.
    """
    list_of_words_in_content = list_words(filename)
    list_of_letters_in_content = []
    letters = "abcdefghijklmnopqrstuvwxyz"
    for word in list_of_words_in_content:
        for letter in word:
            if letter in letters:
                list_of_letters_in_content.append(letter)
    return list_of_letters_in_content

def freq_tuple_value_dict(
    existing_values_in_file, list_of_values_in_content
    ):
    """
    Calculates the frequency of a word in percentage.
    Creates a dictionary:

    (amount, percentage): [value]
    returns the updated dict.
    """
    amount_value = 0
    percentage = 0
    dict_values = {}
    for value in existing_values_in_file:
        for value_in_content in list_of_values_in_content:
            if value == value_in_content:
                amount_value += 1
    # print(value_frequency)
        percentage = round(
            (amount_value / len(list_of_values_in_content)) * 100, 1
            )
        if (amount_value, percentage) not in dict_values:
            dict_values[(amount_value, percentage)] = [value]
        else:
            dict_values[(amount_value, percentage)].append(value)
        amount_value = 0
    # print(percentage)
    return dict_values

def sorts_dict(dict_):
    """
    Sorts the given dictionary by keys (frequency tuple).

    Creates a sorted list with tuples as items of 
    (amount, percent, value),
    called sorted_by_value and sorts the value-list in dictionary
    according to letter in decending order.
    
    Returns sorted_by_value list.
    """
    sorted_dict = sorted(dict_.items(), reverse=True) #sorts dict by frequency (key)
    sorted_by_value = []
    for freq_tuple, word_list in sorted_dict:
        frequency, percent = freq_tuple
        for word in sorted(word_list, reverse=True):
            sorted_by_value.append((word, frequency, percent))
    return sorted_by_value

# Menu choice == "word_frequency"
def word_frequency_results(filename):
    """
    Prints the 7 most common words:
    print({Value}: {amount} | {percentage}%)
    with for loop in value, items in dict.items()

    dictionary is sorted by amount and letters in descending order.
    """
    # Assembles all the words in file only once in list
    list_of_words_in_content = list_words(filename)
    existing_words_in_file = []
    for word in list_of_words_in_content:
        if word not in existing_words_in_file:
            existing_words_in_file.append(word)
    dict_words = freq_tuple_value_dict(
        existing_words_in_file, 
        list_of_words_in_content
        )
    highest_freq_sorted_by_word = sorts_dict(dict_words)

    # prints the 7 first tuples in highest_freq_sorted_by_word
    msg = []
    for word, frequency, percent in highest_freq_sorted_by_word[:7]:
        result = (f"{word}: {frequency} | {percent}%")
        msg.append(result)
    return msg # msg contains 7 tuples of the format above
        # Printing should be done in the main.py module.

# Menu choice == "letter_frequency"
def letter_frequency_results(filename):
    """
    Calculates the frequency of a letter in percentage.
    Returns the percentage value.
    Prints out the 7 most common letters.
    """
    # Assembles all the letters, only once, in file to a list.
    list_of_letters_in_content = list_letters(filename)
    existing_letters = "abcdefghijklmnopqrstuvwxyz"
    existing_letters_in_file = []
    for letter in existing_letters:
        existing_letters_in_file.append(letter)
    
    # Dictionary of (freq, perc): [letters]
    dict_letters = freq_tuple_value_dict(
        existing_letters_in_file,
        list_of_letters_in_content
    )
    # Dictionary into list of sorted letters in descending order
    highest_freq_sorted_by_letter = sorts_dict(dict_letters)
    # prints the 7 first tuples in highest_freq_sorted_by_letter
    msg = []
    for letter, frequency, percent in highest_freq_sorted_by_letter[:7]:
        result = (f"{letter}: {frequency} | {percent}%")
        msg.append(result)
    return msg # msg contains 7 tuples of the format above

    # Printing should be done in the main.py module. 
    # for results in letter_frequency_results:
    # print(results)

##############################################################
# Functions for menu choice == "all"

# Ditt program skall klara av menyvalet all som kör alla analyserings 
# funktioner i följd och skriver ut resultatet. 
# 

def create_dict_all(filename):
    """
    creates a dictionary containing all the resulting data to be printed
    from all analyze-functions.

    "functions" : [msg]
    """
    dict_all = {}
    dict_all["analyze_lines"] = analyze_lines(filename)
    dict_all["analyze_words"] = analyze_words(filename)
    dict_all["analyze_letters"] = analyze_letters(filename)
    dict_all["word_frequency_results"] = word_frequency_results(filename)
    dict_all["letter_frequency_results"] = letter_frequency_results(filename)
    return dict_all

def print_all_analyzes(filename):
    """
    Prints the values of dict_all.
    """
    dict_all = create_dict_all(filename)
    for _, value in dict_all.items():
        if isinstance(value, list):
            for results in value:
                print(results)
        else:
            print(value)

# Tips, låt dina funktioner returnerar ett värde, 
# spara undan resultatet i en dictionary och skriv ut 
# i en egen utskriftsfunktion. 
# 
# Utskriften ska vara soreterad i storleks ordning och 
# bokstavsordning sjunkande. 
# Om två ord har 5 ska orden sorteras i bokstavsordning sjunkande. 
# Skriv minst en funktion för varje kommando i analyzer.py.

def print_results(highest_freq_sorted_by_value):
    """
    prints values according to:

    print({Value}: {amount} | {percentage}%)
    """
    for value, frequency, percent in highest_freq_sorted_by_value[:7]:
        print(f"{value}: {frequency} | {percent}%")


def change(filename):
    """
    Changes the filename and returns it if file exists.
    """
    filename1 = input("Enter filename: ")
    if os.path.isfile(filename1):
        filename = filename1
    else:
        raise FileNotFoundError("File not found")
    return filename

if __name__ == "__main__":
    # filename = "phil.txt"
    # print_all_analyzes(filename)
    pass
