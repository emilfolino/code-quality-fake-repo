"""
File containing functions for program.
"""
def count_lines(file_name):
    """
    Count lines in file.
    """
    with open(file_name, "r") as f:
        lines = f.readlines()
    return len(lines)

def count_words(file_name):
    """
    Count words in file.
    """
    word_count = 0
    with open(file_name, "r") as f:
        for line in f:
            words = line.split()
            word_count += len(words)
    return word_count

def count_letters(file_name):
    """
    Count letters in file.
    """
    with open(file_name, "r") as f:
        file_content = f.read()

    f_content_clean = file_content.replace("\n", "").replace(",", "").replace(".", "").replace("-", "").replace(" ","")

    return len(f_content_clean)

def word_frequency(file_name):
    """
    Return most used words in number and % in a file.
    """
    with open(file_name, "r") as f:
        file_content = f.read()

    words_clean = file_content.replace(",", "").replace(".", "").replace("-", "").lower()
    words_list = words_clean.split()

    return most_frequent(count_words(file_name), words_list)

def letter_frequency(file_name):
    """
    Return most used letters in number and % in a file.
    """
    with open(file_name, "r") as f:
        file_content = f.read()

    letter_list = list(file_content.replace(",", "").replace(".", "").replace("-", "").replace(" ", "").lower())

    return most_frequent(count_letters(file_name), letter_list)

def most_frequent(max_number, lst):
    """
    Helper for most frequent values in list.
    """
    lst.sort(reverse=True)
    most_freq_values = []

    while len(most_freq_values) < 7:
        frequent_value = max(lst, key = lst.count)
        freq_value_percent = round((lst.count(frequent_value)/max_number)*100, 1)
        most_freq_values.append(f"{frequent_value}: {lst.count(frequent_value)} | {freq_value_percent}%")
        while frequent_value in lst:
            lst.remove(frequent_value)

    return most_freq_values
