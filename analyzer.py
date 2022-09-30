"""
Module for analyzing text
"""

def open_file_to_string(filename):
    """Function opens file as string"""
    with open(filename) as fd:
        content = fd.read()
    return content


def lines(filename):
    """analyzes amount of lines (not empty)"""

    content = open_file_to_string(filename)
    content_list = content.split("\n")

    filled_lines = 0     #Store the number of empty lines
    for line in content_list:
        if line != "":
            filled_lines += 1

    return filled_lines

def get_all_words(content):
    """gets amount of words"""

    content = content.lower()
    content = content.replace("\n", " ")
    content = content.replace(".", "")
    content = content.replace(",", "")
    content_list = content.split(" ")

    return content_list


def words_amount(filename):
    """analyzes amount of words"""

    content = open_file_to_string(filename)
    word_list = get_all_words(content)

    amount_of_words = len(word_list)
    return amount_of_words

def get_all_letters(textstring):
    """gets amount of letters"""
        
    letters = ""
    for letter in textstring:
        if letter.lower() in "abcdefghijklmnopqrstuvwxyz":
            letters += letter.lower()

    return letters

def letters_amount(filename):
    """analyzes amount of letters"""

    content = open_file_to_string(filename)

    letters= get_all_letters(content)
    return len(letters)
    


def word_frequency(filename):
    """analyzes frequency of words"""

    content = open_file_to_string(filename)
    word_list = get_all_words(content)

    word_dict = {}
    for word in word_list:
        if word.lower() in word_list:
            if word.lower() in word_dict:
                word_dict[word.lower()] += 1
            else:
                word_dict[word.lower()] = 1   

    word_list_sorted = sorted(word_dict.items(), key=lambda x: (x[1], x[0]), reverse=True)
    list_sorted_7 = word_list_sorted[:7]

    words = get_all_words(content)
    
    print(str(list_sorted_7[0][0]) + ": " + str(list_sorted_7[0][1]) \
        + " | " + str(round(list_sorted_7[0][1] / len(words) * 100, 1)) + "%")
    print(str(list_sorted_7[1][0]) + ": " + str(list_sorted_7[1][1]) \
        + " | " + str(round(list_sorted_7[1][1] / len(words) * 100, 1)) + "%")
    print(str(list_sorted_7[2][0]) + ": " + str(list_sorted_7[2][1]) \
        + " | " + str(round(list_sorted_7[2][1] / len(words) * 100, 1)) + "%")
    print(str(list_sorted_7[3][0]) + ": " + str(list_sorted_7[3][1]) \
        + " | " + str(round(list_sorted_7[3][1] / len(words) * 100, 1)) + "%")
    print(str(list_sorted_7[4][0]) + ": " + str(list_sorted_7[4][1]) \
        + " | " + str(round(list_sorted_7[4][1] / len(words) * 100, 1)) + "%")
    print(str(list_sorted_7[5][0]) + ": " + str(list_sorted_7[5][1]) \
        + " | " + str(round(list_sorted_7[5][1] / len(words) * 100, 1)) + "%")
    print(str(list_sorted_7[6][0]) + ": " + str(list_sorted_7[6][1]) \
        + " | " + str(round(list_sorted_7[6][1] / len(words) * 100, 1)) + "%")


def letter_frequency(filename):
    """analyzes frequency of letters"""
    
    content = open_file_to_string(filename)

    letter_dict = {}
    for letter in content:
        if letter.lower() in "abcdefghijklmnopqrstuvwxyz":
            if letter.lower() in letter_dict:
                letter_dict[letter.lower()] += 1
            else:
                letter_dict[letter.lower()] = 1

    list_sorted = sorted(letter_dict.items(), key=lambda x: (x[1], x[0]), reverse=True)
    list_sorted_7 = list_sorted[:7]

    letters = get_all_letters(content)
    
    print(str(list_sorted_7[0][0]) + ": " + str(list_sorted_7[0][1]) \
        + " | " + str(round(list_sorted_7[0][1] / len(letters) * 100, 1)) + "%")
    print(str(list_sorted_7[1][0]) + ": " + str(list_sorted_7[1][1]) \
        + " | " + str(round(list_sorted_7[1][1] / len(letters) * 100, 1)) + "%")
    print(str(list_sorted_7[2][0]) + ": " + str(list_sorted_7[2][1]) \
        + " | " + str(round(list_sorted_7[2][1] / len(letters) * 100, 1)) + "%")
    print(str(list_sorted_7[3][0]) + ": " + str(list_sorted_7[3][1]) \
        + " | " + str(round(list_sorted_7[3][1] / len(letters) * 100, 1)) + "%")
    print(str(list_sorted_7[4][0]) + ": " + str(list_sorted_7[4][1]) \
        + " | " + str(round(list_sorted_7[4][1] / len(letters) * 100, 1)) + "%")
    print(str(list_sorted_7[5][0]) + ": " + str(list_sorted_7[5][1]) \
        + " | " + str(round(list_sorted_7[5][1] / len(letters) * 100, 1)) + "%")
    print(str(list_sorted_7[6][0]) + ": " + str(list_sorted_7[6][1]) \
        + " | " + str(round(list_sorted_7[6][1] / len(letters) * 100, 1)) + "%")

def show_all(filename):
    """prints all the results from the menu-choices"""
    print(lines(filename))
    print(words_amount(filename))
    print(letters_amount(filename))
    word_frequency(filename)
    letter_frequency(filename)
