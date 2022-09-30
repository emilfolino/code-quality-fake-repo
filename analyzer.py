
"""Functions"""

def lines_count(textFile):
    """Counting the lines"""
    with open(textFile) as text:
        count = len(text.readlines())

    return count

def words(textFile):
    """Getting all the words in a list"""
    with open(textFile) as text:
        word_list = text.read()
        word_list = word_list.lower()
        word_list = word_list.replace("\n", " ")
        word_list = word_list.replace(",", "")
        word_list = word_list.replace(".", "")
        word_list = word_list.split(" ")

    return word_list

def words_count(textFile):
    """Counting Words"""
    count = 0
    word_list = words(textFile)
    count = len(word_list)

    return count

def letters_count(textFile):
    """Counting Letters"""

    letters_string = letters(textFile)
    count = len(letters_string)

    return count

def letters(textfile):
    """Get all the letters"""
    with open(textfile) as text: 
        letters_string = text.read().lower()
        letters_string = letters_string.replace("\n", " ")
        letters_string = letters_string.replace(" ", "")
        letters_string = letters_string.replace(".", "")
        letters_string = letters_string.replace(",", "")
        letters_string = letters_string.replace("-", "")

    return letters_string

def word_frequency(textFile):
    """Word frequency"""
    word_list_single = []
    words_dict = {}

    word_counter = words_count(textFile)
    word_list = words(textFile)

    word_list_single = append_frequency(word_list, word_list_single)
    
    words_dict = insert_frequency(words_dict, word_list_single, word_counter, word_list)
    
    words_dict = sorted(words_dict.items(), key=lambda x: (x[1]['count'], x[0]), reverse=True)

    print_frequency(words_dict)

def letter_frequency(textFile):
    """Letter frequency"""
    letter_list_single = []
    letter_dict = {}

    letter_counter = letters_count(textFile)
    letters_string = letters(textFile)
    letters_string = " ".join(letters_string)
    letters_string = letters_string.split(" ")

    letter_list_single = append_frequency(letters_string, letter_list_single)

    letter_dict = insert_frequency(letter_dict, letter_list_single, letter_counter, letters_string)

    letter_dict = sorted(letter_dict.items(), key=lambda x: (x[1]['count'], x[0]), reverse=True)

    print_frequency(letter_dict)


def append_frequency(function_list, new_list):
    """Appending in a new list"""
    for string in function_list:
        if string not in new_list: 
            new_list.append(string)
    return new_list

def insert_frequency(listing, new_list, count, function_list):
    """Insert frequency"""
    counter = 0
    for word in (new_list):
        value_word = function_list.count(new_list[counter])
        listing[word] = {'count': value_word, 'precentage' : round(((value_word / count) * 100), 1)}
        counter += 1

    return listing

def print_frequency(dictionary):
    """Printing the frequency"""
    count = 0
    for word in dictionary:
        print(word[0] + ": " + str(word[1]['count']) + " | " + str(word[1]['precentage']) + "%")
        count += 1

        if count >= 7:
            break

def all_function(textFile):
    """Printing all functions"""

    print(lines_count(textFile))
    print(words_count(textFile))
    print(letters_count(textFile))
    word_frequency(textFile)
    letter_frequency(textFile)
