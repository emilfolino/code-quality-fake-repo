"Main that start functions"
import menu
import analyzer

def main():
    "Main function that start all functions"
    txt = "phil.txt"

    while True:
        menu.menu()

        pick = input("Input: ")
        if pick == "lines":
            analyzer.lines(txt)
        elif pick == "words":
            analyzer.words(txt)
        elif pick == "letters":
            analyzer.letters(txt)
        elif pick == "word_frequency":
            analyzer.word_frequency(txt)
        elif pick == "letter_frequency":
            analyzer.letter_frequency(txt)
        elif pick == "all":
            analyzer.all(txt)
        elif pick == "change":
            txt = analyzer.change()
        elif pick == "q":
            print("Bye bye, hope the program was good :D")
            break
        else:
            print("try again")

if __name__ == "__main__":
    main()
