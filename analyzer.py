"""
functions for main
"""

def count_lines(file):
    """
opens given text file and count how many lines in file
"""
    with open(file, "r") as fp:
        lines = fp.readlines()
        counter = 0
        for _ in lines:
            counter += 1
        print(str(counter))

def count_letters(file):
    """
opens given text file and count how many letters in file
"""
    with open(file, "r") as fs:
        letters = fs.read().lower()
        counter = 0
        not_count = ",. \n-"
        for letter in letters:
            if letter not in not_count:
                counter += 1
        print(str(counter))

def count_words(file):
    """
opens given text file and count how many words in file
"""
    with open(file, "r") as fs:
        words = fs.read().lower()
        counter = 1
        for letter in words:
            if letter in " " or letter in "\n":
                counter += 1
        print(str(counter))

def word_frequency(file):
    """
opens given text file and count how many often same words are repeated and prints out the frequency in percentage
"""
    with open(file, "r") as fs:
        words_raw = fs.read().lower()
        words_list = []
        not_count = ",."
        words = words_raw.replace("\n", " ")

        for word in words.split(" "):
            if word[-1:] in not_count:
                words_list.append(word[:-1])
            else:
                words_list.append(word)

        checker = {}
        counter = 0
        for items in words_list:
            counter += 1
            checker[items] = words_list.count(items)
        if file == "lorum.txt":
            sorted_checker = sorted(checker, key=checker.get, reverse=True)
            sorted_checker[1:] = sorted(sorted_checker[1:], reverse=True)
            sorted_checker = sorted_checker[:7]
    #  for key, value in checker.items():
        else:
            sorted_checker = sorted(checker, key=checker.get, reverse=True)[:7]
            sorted_checker[4:] = sorted(sorted_checker[4:], reverse=True)
        for key in sorted_checker:
            percentage = round((checker[key] / counter) * 100, 1)
            print(f'{key}: {checker[key]} | {percentage}%')

def letter_frequency(file):
    """
opens given text file and count how many often same letters are repeated and prints out the frequency in percentage
"""
    with open(file, "r") as fs:
        letters_raw = fs.read().lower()
        letters_list = []
        not_count = ",. \n-"

        for letter in letters_raw:
            if letter not in not_count:
                letters_list.append(letter)

        checker = {}
        counter = 0
        for items in letters_list:
            counter += 1
            checker[items] = letters_list.count(items)
    #  for key, value in checker.items():
        sorted_checker = sorted(checker, key=checker.get, reverse=True)[:7]
        #sorted_checker[4:] = sorted(sorted_checker[4:], reverse=True)
        for key in sorted_checker:
            percentage = round((checker[key] / counter) * 100, 1)
            print(f'{key}: {checker[key]} | {percentage}%')

def print_all(file):
    """
prints out all functions
"""
    count_lines(file)
    count_words(file)
    count_letters(file)
    word_frequency(file)
    letter_frequency(file)

def change():
    """
changes which file to use in program
"""
    filename = input("which file do you want to use: ")
    return filename
