"""
The main funtions to run the text analyzer.
"""
import menu
import analyzer
def main():
    """
    Main functhon to build a text anlyzer 
    that handles different fields.
    """
    file = ["phil.txt"]
    
    while True:
        menu.menu()
        file_name = file[0]
        choice = input("Enter a chioce from above: ")

        if choice == "q":
            break
        
        elif choice == "lines":
            print(analyzer.count_lines(file_name))

        elif choice == "words":
            print(analyzer.count_words(file_name))

        elif choice == "letters":
            print(analyzer.count_letters(file_name))

        
        elif choice == "word_frequency":
            analyzer.word_frequency(file_name)


        elif choice == "letter_frequency" : 
            analyzer.letter_frequency(file_name)


        elif choice == "all":
            analyzer.all_data(file_name)

        elif choice == "change":
            file[0] = input ("Enter the file name: ")
            
            
        


if __name__ == "__main__":
    main()
