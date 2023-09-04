# Search History Manager

**Search History Manager** is a Python application designed to facilitate Google searches, display the search results, and maintain a record of your search history in separate CSV files. This project is organized into several Python files for clarity and modularity. Below, you'll find an overview of the project structure and instructions on how to use it effectively.

## Project Structure

- `setup.py`: This module contains functions for conducting Google searches and processing the results.
- `main.py`: Here, the primary application window is created, featuring a search button, and the Tkinter event loop is initialized.
- `searchresults.py`: This module defines a function to display search results and manage the search history.

## Installation

Before running the application, please make sure you have the necessary Python packages installed. You can install them using pip:

```bash
pip install googlesearch-python pandas tkinter
```

## Usage

1. Run the `main.py` script to launch the main application window.

2. In the entry field, type your search query and click the "Search" button.

3. A new window will promptly appear, displaying the search results.

4. The application will automatically save the search results in a CSV file, using the query name as the filename. These CSV files are stored in the same directory as the application scripts.

## Example

Here's a simple example of how to use the application:

1. Enter "Python programming" in the search field.

2. Click the "Search" button.

3. A new window will pop up, showing the search results.

4. The search results will be automatically saved in a CSV file named "Python programming_search_history.csv."

5. You can perform additional searches, and each search result will be saved in its respective CSV file.

## Important Notes

- This application relies on the `googlesearch` library to perform Google searches. Ensure you have a stable internet connection for it to function properly.

- The search results are presented within a scrolling text box, allowing you to review a substantial number of results.

- The application keeps a record of your search history, storing each query's results in a dedicated CSV file identified by the query name.

Enjoy the convenience of managing your search history with the Search History Manager!
