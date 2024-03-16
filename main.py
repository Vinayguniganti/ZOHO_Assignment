from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Function to initialize the database
def init_db():
    conn = sqlite3.connect('userdata.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            age INTEGER,
            dob DATE
        )
    ''')
    conn.commit()
    conn.close()

# Initialize the database
init_db()

# Route for the user input form
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        age = request.form['age']
        dob = request.form['dob']

        # Client-side validation
        try:
            age = int(age)
            if age <= 0:
                raise ValueError("Age must be a positive integer")
            if not email.endswith("gmail.com"):
                raise ValueError("mail must ends with gmail.com")
        except ValueError:
            return render_template('index.html', error="Invalid age")

        conn = sqlite3.connect('userdata.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO users (name, email, age, dob) VALUES (?, ?, ?, ?)', (name, email, age, dob))
        conn.commit()
        conn.close()

        return redirect(url_for('show_data'))

    return render_template('index.html')

# Route for displaying user data
@app.route('/data')
def show_data():
    conn = sqlite3.connect('userdata.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users')
    data = cursor.fetchall()
    conn.close()
    return render_template('data.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
