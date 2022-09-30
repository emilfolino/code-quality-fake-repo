"""
Analyzer functions
"""

def count_lines(file):
    """ 
    number of lines in the file
    """
    with open(file, "r") as fh:
        read_file = fh.readlines()
        line_amount = len(read_file)
        print(line_amount)

def count_words(file):
    """
    Number of words in the file
    """
    counter = 0
    with open(file, "r") as fh:
        read_file = fh.read()
        for word in read_file:
            words = word.split()
            counter += len(words)
            print(counter)


def count_letters(file):
    """
    Number of letters in the file
    """
    counter1 = 0
    with open(file, "r") as fh:
        read_file = fh.read()
        for letter in read_file:
            good_letter = letter.replace(",", "").replace(".", "").replace(" ", "").replace("-", "").replace("\n", "")
            if good_letter.isalpha:
                counter1 += 1
            else:
                counter1 += 0
            print(counter1)

def word_frequency(file):
    """
    Calculates frequency of words used in file
    """
    with open(file, 'r') as fh:
        frequency = {}
        words = fh.read().lower()
        modded_words = words.replace(",", " ").replace(".", "").split()
        frequency = {}
        for word in modded_words:
            frequency[word] = frequency.get(word, 0) + 1

        sort_by_word_value = sorted(frequency.items(), key=lambda x: x[1], reverse=True)

        for a, b in sort_by_word_value:
            word_total = len(modded_words)
            percentage = round(b / word_total * 100, 1)
            out = f"{a}: {b} | {percentage}%"
            print(out)




def letter_frequency(file):
    """
    Calculates frequency of letters used in file
    """
    with open(file, "r") as fh:
        letters = fh.read().lower()
        modded_letters = letters.replace(",", "").replace(".", "").replace(" ", "").replace("-", "").replace("\n", "")
        frequency = {}
        for letter in modded_letters:
            frequency[letter] = frequency.get(letter, 0) + 1

        sort_by_letter_value = sorted(frequency.items(), key=lambda x: x[1], reverse=True)

        for a, b in sort_by_letter_value:
            letter_total = len(modded_letters)
            percentage = round(b / letter_total * 100, 1)
            out = f"{a}: {b} | {percentage}%"
            print(out)




def all_functions(file):
    """
    Uses all functions
    """
    count_lines(file)
    count_words(file)
    count_letters(file)
    word_frequency(file)
    letter_frequency(file)


def change_file():
    """
    Change files to use
    """
    file = input("Enter which file should be used instead of the current one: ")
    return file
