"""
Du skall skapa funktioner för textanalysering i modulen analyzer.py.
"""

from operator import itemgetter

def lines(file):
    """
    Räknar hur många rader det finns
    """
    with open(file, "r") as fd:
        textlines = fd.readlines()

    counter = 0
    for line in textlines:
        if line == "\n":
            pass
        else:
            counter += 1
    return counter

def get_words(file):
    """
    Hämtar alla orden från en fil
    """
    with open(file, "r") as fd:
        textlines = fd.readlines()

    a_string = ""

    for textline in textlines:
        if textline[-2:] == ".\n":
            textline = textline[:-2] + " "

        elif textline[-1:] == "\n":
            textline = textline[:-1]

        for word in textline:
            if "," in word:
                word = word[:-1]
            elif "." in word:
                word = word[:-1]

            a_string += word

    text = a_string.split(" ")

    return text

def words(file):
    """
    Räknar hur många ord
    """
    text = get_words(file)

    counter = 0
    for word in text:
        word = word + ""
        counter += 1

    return counter



def letters(file):
    """
    Räkna antal bokstäver
    """
    text = get_words(file)

    counter = 0

    for word in text:
        for letter in word:
            if letter == "-":
                pass
            else:
                counter += 1

    return counter


def word_frequency(file):
    """
    Analysera ordfrekvensen
    """
    text = get_words(file)

    word_freq = {}

    for word in text:
        word = word.lower()
        word_freq[word] = 0
        for word2 in text:
            word2 = word2.lower()
            if word == word2:
                if word in ("", " "):
                    pass
                else:
                    word_freq[word] += 1

    word_freq_as_list = word_freq.items()
    word_freq_sorted = sorted(word_freq_as_list, key=itemgetter(1), reverse=True)

    total_words = words(file)

    for word, freq in word_freq_sorted:
        freq_p = round(freq / total_words * 100, 1)

        print(word + ": " + str(freq) + " | " + str(freq_p) + "%")


def letter_frequency(file):
    """
    Analysera bokstavsfrekvensen
    """
    text = get_words(file)

    letter_freq = {}
    new_text = ""

    for word in text:
        word = word.lower()
        new_text += word

    for letter in new_text:
        letter_freq[letter] = 0
        for letter2 in new_text:
            if letter == letter2:
                letter_freq[letter] += 1


    letter_freq_as_list = letter_freq.items()
    letter_freq_sorted = sorted(letter_freq_as_list, key=itemgetter(1), reverse=True)

    total_letters = letters(file)

    for letter, freq in letter_freq_sorted:
        freq_p = round(freq / total_letters * 100, 1)

        print(letter + ": " + str(freq) + " | " + str(freq_p) + "%")
