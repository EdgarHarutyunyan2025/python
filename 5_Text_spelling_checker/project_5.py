"""
test.py
This script demonstrates how to use argparse and the spellchecker module to correct spelling errors
in a text file. It takes an input file containing text with potential misspellings, identifies those
misspellings using SpellChecker, prompts the user to select corrections and saves the corrected text
Usage:
    python test.py -f input_file.txt -o output_file.txt

2. **Function Definitions**:
   -open_file(file_name)`**: Opens and reads a file specified by `file_name`, 
    handling `FileNotFoundError`. It returns a list of lines from the file
   -save_file(correct_list, output_file_name)`**: 
    Saves the corrected list (`correct_list`) to a file specified by `output_file_name`
"""

import argparse
try:
    from spellchecker import SpellChecker
except ImportError:
    print("Error: Unable to import SpellChecker from spellchecker module.")
    print("Make sure you have installed the module using 'pip install spellchecker'.")
    exit()

# Initialize the SpellChecker object from the spellchecker module
spell = SpellChecker()


def open_file(file_name):
    '''Function to open and read a file'''
    try:
        list_file = []
        with open(file_name,encoding='utf-8') as f:
            file = f.readlines()
            for line in file:
                list_file.append(line.strip('\n'))
        return list_file
    except FileNotFoundError:
        print("File not found:", file_name)
        return None


def correct_wrong_words(list_file):
    '''Function to correct misspelled words in the input list of lines'''
    try:
        # Iterate through each line in the list
        for i in range(len(list_file)):
            words = list_file[i].split()
            misspelled = spell.unknown(words)
            for word in misspelled:
                word_candidates_list = list(spell.candidates(word))
                if word in words:
                    word_index = words.index(word)
                elif word.capitalize() in words:
                    word_index = words.index(word.capitalize())

                # Print the misspelled word and its candidate corrections
                print(word, '--', word_candidates_list)
                correct_word = int(input('Enter correct answer index: '))
                words[word_index] = word_candidates_list[correct_word]
                result_string = ' '.join(words)
                list_file[i] = result_string
        return list_file
    except Exception as error:
        print("Error:", type(error))
        return None


def save_file(correct_list, output_file_name):
    '''Function to save the corrected list of lines to an output file'''
    try:
        with open(output_file_name, 'w',encoding='utf-8') as f:
            for line in correct_list:
                f.write(line + '\n')
    except FileNotFoundError as e:
        print("Error:", type(e))


def main():
    '''Main function to handle argument parsing and execution flow'''
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--input_file", help='input file_name', required=True)
    parser.add_argument("-o", "--output_file", help='output file_name', required=True)
    args = parser.parse_args()

    # Check if input_file and output_file arguments are provided
    if args.input_file and args.output_file:
        file_lines_list = open_file(args.input_file)
        if file_lines_list:
            correct_lines_list = correct_wrong_words(file_lines_list)
            if correct_lines_list:
                save_file(correct_lines_list, args.output_file)

# Entry point of the script
if __name__ == '__main__':
    main()
