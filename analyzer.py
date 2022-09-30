"""
Contains functions to analyze text
"""


# def read_file(request):
#     """
#     Reads "phil.txt" on startup
#     """
#     with open(request, "r") as fd:
#         full_text = fd

#     return(full_text)

def count_lines(file_name):
    """
    Counts lines in text file
    """
    with open(file_name, "r") as fd:
        full_text = fd.readlines()
        counter = len(full_text)
        
        return counter

def count_words(file_name):
    """
    Counts words in text file
    """
    with open(file_name, "r") as fd:
        counter = 0
        #full_text = fd.read()
        for line in fd:
            list_word = line.split()
            counter += len(list_word)

        return counter

def count_letters(file_name):
    """
    Counts characters in text file, excluding "\n"
    """
    counter = 0
    ab = "abcdefghijklmnopqrstuvwxyzåäö"
    with open(file_name, "r") as fd:
        full_text = fd.read()
        for char in full_text:
            if char.lower() in ab:
                counter += 1

        return counter

def word_frequency(file_name):
    """
    Calculates frequency of words in text file
    """
    result = {}
    punctuation = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
    
    with open(file_name, "r") as fd:
        full_text = fd.read()
        full_text = full_text.translate(full_text.maketrans('', '', punctuation))
        full_text = full_text.lower()
        list_text = full_text.split()
        for word in list_text:
            if word.rstrip() in result:
                result[word] += 1
            else:
                result[word] = 1
        result = sorted(result.items(), key=lambda t: t[::-1], reverse=True)
        #result = sorted(result.items(), key=lambda x: x[1], reverse=True)


        for i in range(7):
            print(f"{result[i][0]}: {result[i][1]} | {calculate_percentage_words(file_name, result[i][1])}%")

def calculate_percentage_words(file_name, number):
    """
    Calculates percentage of word frequency
    """
    amount_of_words = count_words(file_name)

    result = number / amount_of_words * 100

    return round(result, 1)

def letter_frequency(file_name):
    """
    Calculates frequency of letters in text file
    """
    result = {}
    punctuation = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'

    with open(file_name, "r") as fd:
        full_text = fd.read()
        full_text = full_text.translate(full_text.maketrans('', '', punctuation))
        full_text = full_text.lower()
        for char in full_text:
            if char.rstrip() in result:
                result[char] += 1
            else:
                result[char] = 1

        result = sorted(result.items(), key=lambda t: t[::-1], reverse=True)
        for i in range(7):
            print(f"{result[i][0]}: {result[i][1]} | {calculate_percentage_letters(file_name, result[i][1])}%")

def calculate_percentage_letters(file_name, number):
    """
    Calculates percentage of word frequency
    """
    amount_of_words = count_letters(file_name)

    result = number / amount_of_words * 100

    return round(result, 1)

def calculate_all(file_name):
    """
    Prints all categories
    """
    print(count_lines(file_name))
    print(count_words(file_name))
    print(count_letters(file_name))
    word_frequency(file_name)
    letter_frequency(file_name)

def change_file(request):
    """
    Function that lets user change file by input
    """
    with open(request, "r"):
        return request
