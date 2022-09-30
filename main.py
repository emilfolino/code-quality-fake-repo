'''
call menu
'''
#from cProfile import run
#from msilib.schema import File
#from tkinter import Variable
#from analyzer.analyzer import change
import menu
import analyzer




def main():
    '''
    main
    '''
    running = True  
    file = "phil.txt"
    while running:
        open("phil.txt") 

        menu.menu()
        
        choice = input("-->")

        if choice == "lines":
            analyzer.lines(file)
        elif choice == "letters":
            analyzer.letters(file)
        elif choice == "words":
            analyzer.words(file)
            
        elif choice == "word_frequency":
            analyzer.word_frequency(file)

        elif choice == "letter_frequency":
            analyzer.letter_frequency(file)
            
        elif choice == "all":
            analyzer.show_all(file)
            
        elif choice == "change":
            file = analyzer.change()
            

           
            
            
        elif choice in("q" , "Q"):
            running = False
        else:
            print("Input not valid\n")

if __name__ == "__main__":
    main()
