"""
Handles all to do with the menu
"""
import analyzer
def resovleActionFromCommand(command):
    """
    resolves actions from command arguments
    """
    args = command.split(" ")

    match = False

    if args[0] == "q":
        return -1
    
    # main command analyzer
    if args[0] == "menu":
        print("----------Command menu----------")
        print("1) lines: prints the linecount in selected file")
        print("2) words: prints the wordcount in selected file")
        print("3) letters: prints the lettercount in selected file")
        print("4) word_frequency: analyzes the text and copiles the most used words")
        print("5) letter_frequency: analyzes the text and copiles the most used words")
        print("6) all: Compiles all data on file")
        print("7) change: changes the file to be analyzed")
    
    if args[0] == "lines":
        print(analyzer.countLines())
        match = True

    if args[0] == "words":
        print(analyzer.countWords())
        match = True

    if args[0] == "letters":
        print(analyzer.countLetters())
        match = True

    if args[0] == "word_frequency":
        analyzer.wordAnalyzer()
        match = True

    if args[0] == "letter_frequency":
        analyzer.letterAnalyzer()
        match = True
        
    if args[0] == "all":
        analyzer.collectAllData()
        match = True

    if args[0] == "change":
        analyzer.swapfile()
        match = True

    if match:
        return 1

    return 0
