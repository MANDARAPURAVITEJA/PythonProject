from flask import Flask, render_template, request, redirect, url_for, flash
from flask_bcrypt import Bcrypt

app = Flask(__name__, static_folder='static', template_folder='templates')
app.config['SECRET_KEY'] = 'your_secret_key'  # Change this to a random secret key
bcrypt = Bcrypt()

# Dummy user data (replace with a database in a real application)
users = {'john': {'password': bcrypt.generate_password_hash('pass123').decode('utf-8')}}

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    if username in users and bcrypt.check_password_hash(users[username]['password'], password):
        flash('Login successful!', 'success')
        return redirect(url_for('home'))
    else:
        flash('Invalid username or password. Please try again.', 'danger')
        return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
