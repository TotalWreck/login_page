from flask import Flask, render_template, request
import json

app = Flask(__name__)

# Load data from user_data.json
with open('user_data.json', 'r') as json_file:
    users = json.load(json_file)
    
@app.route('/')
def home():
    return render_template("index.html")

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    if username in users and users[username] == password:
        return f'Welcome, {username}!'
    else:
        return render_template("index.html", login_invalid=True)
    
@app.route('/signup')
def sign_up():
    return render_template('signup.html')

@app.route('/register', methods=['POST'])
def register():
    new_username = request.form['new_username']
    new_password = request.form['new_password']

    if new_username in users:
        return "Username already taken. Please choose another username."

    users[new_username] = new_password

    with open('user_data.json', 'w') as json_file:
        json.dump(users, json_file, indent=4)

    return f'Welcome, {new_username}! Your account has been created. <a href="/">Return to login</a>.'


if __name__ == "__main__":
    app.run(debug=True, port=7000)