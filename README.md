# ZOHO Assignment

This project implements a simple web application using Flask, a Python web framework, for user input form validation, data storage in a SQLite database, and data retrieval to display it in a tabular format using HTML.

## Requirements

- Python 3.x
- Flask
- SQLite

## Setup

1. Install Python 3.x from [Python official website](https://www.python.org/).
2. Install Flask using pip:
3. No separate installation is required for SQLite as it comes bundled with Python.

## Usage

1. Clone this repository:
2. Navigate to the project directory:
3. Run the Flask application (python main.py):
4. Access the application in your web browser at [http://localhost:5000/](http://localhost:5000/).

## Functionality

- The web application presents a user input form that includes fields for name, email, age, and date of birth.
- Client-side validation ensures that the email format is valid and the age is a positive integer.
- Submitted data is stored in a SQLite database.
- A separate route `/data` retrieves data from the database and displays it in a tabular format.
- Additionally, there is a button available to retrieve all data from the database and display it.

## Project Structure

project_directory/
│
├── main.py # Python script containing Flask application
├── templates/ # HTML templates for rendering pages
│ ├── index.html # User input form
│ ├── data.html # Display user data
│ └── all_data.html # Display all data
└── userdata.db # SQLite database file


## Credits

- This project is created as part of an assignment.
- Flask documentation: [Flask Documentation](https://flask.palletsprojects.com/)
- SQLite documentation: [SQLite Documentation](https://www.sqlite.org/docs.html)
