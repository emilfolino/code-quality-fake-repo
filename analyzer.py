"""
Module Docstring
"""
def lines_checker(doc):
    """
    Checkin the things
    """
    with open(doc) as hd:
        e = hd.readlines()
        counter = 0
        counter = len(e)
        print(str(counter))
    return doc

def words_checker(doc):
    """
    Checkin the things
    """
    with open(doc) as hd:
        e = hd.read()
        stringen = ""
        counter = 0
        for d in e:
            stringen = stringen + d
        s = stringen.split()
        counter = len(s)
        print(str(counter))
    return doc

def char_checker(doc):
    """
    Checkin the things
    """
    with open(doc) as hd:
        e = hd.read()
        counter = 0
        for d in e:
            if d not in ("\n"," ",",",".","-"):
                counter = counter + 1
            else:
                continue
        print(counter)
    return doc

def word_frequency(doc):
    """
    Checkin the things
    """
    with open(doc) as hd:
        dicten = {}
        e = hd.read()
        stringen = ""
        returner = ""
        counter = 0
        count = 0
        for d in e:
            d = d.rstrip(",.")
            stringen = stringen + d.lower()
        s = stringen.split()
        for w in s:
            counter = counter + 1
            if w.lower() in dicten:
                dicten[w] += 1
            else:
                dicten[w] = 1
        dicten = {k: v for k,v in sorted(dicten.items(), key=lambda x: (x[1],x,[0]), reverse=True)}
        for (k,v) in dicten.items():
            returner = returner + k + ": " + str(v) + " | " + str(round((v * 100)/counter, 1)) + "%\n"
            if count == 6:
                break
            count = count + 1
        print(str(returner))
    return doc

def letter_frequency(doc):
    """
    Checkin the things
    """
    with open(doc) as hd:
        dicten = {}
        e = hd.read()
        stringen = ""
        returner = ""
        counter = 0
        count = 0
        for d in e:
            d = d.rstrip(",.- \n")
            stringen = stringen + d.lower()
        for c in stringen:
            counter = counter + 1
            if c.lower() in dicten:
                dicten[c] += 1
            else:
                dicten[c] = 1
        dicten = {k: v for k,v in sorted(dicten.items(), key=lambda x: (x[1],x,[0]), reverse=True)}
        for (k,v) in dicten.items():
            returner = returner + k + ": " + str(v) + " | " + str(round((v * 100)/counter, 1)) + "%\n"
            if count == 6:
                break
            count = count + 1
        print(str(returner))
        return doc

def alles(doc):
    """
    Checkin all the things
    """
    lines_checker(doc)
    words_checker(doc)
    char_checker(doc)
    word_frequency(doc)
    letter_frequency(doc)
    return doc

def changer_phile(rimput):
    """
    Changer the filythings
    """
    fil = rimput
    return fil
