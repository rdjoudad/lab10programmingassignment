"""
Word Count Project
Ryma Djoudad
OOP-based program that allows the user to select a file, 
which will then analyze the frequency of each word and print the information out.
Imported text files containing public domain stories
03/28/2026
"""
import pathlib, string

class WordAnalyzer:
    """
    WordAnalyzer Class
    Ryma Djoudad
    Class that processes the files, strips them of characters and prints their frequency
    Imported pathlib and string modules
    03/29/2026
    """
    def __init__(self, filepath):
        self.__filepath = pathlib.Path(filepath)
        self.__word_mentions = {}
    def process_file(self):
        try:
            if self.__filepath.exists():   
                extra = "“”‘’—–"
                ignored_characters = str.maketrans("", "", string.punctuation + extra)
                with self.__filepath.open(encoding="utf-8") as book:
                    for line in book:
                        stripped_lines = line.translate(ignored_characters)
                        words = stripped_lines.lower().split()
                        for word in words:
                            if word in self.__word_mentions:
                                self.__word_mentions[word] += 1 
                            else:
                                self.__word_mentions[word] = 1
                return True
        except FileNotFoundError:
            print("That file does not exist.")
            return False
    
    def print_report(self):
        sorted_words = sorted(self.__word_mentions.keys())
        for word in sorted_words: 
            print(f"{word} :: {self.__word_mentions[word]}")

def main():
    """
    Main function
    Ryma Djoudad
    Function acting as the user interface that is interactive with choices including exit
    Using imported pathlib
    03/29/2026
    """
    files = {
        "1" : pathlib.Path("monte_cristo.txt"),
        "2" : pathlib.Path("princess_mars.txt"),
        "3" : pathlib.Path("Tarzan.txt"),
        "4" : pathlib.Path("treasure_island.txt")
    }
    print("--- Word Analyzer ---")
    print("Please select a file to analyze:")
    print("1. Monte Cristo")
    print("2. Princess Mars")
    print("3. Tarzan")
    print("4. Treasure Island")
    print("5. Exit")

    user_response = ""
    while user_response != '5':
        user_response = input("Enter your choice: ")
        if user_response in files:
            analyzer = WordAnalyzer(files[user_response])
            analyzer.process_file()
            analyzer.print_report()
        elif user_response !='5':
            print("That choice is not valid. Please select again.") 

main()