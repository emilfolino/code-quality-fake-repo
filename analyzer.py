"""
Analyzer funtions
"""

def file_open(text_file):
    """
    opens files
    """
    try:
        with open(text_file) as filehold:
            whole_text = filehold.read()
        return whole_text
    except FileNotFoundError as file_not_exist:
        raise FileNotFoundError("File does not exist! Please change file") from file_not_exist

def line_count(text_file):
    """
    counts lines in files
    """
    text = file_open(text_file)
    line_count_ = 1
    for line in text:
        if line == "\n":
            line_count_ +=1
    return(line_count_)

def word_count(text_file):
    """
    counts words in files
    """
    text = file_open(text_file)
    list_of_text = text.split()
    word_count_ = 0
    for words in list_of_text:
        words = words.rstrip()
        words = words.translate(words.maketrans("","","!.,?-#@£$"))
        word_count_ += 1
    return(word_count_)

def letter_count(text_file):
    """
    counts letters in files
    """
    text = file_open(text_file)
    letter_count_ = 0
    for letter in text:
        if letter.isalnum():
            letter_count_ += 1
    return(letter_count_)
    
def word_frequency(text_file):
    """
    Checks how often words are used in files
    """
    text = file_open(text_file)
    words = {}
    list_of_words = text.split()
    for word in list_of_words:
        word = word.rstrip()
        word = word.translate(word.maketrans("","","!.,?-#@£$"))
        word = word.lower()
        wordlist = word.split()
        for word_in_list in wordlist:
            if word_in_list not in words:
                words[word_in_list] = 1
            else:
                words[word_in_list] += 1
     
    sorted_dict = sorted(words.items(), key=lambda k: (k[1], k[0]), reverse = True)
    sorted_str = ""
    
    for items in sorted_dict[:7]:
        item = items[0]
        percentage = round(items[1]/word_count(text_file) * 100,1)
        sorted_str += item + ": " + str(items[1]) + " | " + str(percentage) + "%\n"
    return(sorted_str)
    
def letter_frequency(text_file):
    """
    Checks how often letters are used in files
    """
    text = file_open(text_file)
    letters = {}
    for letter in text:
        letter = letter.rstrip()
        letter = letter.translate(letter.maketrans("","","!.,?-#@£$"))
        letter = letter.lower()
        letterlist = letter.split()
        for letter_in_list in letterlist:
            if letter_in_list not in letters:
                letters[letter_in_list] = 1
            else:
                letters[letter_in_list] += 1
    sorted_dict = sorted(letters.items(), key=lambda k: (k[1], k[0]), reverse = True)
    sorted_str = ""

    for items in sorted_dict[:7]:
        item = items[0]
        percentage = round(items[1]/letter_count(text_file) * 100,1)
        sorted_str += item + ": " + str(items[1]) + " | " + str(percentage) + "%\n"
    return(sorted_str)

def all_(word_count_, line_count_, letter_count_, word_frequency_, letter_frequency_):
    """
    writes all functions returns
    """
    all_str = (str(line_count_) + "\n" + str(word_count_) + "\n" + str(letter_count_) + "\n" +
    str(word_frequency_) + str(letter_frequency_) + "\n")
    return all_str
    