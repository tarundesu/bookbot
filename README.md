# bookbot

📚 BookBot

BookBot is a simple command-line tool for analyzing books and extracting basic textual statistics. It reads a .txt file, counts total words, and provides a frequency breakdown of characters—sorted and presented in a clean, human-readable report.

✨ Features

📖 Analyze any plain text book

🔢 Word count summary

🔤 Character frequency analysis (case-insensitive)

📊 Sorted report output (alphabetical characters only)

🧩 Modular and clean Python code structure

🧪 CLI-friendly — works with different books passed via arguments

📁 Project Structure

- main.py: Entry point for the app, handles CLI interaction and report generation.

- stats.py: Contains all functions for counting words and characters, and sorting the results.

- books/: Directory where .txt books are stored for analysis.

⚙️ Installation

1. Clone this repo
   git clone https://github.com/<your-username>/bookbot.git
   cd bookbot

2. (Optional) Create a virtual environment
   python3 -m venv venv
   source venv/bin/activate

3. Add books to the books/ directory
   You can download .txt books from [Project Gutenberg](https://www.gutenberg.org/) and place them inside the books/ folder.



🚀 Usage

python3 main.py <path_to_book>

Example:
python3 main.py books/frankenstein.txt

Expected output:
============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
Found 75767 total words
--------- Character Count -------
e: 44538
t: 29493
a: 25894
...
============= END ===============


🛠️ Functions Overview

get_num_words(text)
Returns the total number of words in the text.

get_char_count(text)
Returns a dictionary with the frequency of each character (converted to lowercase).

sort_char_count(char_dict)
Takes the dictionary of characters and returns a list sorted by frequency, descending.

💡 Notes
Non-alphabetic characters are ignored in the final report.

Make sure to pass the full path to your book file if it's outside the books/ folder.

📌 Example Books

This project has been tested with:

1. Frankenstein by Mary Shelley
2. Moby Dick by Herman Melville
3. Pride and Prejudice by Jane Austen

📄 License
This project is open-source and free to use. Feel free to fork, modify, or suggest improvements.
