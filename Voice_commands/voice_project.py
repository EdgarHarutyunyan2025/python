"""# Voice-Controlled Assistant

This Python script allows users to perform various tasks using voice commands.
It leverages the `speech_recognition` library for voice input and
Google Speech Recognition API for processing commands.
The script currently supports Google searching and managing a text-based notepad.

## Features

- **Google Search**: Perform a Google search based on voice input.
- **Notepad Management**:
  - **Write to Notepad**: Dictate text to be written into a text file (`notepad.txt`).
  - **Read Notepad**: Display contents of the notepad.

## Requirements

- `webbrowser` module
- `speech_recognition` library (`pip install SpeechRecognition`)"""

import webbrowser
#library for voice input and Google Speech Recognition API for processing commands
import speech_recognition as sr

# Initialize microphone with a specific device index
mic = sr.Microphone(device_index=2)

def speech_command():
    """
    Capture audio input from the microphone and return the recorded audio.
    """
    r = sr.Recognizer()
    with mic as source:
        print("Say something!")
        audio = r.listen(source)
    return audio

def command_voice(audio_command):
    """
    Recognize speech from the provided audio command using Google Speech Recognition.
    """
    try:
        r = sr.Recognizer()
        command = r.recognize_google(audio_command, language='ru-RU')
        print(f"Google Speech Recognition thinks you said {command}")
        return command
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
        return None
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return None

def google_search():
    """
    Perform a Google search based on voice command input.
    """
    print('What do you want to search in Google?')
    google_audio = speech_command()
    try:
        r = sr.Recognizer()
        google_search_command = r.recognize_google(google_audio, language='ru-RU')
        webbrowser.open(f'https://www.google.com/search?q={google_search_command}')
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")

def write_to_notepad():
    """
    Record user input and write it to a text file (notepad).
    """
    print('Что вы хотите добавить в блокнот? Скажите «закрыть блокнот», чтобы остановить.')
    write_notepad_audio = speech_command()
    try:
        r = sr.Recognizer()
        write_command = r.recognize_google(write_notepad_audio, language='ru-RU')
        if write_command == 'закрыть блокнот':
            return None
        with open('notepad.txt', 'a', encoding='utf-8') as f:
            f.write(write_command + '\n')
            print('Что-нибудь еще?')
            write_to_notepad()
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
    return None

def open_notepad():
    """
    Open the notepad and read its contents.
    """
    print('Блокнот открыта !...')
    with open('notepad.txt', encoding='utf-8') as f:
        mdict = {}
        for idx, line in enumerate(f, start=1):
            mdict[idx] = line.strip()
    return mdict

def main():
    """
    Main function to orchestrate the speech recognition commands.
    """
    audio = speech_command()
    command = command_voice(audio)
    if command == 'Open Google':
        google_search()
    elif command == 'Открой блокнот':
        write_to_notepad()
    elif command == 'Покажи заметки':
        notepad = open_notepad()
        for key, value in notepad.items():
            print(key, value)

if __name__ == '__main__':
    main()
