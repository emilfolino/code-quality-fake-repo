"""
Module for analyzing text
"""
import operator


def lines(filename):
    """
    Returns the amount of lines in the selected file
    :param filename:
    :return:
    """
    try:
        with open(filename) as fh:
            lns = 0
            for _ in fh:
                lns += 1
            return lns
    except FileNotFoundError:
        return "Wrong file, please select a new one."


def words(filename):
    """
    Returns the amount of words in the selected file
    :param filename:
    :return:
    """
    try:
        with open(filename) as fh:
            wds = 0
            for line in fh:
                line_list = line.split(" ")
                for _ in line_list:
                    wds += 1
        return wds
    except FileNotFoundError:
        return "Wrong file, please select a new one."


def letters(filename):
    """
    Returns the amount of letters in the selected file
    :param filename:
    :return:
    """
    try:
        with open(filename) as fh:
            ltrs = 0
            for line in fh:
                for letter in line:
                    if letter not in ('.', ',', ' ', '\n', '-'):
                        ltrs += 1
        return ltrs
    except FileNotFoundError:
        return "Wrong file, please select a new one."


def txt_to_string(filename):
    """
    Converts the .txt file to a string
    :param filename:
    :return:
    """
    with open(filename) as fh:
        final_string = ""
        for line in fh:
            for letter in line:
                if letter not in ('.', ',', '\n', '-'):
                    final_string += letter
                elif letter in ('.', ',', '\n', '-'):
                    final_string = final_string + " "
    return final_string


def percent_of_total(amount, total_words):
    """
    Returns the percent of the total words/letters
    :param amount:
    :param total_words:
    :return:
    """
    percent = round(float((amount / total_words) * 100), 1)
    percent = str(percent) + "%"
    return percent


def word_frequency(filename):
    """
    Returns the most used words
    :param filename:
    :return:
    """
    word_freq_dict = {}
    words_total = 0
    string_txt = txt_to_string(filename)
    list_txt = string_txt.split(" ")
    for item in list_txt:
        if item.lower() not in word_freq_dict and item != "":
            word_freq_dict[item.lower()] = 1
            words_total += 1
        elif item.lower() in word_freq_dict and item != "":
            word_freq_dict[item.lower()] += 1
            words_total += 1
    top_seven = sort_dict(word_freq_dict)[0:7]
    word_freq_dict = {}
    for item in top_seven:
        totp = percent_of_total(item[1], words_total)
        word_freq_dict[item[0]] = f": {str(item[1])} | {totp}"
    return output_format(word_freq_dict)


def output_format(dict_to_format):
    """
    Formats a string to print
    :param dict_to_format:
    :return:
    """
    final_string = ""
    for key, value in dict_to_format.items():
        if final_string == "":
            final_string = final_string + key + str(value)
        else:
            final_string = final_string + "\n" + key + str(value)
    return final_string


def sort_dict(dict_to_sort):
    """
    Sorts by value and letter
    :param dict_to_sort:
    :return:
    """
    sorted_dict = sorted(dict_to_sort.items(), key=operator.itemgetter(0), reverse=True)
    sorted_dict = sorted(sorted_dict, key=operator.itemgetter(1), reverse=True)
    return sorted_dict


def letter_frequency(filename):
    """
    Returns the frequency of the letters
    :param filename:
    :return:
    """
    with open(filename) as fh:
        letter_dict = {}
        letters_total = 0
        for line in fh:
            for letter in line:
                if letter in ('.', ',', '\n', '-', ' '):
                    pass
                else:
                    if letter.lower() in letter_dict:
                        letter_dict[letter.lower()] += 1
                        letters_total += 1
                    else:
                        letter_dict[letter.lower()] = 1
                        letters_total += 1
        letter_dict = sort_dict(letter_dict)
        letter_freq_dict = {}
        for item in letter_dict[:7]:
            totp = percent_of_total(item[1], letters_total)
            letter_freq_dict[item[0]] = f": {str(item[1])} | {totp}"
        return output_format(letter_freq_dict)


def do_all(filename):
    """
    Combines every function
    :param filename:
    :return:
    """
    to_return = str(lines(filename)) + "\n"
    to_return = to_return + str(words(filename)) + "\n"
    to_return = to_return + str(letters(filename)) + "\n"
    to_return = to_return + word_frequency(filename) + "\n"
    to_return = to_return + letter_frequency(filename)
    return to_return
