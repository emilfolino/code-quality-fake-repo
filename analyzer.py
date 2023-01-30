"""
Functions for textanalyzing
"""
import string

def count(choice, filename):
    """
    Counts lines, words or letters
    """
    if choice == "lines":
        with open(filename) as fhand:
            num_of_lines_list = fhand.readlines()
        return(len(num_of_lines_list))

    if choice == "words":
        with open(filename) as fhand:
            num_of_words = fhand.read()

        num_of_words = num_of_words.replace("\n", " ")
        num_of_words_list = num_of_words.split(" ")
        return(len(num_of_words_list))

    if choice == "letters":
        with open(filename) as fhand:
            num_of_letters = fhand.read()

        num_of_letters = num_of_letters.lower()
        num_of_letters = num_of_letters.translate(num_of_letters.maketrans('', '', string.punctuation))
        num_of_letters = num_of_letters.replace(" ", "").replace("\n", "")
        return(len(num_of_letters))
    return(0)

def frequency(choice, filename):
    """
    Defines frequency for words or letters
    """

    if choice == "word_frequency":
        with open(filename) as fhand:
            text = fhand.read()

        text = text.translate(text.maketrans('', '', string.punctuation))
        text = text.lower()
        text = text.rstrip()
        words = text.split()

        d = {}
        for c in words:
            d[c] = d.get(c, 0) + 1

        d = sorted(d.items(), key=lambda i: i[::-1], reverse=True)

        for key, value in d[:7]:
            print(f"{key}: {value} | {round((value / count('words', filename)) * 100, 1)}%")

    if choice == "letter_frequency":
        with open(filename) as fhand:
            text = fhand.read()

        d = {}
        text = text.lower()
        text = text.rstrip()
        text = text.translate(text.maketrans('', '', string.punctuation))
        letters = text.replace(" ", "")

        for c in letters:
            d[c] = d.get(c, 0) + 1

        d = sorted(d.items(), key=lambda i: i[::-1], reverse=True)

        for key, value in d[:7]:
            print(f"{key}: {value} | {round((value / count('letters', filename)) * 100, 1)}%")

def print_all(filename):
    """
    Prints all results from all analyzes
    """
    lst = [count("letters", filename), count("lines", filename), count("words", filename)]
    lst.sort()
    lst = '\n'.join(map(str, lst))
    print(lst)

    return(str(frequency("word_frequency", filename)) + str(frequency("letter_frequency", filename)))
