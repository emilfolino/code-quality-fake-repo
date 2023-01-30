"""
The folder containing all functions used in main.py
Except the first function mentioned in main.py (print_menu)
"""

def txt_string(file):
    """
    Returns the string of inputed txt file
    """
    with open(file, 'r') as txt:
        string = txt.read()

    return string

def lines(file):
    """
    Returns the number of lines inside the txt file placed as the input
    """
    with open(file, 'r') as txt:
        txt_array = txt.readlines()

    return len(txt_array)

def words(file):
    """
    Returns the number of words inside the txt file placed as the input
    The function counts from 1 instead of 0 under the assumption that no
    txt file without any words will be inputed into the function
    """
    word_count = 1
    string = txt_string(file)

    for x in string:
        if x in " " or x in "\n":
            word_count += 1

    return word_count

def letters(file):
    """
    Returns the number of letters inside the txt file placed as the input
    """
    letter_count = 0
    string = txt_string(file)
    
    for x in string:
        if x.isalpha():
            letter_count += 1

    return letter_count

def word_frequency(file):
    """
    The shell function that sorts and returns the information word_freq 
    returns (in a string)
    It also compares the amount of times each word has been said, 
    compared to the total amount of words used in the txt file
    """
    result = dict(sorted(word_freq(file).items(), key=lambda item: item[0], reverse=True))
    result = dict(sorted(result.items(), key=lambda item: item[1], reverse=True))

    while len(result) > 7:
        result.popitem()

    all_words = words(file)
    final_result = ""

    for key, value in result.items():
        percent = (value/all_words) * 100
        percent = round(percent, 1)
        final_result = final_result + f"{key}: {value} | {percent}%\n"

    return final_result[:-1]

def word_freq(file):
    """
    Counts the amount of times a word is used in the inputed txt file
    """
    current_word = ""
    word_directory = {}
    string = txt_string(file)

    string = string.replace("\n", " ")
    string = string.lower()

    for x in string:
        if x not in " " and x not in "." and x not in "," and x.isalpha:
            current_word = current_word + x
        if x in " " or x in "." or x in ",":
            if current_word != "" and current_word in word_directory:
                word_directory[current_word] += 1
                current_word = ""
            elif current_word != "" and current_word not in word_directory:
                word_directory[current_word] = 1
                current_word = ""

    return word_directory

def letter_frequency(file):
    """
    The shell function that sorts and returns the information letter_freq 
    returns (in a string)
    It also compares the amount of times each letter has been said, 
    compared to the total amount of letters used in the txt file
    """
    result = dict(sorted(letter_freq(file).items(), key=lambda item: item[1], reverse=True))

    while len(result) > 7:
        result.popitem()

    all_words = letters(file)
    final_result = ""

    for key, value in result.items():
        percent = (value/all_words) * 100
        percent = round(percent, 1)
        final_result = final_result + f"{key}: {value} | {percent}%\n"

    return final_result[:-1]

def letter_freq(file):
    """
    Counts the amount of times a letter is used in the inputed txt file
    """
    letter_directory = {}
    string = txt_string(file)

    string = string.replace("\n", "")
    string = string.lower()

    for x in string:
        if x not in " " and x not in "." and x not in "," and x.isalpha:
            if x in letter_directory:
                letter_directory[x] += 1
            elif x not in letter_directory:
                letter_directory[x] = 1

    return letter_directory

def run_all(file):
    """
    Runs all the functions above and returns a string cotaining all
    the results
    """
    final_output = str(lines(file)) + "\n"
    final_output = final_output +  str(words(file)) + "\n"
    final_output = final_output +  str(letters(file)) + "\n"
    final_output = final_output +  word_frequency(file) + "\n"
    final_output = final_output +  letter_frequency(file)

    return final_output
