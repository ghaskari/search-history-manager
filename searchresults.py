from setup import *
import tkinter as tk
from tkinter import scrolledtext


def show_search_results():
    global search_history  # Declare search_history as global
    query = entry.get()
    search_results = perform_search(query)
    ranking, site_name, results = process_results(search_results)
    search_results_df = create_dataframe(ranking, site_name, results)

    results_window = tk.Toplevel(root)
    results_window.title("Search Results")

    text_box = scrolledtext.ScrolledText(results_window, width=60, height=20)
    text_box.pack()

    for result in search_results:
        text_box.insert(tk.END, result + '\n')

    text_box.config(state=tk.DISABLED)

    # Store the search results DataFrame with the query name as key
    search_history[query] = search_results_df

    # Save the search history DataFrames to separate CSV files
    for query_name, df in search_history.items():
        df.to_csv(f'{query_name}_search_history.csv', index=False)


# Create the main window
root = tk.Tk()
root.title("Search Box Example")

# Create a label
label = tk.Label(root, text="Enter your search query:")
label.pack()

# Create an entry field
entry = tk.Entry(root)
entry.pack()
