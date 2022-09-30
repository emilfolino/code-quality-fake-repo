"""
In this module we have function regarding to text analyzing.
"""

file = "phil.txt"


def get_file_content() -> list:
    """
    This function returns the content of the file.
    """
    fopen = open(file)
    content = fopen.readlines()
    fopen.close()
    return content


def count_lines() -> int:
    """
    This function will count the number of lines in the file.
    """
    return len(get_file_content())


def count_words():
    """
    This function will count the number of words in the file
    """
    number_of_words = 0
    content = get_file_content()
    for line in content:
        number_of_words += len(line.split())
    return number_of_words


def count_letters():
    """
    This function will count the number of letters
    """
    number_of_letters = 0
    content = get_file_content()
    for line in content:
        for word in line.split():
            number_of_letters += len(clean(word))
    return number_of_letters


def clean(word: str) -> str:
    """
    This method will clean a word from , .
    """
    letters = list(word)
    if "," in word:
        letters.remove(",")

    if "." in word:
        letters.remove(".")

    if "-" in word:
        letters.remove("-")
    return "".join(letters)


def word_frequency():
    """
    This method returns the frequency for every word.
    """
    freq = get_word_frequency()
    sorted_freq = sort_dictionary(freq, True)
    return add_frequency(sorted_freq, count_words())


def alphabetical_sorted(dictionary: dict, rev: bool):
    """
    Sorts a dictionary alphabetical
    """
    temp_dict = {}
    for key in sorted(dictionary.keys(), reverse=rev):
        temp_dict[key] = dictionary[key]
    return temp_dict


def sort_dictionary(freq, at5: bool):
    """
    Sorts a given dictionary.
    """
    sorted_dict = {}
    value_sorted = dict(sorted(freq.items(), key=lambda item: item[1], reverse=True))
    for _, v1 in value_sorted.items():
        value = v1
        temp_dict = {}
        for key2, v2 in value_sorted.items():
            if v2 == value:
                temp_dict[key2] = value_sorted[key2]
        if at5 and value == 5:
            temp_dict = alphabetical_sorted(temp_dict, True)
        else:
            temp_dict = alphabetical_sorted(temp_dict, True)
        for key3, _ in temp_dict.items():
            sorted_dict[key3] = temp_dict[key3]
    return sorted_dict


def get_word_frequency():
    """
    This method return the word frequency
    """
    number_of_words = {}
    content = get_file_content()
    for line in content:
        for word in line.split():
            word = clean(word).lower()
            if word in number_of_words.keys():
                number_of_words[word] += 1
            else:
                number_of_words[word] = 1
    return number_of_words


def get_letter_frequency():
    """
    This method return the word frequency
    """
    number_of_letters = {}
    content = get_file_content()
    for line in content:
        for word in line.split():
            for letter in str(word).lower():
                if letter in number_of_letters.keys():
                    number_of_letters[letter] += 1
                else:
                    number_of_letters[letter] = 1
    return number_of_letters


def add_frequency(dictionary: dict, total: int):
    """
    Adds frequency for each word number.
    """
    for key in dictionary:
        dictionary[key] = [
            dictionary[key],
            round(100 * dictionary[key] / total, 1)
        ]
    return dictionary


def letter_frequency():
    """
    This method return the frequency for every letter.
    """
    freq = get_letter_frequency()
    sorted_freq = sort_dictionary(freq, False)
    return add_frequency(sorted_freq, count_letters())


def print_frequency(res: dict, param):
    """
    Prints a dictionary with frequencies.
    """
    it = 0
    for key in res:
        if it == param:
            break
        print(key + ": " + str(res[key][0]) + " | " + str(res[key][1]) + "%")
        it += 1


def set_file(new_file):
    """
    This method sets the file path.
    """
    global file
    file = new_file
