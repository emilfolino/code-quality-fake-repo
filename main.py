"""
Contains the command-loop, while-loop, and the defined function main()
"""
from menu import choice
import analyzer as a

def main():
    """
    This is where all commads are executed
    """
    inp = choice()
    filename = "phil.txt"
    while inp != "q":

        if inp == "lines":
            print(a.analyze_lines(filename))

        elif inp == "words":
            print(a.analyze_words(filename))

        elif inp == "letters":
            print(a.analyze_letters(filename))

        elif inp == "word_frequency":
            result_list = a.word_frequency_results(filename)
            for results in result_list:
                print(results)

        elif inp == "letter_frequency":
            result_list = a.letter_frequency_results(filename)
            for results in result_list:
                print(results)

        elif inp == "all":
            a.print_all_analyzes(filename)

        elif inp == "change":
            try:
                filename = a.change(filename)
            except FileNotFoundError as e:
                print(str(e))

        else:
            print("This is not a valid menu choice.")
        
        inp = choice()

if __name__ == "__main__":
    main()
