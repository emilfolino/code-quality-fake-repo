"""
Functions for analyzer
"""


def line_count(file):
    """
    Counts the lines
    """
    text = read_file(file)
    return len(text)

def word_count(file):
    """
    Counts the words
    """
    text = string_file(file)
    words = text.split(" ")
    return len(words)

def letter_count(file):
    """
    counts the letters
    """
    text = string_file(file)
    count = 0
    for letters in text:
        if letters in (" ", ".", ",", "-"):
            pass
        else:
            count += 1
    return count

def word_frequency(file):
    """
    Gets the word frequency
    """
    total = word_count(file)
    text = string_file(file)
    fix_text = remove_extra(text).lower()
    word = fix_text.split(" ")
    

    
    return count_sort(total, word)

def letter_frequency(file):
    """
    Gets the letter frequency
    """
    total = letter_count(file)
    text = string_file(file)
    fix_text = remove_extra(text).lower().strip()
    col_letter = ""

    for letter in fix_text:
        if letter == " ":
            pass
        else:
            col_letter += letter
    return count_sort(total, col_letter)


def print_freq(freq_data):
    """
    Prints the freq_data
    """
    for n in range(7):
        key = freq_data[n][0]
        times = freq_data[n][1][0]
        procent = freq_data[n][1][1]
        print(f"{key}: {times} | {procent}%")

def count_sort(total, text):
    """
    Counts and sorts the amout of times words and letters appear
    """
    dic = {}

    for n in text:
        dic[n] = ""

    for key in dic:
        count = 0
        for n in text:
            if n == key:
                count += 1
        procent = round((count/total)*100, 1)
        dic[key] = (count, procent)
    return sorted(sorted(dic.items(), reverse=True), key=lambda item: item[1], reverse=True)

def remove_extra(text):
    """
    Removes . and , for text
    """
    extra =  [".", ","]
    for n in extra:
        text = text.replace(n, "")
    return text

def remove_empty(text):
    """
    Removes empty rows and \n
    """
    newText = []
    for lines in text:
        if lines == "\n":
            pass
        else:
            lines = str(lines)
            newText.append(lines.replace("\n", " "))
    return newText

def read_file(file):
    """
    Reads file
    """
    with open(file, "r") as fh:
        text =  fh.readlines()
    return remove_empty(text)

def string_file(file):
    """
    Makes the read file in to string
    """
    text = read_file(file)
    return "".join(text)

def change():
    """
    Change the file
    """
    filename = input("Whats the name of the file you want to change to... ")
    return filename

if __name__ == "__main__":
    letter_frequency("phil.txt")
