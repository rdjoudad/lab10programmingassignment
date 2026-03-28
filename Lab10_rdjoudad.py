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
        self.__filepath = filepath.Path(filepath)
        self.__word_occurences = {}

    