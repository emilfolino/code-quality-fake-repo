"""
analyzer
"""

choose = 'phil.txt'
def lines():
    """
    lines
    """
    global choose
    with open(choose,"r") as linesCounter:
        linesCount = len(linesCounter.readlines())
        return linesCount
        
def Words():
    """
    words
    """
    global choose
    with open(choose,"r") as wordsCounter:
        num_words = 0
        for line in wordsCounter:
            words = line.split()
            num_words += len(words)
        return num_words

def Letters():
    """
    letters
    """
    global choose
    with open(choose,"r") as lettersCounter:
        lettersCount = 0
        for letters in lettersCounter.read():
            if letters.isalpha():
                lettersCount += 1
        return lettersCount

def word_frequency():
    """
    word_frequency
    """
    global choose
    with open(choose,"r") as word_freq:
        text = str(word_freq.read())
        words = text.lower().replace(',','').replace('.','').split()
        dict_of_counts = {item:words.count(item) for item in words}
        newDic = {k: v for k, v in sorted(dict_of_counts.items(), key=lambda t: t[::-1], reverse= True)}
        return newDic,len(words)
        

def letter_frequency():
    """
    letter_frequency
    """
    global choose
    with open(choose,"r") as letters_freq:
        textL = str(letters_freq.read())
        letters = textL.lower().replace('-','').replace(',','').replace('.','').replace(' ','').replace('\n','')
        letters_count = {item:letters.count(item) for item in letters}
        newLDic = {k: v for k, v in sorted(letters_count.items(), key=lambda t: t[::-1], reverse= True)}
        return newLDic,len(letters)

def All():
    """
    all
    """
    firstText = f'{lines()}\n'\
                  f'{Words()}\n'\
                  f'{Letters()}\n'
    data = word_frequency()
    keyList = list(data[0].keys())
    valueList = list(data[0].values())
    textToShow = ''
    index = 0
    for _ in range(7):
        textToShow = textToShow + f'{keyList[index]}: {valueList[index]} |'\
            f' {round( int(valueList[index]) / data[1] * 100, 1)}%\n'
        index += 1
    l_Data = letter_frequency()
    letter_key = list(l_Data[0].keys())
    letter_value = list(l_Data[0].values())
    lettersToShow = ''
    l_index = 0
    for _ in range(7):
        lettersToShow = lettersToShow + f'{letter_key[l_index]}: {letter_value[l_index]} |'\
            f' {round(int(letter_value[l_index]) / l_Data[1] * 100, 1)}%\n'
        l_index += 1
   
    finalText = firstText + textToShow + lettersToShow
    print(finalText)
    
def change():
    """
    change
    """
    choice = input("Enter filename: ")
    global choose
    if choice == 'phil.txt':
        choose = choice
        print('you are in file phil.txt now')
    elif choice == 'lorum.txt':
        choose = choice
        print('you are in file lorum.txt now')
    else:
        print('no such file')


      

        
             
       