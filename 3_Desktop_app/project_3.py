"""
## Introduction:
- This application allows you to open a text file ,
  containing currency data fetched from CoinCap API, 
  display its contents, and save it as an Excel (XLSX)file
  for further analysis.
## Features:
- Fetches cryptocurrency data from CoinCap API.
- Creates and writes data to a text file (`coins.txt`).
- Opens and displays contents of a user-selected text file.
- Saves displayed text contents to an Excel (XLSX) file.
##Install dependencies:
- pip install requests
- pip install xlsxwriter
"""

import os
from tkinter import *
from tkinter import filedialog as fd
from tkinter.scrolledtext import ScrolledText
import requests
import xlsxwriter


def convert_currency():
    '''Function to fetch currency data from CoinCap API'''
    try:
        response = requests.get('https://api.coincap.io/v2/assets')
    except Exception as e:
        print(f"Request Exception: {e}")
        return None
    if response.status_code==200:
        response.raise_for_status()  # Raise HTTPError for bad status codes
        data = response.json()
        return data

def create_txt(data):
    '''Function to create a text file and write coin data to it'''
    try:
        with open('3_Desktop_app/coins.txt', 'w', encoding='utf-8') as f:
            for coin in data['data'][:4]:
                for key, value in coin.items():
                    f.write(f"{key.upper()}: {value}\n")
                f.write("\n")
    except FileNotFoundError as e:
        print(f"Error writing to file: {e}")

def open_file():
    '''Function to open a text file and read its contents'''
    try:
        file_types = [('Text Files', '*.txt')]
        file_name = fd.askopenfilename(initialdir=os.path.expanduser("D:/"),
                             title="Select a file", filetypes=file_types)
        if file_name:
            with open(file_name, "r",encoding='utf-8') as f:
                return f.readlines()
    except Exception as e:
        print(f"Error opening file: {e}")
        return []

def create_xlsx(file_list):
    '''Function to create an Excel (XLSX) file and write data to it'''
    try:
        file_path = save_file()
        if file_path:
            workbook = xlsxwriter.Workbook(file_path)
            worksheet = workbook.add_worksheet()
            col=0
            row=0
            for line in file_list:
                if len(line) ==0 :
                    continue
                parts = line.strip().strip("()").split(',')
                for part in parts:
                    worksheet.write(row,col,part.strip())
                    row+=1
                    if 'EXPLORER' in part:
                        col+=1
                        row=0
            workbook.close()
            window.quit()
    except Exception as e:
        print(f"Error creating XLSX: {e}")

def save_file():
    '''Function to prompt user to save the XLSX file'''
    try:
        file_types = [('XLSX Files', '*.xlsx')]
        file_path = fd.asksaveasfilename(title='Save File As',
             filetypes=file_types, defaultextension=".xlsx")
        return file_path
    except FileNotFoundError as e:
        print(f"Error saving file: {e}")
        return None

def read_file():
    '''Function to read currency data, create text file, 
    open user-selected file, and display its contents'''
    coin_data = convert_currency()
    if coin_data:
        create_txt(coin_data)
        open_file_data = open_file()
        if open_file_data:
            display_text.insert(END, "".join(open_file_data))

def save():
    '''Function to save contents of scrolled text area to an XLSX file'''
    open_file_data = display_text.get("1.0", END).splitlines()
    create_xlsx(open_file_data)

# Main Tkinter window setup
window = Tk()
window.iconbitmap('3_Desktop_app/globe_earth_planet_2767.ico')
window.title('OpenFile')
window.geometry('400x500+600+300')
window.resizable(False, False)

open_button = Button(window, text='Open', command=read_file)
open_button.place(x=50, y=450)

save_button = Button(window, text='Save', command=save)
save_button.place(x=150, y=450)

close_button = Button(window, text='Close', command=window.quit)
close_button.place(x=250, y=450)

display_text = ScrolledText(window)
display_text.place(x=50, y=50, width=300, height=380)

window.mainloop()
