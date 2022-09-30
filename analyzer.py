"""
funktionerna för textanalysprogrammet
"""
the_text = "not changed"

def read_file():
    """
    funktions om läser in den initiella textfilen
    """
    global the_text
    with open("phil.txt", "r", encoding="utf-8") as f:
        the_text = f.read()

def change():
    """
    ändrar vilken fil som ska analyseras
    """
    global the_text
    in_file = input("Enter filename:\n")
    try:
        with open(in_file, "r") as f:
            the_text = f.read()
    except FileNotFoundError:
        print("File does not exist, nothing changed")

def lines():
    """
    returnerar antalet rader och dessa rader i en lista
    """
    lines_list = []
    for line in the_text.lower().split("\n"):
        if line == "\n":
            continue
        lines_list.append(line)
    return len(lines_list), lines_list

def words():
    """
    returnerar antalet ord och dessa ord i en lista
    """
    words_list = []
    for line in lines()[1]:
        for word in line.split():
            temp_word = ""
            for letter in word:
                if not letter.isalpha():
                    continue
                temp_word += letter
            words_list.append(temp_word)
    return len(words_list), words_list

def letters():
    """
    retrunerar antalet bokstäver och dessa bokstäver i en lista
    """
    letters_list = []
    for word in words()[1]:
        for letter in word:
            if not letter.isalpha():
                continue
            letters_list.append(letter)

    return len(letters_list), letters_list

def word_frequency():
    """
    retrunerar en lista med alla ord och hur många gånger de finns i texten
    """
    all_words = words()[1]
    words_dict = {}
    for word in all_words:
        words_dict[word] = words_dict.get(word, 0) +1

    words_list = []
    for word, freq in words_dict.items():
        words_list.append((freq, word))
    sorted_words_list = sorted(words_list, reverse=True)

    return sorted_words_list

def letter_frequency():
    """
    retrunerar en lista med alla bokstäver och hur många gånger de finns i texten
    """
    all_letters = letters()[1]
    letters_dict = {}
    for letter in all_letters:
        letters_dict[letter] = letters_dict.get(letter, 0) +1

    letters_list = []
    for letter, freq in letters_dict.items():
        letters_list.append((freq, letter))
    sorted_letters_list = sorted(letters_list, reverse=True)

    return sorted_letters_list

def dict_printer(alpha, all_alpha):
    """
    skriver ut formaterad information frequency funktionerna
    """
    for key, value in alpha[:7]:
        print("{value}: {key} | {procent:.1f}%".format(
                    value=value,
                    key=key,
                    procent=(key/all_alpha)*100
                    ))

def print_all():
    """
    printar ut all information i rätt format
    """
    sorted_tup_letters = letter_frequency()
    sorted_tup_words = word_frequency()
    print(lines()[0])
    print(words()[0])
    print(letters()[0])
    dict_printer(sorted_tup_words, words()[0])
    dict_printer(sorted_tup_letters, letters()[0])
