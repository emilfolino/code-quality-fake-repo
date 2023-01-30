"""Module with functions for analyzer"""


def number_of_lines(selected_file="phil.txt"):
    """Returns number of lines"""
    return lines_words_letters(selected_file)[0]


def number_of_words(selected_file="phil.txt"):
    """Returns number of words"""
    return lines_words_letters(selected_file)[1]


def number_of_letters(selected_file="phil.txt"):
    """Returns number of letters"""
    return lines_words_letters(selected_file)[2]


def lines_words_letters(selected_file="phil.txt"):
    """Counts lines, words and letters from file"""
    with open(selected_file) as file:
        
        total_lines = 0
        total_words = 0
        total_letters = 0
        for line in file:
            line = line.rstrip().lower()
            words = line.split()
            
            total_lines += 1
            total_words += len(words)
            for letter in line:
                if letter not in (' ', ',', '.', '-'):
                    total_letters += 1
        return total_lines, total_words, total_letters

def word_frequency(selected_file="phil.txt"):
    """Returns frequency of words"""

    with open(selected_file) as file:
        words_dict = {}
        clean_words = []

        for line in file:
            line = line.rstrip().lower()
            words = line.split()

            for word in words:
                word = word.replace('.', '')
                word = word.replace(',', '')
                clean_words.append(word)
                
        for word in clean_words:

            words_dict[str(word)] = words_dict.get(word, 0) + 1


    words_dict = sorted(words_dict.items(), key=lambda x: (x[1],x[0]), reverse=True)
    words_list = []
    
    for word in words_dict:
        
        percentage = round((word[1] / number_of_words(selected_file)) * 100, 1)
        
        words_list.append(str(word[0]) + ": " + str(word[1]) + " | " + str(percentage) + "%")

        

    return words_list[0:7]

def letter_frequency(selected_file="phil.txt"):
    """Returns frequency of letters"""

    with open(selected_file) as file:
        
        letters_dict = {}
        clean_words = []

        for line in file:
            line = line.rstrip().lower()
            words = line.split()

            for word in words:
                word = word.replace('.', '')
                word = word.replace(',', '')
                clean_words.append(word)

        for word in clean_words:
            
            for letter in word:
                if letter.isalpha():
                    letters_dict[str(letter)] = letters_dict.get(letter, 0) + 1

        
        letters_dict = sorted(letters_dict.items(), key=lambda x: int(x[1]), reverse=True)
        letters_list = []

        for letter in letters_dict:
            
            percentage = round((letter[1] / number_of_letters(selected_file)) * 100, 1)

            letters_list.append(str(letter[0]) + ": " + str(letter[1]) + " | " + str(percentage) + "%")
            
        return letters_list[0:7]
