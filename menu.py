"""
Menu for the program
"""
import analyzer

def menu(file):
    """
    Menu
    """
    print("lines) Count amount of lines in file")
    print("words) Count amount of words in file")
    print("letters) Count amount of letters in file")
    print("word_frequency) Check how often words apper in file")
    print("letter_frequency) Check how often letters apper in file ")
    print("all) Do all of the above")
    print("change) Change file")
    print("q) Quit")

    choice = input("Please enter command here: ")

    if choice == "lines":
        print(analyzer.line_count(file))
    
    elif choice == "words":
        print(analyzer.word_count(file))
    
    elif choice == "letters":
        print(analyzer.letter_count(file))

    elif choice == "word_frequency":
        data_freq = analyzer.word_frequency(file)
        analyzer.print_freq(data_freq)

    elif choice == "letter_frequency":
        data_freq = analyzer.letter_frequency(file)
        analyzer.print_freq(data_freq)
    
    elif choice == "all":
        print(analyzer.line_count(file))
        print(analyzer.word_count(file))
        print(analyzer.letter_count(file))
        data_freq = analyzer.word_frequency(file)
        analyzer.print_freq(data_freq)
        data_freq = analyzer.letter_frequency(file)
        analyzer.print_freq(data_freq)
    
    elif choice == "change":
        return analyzer.change()

    elif choice == "q":
        raise ValueError

    else:
        print("Please make a valid input")
    
    return file
