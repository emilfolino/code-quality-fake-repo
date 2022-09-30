"""
Description
"""
from operator import itemgetter

# Går också att import string och sen skriva string.ascii_lowercase så får man ut en sån sträng där
# list(string.ascii_lowercase får ut identisk lista som nedan).
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


# def all(file_name):
#     """
#     Performs all functions and return result in a string
#     """
#     str_return = f"{lines(file_name)} \n {words(file_name)}"
#     return str_return

def lines(file_name):
    """
    Return the lines in a file
    """
    return(len(return_from_file(file_name, "l")))


def words(file_name):
    """
    Returns the words in a file
    """
    return(len(return_from_file(file_name, "w")))


def letters(file_name):
    """
    Returns the letters in a file
    """
    return(len(return_from_file(file_name, "c")))


def word_frequency(file_name):
    """
    Returns the seven most frequent word in a file
    """
    words_list = return_from_file(file_name, "w")
    freq_list = check_frequency(words_list)
    str_return = ""
    for tup in freq_list:
        str_return += f"{tup[0]}: {tup[1]} | {round(tup[1] * 100 /len(words_list), 1)}%\n"
    return(str_return.strip())


def letter_frequency(file_name):
    """
    Returns the seven most frequent word in a file
    """
    words_list = return_from_file(file_name, "c")
    freq_list = check_frequency(words_list)
    str_return = ""
    for tup in freq_list:
        str_return += f"{tup[0]}: {tup[1]} | {round(tup[1] * 100 /len(words_list), 1)}%\n"
    return(str_return)


def return_from_file(file_name, what_to_return):
    """
    Returns a list of either all lines, words or characters in a file.
    As second argument, choose 'l' for lines, 'w' for words or 'c' for characters
    'c' is chosen if no other valid arg is given
    """
    lines_return = []
    words_return = []
    chr_return = []

    with open(file_name) as f:
        for line in f:
            lines_return.append(line)

            words_in_line = line.split()
            for word in words_in_line:
                word = word.replace(",", "")
                word = word.replace(".", "")
                words_return.append(word)

            for c in line:
                if c.lower() in alphabet:
                    chr_return.append(c)

    if (what_to_return == "l"):
        return lines_return
    if (what_to_return == "w"):
        return words_return
    return chr_return


def check_frequency(list_check):
    """
    Returns the seven most frequent elements in a list
    """

    list_check_lower = []
    for el in list_check:
        list_check_lower.append(el.lower())

    dict_count = {}

    for el in list_check_lower:
        if el.lower() in dict_count:
            dict_count[el] += 1
        else:
            dict_count[el] = 1

    list_items = []
    for tup in dict_count.items():
        list_items.append(tup)

    # Sorterar först alla på key (omvänd bokstavsordning)
    # sorted_list = sorted(list_items, key=key_lower)
    sorted_list = sorted(list_items, reverse=True)

    # Sorterar sedan alla på value med itemgetter (import operator) från störst till minst
    sorted_list = sorted(sorted_list, key=itemgetter(1), reverse=True)

    # Väljer de sju med störst värde
    sorted_list = sorted_list[0:7]

    return sorted_list


# def key_lower(tup):
#     """
#     Assuming it's a string, return the first element in tuple in lower case.
#     """
#     return (tup[0].lower())
