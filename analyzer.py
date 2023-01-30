""" Analyzer functions """


def count_lines(file_name):
    """ Counting lines from file """
    counter = 0
    with open(file_name) as filefetcher:
        for row in filefetcher.readlines():
            if row != "\n":
                counter += 1
    
    return counter

def count_words(file_name):
    """ Counting words from file """
    with open(file_name) as filefetcher:
        final_string = filefetcher.read().split()
            
    
    return len(final_string)

def count_letters(file_name):
    """ Counting letters from file """
    counter = 0
    with open(file_name) as filefetcher:
        for row in filefetcher.read():
            if row.isalpha():
                counter += 1
    
    return counter

def word_frequency(file_name):
    """ Get 7 most used words in textfile """
    final_string = ""
    with open(file_name) as filefetcher:
        final_string = filefetcher.read().split()

    word_f = { }

    for row in sorted(final_string, key=str.lower, reverse=True):
        #Tar bort tecken som ,.- intill ord
        row = ''.join(filter(str.isalpha, row.lower()))

        if row in word_f and len(row) > 1:
            word_f[row] += 1
        else:
            word_f.update({row: 1})

    return_string = ""
    for _ in range(0, 7):
        max_get = max(word_f, key=word_f.get)
        word_max = word_f.get(max_get)
        word_value = int(word_max)
        fetch_percent = str("{:.1f}".format((word_value / len(final_string) * 100)))

        return_string += str(max_get) + ": " + str(word_max) + " | " + fetch_percent + "% \n"
        word_f.pop(max(word_f, key=word_f.get), None)


    return return_string
    
def letter_frequency(file_name):
    """ Get 7 most used letters in textfile """
    final_string = ""
    with open(file_name) as filefetcher:
        final_string = filefetcher.read()

    word_f = { }
    final_string = ''.join(filter(str.isalpha, final_string))
    for row in sorted(final_string, key=str.lower, reverse=True):
        #Tar bort tecken som ,.- intill ord
        row = ''.join(filter(str.isalpha, row.lower()))

        if row in word_f:
            word_f[row] += 1
        else:
            word_f.update({row: 1})

    return_string = ""
    for _ in range(0, 7):
        max_get = max(word_f, key=word_f.get)
        word_max = word_f.get(max_get)
        word_value = int(word_max)
        fetch_percent = str("{:.1f}".format((word_value / len(final_string) * 100)))

        return_string += str(max_get) + ": " + str(word_max) + " | " + fetch_percent + "% \n"
        word_f.pop(max_get, None)


    return return_string

def all_function(file_name):
    """ Printing all frequencys """
    lines_string = str(count_lines(file_name)) + "\n"
    words_string = str(count_words(file_name)) + "\n"
    letters_string = str(count_letters(file_name)) + "\n"

    word_string = word_frequency(file_name)
    letter_string = letter_frequency(file_name)

    return lines_string + words_string + letters_string + word_string + letter_string
