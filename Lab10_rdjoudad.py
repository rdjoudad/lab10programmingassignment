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

    def __init__(self, filepath):
        # triple docstring goes here
        self.__filepath = pathlib.Path(filepath)
        self.__word_occurences = {}
    def process_file(self):
        try:
            if self.__filepath.exists():
                with self.__filepath.open() as book:
                     for line in book:
                          ignored_characters = str.maketrans("", "", string.punctuation)
                          words = line.lower().split()
                          for word in words:
                                if word in self.__word_occurences:
                                    self.__word_occurences[word] += 1 
                                else:
                                    self.__word_occurences[word] = 1
                return True
        except FileNotFoundError:
                print("That file does not exist.")
                return False
    
    def print_report(self):
         #triple docstring goes here
         sorted_words = sorted(self.__word_occurences.keys())
         for word in sorted_words: 
            print(f"{word} :: {self.__word_frequencies[word]}")
