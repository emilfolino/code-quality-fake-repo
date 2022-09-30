'''
min menu fil
'''

import analyzer

def loop():
    """ a function for looping the program """
    filename = "phil.txt" 

    while True:
        print("\nPrint either of these options:\n")
        print("q) Ends the program")
        print("lines) Let me print the amount of lines")
        print("words) Let me print the amount of words")
        print("letters) Let me print the amount of letters")
        print("word_frequency) Let me compare words")
        print("letter_frequency) Let me compare letters")
        print("all) Do all of the above")
        print("change) Change textfile to read from")

        choice = input("--> ")

        if choice == "q":
            break

        elif choice == "lines":
            analyzer.line_count(filename)
        elif choice == "words":
            analyzer.word_count(filename)
        elif choice == "letters":
            analyzer.letter_count(filename)
        elif choice == "word_frequency":
            analyzer.word_freq(filename)
        elif choice == "letter_frequency":
            analyzer.letter_freq(filename)
        elif choice == "all":
            analyzer.all_(filename)
        elif choice == "change":
            filename = input("which file? 'lorum.txt' or 'phil.txt' --> ")


        print("\n\n\n\n")
