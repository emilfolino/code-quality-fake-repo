"""
Main.py
"""
import analyzer
import menu

def main(doc = 'phil.txt'):
    """
    main function
    """
    
    while True:
        menu.menu()
        choice = input("--> ")
        if choice == "q":
            break
        elif choice == "lines":
            print(analyzer.line_count(doc))
        elif choice == "words":
            print(analyzer.words_count(doc))
        elif choice == "letters":
            print(analyzer.letters_count(doc))
        elif choice == "word_frequency":
            print(analyzer.word_frequency(doc))
        elif choice == "letter_frequency":
            print(analyzer.letter_frequency(doc))
        elif choice == "all":
            print(analyzer.allx(doc))
        elif choice == "change":
            doc = analyzer.change()
         
           

        input("\n The knowledge has been granted. Now go bother someone else..")


if __name__ == "__main__":
    main()
