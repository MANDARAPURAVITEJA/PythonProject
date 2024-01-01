from flask import Flask, render_template, request, redirect, url_for, flash,jsonify
import SQL_operations as sql_obj
import pymysql

app = Flask(__name__, static_folder='static', template_folder='templates')
app.config['SECRET_KEY'] = 'your_secret_key'  # Change this to a random secret key

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/homepage', methods=['GET'])
def homepage():
    row_data=sql_obj.homepage_data()

    return render_template('homepage.html',data=row_data)

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    if sql_obj.retrieve_data(username,password):
        flash('Login successful!', 'success')
        return redirect(url_for('homepage'))
    else:
        flash('Invalid username or password. Please try again.', 'danger')
        return redirect(url_for('homepage'))

@app.route('/newuser',methods=['POST','GET']) #
def index():
    if request.method == 'POST':
        try:
            FIRST_NAME = request.form['FIRST_NAME']
            LAST_NAME = request.form['LAST_NAME']
            EMAILID = request.form['EMAILID']
            PASSWORD = request.form['PASSWORD']
            SECURITY_QUESTION = request.form['SECURITY_QUESTION']

            student_info = sql_obj.Insert_Data(first_name=FIRST_NAME,
                                              last_name=LAST_NAME,
                                              emailid=EMAILID,
                                              password=PASSWORD,
                                              security_question=SECURITY_QUESTION
                                        )
            context = "Student details Submitted Successfully"
            return render_template('index.html', context="New User Created Successfully")

        except Exception as e:
            print('The Exception message is: ',e)
            context="Some issue with the code, details not saved. Contact IT Support"
            return render_template('index.html',context=context)

    else:
        return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True)
