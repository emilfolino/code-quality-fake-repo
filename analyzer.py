"""funktioner för textanalysering"""
import string

# File opener
def file_opener(file_name):
    """Opens a the file"""
    try:
        with open(file_name, "r") as file_handler:
            all_data = file_handler.read()
        return all_data
    except FileNotFoundError:
        return None

# Remove excess characters
def lower_letters(letters):
    """Removes unvanted characters, turn all letters to lowercase"""
    letters = letters.translate(letters.maketrans('', '', string.whitespace))
    letters = letters.translate(letters.maketrans('', '', string.punctuation))
    letters = letters.lower()
    return(letters)

def file_to_word(words):
    """turns file data into words"""
    words = words.replace("\n"," ")
    words = words.split(" ")
    for i, word in enumerate(words):
        words[i] = lower_letters(word)
    return(words)


## count lines, words and letters
def line_count(lines):
    """Räkna antalet rader"""
    lines = lines.split("\n")
    print(len(lines))

def word_count(file):
    """Räkna antalet ord"""
    len_word = len(file_to_word(file))
    return len_word
    
def letter_count(file):
    """Räkna antalet bokstäver"""
    len_lett = len(lower_letters(file))
    return len_lett


## Count frequency of words and letters
def histogram(data, tot):
    """Calculates the frequency of words or letters"""
    d = {}
    t = []
    for part in data:
        d[part] = d.get(part, 0) +1 
    for letter, occurance in d.items():
        t.append((occurance, letter))
    t.sort(reverse=True)
    top_list = t[0:7]
    for occurance, letter in top_list:
        freq = round(100*occurance/tot,1)
        print(letter + ": " + str(occurance) + " | " + str(freq) + "%")


def word_frequency(file):
    """Calls on function to calculate frequency of words"""
    words = file_to_word(file)
    tot = word_count(file)
    histogram(words,tot)

def letter_frequency(file):
    """Calls on function to calculate frequency of letters"""
    letters = lower_letters(file)
    tot = letter_count(file)
    histogram(letters,tot)



## Other
def do_all(data):
    """Why not go crazy and call every function at once?"""
    line_count(data)
    print(word_count(data))
    print(letter_count(data))
    word_frequency(data)
    letter_frequency(data)
