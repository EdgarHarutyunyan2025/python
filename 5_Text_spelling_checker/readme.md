# Spell Checker for Text Files

This Python script utilizes the `spellchecker` module to correct misspelled words in a text file. It provides functionality to open, correct, and save the corrected text to a new file. The script is designed to be run from the command line using arguments for specifying input and output files.

## Features

- **Spell Checking**: Uses the `SpellChecker` class from the `spellchecker` module to identify and correct misspelled words in the input text file.
  
- **File Handling**: Supports opening an input file, correcting misspellings, and saving the corrected text to an output file.

## Requirements

- Python 3.x
- `spellchecker` module: Install using `pip install spellchecker`

## Usage

1. **Run the Script**:
   - Execute the script (`spell_checker.py`) from the command line:
     ```
     python spell_checker.py -f input_file.txt -o output_file.txt
     ```

2. **Arguments**:
   - `-f, --input_file`: Specify the input text file to be corrected.
   - `-o, --output_file`: Specify the output file to save the corrected text.

3. **Interaction**:
   - The script will read the input file, identify misspelled words, prompt the user to select correct replacements for each misspelled word, and save the corrected text to the output file.

4. **Error Handling**:
   - If the `spellchecker` module is not installed, the script will prompt an error message and exit.

5. **Note**:
   - Ensure the input file is accessible and contains text with potential misspelled words.
   - Review the console prompts to select correct replacements for identified misspellings.

## Example

Suppose you have an input file `input_file.txt` containing:
```
Thes is a speling misteak in this sentence.
```

Running the script:
```
python spell_checker.py -f input_file.txt -o output_file.txt
```

The corrected `output_file.txt` will contain:
```
This is a spelling mistake in this sentence.
```

## Author

- Edgar Hautyunyan