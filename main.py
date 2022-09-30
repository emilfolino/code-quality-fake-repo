"""
Main program for text analyzer.
"""

from menu import menu
import analyzer


def main():
    """
    Input command routing and output printing
    """
    text = None
    q = False
    
    def load_file(filename):
        nonlocal text
        try:
            with open(filename, "r") as fhand:
                text = fhand.read()
        except FileNotFoundError as e:
            text = None
            print(str(e))

    def route_command(command):
        """
        Command picker to allow multi-commands calls like 'all'.
        """
        nonlocal q

        if command == 'q':
            q = True

        elif command == 'lines':
            print(str(analyzer.non_empty_line_count(text)))

        elif command == 'words':
            print(str(analyzer.word_count(text)))
        
        elif command == 'letters':
            print(str(analyzer.letter_count(text)))

        elif command == 'word_frequency':
            analyzer.freq_printout(text, 'words')

        elif command == 'letter_frequency':
            analyzer.freq_printout(text, 'letters')

        elif command == 'change':
            load_file(input("enter filename to load: "))
            
        else: print("Invalid command!")

    if text is None:
        load_file("phil.txt")

    while text and not q:
        menu()
        command = input('--> ')
        if command == 'all':
            for c in ['lines', 'words', 'letters', 'word_frequency', 'letter_frequency']:
                route_command(c)
        else:
            route_command(command)


if __name__ == "__main__":
    main()
