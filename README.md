
# Personal Journal Manager

A simple command-line Personal Journal Manager built with Python. This application allows users to write, view, search, and delete journal entries. All entries are stored in a text file with the current date and time.

## Features

- Add new journal entries
- View all saved entries
- Search entries by keyword or date
- Delete all journal entries with confirmation
- Stores entries with timestamp
- Easy-to-use menu-driven interface

## Technologies Used

- Python 3
- os module
- datetime module

## Project Structure

```
Personal-Journal-Manager/
│── main.py
│── journal.txt
│── README.md
```

## How to Run

1. Make sure Python 3 is installed.
2. Clone the repository.

```bash
git clone https://github.com/pranamiraj083-ship-it/file-operator.git
```

3. Open the project folder.

```bash
cd Personal-Journal-Manager
```

4. Run the program.

```bash
python main.py
```

## Menu Options

```
1. Add a New Entry
2. View All Entries
3. Search for an Entry
4. Delete All Entries
5. Exit
```

## Example

```
Welcome to Personal Journal Manager!

1. Add a New Entry
2. View All Entries
3. Search for an Entry
4. Delete All Entries
5. Exit

User Input: 1

Enter your journal entry:
Today I learned Python file handling.

Entry added successfully!
```

## Future Improvements

- Edit existing entries
- Delete a single entry
- Password protection
- Export journal to PDF
- GUI version using Tkinter
- Database support (SQLite)

## Author

Created as a Python File Handling project for learning purposes.

## License

This project is open source and available under the MIT License.
