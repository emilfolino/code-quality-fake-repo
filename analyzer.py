"""
This module is containing all functions which are used to analyze the text file
"""

textfile = ["phil.txt"]

# with open(textfile[0], "r") as fd:
    # lines_str = fd.read().lower()
    # lines_lst = lines_str.split("\n")
    # lines_no_spaces = lines_str.split()
    # words = lines_str
    # for char in lines_str:
    #     if char in (',', '.', '\n', '-'):
    #         words = words.replace(char, "")

def amount_of_lines():
    """
    This function is for analyzing the amount of lines in a text file
    """
    with open(textfile[0], "r") as fd:
        lines_str = fd.read().lower()
        lines_lst = lines_str.split("\n")

    lines_amount = len(lines_lst)
    return lines_amount


def amount_of_words():
    """
    This function is for analyzing the amount of words in a text file
    """
    with open(textfile[0], "r") as fd:
        lines_str = fd.read().lower()
    
    words_amount = lines_str.split()
    return len(words_amount)
    

def amount_of_letters():
    """
    This function is for analyzing the amount of letters in a text file
    """
    with open(textfile[0], "r") as fd:
        lines_str = fd.read().lower()
        words = lines_str
        for char in lines_str:
            if char in (',', '.', '\n', '-'):
                words = words.replace(char, "")

    letters_amount = words.replace(" ", "")
    return len(letters_amount)

def word_frequency():
    """
    This function finds out the frequency of words in the text file
    """
    with open(textfile[0], "r") as fd:
        lines_str = fd.read().lower()
        lines_no_spaces = lines_str.split()

    word_count_dict = {}
    all_words = lines_str
    for char in " ".join(lines_no_spaces):
        if char in (',', '.'):
            all_words = all_words.replace(char, "")
    all_words = all_words.replace("\n", " ")

    unique_words = set(all_words.split())
    
    for word in unique_words:
        word_count_dict[word] = all_words.split().count(word)

    word_count_dict_key_sorted = dict(sorted(word_count_dict.items(), reverse=True))
    word_count_sorted = dict(sorted(word_count_dict_key_sorted.items(), key=lambda item: item[1], reverse=True))

    count = 0
    for word1 in word_count_sorted:
        if count < 7:
            word_amount = word_count_sorted.get(word1)
            percent = round(100 * (word_amount / amount_of_words()), 1)
            print(f"{word1}: {word_count_sorted.get(word1)} | {percent}%")
            count += 1

def letter_frequency():
    """
    This function finds out the frequency of letters in the text file
    """
    with open(textfile[0], "r") as fd:
        lines_str = fd.read().lower()
        words = lines_str
        for char in lines_str:
            if char in (',', '.', '\n', '-'):
                words = words.replace(char, "")
    letter_count_dict = {}
    letters = words.replace(" ", "")
    unique_letters = set(letters)

    for letter in unique_letters:
        letter_count_dict[letter] = letters.count(letter)

    letter_count_dict_key_sorted = dict(sorted(letter_count_dict.items(), reverse=True))
    letter_count_sorted = dict(sorted(letter_count_dict_key_sorted.items(), key=lambda item: item[1], reverse=True))

    count = 0
    for letter1 in letter_count_sorted:
        if count < 7:
            letter_amount = letter_count_sorted.get(letter1)
            percent = round(100 * (letter_amount / amount_of_letters()), 1)
            print(f"{letter1}: {letter_count_sorted.get(letter1)} | {percent}%")
            count += 1

def print_all():
    """
    This function prints all information about the text file
    """
    print(amount_of_lines())
    print(amount_of_words())
    print(amount_of_letters())
    word_frequency()
    letter_frequency()

def change(new_filename):
    """
    This function changes the text file
    """
    textfile.pop()  
    textfile.append(new_filename)
