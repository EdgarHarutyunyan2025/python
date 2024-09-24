# Currency Data Desktop App

This Python desktop application allows users to interact with currency data fetched from the CoinCap API. Users can perform tasks such as viewing currency details, saving them to a text file, opening and reading text files, and saving displayed data to an Excel (XLSX) file. The application is built using the Tkinter library for the graphical user interface (GUI) and integrates with external APIs and file handling functionalities.

## Features

- **Fetch Currency Data**: Retrieves currency data from the CoinCap API (https://api.coincap.io/v2/assets).
  
- **Save to Text File**: Writes fetched currency data to a text file (`coins.txt`).

- **Open and Read Text File**: Allows users to select and open a text file, displaying its contents in a scrollable text area.

- **Save Displayed Data to Excel File**: Enables users to save the displayed text area contents (currency data) to an Excel (XLSX) file.

## Setup and Requirements

1. **Python and Libraries**:
   - Ensure Python 3.x is installed on your system.
   - Install required libraries using pip:
     ```
     pip install requests xlsxwriter
     ```

2. **API Setup**:
   - The application uses the CoinCap API to fetch currency data. Ensure your system has internet access to connect to the API.

3. **File Dependencies**:
   - Download the necessary files (`globe_earth_planet_2767.ico`) for window icon setup.

## How to Use

1. **Run the Application**:
   - Execute the script (`3_Desktop_app.py`) to launch the application:
     ```
     python 3_Desktop_app.py
     ```

2. **Main Window**:
   - The main window provides options:
     - **Open**: Fetch currency data, write to `coins.txt`, and display contents in the text area.
     - **Save**: Save displayed text area contents to an Excel file (.xlsx).
     - **Close**: Quit the application.

3. **Interaction**:
   - Click **Open** to fetch and display currency data.
   - Select **Save** to save displayed data as an Excel file.
   - Use the scrollable text area to view opened text file contents.

4. **Notes**:
   - Ensure proper file paths and internet connectivity for fetching data and saving files.
   - Adjust GUI elements and functionalities as needed based on your requirements.

## Author

- Edgar Hautyunyan