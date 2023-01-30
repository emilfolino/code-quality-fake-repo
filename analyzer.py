"""
Functions for the analyzer program
"""

def line_count(file_choice="phil.txt"):
    """
    Returns the amount of lines inside the file
    """
    with open(file_choice, "r") as fd:
        content = fd.readlines()
        counter = 0
        for _ in content:
            counter += 1
    return counter

def word_count(file_choice="phil.txt"):
    """
    Returns the amount of words inside the file
    """
    with open(file_choice, "r") as fd:
        content = fd.readlines()
        counter = 0
        for words in content:
            new_line = words.split(" ")
            counter += len(new_line)
    return counter

def letter_count(file_choice="phil.txt"):
    """
    Returns the amount of letters inside the file
    """
    with open(file_choice, "r") as fd:
        content = fd.readlines()
        counter = 0
        for words in content:
            for letters in words:
                if letters.isalpha():
                    counter += 1
    return counter

def word_frequency(file_choice="phil.txt"):
    """
    Returns statistics regarding the word frequency inside the file
    """
    with open(file_choice) as fd:
        content = fd.read().lower()
        content = content.replace(",", "")
        content = content.replace(".", "")
        content = content.replace("\n", " ")
        word_content = content.split(" ")
        word_content.sort()
        word_freq = {}
        for word in word_content:
            word_freq[word] = round(((word_content.count(word) / len(word_content)) * 100), 1)
        word_freq = dict(sorted(word_freq.items(), reverse=True, key=lambda item: item[1]))
        for word in word_freq:
            word_freq[word] = str(word_content.count(word)) + " | " + str(word_freq[word]) + "%"
        for key in word_freq:
            print(key + ": " + str(word_freq[key]))

def letter_frequency(file_choice="phil.txt"):
    """
    Returns statistics regarding the letter frequency inside the file
    """
    with open(file_choice) as fd:
        content = fd.read().lower()
        content = content.replace(",", "")
        content = content.replace(".", "")
        content = content.replace("\n", " ")
        content = content.replace(" ", "")
        content = content.replace("-", "")
        letter_content = list(content)
        letter_content.sort()
        letter_freq = {}
        for letter in letter_content:
            letter_freq[letter] = round(((letter_content.count(letter) / len(letter_content)) * 100), 1)
        letter_freq = dict(sorted(letter_freq.items(), reverse=True, key=lambda item: item[1]))
        for letter in letter_freq:
            letter_freq[letter] = str(letter_content.count(letter)) + " | " + str(letter_freq[letter]) + "%"
        for key in letter_freq:
            print(key + ": " + str(letter_freq[key]))

def print_all(file_choice="phil.txt"):
    """
    Prints out all the statistics inside the file
    """
    print(line_count(file_choice))
    print(word_count(file_choice))
    print(letter_count(file_choice))
    word_frequency(file_choice)
    letter_frequency(file_choice)

def change_file(file_name):
    """
    Function to change the file from the default file
    """
    return file_name

if __name__ == "__main__":
    pass
