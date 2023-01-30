"Analyzer functions"
def lines(txt):
    "Function that checks how many lines in txt file"
    with open(txt, "r") as linerd:
        count = 0
        for i in linerd:
            if i != "\n":
                count += 1
    return print(count)

def words(txt):
    "Function that checks how many words int text file"
    with open(txt, "r") as wordrd:
        count1 = 0
        wordrd1 = wordrd.read()
        count1 = len(wordrd1.split())
    return print(count1)

def letters(txt):
    "Function that checks how many total letter in txt file"
    with open(txt, "r") as letterrd:
        count2 = 0
        letr = letterrd.read()
        for i in letr:
            if i.isalpha():
                count2 += 1
    return print(count2)

def word_frequency(txt):
    """Function that checks the frequency of the first 7 words.
    Använder pylint disable här för att det inte går med .items()"""
    with open(txt, "r") as freqcy:
        dctwords = {}
        wordlist = freqcy.read()
        wordlist = wordlist.replace(".","")
        wordlist = wordlist.replace("\n"," ")
        wordlist = wordlist.replace(",","")
        wordlist = wordlist.split()
        totwordlst = len(wordlist)
        for i in wordlist:
            i = i.lower()
            if i not in dctwords:
                dctwords[i] = 1
            else:
                dctwords[i] += 1
        dctwords = dict(sorted(dctwords.items(), key = lambda x: x[1], reverse=True))
        srtdct = {}
        for val, ky in dctwords.items():
            if ky in dctwords.values():
                srtdct[ky] = []
        for val, ky in dctwords.items():
            if ky in dctwords.values():
                srtdct[ky].append(val)
        srtdct = {x:sorted(srtdct[x], reverse=True) for x in srtdct} #pylint: disable=c0206 
        dctword = {}
        for k in srtdct:
            for x in srtdct[k]:
                dctword[x] = k
        dctwords = dctword
            
        

        stransw = ""
        cntr=0
        dctansw = {}
        for values, keys in dctwords.items():
            if cntr < 7:
                dctansw[values] = keys
                divval = keys
                procentval = round((int(divval)/totwordlst)*100,1)
                if cntr < 6:
                    stransw += str(values) + ": " + str(keys) + " | " + str(procentval) + "%\n"
                else:
                    stransw += str(values) + ": " + str(keys) + " | " + str(procentval) + "%"
                cntr+=1
        return print(stransw)
    
        
def letter_frequency(txt):
    "Checks frequency of letters"
    with open(txt, "r") as freq:
        cntr = 0
        dctletr = {}
        letrlist = freq.read()
        letrlist = letrlist.replace(".","")
        letrlist = letrlist.replace("\n"," ")
        letrlist = letrlist.replace(",","")
        letrlist = letrlist.replace(" ", "")
        letrlist = letrlist.replace("-", "")
        letrlist = letrlist.rstrip()
        totletrlst = len(letrlist)
        for i in letrlist:
            i = i.lower()
            if i not in dctletr:
                dctletr[i] = 1
            else:
                dctletr[i] += 1
        dctletr = dict(sorted(dctletr.items(), key = lambda x: x[1], reverse=True))
        dctltransw = {}
        stransw1 = ""
        for values, keys in dctletr.items():
            if cntr < 7:
                dctltransw[values] = keys
                divval = keys
                #dctltransw = sorted(dctltransw)
                procentval = round((int(divval)/totletrlst)*100,1)
                if cntr < 6:
                    stransw1 += str(values) + ": " + str(keys) + " | " + str(procentval) + "%\n"
                else:
                    stransw1 += str(values) + ": " + str(keys) + " | " + str(procentval) + "%"
                cntr+=1      
        return print(stransw1)

def all(txt): #pylint: disable=W0622 
    """Prints all data, Använder pylint disable här för att jag får inte ändra på namnet till functionen,
    men namnet går emot inbyggda funtionen all!"""
    print(lines(txt))
    print(words(txt))
    print(letters(txt))
    print(word_frequency(txt))
    print(letter_frequency(txt))

def change():
    "Changes textfiles"
    while True:
        filinp = input("Write the file of input: ")
        if filinp == "phil.txt":
            break

        elif filinp == "lorum.txt":
            break
        
        else:
            print("Try again")
    return filinp

#getkey
#all()
#print(word_frequency())
#print(letter_frequency())         
