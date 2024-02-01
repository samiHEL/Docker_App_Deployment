from typing import List, Dict
# from flask import Flask,render_template,jsonify, redirect, url_for, request
# import mysql.connector
# import json

# app = Flask(__name__)

# def test_table() -> List[Dict]:
#     config = {
#         'user': 'root',
#         'password': 'root',
#         'host': 'db',
#         'port': '3306',
#         'database': 'devopsroles'
#     }
#     connection = mysql.connector.connect(**config)
#     cursor = connection.cursor()
#     cursor.execute('SELECT * FROM test_table')
#     results = [{login: mdp} for (login, mdp) in cursor]
#     cursor.close()
#     connection.close()

#     return results

# @app.route('/')
# def index():
#    return render_template('index.html',text=test_table())
# @app.route('/', methods=['GET', 'POST'])
# def login():
#     error = None
#     go=None
#     if request.method == 'POST':
#         if request.form['username'] != 'admin' or request.form['password'] != 'admin':
#             error = 'Invalid Credentials. Please try again.'
#         else:
#             go = 'Felicitation '+request.form['username'] 
#     return render_template('index.html', error=error,go=go)

# @app.route('/api', methods=['GET'])
# def get_api_data():
#     # data = test_table()  # Fonction que vous utilisez pour récupérer les données
#     # return jsonify(data)
#     return render_template('index.html')

# if __name__ == '__main__':
#     app.run(host='0.0.0.0')











from flask import Flask, render_template, request, redirect, url_for, session, jsonify
import mysql.connector

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a secure secret key


def create_connection():
    return mysql.connector.connect(
        host='db',
        user='root',
        password='root',
        database='devopsroles',
        port='3306'
    )

def test_table(login=None, password=None):
    connection = create_connection()
    cursor = connection.cursor(dictionary=True)

    if login is not None and password is not None:
        # If login and password are provided, filter by them
        cursor.execute('SELECT * FROM test_table WHERE login = %s AND mdp = %s', (login, password))
    else:
        # If no login and password provided, get all data
        cursor.execute('SELECT * FROM test_table')

    results = cursor.fetchall()
    connection.close()
    return results


@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    # Validate credentials using the test_table function
    data = test_table(username, password)
    
    if data:
        session['username'] = data[0]['login']
        session['password'] = data[0]['mdp']
        return redirect(url_for('dashboard'))
    else:
        return render_template('login.html', error='Invalid Credentials. Please try again.')


@app.route('/dashboard')
def dashboard():
    if 'username' in session and 'password' in session:
        # Perform any additional checks or data retrieval here
        return render_template('dashboard.html', text='Logged in as: {}'.format(session['username']))
    else:
        return redirect(url_for('index'))
    
@app.route('/api/get_data', methods=['GET'])
def get_data():
    data = test_table()
    return jsonify(data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)



