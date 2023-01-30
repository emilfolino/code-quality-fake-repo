"""
functions for analyzing a text-file
"""
import string
from operator import itemgetter

def prepare_file2(a):
    """
    Prepare the contents of a txt-file for further analysis. Read the contents of the file, strip, lowercase it and
    remove punctuation. #Please note: " "(white space) and "\n"(newline) remain.
    Return: the prepared contents as a string.
    """
    with open(a) as f:
        content = f.read()
    line = content.strip().lower()
    line = line.translate(line.maketrans('', '', string.punctuation))

    return line


def lines(a):
    """
    Count and return the number of lines in the prepared text file
    a: name of the txt-file to use
    Return: number of lines
    """
    this_text = prepare_file2(a)
    this_text = this_text.split("\n")

    return len(this_text)


def words(a):
    """
    Count and return the number of words in the prepared text file.
    a: name of the txt-file to use
    Return: number of words
    """
    this_text = prepare_file2(a)
    these_words = this_text.split()

    return len(these_words)


def letters(a):
    """
    Remove white space and newline characters.
    Count and return the number of letters in the prepared text file.
    a: name of the txt-file to use
    Return: number of letters
    """
    this_text = prepare_file2(a)
    this_text = this_text.replace(" ", "").replace("\n", "")

    return len(this_text)


def sort_and_print_list(the_list, a, word_or_letter):
    """
    Sort and print a list of tuples. First sort on the first element then on the second.
    Then print the list as well as relative frequencies (total count from file a).
    the_list:  a list of tuples
    a: name of the txt-file to use
    word_or_letter: decides which type of counting to do on file a.
    """
    counts = {}
    for word in the_list:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1

    strange_order = sorted(counts.items(),reverse=True, key=itemgetter(0))
    final_list = sorted(strange_order,reverse=True, key=itemgetter(1))

    total = 1
    if word_or_letter == "use_word":
        total = words(a)
    elif word_or_letter == "use_letter":
        total = letters(a)

    for i in range(7):
        print(f"{final_list[i][0]}: {final_list[i][1]} | {round((100*final_list[i][1])/total,1)}%")


def letter_frequency(a):
    """
    Print table of letters and their frequencies by preparing the file and calling sort_and_print_list().
    a: file to process
    """
    this_text = prepare_file2(a)
    this_text = this_text.replace(" ", "").replace("\n", "")

    word_or_letter = "use_letter"
    sort_and_print_list(this_text, a, word_or_letter)



def word_frequency(a):
    """
    Print table of words and their frequencies by preparing the file and calling sort_and_print_list().
    a: file to process
    """
    this_text = prepare_file2(a)
    these_words = this_text.split()

    word_or_letter = "use_word"
    sort_and_print_list(these_words, a, word_or_letter)

def all_included(a):
    """
    Print all text data.
    """
    print(lines(a))
    print(words(a))
    print(letters(a))
    word_frequency(a)
    letter_frequency(a)

###
if __name__ == "__main__":
    print("Hello from module: analyzer2.py")
    #a = "phil.txt"
    # result = prepare_file2(a)
    # print(result)
    # result2 = letters(a)
    # print(result2)
    # result3 = words(a)
    # print(result3)
    # result4 = lines(a)
    # print(result4)
    # result5 = word_frequency(a)
    # print(result5)
    #result6 = letter_frequency(a)
    #print(result6)
