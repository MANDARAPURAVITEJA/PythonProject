from flask import Flask, render_template, request, redirect, url_for, flash,jsonify
import SQL_operations as sql_obj
import pymysql

app = Flask(__name__, static_folder='static', template_folder='templates')
app.config['SECRET_KEY'] = 'your_secret_key'  # Change this to a random secret key
email_id=""

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
        return redirect(url_for('home'))
    
# @app.route('/resetpassword', methods=['POST','GET'])
# def resetpassword():
#     try:
#         emailid = request.form['emailid']
#         security_question = request.form['security_question']

#         if sql_obj.resetpassword1(emailid=emailid,security_question=security_question):
#             flash('Reset successful!', 'success')
#             return redirect(url_for('homepage'))
#         else:
#             flash('Invalid username or Place name. Please try again.', 'danger')
#             return redirect(url_for('home'))
#     except Exception as e:
#         print('The Exception message is: ',e)
#         context="Some issue with the code, details not saved. Contact IT Support"
#         return render_template('resetpassword.html',context=context)

@app.route('/newuser',methods=['POST','GET']) #
def index():
    if request.method == 'POST':
        try:
            FIRST_NAME = request.form['FIRST_NAME']
            LAST_NAME = request.form['LAST_NAME']
            EMAILID = request.form['EMAILID']
            PASSWORD = request.form['PASSWORD']
            SECURITY_QUESTION = request.form['SECURITY_QUESTION']

            user_info = sql_obj.Insert_Data(first_name=FIRST_NAME,
                                              last_name=LAST_NAME,
                                              emailid=EMAILID,
                                              password=PASSWORD,
                                              security_question=SECURITY_QUESTION
                                        )
            context = "New User Created Successfully"
            return render_template('index.html', context=context)

        except Exception as e:
            print('The Exception message is: ',e)
            context="Some issue with the code, details not saved. Contact IT Support"
            return render_template('index.html',context=context)

    else:
        return render_template('index.html')
    

@app.route('/reset',methods=['POST','GET']) #
def reset():
    if request.method == 'POST':
        try:
            global email_id
            EMAILID = request.form['EMAILID']
            SECURITY_QUESTION = request.form['SECURITY_QUESTION']

            reset_info = sql_obj.resetpassword1(emailid=EMAILID,
                                              security_question=SECURITY_QUESTION
                                        )

            if reset_info:
                email_id=EMAILID
                context="Values validated"
                return render_template('changepassword.html', context=context)
            else:
                messages=False
                context="Entered details don't match with database."
            return render_template('reset.html', context=context)

        except Exception as e:
            print('The Exception message is: ',e)
            context="Some issue with the code, details not saved. Contact IT Support"
            return render_template('reset.html',context=context)

    else:
        return render_template('reset.html')
    
   

@app.route('/changepassword',methods=['POST','GET']) #
def changepassword():
    if request.method == 'POST':
        try:
            NewPassword = request.form['NewPassword']
            NewPassword_confirm = request.form['NewPassword_confirm']

            if(NewPassword!=NewPassword_confirm):
                context="Please check, Passwords doesn't match!!"
                return render_template('changepassword.html',context=context)

            update_password = sql_obj.updatepassword(emailid=email_id,
                                                  NewPassword=NewPassword
                                                  )
            print(email_id,NewPassword)

            context="Your New Password updated Successfully!!"
            return render_template('changepassword.html', context=context)

        except Exception as e:
            print('The Exception message is: ',e)
            context="Some issue with the code, details not saved. Contact IT Support"
            return render_template('changepassword.html',context=context)

    else:
        return render_template('changepassword.html')


if __name__ == '__main__':
    app.run(debug=True)
