from flask import Flask, render_template, request, session, redirect
import mysql.connector

app = Flask(__name__)
app.secret_key = "your_secret_key"

# Establish a connection to the MySQL database
cnx = mysql.connector.connect(
    host="localhost",
    user="your_username",
    password="your_password",
    database="your_database"
)

@app.route('/')
def home():
    # Check if user is logged in
    if 'username' in session:
        username = session['username']
        return f'Hello, {username}! You are logged in.'
    else:
        return 'Home page'

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Perform any necessary validation checks on the username and password

        # Insert the user's information into the MySQL table
        cursor = cnx.cursor()
        query = "INSERT INTO users (username, password) VALUES (%s, %s)"
        values = (username, password)
        cursor.execute(query, values)
        cnx.commit()

        # Set the username in the session to indicate successful registration
        session['username'] = username

        cursor.close()

        # Redirect to the home page or any other desired page
        return redirect('/')
    else:
        return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Query the MySQL table to check if the username and password match
        cursor = cnx.cursor()
        query = "SELECT * FROM users WHERE username = %s AND password = %s"
        values = (username, password)
        cursor.execute(query, values)
        result = cursor.fetchone()

        if result:
            # User login successful
            # Set the username in the session
            session['username'] = username

            cursor.close()

            # Redirect to the home page or any other desired page
            return redirect('/')
        else:
            # User login failed
            return 'Invalid username or password'
    else:
        return render_template('login.html')

@app.route('/logout')
def logout():
    # Clear the session and log the user out
    session.clear()

    # Redirect to the home page or any other desired page
    return redirect('/')

if __name__ == '__main__':
    app.run(