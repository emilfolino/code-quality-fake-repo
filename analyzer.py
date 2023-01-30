"""
functions for main
"""

def lines(f):
    """ count lines in file """
    fil = open(f,"r")
    count = 0
    for a in fil:
        if a != "\n":
            count += 1
    print(count)

    fil.close()

def words(f):
    """ Count words """
    fil = open(f,"r")
    txt = fil.read()
    txt = txt.replace("\n", " ")
    l = txt.split(" ")
    print(len(l))
    fil.close()

def letters(f):
    """ Count letters """
    fil = open(f,"r")
    txt = fil.read()
    txt = ''.join(filter(str.isalnum, txt))
    print(len(txt))
    fil.close()

def word_frequency(f):
    """ Count Words """
    fil = open(f,"r")
    txt = fil.read()
    txt = txt.replace("\n", " ")
    l = txt.split(" ")
    fil.close()

    #gör alla ord lowercase och ta bort special char
    for a, _ in enumerate(l):
        l[a] = l[a].lower()
        l[a] = ''.join(filter(str.isalnum, l[a]))

    #räkna ord till ny dictionary
    d = {}

    for a in l:
        if a in d:
            d[a] += 1
        else:
            d[a] = 1

    total = 0 # total words
    for a in d.values():
        total += a

    #Sortera först bokstavs-ordning sedan value
    dS = sorted(d, reverse=True)
    dS = sorted(dS, key=d.get, reverse=True)

    #Ta 7 ord och printa dem
    for _, item in zip(range(7), dS):
        part = str(round((d[item]/total) * 100, 1))
        print(item + ": " + str(d[item]) + " | " + part + "%")

def letter_frequency(f):
    """ Count letters """
    fil = open(f,"r")
    txt = fil.read()
    txt = ''.join(filter(str.isalnum, txt))
    fil.close()

    #gör alla bokstäver lowercase
    txt = txt.lower()

    #räkna ord till ny dictionary
    d = {}

    for a in txt:
        if a in d:
            d[a] += 1
        else:
            d[a] = 1

    total = 0 # total letters
    for a in d.values():
        total += a

    #Sortera först bokstavs-ordning sedan value
    dS = sorted(d, reverse=True)
    dS = sorted(dS, key=d.get, reverse=True)

    #Ta 7 ord och printa dem
    for _, item in zip(range(7), dS):
        part = str(round((d[item]/total) * 100, 1))
        print(item + ": " + str(d[item]) + " | " + part + "%")

def all_f(f):
    """ Do Everything """
    lines(f)
    words(f)
    letters(f)
    word_frequency(f)
    letter_frequency(f)

def change():
    """ change file """
    x = input("--> ")
    return x
