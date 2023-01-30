'''
min analyzer fil
'''

def letter_freq_counter(filename, letter):
    """ used to find """
    r = open(filename, 'r').read().lower()
    return r.count(letter)

#######################################################

def line_count(filename):
    """ counts lines """
    num_lines = sum(1 for line in open(filename))
    print(num_lines)

def word_count(filename):
    """ counts words """
    r = open(filename, 'r').read()
    words = r.split()
    print(len(words))

def letter_count(filename):
    """ counts letters """
    r = open(filename, "r").read().replace(" ","").replace("\n","").replace(".","").replace(",","").replace("-","")
    print(len(r))

def word_freq(filename):
    """ print 7 words and their frequencies """

    file_ = open(filename)
    content = file_.read().lower()
    file_.close()


    words = {}
    for word in content.replace("\n", " ").replace(".","").replace(",","").split(" "):
        if word in words:
            words[word] += 1
        else:
            words[word] = 1

    sort_by_key = sorted(words.items(), key=lambda kv: kv[0], reverse=True)

    sorted_list = {}
    for i in range(len(words)):
        sorted_list[sort_by_key[i][0]] = sort_by_key[i][1]

    sorted_dict = sorted(sorted_list.items(), key=lambda kv: kv[1], reverse=True)

    letter_tot = 0
    for i in sorted_dict:
        letter_tot = letter_tot + i[1]
    for i in range(7):
        print(f"{sorted_dict[i][0]}: {sorted_dict[i][1]} | {round((sorted_dict[i][1] / letter_tot * 100), 1)}%")

def letter_freq(filename):
    """ print 7 letters and their frequencies """

    alphabet = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0,
    'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}
    for i in alphabet:
        alphabet[i] = letter_freq_counter(filename, i)

    sort_by_key = sorted(alphabet.items(), key=lambda kv: kv[0], reverse=True)

    sorted_list = {}
    for i in range(26):
        sorted_list[sort_by_key[i][0]] = sort_by_key[i][1]

    sorted_dict = sorted(sorted_list.items(), key=lambda kv: kv[1], reverse=True)


    letter_tot = 0
    for i in sorted_dict:
        letter_tot = letter_tot + i[1]
    for i in range(7):
        print(f"{sorted_dict[i][0]}: {sorted_dict[i][1]} | {round((sorted_dict[i][1] / letter_tot * 100), 1)}%")
        


def all_(filename):
    """ prints all of the above functions """
    line_count(filename)
    word_count(filename)
    letter_count(filename)
    word_freq(filename)
    letter_freq(filename)
