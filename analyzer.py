"""Contains functions for the analyzer"""

def get_file_content(filename):
    """Reads and returns content of a file"""
    with open(filename) as filehandle:
        return filehandle.read()

def get_words(filename):
    """Returns words in file as a list"""
    content = get_file_content(filename)
    content = content.lower()
    content = content.replace(",", "").replace(".", "")
    return content.split()

def get_letters(filename):
    """Returns a string with only letters read from given file"""
    content = get_file_content(filename)
    content = content.lower()
    for char in ["\n", ",", ".", "-", " "]:
        if char in content:
            content = content.replace(char, "")
    return content

def count_lines(filename):
    """Counts number of non-empty lines in a file"""
    content = get_file_content(filename)
    content_as_list = content.split("\n")

    return len(content_as_list)

def count_words(filename):
    """Counts number of words in a file"""
    words = get_words(filename)
    return len(words)

def count_letters(filename):
    """Counts number of letters in a file"""
    return len(get_letters(filename))

def print_frequency(el_list, print_num=7):
    """Prints frequency of top elements in a list, default is 7"""

    # Create a dict with elements and count up each time a duplicate is found
    el_dict = {}
    for element in el_list:
        if element in el_dict:
            el_dict[element] += 1
        else:
            el_dict[element] = 1

    # Make a sorted list of element-count tuples, sorted on values in the dictionary
    frequency_list = sorted(el_dict.items(), key=lambda x: (x[1],x[0]), reverse=True)

    # Print top 7
    for element in frequency_list[:print_num]:
        print(element[0] + ": " + 
        str(element[1]) + " | " + 
        str(round((element[1] / len(el_list)) * 100, 1)) + "%"
        )

def word_frequency(filename):
    """Count frequency of words in a file, return percentages of the 7 most common"""
    words = get_words(filename)
    print_frequency(words)

def letter_frequency(filename):
    """Count frequency of letters in a file, return percentages of the 7 most common"""
    letters = get_letters(filename)
    print_frequency(letters)
