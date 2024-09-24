# Who Wants to Be a Millionaire Game

This Python script implements a simplified version of the "Who Wants to Be a Millionaire" game using Tkinter for GUI, Pygame for audio playback, and Pyttsx3 for text-to-speech functionalities. The game allows users to answer multiple-choice questions, use lifelines, and win virtual money based on their performance.

## Features

- **Game Setup**: The game initializes with a main window where users can enter their name to start playing.
  
- **Question Handling**: Questions and answer options are loaded from a JSON file (`my.json`). Users select answers by clicking on the corresponding buttons.
  
- **Lifelines**: Implemented lifelines include:
  - **50-50**: Removes two incorrect options.
  - **Audience Poll**: Displays audience poll results using progress bars to indicate percentage votes for each option.
  - **Phone a Friend**: Simulates calling a friend for help using text-to-speech to read out the correct answer.

- **User Experience**: 
  - Upon answering all questions correctly, users win a virtual prize of $1,000,000 and can view top users' scores.
  - If a wrong answer is selected, users can try again or view top users' scores.

## Installation and Usage

1. **Dependencies**:
   - Python 3.x
   - Tkinter (standard library for GUI)
   - Pygame (`pip install pygame`) for audio playback
   - Pyttsx3 (`pip install pyttsx3`) for text-to-speech

2. **Running the Game**:
   - Navigate to the directory containing `main.py` and run:
     ```
     python main.py
     ```
   - Ensure the `4_Who_wants_to_be_a_millionaire` folder contains necessary audio files (`mp3`), image files (`images`), and the JSON file (`my.json`).

3. **Gameplay**:
   - Enter your name in the main window and click "Enter".
   - Answer questions by clicking on the corresponding buttons (A, B, C, D).
   - Use lifelines strategically when unsure of answers.
   - Win virtual money and view top users' scores upon completion.

4. **Customization**:
   - Modify the questions and answer options in `my.json` to customize the game content.
   - Update images and audio files to personalize the game interface.

## Author

- Edgar Hautyunyan