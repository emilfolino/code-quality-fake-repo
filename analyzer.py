# Du skall skapa funktioner för textanalysering i modulen analyzer.py.

# Analysera antal rader (ej tomma), ord och bokstäver med menyvalen lines, words och letters. 
# Skriv minst en funktion för varje kommando i analyzer.py.

# def append_or_write_to_file(filename, content, mode):
#     with open(filename, mode) as fd:
#         fd.write(content)

"""
Main analyzer functions
"""

def line_count(filename):
    """
    Counts amount of lines in a file
    """
    with open(filename) as fh:
        lines = 0
        for line in fh.readlines():
            if line == '\n':
                continue
            lines += 1
    return lines

# Borde gå att kombinera med word_frequency
def word_count(filename):
    """
    Counts amount of words in a file
    """
    with open(filename) as fh:
        content = fh.read()
        content_list = content.split()
        words = len(content_list)
    
    return words

def letter_count(filename):
    """
    Counts amount of letters in a file
    """
    with open(filename) as fh:
        letters = 0
        content = fh.read()
        for char in content:
            if char.isalnum():
                letters += 1
    
    return letters

#Borde gå att kombinera med word_count
def word_frequency(filename, amount=7):
    """
    Creates a dictionary over most frequent words in a file
    """
    with open(filename) as fh:
        word_dic = {}
        content = fh.read()
        words = content.lower().split()
        for word in words:
            word = ''.join(filter(str.isalnum, word))
            word_dic[word] = word_dic.get(word, 0) + 1
    
    for key, value in word_dic.items():
        word_dic[key] = [
            value, calculate_percentage(value / word_count(filename))
            ]
    
    sorted_dic = sort_dictionary(word_dic)

    print_dictionary(sorted_dic, amount)

def letter_frequency(filename, amount=7):
    """
    Creates a dictionary over most frequent letters in a file
    """
    with open(filename) as fh:
        letter_dic = {}
        content = fh.read()
        for letter in content.lower():
            if letter.isalpha():
                letter_dic[letter] = letter_dic.get(letter, 0) + 1
    
    for key, value in letter_dic.items():
        letter_dic[key] = [
            value, calculate_percentage(value / letter_count(filename))
        ]
    sorted_dic = sort_dictionary(letter_dic)
    print_dictionary(sorted_dic, amount)

def print_dictionary(sorted_dic, amount):
    """
    Prints a dictionary
    """
    for index, ki in enumerate(sorted_dic):
        if amount is None or index < amount:
            print(f'{ki[0]}: {ki[1][0]} | {ki[1][1]}')

def calculate_percentage(floating_point):
    """
    Converts from floating point number to percent
    """
    return f'{round((floating_point * 100), 1)}%'

def sort_dictionary(dictionary):
    """
    Sorts dictionary first by value, then by key
    """
    data = sorted(dictionary.items(), key = lambda x: (x[1], x[0]), reverse=True)
    return data

def do_everything(filename):
    """
    Calls all functions above
    """
    print(line_count(filename))
    print(word_count(filename))
    print(letter_count(filename))
    word_frequency(filename)
    letter_frequency(filename)
