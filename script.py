import tkinter as tk
from tkinter import filedialog as fd
from tkinter.scrolledtext import ScrolledText
import requests
import xlsxwriter

# Function to fetch cryptocurrency data from API
def convert_currency():
    try:
        response = requests.get('https://api.coincap.io/v2/assets')
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            print('Error:', response.status_code)
            return None
    except Exception as e:
        print('Error fetching data:', type(e))
        return None

# Function to create a text file with cryptocurrency data
def create_txt(data):
    try:
        with open('3_Desktop_app\\coins.txt', 'a') as f:
            for i in range(2):  # Limiting to the first two entries for demo
                coin_list = data['data'][i]
                for key, value in coin_list.items():
                    f.write(f"{key}: {value}\n")
    except Exception as e:
        print('Error writing to file:', type(e))

# Function to open a text file and return its contents as a list
def openFile(flag):
    try:
        text = ScrolledText(button)
        text.pack()
        file_types = [('Text Files', '*.txt')]
        file_name = fd.askopenfilename(initialdir="D:/", title="FIND A FILE", filetypes=file_types)
        if file_name:
            with open(file_name, "r") as f:
                if not flag:
                    text.insert(tk.END, f.read())
                file_list = f.readlines()
            return file_list
    except Exception as e:
        print('Error opening file:', type(e))
        return []

# Function to create an Excel file from a list of data
def create_xlsx(file_list):
    try:
        file_name = save_file()
        workbook = xlsxwriter.Workbook(file_name)
        worksheet = workbook.add_worksheet()

        row = 0
        col = 0
        for line in file_list:
            el = line.strip().strip('()\n').split(',')
            worksheet.write(row, col, el[0].upper() + ' -> ' + el[1])
            row += 1
            if el[0] == "'explorer'":
                col += 1
                row = 0
        workbook.close()
        window.quit()
    except Exception as e:
        print('Error creating Excel file:', type(e))

# Function to save the Excel file with user-specified name and location
def save_file():
    try:
        file_types = [('Xlsx Files', '*.xlsx')]
        file_path = fd.asksaveasfilename(title='Save Title', filetypes=file_types)
        return file_path
    except Exception as e:
        print('Error saving file:', type(e))

# Function to initiate fetching cryptocurrency data, creating text file, and opening it
def read_file():
    coin_data = convert_currency()
    if coin_data:
        create_txt(coin_data)
        openFile(False)

# Function to handle saving the opened text file data into an Excel file
def save():
    file_list = openFile(True)
    if file_list:
        create_xlsx(file_list)

# Initialize the Tkinter window
window = tk.Tk()
window.iconbitmap('3_Desktop_app\\globe_earth_planet_2767.ico')
window.title('OpenFile')
window.geometry('400x500+600+300')
window.resizable(False, False)

# Create buttons for opening, saving, and closing the application
button = tk.Button(text='Open', command=read_file)
button.place(x=300, y=450)
button2 = tk.Button(text='Save', command=save)
button2.place(x=250, y=450)
button3 = tk.Button(text='Close', command=window.quit)
button3.place(x=200, y=450)

# Start the Tkinter event loop
window.mainloop()


