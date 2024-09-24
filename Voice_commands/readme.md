# Voice-Controlled Assistant

This Python script allows users to perform various tasks using voice commands. It leverages the `speech_recognition` library for voice input and Google Speech Recognition API for processing commands. The script currently supports Google searching and managing a text-based notepad.

## Features

- **Google Search**: Perform a Google search based on voice input.
- **Notepad Management**:
  - **Write to Notepad**: Dictate text to be written into a text file (`notepad.txt`).
  - **Read Notepad**: Display contents of the notepad.

## Requirements

- Python 3.x
- `webbrowser` module
- `speech_recognition` library (`pip install SpeechRecognition`)

## Installation

1. Clone the repository or download the script.
2. Install the required dependencies using pip:
   ```
   pip install SpeechRecognition
   ```

## Usage

1. Run the script:
   ```
   python voice_assistant.py
   ```

2. Follow the prompts:
   - When prompted, say a command such as "Open Google" to perform a Google search, "Открой блокнот" to write to the notepad, or "Покажи заметки" to read the contents of the notepad.

3. Speak clearly into the microphone when prompted. Ensure your microphone is correctly set up and the environment is quiet for accurate speech recognition.

4. To close the notepad writing session, say "закрыть блокнот".

## Notes

- Ensure your microphone is properly configured and functional.
- The script currently supports Russian language (`ru-RU`) for speech recognition.

## Troubleshooting

- If Google Speech Recognition encounters issues (e.g., network problems), check your internet connection and retry.
- Ensure the microphone is correctly set up and recognized by your system.

## Author

- Edgar Hautyunyan