from email import message
import email
from json import decoder
from flask import Flask, render_template, request, redirect, url_for, session
from requests.sessions import Session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re
import math, random
import random
from ssl import create_default_context
from email.message import EmailMessage
from flask_mail import * 
from flask import *
from flask import Flask, render_template, flash, request, redirect, url_for
from flask_mail import Message 
import os 
import hashlib
import sys
import jwt
import requests
import json
from time import time
#sys.path.insert(0, 'Rportal/config')
#from config import credentials as cred
API_KEY = 'DVKW9UngTg2lI1FnqrQVWA'
API_SEC = 'ZIN4AsaniiKYBBA0cQHLSupJOIZwMEdbcRm2'
UPLOAD_FOLDER = '/path/to/the/uploads'
UPLOAD_DOCS = '/path/to/the/uploads/docs'
ALLOWED_EXTENSIONS = {'pdf', 'png', 'jpg', 'jpeg'}
app = Flask(__name__)
app.secret_key = '65142'
app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '1234'
app.config['MYSQL_DB'] = 'rportal'
app.config['charset'] ='utf8'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['UPLOAD_DOCS'] = UPLOAD_DOCS
mysql = MySQL(app)
 
mail = Mail(app)
app.config["MAIL_SERVER"]='smtp.gmail.com'  
app.config["MAIL_PORT"] =465 #465 or 587 
app.config["MAIL_USERNAME"] = 'ajinfotics@gmail.com'  
app.config['MAIL_PASSWORD'] = 'Ajinfo@1234'  
#app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
part2 ="Your One Time Password for logging into R-Portal is\n\n" 
part3="""\n\nIf you did not Initiated this request,please ignore this mail.

If you have more queries, feel free to contact us at ajinfotics@gmail.com. 

We will love to help and assist you at any movement.

Automated mail sent by R-Portal. Please do not reply.
Regards! """
part4 ="""\nIf you have any queries, feel free to contact us at ajinfotics@gmail.com. 
We will love to help and assist you at any movement.
Automated mail sent by R-Portal. Please do not reply.
Regards! """
mail = Mail(app)
otp = random.randint(000000,999999)  

#   Index Page - R-Portal
@app.route('/')
def index():
    return rportal()
@app.route('/R-Portal/')
def rportal():
    return render_template('rportal.html')

#
#   Registrations
#

#   User Registration
@app.route('/R-Portal/register', methods=['GET','POST'])
def register():
    msg = ''
    if request.method == 'POST'and 'name' in request.form and 'username' in request.form and 'mobile' in request.form and 'email' in request.form and 'password' in request.form :
        name = request.form['name']
        username = request.form['username']
        mobile = request.form['mobile']
        email = request.form['email']
        passtext = request.form['password']
        password = hashlib.sha256((passtext).encode('utf-8')).hexdigest()

        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM userdetails WHERE username = %s', (username,))
        account = cursor.fetchone()
        cursor1 = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor1.execute('SELECT * FROM userdetails WHERE email = %s', (email,))
        account1 = cursor1.fetchone()

        if account:
            msg = 'Warning! Username already exists!!'
        elif account1:
            msg = 'Warning! Account already exists!!'
        else:
            cursor1.execute('INSERT INTO userdetails VALUES (NULL, %s, %s, %s, %s, %s, DEFAULT)', (username , name ,  password , mobile ,  email ,))
            mysql.connection.commit()
            msg = 'You have successfully registered!'
    elif request.method == 'POST':
            msg = 'elif code!'
    return render_template('register.html',msg=msg)

#   Secretary Registration 
def invitation():
    num = '0123456789'
    string = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    num1 = ""
    str1 = ""
    length = len(string)
    length1 = len(num)
    for i in range(4):
        str1 += string[math.floor(random.random() * length)]
    for i in range(2):
        num1 += num[math.floor(random.random() * length1)]
    code = str(str1 + num1)
    return code
    
@app.route('/R-Portal/sregister', methods=['GET','POST'])
def sregister():
    if 'user' in session:
        msg = ''
        target = os.path.join( '/Rportal/static/upload/')
        if not os.path.isdir(target):
            os.makedirs(target)
        if request.method == 'POST' and 'Sflatno' in request.form and 'Swing' in request.form:
            username = session['username']
            email = session['user_email']
            Aname = session['user_name']
            flatno = request.form['Sflatno']
            wing = request.form['Swing']
            mobile = session['user_mobile']
            acname = request.form['acname']  
            acno = request.form['acno']
            mmid = request.form['mmid']
            bankname = request.form['bankname']
            branch = request.form['branch']
            ifsc = request.form['ifsc']
            name = request.form['name']
            area = request.form['area']
            road = request.form['road']   
            city = request.form['city']
            state = request.form['state']
            pin = request.form['pin']
            ...
            file = request.files['file']
            file_name = file.filename or ''
            destination = ''.join([target, file_name])
            file.save(destination)
            kyc_file  = file_name
            ...
            code = ""
            code =invitation()
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute('SELECT * FROM member WHERE username = %s AND Mcode = %s AND Mflatno = %s AND Mwing = %s', (username, code, flatno, wing,))
            account = cursor.fetchone()
            cursor1 = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute('SELECT * FROM secretary WHERE username = %s AND Scode = %s AND Sflatno = %s AND Swing = %s', (username, code, flatno, wing,))
            account1 = cursor1.fetchone()
            cursor2 = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor2.execute('SELECT * FROM society WHERE code = %s', (code,))
            account2 = cursor2.fetchone()
            if account:
                msg = 'Warning! User already exists!!'
            elif account1:
                msg = 'Warning! User already exists!!'
            elif account2:
                msg = 'Something went wrong:( Please try again!'
            elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
                msg = 'Invalid email address!'
            elif not re.match(r'[A-Za-z0-9]+', username):
                msg = 'Username must contain only characters and numbers!'
            else:
                cursor1.execute('INSERT INTO secretary VALUES (NULL, %s, %s, %s, %s, %s, %s,%s , DEFAULT , DEFAULT)', (username , code ,  email , Aname , flatno , wing , mobile ,))
                cursor2.execute('INSERT INTO society VALUES (NULL, %s, %s, %s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, NULL, NULL,%s, DEFAULT , DEFAULT)', (code , name , city , road , area , state , pin , acname, acno, mmid, bankname, branch, ifsc, kyc_file))
                cursor.execute('INSERT INTO member VALUES (NULL, %s, %s, %s, %s, %s, %s,%s,DEFAULT,DEFAULT )', (username , code ,  email , Aname , flatno , wing , mobile))
                mysql.connection.commit()
                msg = 'You have successfully registered!'
        elif request.method == 'POST':
            msg = 'elif code!' 
        return render_template('secretary/sregister.html', msg=msg, name=session['user_name'],username=session['username'], email=session['user_email'], mobile=session['user_mobile'])
    elif session.get('user') is None:
            return login()
    else:
        return logout()

#   Member Registration
@app.route('/R-Portal/mcode', methods=['GET', 'POST'])
def mcode():
    if 'user' in session:
        msg = ''
        if request.method == 'POST' and 'code' in request.form:
            code = request.form['code']
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute('SELECT * FROM society WHERE code = %s', (code,))
            account = cursor.fetchone()
            if account:
                cursor.execute('select name, city, road, area, state, pin, code , Semail from society inner join secretary WHERE code = %s', (code ,))
                account = cursor.fetchone()
                return render_template('member/mverify.html', account=account, msg=msg,  name=session['user_name'],username=session['username'], email=session['user_email'], mobile=session['user_mobile'])
            else:
                mysql.connection.commit()
                msg='Invalid Society Code!'
        return render_template('member/mcode.html', msg=msg)
    elif session.get('user') is None:
            return login()
    else:
        return logout()

@app.route('/R-Portal/mcode1/<string:code>', methods=['GET', 'POST'])
def mcode1(code):
    if 'user' in session:
        msg = ''
        if request.method == 'POST' and 'code' in request.form:
            code = request.form['code']
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute('SELECT * FROM society WHERE code = %s', (code,))
            account = cursor.fetchone()
            if account:
                cursor.execute('select name, city, road, area, state, pin, code , Semail from society inner join secretary WHERE code = %s', (code ,))
                account = cursor.fetchone()
                name =session['user_name']
                return render_template('member/mverify.html', account=account, msg=msg, name = name ,username=session['username'], email=session['user_email'], mobile=session['user_mobile'])
            else:
                mysql.connection.commit()
                msg='Invalid Society Code!'
        return render_template('member/mcode.html', msg=msg)
    elif session.get('user') is None:
            return login()
    else:
        return logout()

@app.route('/R-Portal/mregister', methods=['GET', 'POST'])
def mregister():
    if 'user' in session:
        msg = ''
        msg1= ''
        if request.method == 'POST' and 'Mcode' in request.form and 'Mflatno' in request.form and 'Mwing' in request.form and 'Semail' in request.form:
            username = session['username']
            code = request.form['Mcode']
            email = session['user_email']
            name = session['user_name']
            flatno = request.form['Mflatno']
            wing = request.form['Mwing']
            mobile = session['user_mobile']   
            Semail = request.form['Semail']
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute('SELECT * FROM member WHERE username = %s AND Mcode = %s AND Mflatno = %s AND Mwing = %s', (username, code, flatno, wing,))
            account = cursor.fetchone()
            cursor1 = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor1.execute('SELECT * FROM secretary WHERE username = %s AND Scode = %s AND Sflatno = %s AND Swing = %s', (username, code, flatno, wing,))
            account1 = cursor1.fetchone()
            if account:
                msg = 'Warning! User already exists!!'
            elif account1:
                msg = 'Warning! User already exists!!'
            elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
                msg = 'Invalid email address!'
            elif not re.match(r'[A-Za-z0-9]+', username):
                msg = 'Username must contain only characters and numbers!'
            else:
                cursor.execute('INSERT INTO member VALUES (NULL, %s, %s, %s, %s, %s, %s,%s,DEFAULT,DEFAULT )', (username , code ,  email , name , flatno , wing , mobile))
                mysql.connection.commit()
                msg = Message('New Member Request' ,sender ='Rportal<me@Rportal.com', recipients = [Semail]) 
                text = "Hello \nYou have received new member request with followinh member details. \n Member details are :\n"
                msg.body = text + "\n Flat No :" + wing + flatno + "\n Name : " + name + "\n phone No : " + mobile + "\n Email ID : " + email + part4
                mail.send(msg)  
                msg1 = 'You have successfully registered!'
        elif request.method == 'POST':
            msg = 'Please fill out the form!'
        return render_template('member/mcode.html', msg=msg, msg1=msg1)
    elif session.get('user') is None:
            return login()
    else:
        return logout()


#   Security Guard Registeration
@app.route('/R-Portal/add_security', methods=['GET','POST'])
def security():
    msg = ''
    if request.method == 'POST' and 'security_name' in request.form and 'security_username' in request.form and 'security_password' in request.form:
        security_username = request.form['security_username']
        security_mobile = request.form['security_mobile'] 
        passtext  = request.form['security_password']
        security_password = hashlib.sha256((passtext).encode('utf-8')).hexdigest()
        security_name = request.form['security_name']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM security WHERE security_username = %s AND security_mobile = %s', (security_username, security_mobile))
        account = cursor.fetchone()
        if account:
            msg = 'Warning! Account already exists!!'
        elif not re.match(r'[A-Za-z0-9]+', security_username):
            msg = 'Username must contain only characters and numbers!'
        elif not security_username or not security_password or not security_mobile:
            msg = 'Please fill out the form!'
        else:
            cursor.execute('INSERT INTO security VALUES (NULL, %s, %s, %s, %s, %s, DEFAULT)', (security_username , security_password , security_name , security_mobile, session['code']))
            mysql.connection.commit()
            msg = 'You have successfully registered!'
    elif request.method == 'POST':
        msg = 'elif code!' 
    return people()

#   Staff Member Registaration
@app.route('/R-Portal/add_staff', methods=['GET','POST'])
def staff():
    msg = ''
    if request.method == 'POST' and 'staff_name' in request.form and 'staff_username' in request.form and 'staff_password' in request.form  and 'post' in request.form:
        
        staff_username = request.form['staff_username']
        staff_mobile = request.form['staff_mobile']
        passtext  = request.form['staff_password']
        staff_password  = hashlib.sha256((passtext).encode('utf-8')).hexdigest()
        staff_name = request.form['staff_name']
        post = request.form['post']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM staff WHERE staff_username = %s AND staff_mobile = %s', (staff_username, staff_mobile))
        account = cursor.fetchone()
        if account:
            msg = 'Warning! Account already exists!!'
        elif not re.match(r'[A-Za-z0-9]+', staff_username):
            msg = 'Username must contain only characters and numbers!'
        elif not staff_username or not staff_password or not staff_mobile:
            msg = 'Please fill out the form!'
        else:
            cursor.execute('INSERT INTO staff VALUES (NULL, %s, %s, %s, %s, %s , DEFAULT, %s )', (staff_username , staff_password , staff_name , staff_mobile, session['code'],post))
            mysql.connection.commit()
            msg = 'You have successfully registered!'
    elif request.method == 'POST':
        msg = 'elif code!'
    return people()

#
#   Login Page
#

@app.route('/R-Portal/login', methods=['GET', 'POST'])
def login():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        passtext = request.form['password']
        password = hashlib.sha256((passtext).encode('utf-8')).hexdigest()
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM userdetails WHERE username = %s AND password = %s ', (username, password))
        account = cursor.fetchone()
        if account:
            session['user'] = True
            session['uid'] = account['uid']
            session['username'] = account['username']
            session['user_name'] = account['name']
            session['user_email'] = account['email']
            session['user_mobile'] = account['mobile']
            return uotp() 
        elif request.method == 'POST' and 'username' in request.form and 'password' in request.form:
            username = request.form['username']
            passtext = request.form['password']
            password = hashlib.sha256((passtext).encode('utf-8')).hexdigest()
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute('SELECT * FROM admin WHERE Ausername = %s AND Apassword = %s', (username, password,))
            account = cursor.fetchone()
            if account:
                session['admin'] = True
                session['Aid'] = account['Aid']
                session['Ausername'] = account['Ausername']
                return render_template("admin/admin.html")       
            elif request.method == 'POST' and 'username' in request.form and 'password' in request.form:
                username = request.form['username']
                passtext = request.form['password']
                password = hashlib.sha256((passtext).encode('utf-8')).hexdigest()
                cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
                cursor.execute('SELECT * FROM security WHERE security_username = %s AND security_password = %s AND security_status=%s', (username, password,'active'))
                account = cursor.fetchone()
                if account:
                    session['security'] = True
                    session['security_id'] = account['security_id']
                    session['security_username'] = account['security_username']
                    session['security_code'] = account['security_code']
                    return render_template("security/security_home.html")       
                elif request.method == 'POST' and 'username' in request.form and 'password' in request.form:
                    username = request.form['username']
                    passtext = request.form['password']
                    password = hashlib.sha256((passtext).encode('utf-8')).hexdigest()
                    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
                    cursor.execute('SELECT * FROM staff WHERE staff_username = %s AND staff_password = %s AND staff_status=%s', (username, password,'active'))
                    account = cursor.fetchone()
                    if account:
                        session['staff'] = True
                        session['staff_id'] = account['staff_id']
                        session['staff_username'] = account['staff_username']
                        session['staff_code'] = account['staff_code']
                        session['staff_post'] = account['post']
                        return render_template("staff/staff_home.html") 
                    elif request.method == 'POST' and 'username' in request.form and 'password' in request.form:
                        username = request.form['username']
                        passtext = request.form['password']
                        password = hashlib.sha256((passtext).encode('utf-8')).hexdigest()
                        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
                        cursor.execute('SELECT * FROM security WHERE security_username = %s AND security_password = %s AND security_status=%s', (username, password,'request'))
                        account = cursor.fetchone()
                        if account:
                            msg = 'Your account is not activated yet or under verification process! Please come back once your account get verified!!'
                        elif request.method == 'POST' and 'username' in request.form and 'password' in request.form:
                            username = request.form['username']
                            passtext = request.form['password']
                            password = hashlib.sha256((passtext).encode('utf-8')).hexdigest()
                            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
                            cursor.execute('SELECT * FROM staff WHERE staff_username = %s AND staff_password = %s AND staff_status=%s', (username, password,'request'))
                            account = cursor.fetchone()
                            if account:
                                msg = 'Your account is not activated yet or under verification process! Please come back once your account get verified!!'  
                            elif request.method == 'POST' and 'username' in request.form and 'password' in request.form:
                                username = request.form['username']
                                passtext = request.form['password']
                                password = hashlib.sha256((passtext).encode('utf-8')).hexdigest()
                                cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
                                cursor.execute('SELECT * FROM security WHERE security_username = %s AND security_password = %s AND security_status=%s', (username, password,'inactive'))
                                account = cursor.fetchone()
                                if account:
                                    msg = 'Your account is temparorily disbanded! Contact Secretary of your society to learn more.'
                                elif request.method == 'POST' and 'username' in request.form and 'password' in request.form:
                                    username = request.form['username']
                                    passtext = request.form['password']
                                    password = hashlib.sha256((passtext).encode('utf-8')).hexdigest()
                                    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
                                    cursor.execute('SELECT * FROM staff WHERE staff_username = %s AND staff_password = %s AND staff_status=%s', (username, password,'inactive'))
                                    account = cursor.fetchone()
                                    if account:
                                        msg = 'Your account is temparorily disbanded! Contact Secretary of your society to learn more.'
                                    else:
                                        msg = 'Incorrect username/password! Please check Username/Password and try again!'
    return render_template('login.html', msg=msg)

#   User OTP Validators
@app.route('/validate',methods=["POST"])
def validate(): 
    if 'user' in session:     
        user_otp = request.form['otp']  
        if otp == int(user_otp):  
              return redirect(url_for('mainhome')) 
        else: 
            msg = 'OTP Does not match! Try Again!!'
            return render_template('otp.html', msg=msg)
    elif session.get('user') is None:
            return login()
    else:
        return logout()

def uotp(): 
    if 'user' in session:
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM  userdetails WHERE uid = %s', (session['uid'],))
        account = cursor.fetchone()
        if account:
            email = account['email']
            msg = Message('OTP confirmation for RPortal' ,sender ='Rportal<me@Rportal.com', recipients = [email])
            msg.body = part2 + str(otp)+ part3 
            mail.send(msg) 
            msg1 = 'OTP: ',otp
            return render_template('otp.html', msg1=msg1)
        else:
            msg = 'Something went wrong:( Please try again!'
    elif session.get('user') is None:
        return login()
    else: 
        return logout()
 
#   Forgot Password
@app.route('/R-Portal/forgot_password', methods=['GET', 'POST'])
def forgot_password():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'email' in request.form and 'password' in request.form:
        username = request.form['username']
        mail = request.form['email']
        passtext = request.form['password']
        password = hashlib.sha256((passtext).encode('utf-8')).hexdigest()
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM userdetails WHERE username = %s AND email = %s', (username, mail,))
        account = cursor.fetchone()
        if account:
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute('UPDATE userdetails SET password = %s WHERE username = %s', (password,username))  
            mysql.connection.commit()
            msg = 'Password Changed Sucsessfully'
            return render_template('forgot_password.html', msg=msg)
        elif request.method == 'POST' and 'username' in request.form:
            username = request.form['username']
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute('SELECT * FROM security WHERE security_username = %s', (username,))
            account = cursor.fetchone()
            if account:
                msg = 'Cannot change password for Security! Contact Secretary to change your password.'
                return render_template('forgot_password.html', msg=msg)       
            elif request.method == 'POST' and 'username' in request.form:
                username = request.form['username']
                cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
                cursor.execute('SELECT * FROM staff WHERE staff_username = %s', (username,))
                account = cursor.fetchone()
                if account:
                    msg = 'Cannot change password for Staff! Contact Secretary to change your password.'
                    return render_template('forgot_password.html', msg=msg)    
                else:
                    msg = 'Invalid username/Email! Please check Username/Email and try again!'
                    return render_template('forgot_password.html', msg=msg)    
    return render_template('forgot_password.html', msg=msg)

#   Logout 
@app.route('/R-Portal/logout')
def logout():   
    if 'secretary' in session:
        session.pop('secretary', None)
        session.pop('Sid', None)
        session.pop('Sname', None)
        session.pop('Susername', None)
        session.pop('Scode', None)
        session.pop('Semail', None)
        session.pop('user', None)
        session.pop('uid', None)
        session.pop('username', None)
        session.pop('user_name', None)
        session.pop('user_email', None)
        session.pop('user_mobile', None)
        session.pop('member', None)
        session.pop('Mid', None)
        session.pop('Mname', None)
        session.pop('Musername', None)
        session.pop('Mcode', None)
        session.pop('Memail',None)
        return redirect(url_for('rportal'))
    elif 'member' in session:
        session.pop('member', None)
        session.pop('Mid', None)
        session.pop('Mname', None)
        session.pop('Musername', None)
        session.pop('Mcode', None)
        session.pop('Memail',None)
        session.pop('secretary', None)
        session.pop('Sid', None)
        session.pop('Sname', None)
        session.pop('Susername', None)
        session.pop('Scode', None)
        session.pop('Semail', None)
        session.pop('user', None)
        session.pop('uid', None)
        session.pop('username', None)
        session.pop('user_name', None)
        session.pop('user_email', None)
        session.pop('user_mobile', None)
        return redirect(url_for('rportal'))
    elif 'admin' in session:
        session.pop('admin', None)
        session.pop('id', None)
        session.pop('username', None)
        return redirect(url_for('rportal'))
    elif 'security' in session:
        session.pop('security', None)
        session.pop('id', None)
        session.pop('username', None)
        session.pop('security_code', None)
        return redirect(url_for('rportal'))
    elif 'staff' in session:
        session.pop('staff', None)
        session.pop('id', None)
        session.pop('username', None)
        session.pop('staff_code', None)
        session.pop('staff_post', None)
        return redirect(url_for('rportal'))
    elif 'user' in session:
        session.pop('user', None)
        session.pop('uid', None)
        session.pop('username', None)
        session.pop('user_name', None)
        session.pop('user_email', None)
        session.pop('user_mobile', None)
        session.pop('secretary', None)
        session.pop('Sid', None)
        session.pop('Sname', None)
        session.pop('Susername', None)
        session.pop('Scode', None)
        session.pop('Semail', None)
        session.pop('member', None)
        session.pop('Mid', None)
        session.pop('Mname', None)
        session.pop('Musername', None)
        session.pop('Mcode', None)
        session.pop('Memail',None)
        return redirect(url_for('rportal'))

#
#   User Part (MainHomePage)
#
@app.route('/R-Portal/mainhome')
def mainhome():
    session.pop('member', None)
    session.pop('Mid', None)
    session.pop('Mname', None)
    session.pop('Musername', None)
    session.pop('Mcode', None)
    session.pop('Memail', None)
    session.pop('secretary', None)
    session.pop('Sid', None)
    session.pop('Sname', None)
    session.pop('Susername', None)
    session.pop('Scode', None)
    session.pop('Semail', None)

    if 'user' in session:
        username = session['username']
        cursor1 = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor1.execute('select * from secretary inner join society where society.code = secretary.Scode AND username = %s AND secretarty_status = %s ', (username,"active"))
        account1 = cursor1.fetchall()
        cursor2 = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor2.execute('select * from member inner join society where society.code = member.Mcode AND username =  %s AND member_status = %s', (username,"active"))
        account2 = cursor2.fetchall()
        cursor3 = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor3.execute('select * from secretary inner join society where society.code = secretary.Scode AND username = %s AND secretarty_status = %s ', (username,"inactive"))
        account3 = cursor3.fetchall()
        cursor4 = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor4.execute('select * from member inner join society where society.code = member.Mcode AND username =  %s AND member_status = %s', (username,"inactive"))
        account4 = cursor4.fetchall()
        cursor5 = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor5.execute('select * from secretary inner join society where society.code = secretary.Scode AND username = %s AND secretarty_status = %s ', (username,"request"))
        account5 = cursor5.fetchall()
        cursor6 = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor6.execute('select * from member inner join society where society.code = member.Mcode AND username =  %s AND member_status = %s', (username,"request"))
        account6 = cursor6.fetchall()
        return render_template('mainhome.html',account1 = account1,account2 =account2,account3 =account3 ,account4 =account4,account5 =account5,account6 =account6) 
    elif session.get('user') is None:
            return login()
    else:
        return logout()
   

#
#   Secretary Part
#
@app.route('/R-Portal/society_details')
def people():
    if 'secretary' in session:
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT Mname, member_status, Mmobile ,Mid, Mflatno,Mwing ,Memail from secretary inner join member on secretary.Scode = member.Mcode WHERE Sid = %s AND member_status=%s', (session['Sid'],'active'))
        account = cursor.fetchall()     
        cursor1 = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor1.execute('SELECT Sname,secretarty_status, Smobile ,Semail from secretary WHERE Sid = %s AND secretarty_status=%s', (session['Sid'],'active'))
        account1 = cursor1.fetchone()  
        cursor2 = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor2.execute('SELECT   security_id,security_name, security_status, security_mobile from secretary inner join security on secretary.Scode = security.security_code WHERE Sid = %s AND security_status=%s', (session['Sid'],'active'))
        account2 = cursor2.fetchall()     
        cursor3 = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor3.execute('SELECT staff_name, staff_status, staff_mobile ,staff_id from secretary inner join staff on secretary.Scode = staff.staff_code WHERE Sid = %s AND staff_status=%s', (session['Sid'],'active'))
        account3 = cursor3.fetchall()         
        return render_template('secretary/people.html', account=account, account1=account1, account2=account2, account3=account3)
    elif session.get('secretary') is None:
        return login()
    else:
        return logout()

@app.route('/R-Portal/inactive_people')
def inpeople():
    if 'secretary' in session:
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT Mname, member_status, Mmobile, Mid ,Memail ,Mflatno,Mwing from secretary inner join member on secretary.Scode = member.Mcode WHERE Sid = %s AND member_status=%s', (session['Sid'],'inactive'))
        account = cursor.fetchall()     
        cursor1 = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor1.execute('SELECT Sname,secretarty_status, Smobile from secretary WHERE Sid = %s AND secretarty_status=%s', (session['Sid'],'inactive'))
        account1 = cursor1.fetchone()  
        cursor2 = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor2.execute('SELECT security_name, security_status, security_mobile,security_id from secretary inner join security on secretary.Scode = security.security_code WHERE Sid = %s AND security_status=%s', (session['Sid'],'inactive'))
        account2 = cursor2.fetchall()     
        cursor3 = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor3.execute('SELECT staff_name, staff_status, staff_mobile ,staff_id from secretary inner join staff on secretary.Scode = staff.staff_code WHERE Sid = %s AND staff_status=%s', (session['Sid'],'inactive'))
        account3 = cursor3.fetchall()        
        return render_template('secretary/inactive_people.html', account=account, account1=account1, account2=account2, account3=account3)
    elif session.get('secretary') is None:
        return login()
    else:
        return logout()

@app.route('/R-Portal/allow_members/')
def allow_members():
    if 'secretary' in session:
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT Mid, Mname, member_status, Mmobile, Mwing, Mflatno, Memail, Sname, name from secretary inner join member inner join society on secretary.Scode = member.Mcode AND secretary.Scode = society.code WHERE Sid = %s AND member_status=%s', (session['Sid'],'Request'))
        account = cursor.fetchall() 
        return render_template('secretary/allow_members.html', account=account )
    elif session.get('secretary') is None:
        return login()
    else:
        return logout()
    
@app.route('/R-Portal/a_members/<int:Mid>' , methods=['GET', 'POST'])
def a_members(Mid):
    if 'secretary' in session:
        if request.method == 'POST' and 'Memail' in request.form and 'Mname':
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute("UPDATE member SET member_status = %s WHERE Mid = %s" ,('active',Mid,)) 
            mysql.connection.commit()
            email = request.form['Memail']
            Mname = request.form['Mname']
            msg = Message('Your Joining Request is accepted' ,sender ='Rportal<me@Rportal.com', recipients = [email])
            msg.body ="Hello!" + Mname + " \n your account activate for login please login on rportal ." + part4
            mail.send(msg) 
        return allow_members()
    elif session.get('secretary') is None:
        return login()
    else:
        return logout()

@app.route('/R-Portal/i_members/<int:Mid>', methods=['GET', 'POST'])
def i_members(Mid):
    if 'secretary' in session:
        if request.method == 'POST' and 'Memail' in request.form and 'Mname':
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute("UPDATE member SET member_status = %s WHERE Mid = %s" ,('inactive',Mid,)) 
            mysql.connection.commit()
            email = request.form['Memail']
            Mname = request.form['Mname']
            msg = Message('Account Inactive' ,sender ='Rportal<me@Rportal.com', recipients = [email])
            msg.body ="Hello!" + Mname + " \n You have Temporary Inactive from secreatry please contact with your secretary." + part4
            mail.send(msg)  
            return people()
    elif session.get('secretary') is None:
        return login()
    else:
        return logout()

@app.route('/R-Portal/ac_members/<int:Mid>', methods=['GET', 'POST'])
def ac_members(Mid):
    if 'secretary' in session:
        if request.method == 'POST' and 'Memail' in request.form and 'Mname':
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute("UPDATE member SET member_status = %s WHERE Mid = %s" ,('active',Mid,)) 
            mysql.connection.commit()
            email = request.form['Memail']
            Mname = request.form['Mname']
            msg = Message('Account activated' ,sender ='Rportal<me@Rportal.com', recipients = [email])
            msg.body ="Hello!" + Mname + " \n You have active from secreatry any query please contact with your secretary." + part4
            mail.send(msg)  
        return inpeople()
    elif session.get('secretary') is None:
        return login()
    else:
        return logout()

@app.route('/R-Portal/r_members', methods=['GET', 'POST'])
def r_members():
    if 'secretary' in session:
        if request.method == 'POST' and 'email' in request.form and 'message'  in request.form and 'Mid' :
            email = request.form['email']
            message = request.form['message']
            Sname = request.form['Sname']
            name = request.form['name']
            Mid = request.form['Mid']
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute('DELETE FROM member WHERE Mid = %s',[Mid]) 
            mysql.connection.commit()
            msg = Message('Member Request Rejected' ,sender ='Rportal<me@Rportal.com', recipients = [email])
            msg.body ="Hello! \n Your member request for the "+ name + " is rejected by "+ Sname + "!\n Reason: " + message +"\n\n Thank you for using R-Portal!\n" +part4
            mail.send(msg)  
            msg = 'Member Rejected/Deleted'
        return allow_members()
    elif session.get('secretary') is None:
        return login()
    else:
        return logout()

@app.route('/R-Portal/d_members/<int:Mid>' , methods=['GET', 'POST'])
def d_members(Mid):
    if 'secretary' in session:
        if request.method == 'POST' and 'Memail' in request.form and 'Mname':
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute('DELETE FROM member WHERE Mid = %s',[Mid]) 
            mysql.connection.commit()
            email = request.form['Memail']
            Mname = request.form['Mname']
            msg = Message('Account Delete' ,sender ='Rportal<me@Rportal.com', recipients = [email])
            msg.body ="Hello!" + Mname + " \n Your account has deleted from secreatry please contact with your secretary.\n" + part4
            mail.send(msg)  
        return people()
    elif session.get('secretary') is None:
        return login()
    else:
        return logout()

@app.route('/R-Portal/din_members/<int:Mid>')
def din_members(Mid):
    if 'secretary' in session:
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('DELETE FROM member WHERE Mid = %s',[Mid]) 
        mysql.connection.commit()
        msg = 'Member Delete'
        return inpeople()
    elif session.get('secretary') is None:
        return login()
    else:
        return logout()

@app.route('/R-Portal/i_security/<int:security_id>', methods=['GET', 'POST'])
def i_security(security_id):
    if 'secretary' in session:
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute("UPDATE security SET security_status = %s WHERE security_id= %s" ,('inactive',security_id,)) 
        mysql.connection.commit()
        return people()
    elif session.get('secretary') is None:
        return login()
    else:
        return logout()
        
@app.route('/R-Portal/a_security/<int:security_id>', methods=['GET', 'POST'])
def a_security(security_id):
    if 'secretary' in session:
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute("UPDATE security SET security_status = %s WHERE security_id= %s" ,('active',security_id,)) 
        mysql.connection.commit()
        return inpeople()
    elif session.get('secretary') is None:
        return login()
    else:
        return logout()

@app.route('/R-Portal/d_security/<int:security_id>')
def d_security(security_id):
    if 'secretary' in session:
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('DELETE FROM security WHERE security_id = %s',[security_id]) 
        mysql.connection.commit()
        return people()
    elif session.get('secretary') is None:
        return login()
    else:
        return logout()

@app.route('/R-Portal/din_security/<int:security_id>')
def din_security(security_id):
    if 'secretary' in session:
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('DELETE FROM security WHERE security_id = %s',[security_id]) 
        mysql.connection.commit()
        return inpeople()
    elif session.get('secretary') is None:
        return login()
    else:
        return logout()

@app.route('/R-Portal/i_staff/<int:staff_id>', methods=['GET', 'POST'])
def i_staff(staff_id):
    if 'secretary' in session:
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute("UPDATE staff SET staff_status = %s WHERE staff_id= %s" ,('inactive',staff_id,)) 
        mysql.connection.commit()
        return people()
    elif session.get('secretary') is None:
        return login()
    else:
        return logout()
        
@app.route('/R-Portal/a_staff/<int:staff_id>', methods=['GET', 'POST'])
def a_staff(staff_id):
    if 'secretary' in session:
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute("UPDATE staff SET staff_status = %s WHERE staff_id= %s" ,('active',staff_id,)) 
        mysql.connection.commit()
        return inpeople()
    elif session.get('secretary') is None:
        return login()
    else:
        return logout()

@app.route('/R-Portal/d_staff/<int:staff_id>')
def d_staff(staff_id):
    if 'secretary' in session:
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('DELETE FROM staff WHERE staff_id = %s',[staff_id]) 
        mysql.connection.commit()
        return people()
    elif session.get('secretary') is None:
        return login()
    else:
        return logout()

@app.route('/R-Portal/din_staff/<int:staff_id>')
def din_staff(staff_id):
    if 'secretary' in session:
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('DELETE FROM staff WHERE staff_id = %s',[staff_id]) 
        mysql.connection.commit()
        return inpeople()
    elif session.get('secretary') is None:
        return login()
    else:
        return logout()

@app.route('/R-Portal/shome', methods=['GET','POST'])
def shome():
    if 'user' in session:
        if request.method == 'POST' and 'Sname' in request.form and 'Scode' in request.form and 'Semail'  in request.form and 'username'  in request.form and 'Sid':
            Sname= request.form['Sname']
            Scode = request.form['Scode']
            Semail = request.form['Semail']
            username = request.form['username']
            Sid = request.form['Sid']
            session['secretary'] = True
            session['Sid'] = Sid
            session['Susername'] = username
            session['Scode'] = Scode
            session['Semail'] = Semail
            session['Sname'] = Sname
        if 'secretary' in session:
                return render_template('secretary/shome.html')
        elif 'secretary' in session:
            return render_template('secretary/shome.html')
        elif session.get('secretary') is None:
            return login()
   
    elif session.get('user') is None:
            return login()

    else:
        return logout()

@app.route('/R-Portal/sprofile')
def sprofile():
    if 'secretary' in session:
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM secretary INNER JOIN society ON secretary.Scode = society.code WHERE Sid = %s', (session['Sid'],))
        account = cursor.fetchone()
        return render_template('secretary/sprofile.html', account=account)
    elif session.get('secretary') is None:
        return login()
    else:
        return logout()

@app.route('/R-Portal/createnotice', methods=['GET', 'POST'] )
def createnotice():
    if 'secretary' in session:
        if request.method == 'POST' and 'editor' in request.form and 'subject' :
            notice_subject = request.form['subject']
            notice_message = request.form['editor']
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute('INSERT INTO notice VALUES (NULL, %s , %s, %s, DEFAULT )', (notice_subject ,notice_message , session['Scode'] ))
            mysql.connection.commit()
        return render_template('secretary/createnotice.html')
    elif session.get('secretary') is None:
        return login()
    else:
        return logout()
    
@app.route('/R-Portal/manage_complaint', methods=['GET','POST'])
def complaint():
    if 'secretary' in session:
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM complaint WHERE complaint_status = %s AND complaint_code = %s', ('active', session['Scode']))
        account = cursor.fetchall()
        cursor1 = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor1.execute('SELECT * FROM complaint WHERE complaint_status = %s AND complaint_code = %s', ('review', session['Scode']))
        account1 = cursor1.fetchall()
        cursor2 = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor2.execute('SELECT * FROM complaint WHERE complaint_status = %s AND complaint_code = %s', ('closed', session['Scode']))
        account2 = cursor2.fetchall()
        if request.method == 'POST' and 'cid' in request.form and 'reply' in request.form:
            complaint_id = request.form['cid']
            complaint_reply = request.form['reply']
            cursor3 = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor3.execute('UPDATE complaint SET complaint_reply_closing = %s, complaint_status = %s  WHERE complaint_id = %s', (complaint_reply, 'closed', complaint_id ))
            mysql.connection.commit()
        return render_template('secretary/complaint.html', account=account, account1=account1, account2=account2)
    elif session.get('secretary') is None:
        return login()
    else:
        return logout()

def generateToken():
    token = jwt.encode( {'iss': API_KEY, 'exp': time() + 5000},
        API_SEC,
        algorithm = 'HS256'  
    )
    return token

@app.route('/R-Portal/createmeeting', methods=['GET', 'POST'] )
def createmeeting():
    if 'secretary' in session:
        msg = ''
        msg1 = ''
        if request.method == 'POST' and 'topic' in request.form and 'starttime' in request.form and 'duration' in request.form and 'agenda' in request.form  :
            topic = request.form['topic']
            start_time = request.form['starttime']
            duration = request.form['duration']
            agenda = request.form['agenda']
            meetingdetails = {
                "topic":  topic,
                "type": 1,
                "start_time":  start_time,
                "duration":  duration,
                "timezone": "India/Mumbai",
                "agenda":  agenda,
               
                "recurrence": {"type": 1,
                            "repeat_interval": 2
                            },
                "settings": {"host_video": "true",
                            "participant_video": "true",
                            "join_before_host": "true",
                            "mute_upon_entry": "False",
                            "watermark": "true",
                            "audio": "voip",
                            "auto_recording": "cloud",
                            "private_meeting":"true",
                            "pre_schedule":"true",
                            }
                }
            headers = {'authorization': 'Bearer %s' % generateToken(),
               'content-type': 'application/json'}
            r = requests.post(
            f'https://api.zoom.us/v2/users/me/meetings/', 
            headers=headers, data=json.dumps(meetingdetails))
            print("\n creating zoom meeting ... \n")
            print(r.text,sep='\n')
            print("\n creating zoom meeting ... \n")
            join_URL = [json.loads(r.text)]
            #meetingPassword = ["password"]
            print(
                f'\n here is your zoom meeting link {join_URL} and your \ password: \n')
            msg = join_URL
            #msg1 = "paasword :" + meetingPassword
        return render_template('secretary/createmeeting.html', msg = msg)
    elif session.get('secretary') is None:
        return login()
    else:
        return logout()

@app.route('/R-Portal/contact')
def contact():
    if 'secretary' in session:
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT *  from contact WHERE society_code = %s', (session['Scode'],) ) 
        account = cursor.fetchall() 
        return render_template('secretary/contact.html', account=account)
    elif session.get('secretary') is None:
        return login()
    else:
        return logout()

@app.route('/R-Portal/add_contact', methods=['GET', 'POST'] )
def add_contact():
    if 'secretary' in session:
        msg = ''
        if request.method == 'POST'and 'contact_label' in request.form and 'contact_no'  in request.form and 'Scode' :
            contact_label = request.form['contact_label']
            contact_no = request.form['contact_no']
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute('INSERT INTO contact values (NULL , %s, %s, %s)', (contact_label, contact_no,session['Scode']))
            mysql.connection.commit()    
            msg="Contacts Inserted!"  
        return contact()
    elif session.get('secretary') is None:
        return login()
    else:
        return logout()
        
@app.route('/R-Portal/d_contact/<int:contact_id>' , methods=['GET', 'POST'])
def d_contact(contact_id):
    if 'secretary' in session:
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute('DELETE FROM contact WHERE contact_id = %s',[contact_id]) 
            mysql.connection.commit()
            return contact()
    elif session.get('secretary') is None:
        return login()
    else:
        return logout()

@app.route('/R-Portal/add_docs', methods=['GET', 'POST'] )
def add_docs():
    if 'secretary' in session:
        msg = ''
        target1 = os.path.join( '/Rportal/static/upload/docs/')
        if not os.path.isdir(target1):
            os.makedirs(target1)
        if request.method == 'POST'and 'document'  :
             ...
        file = request.files['document']
        file_name = file.filename or ''
        destination = ''.join([target1, file_name])
        file.save(destination)
        doc_filename = file_name;
        document = destination  ;
        ... 
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('INSERT INTO document values (NULL , %s, %s, %s)', (doc_filename,session['Scode'], document))
        mysql.connection.commit()    
        msg="File upload suceesfully"   
        return docs()
    elif session.get('secretary') is None:
        return login()
    else:
        return logout()

@app.route('/R-Portal/docs')
def docs():
    if 'secretary' in session:
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT *  from document WHERE society_code = %s', (session['Scode'],) ) 
        account = cursor.fetchall() 
        return render_template('secretary/docs.html', account=account)
    elif session.get('secretary') is None:
        return login()
    else:
        return logout()
        
@app.route('/R-Portal/d_docs/<int:doc_id>' , methods=['GET', 'POST'])
def d_docs(doc_id):
    if 'secretary' in session:
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('DELETE FROM document  WHERE doc_id = %s',[doc_id]) 
        mysql.connection.commit()
        return docs()
    elif session.get('secretary') is None:
        return login()
    else:
        return logout()

@app.route('/R-Portal/invite')
def invite():
    if 'secretary' in session:
        account = session['Scode'];
        return render_template('secretary/invite.html', account=account)
    elif session.get('secretary') is None:
        return login()
    else:
        return logout() 

@app.route('/R-Portal/chats')
def chats():
    if 'secretary' in session:
        cursor1 = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor1.execute('DELETE FROM chat WHERE society_code = %s AND msg_time < now() - interval 3 day', (session['Scode'],))
        mysql.connection.commit()
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT *  from chat WHERE society_code = %s', (session['Scode'],) ) 
        account = cursor.fetchall() 
        return render_template('secretary/chats.html', account=account)
    elif session.get('secretary') is None:
        return login()
    else:
        return logout() 

@app.route('/R-Portal/add_chats', methods=['GET', 'POST'] )
def add_chats():
    if 'secretary' in session:
        msg = ''
        if request.method == 'POST'and 'message' in request.form :
            message = request.form['message']
            msg_username = session['Sname'] 
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute('INSERT INTO chat values (NULL , %s, %s, %s,  DEFAULT )', ( msg_username , message,session['Scode']))
            mysql.connection.commit()   
            cursor1 = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor1.execute('DELETE FROM chat WHERE society_code = %s AND msg_time < now() - interval 3 day', (session['Scode'],))
            mysql.connection.commit()
        return redirect(url_for('chats'))
        
    elif session.get('secretary') is None:
        return login()
    else:
        return logout()
             
#
#   Member Part
#
@app.route('/R-Portal/mhome' , methods=['GET','POST'])
def mhome():
    if 'user' in session:
        if request.method == 'POST' and 'Mname' in request.form and 'Mcode' in request.form and 'Memail'  in request.form and 'username'  in request.form and 'Mid':
            Mname= request.form['Mname']
            Mcode = request.form['Mcode']
            Memail = request.form['Memail']
            username = request.form['username']
            Mid = request.form['Mid']
            session['member'] = True
            session['Mid'] = Mid
            session['Musername'] = username
            session['Mcode'] = Mcode
            session['Memail'] = Memail
            session['Mname'] = Mname
        if 'member' in session:
                return render_template('member/mhome.html', Mname=session['Mname'])
        elif 'member' in session:
                return render_template('member/mhome.html', Mname=session['Mname'])
        elif session.get('member') is None:
                return login()
    elif session.get('user') is None:
            return login()
    else:
        return logout()

@app.route('/R-Portal/mprofile')
def mprofile():
    if 'member' in session:
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT username, Memail, Mname, Mflatno, Mwing, Mmobile, code, name, city, road, area, state, pin FROM member INNER JOIN society ON member.Mcode = society.code WHERE Mid = %s;', (session['Mid'],))
        account = cursor.fetchone()
        return render_template('member/mprofile.html', account=account)
    elif session.get('member') is None:
        return login()
    else:
        return logout()

@app.route('/R-Portal/viewnotice')
def viewnotice():
    if 'member' in session:
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT *  from notice WHERE notice_code = %s', (session['Mcode'],) ) 
        account = cursor.fetchall() 
        return render_template('member/viewnotice.html', account=account)
    elif session.get('member') is None:
        return login()
    else:
        return logout()
    
@app.route('/R-Portal/docsm')
def docsm():
    if 'member' in session:
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT *  from document WHERE society_code = %s', (session['Mcode'],) ) 
        account = cursor.fetchall() 
        return render_template('member/docsm.html', account=account)
    elif session.get('member') is None:
        return login()
    else:
        return logout()

@app.route('/R-Portal/complaint', methods=['GET','POST'])
def member_complaint():
    if 'member' in session:
        msg = ''
        cursor1 = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor1.execute('SELECT post from staff WHERE staff_code= %s AND staff_status=%s', (session['Mcode'],'active',))
        account = cursor1.fetchall() 
        cursor4 = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor4.execute('SELECT * from complaint WHERE complaint_username= %s AND complaint_status = %s', (session['Musername'], 'active'))
        account4 = cursor4.fetchall()
        cursor2 = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor2.execute('SELECT * from complaint WHERE complaint_username= %s AND complaint_status = %s', (session['Musername'], 'review'))
        account2 = cursor2.fetchall()
        cursor3 = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor3.execute('SELECT * from complaint WHERE complaint_username= %s AND complaint_status = %s', (session['Musername'], 'closed'))
        account3 = cursor3.fetchall() 
        if request.method == 'POST' and 'complaint_subject' in request.form and 'complaint_message' in request.form and 'complaint_against'in request.form:  
            compaint_subject = request.form['complaint_subject']
            complaint_message = request.form['complaint_message']
            complaint_against = request.form['complaint_against']
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute('INSERT INTO complaint VALUES (NULL, %s, %s, %s, %s, %s, %s, DEFAULT, NULL, NULL, DEFAULT)', (session['Musername'] , session['Mname'] , compaint_subject, complaint_message, session['Mcode'], complaint_against,))
            mysql.connection.commit()
            msg = 'Complaint Added Succsesfully!'
        elif request.method == 'POST':
            msg = 'Please fill out the form!'
        return render_template('member/member_complaint.html', msg=msg , account=account,account2= account2, account3=account3, account4=account4)
    elif session.get('member') is None:
        return login()
    else:
        return logout()

@app.route('/R-Portal/view_contact')
def view_contact():
    if 'member' in session:
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT *  from contact WHERE  society_code = %s', (session['Mcode'],) ) 
        account = cursor.fetchall() 
        return render_template('member/view_contact.html', account=account)
    elif session.get('member') is None:
        return login()
    else:
        return logout()

@app.route('/R-Portal/chat')
def chat():
    if 'member' in session:
        cursor1 = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor1.execute('DELETE FROM chat WHERE society_code = %s AND msg_time < now() - interval 3 day', (session['Mcode'],))
        mysql.connection.commit()
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT *  from chat WHERE society_code = %s', (session['Mcode'],) ) 
        account = cursor.fetchall() 
        return render_template('member/chat.html', account=account)
    elif session.get('member') is None:
        return login()
    else:
        return logout() 

@app.route('/R-Portal/add_chat', methods=['GET', 'POST'] )
def add_chat():
    if 'member' in session:
        msg = ''
        if request.method == 'POST'and 'message' in request.form :
            message = request.form['message']
            msg_username = session['Mname'] 
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute('INSERT INTO chat values (NULL , %s, %s, %s,  DEFAULT )', ( msg_username , message,session['Mcode']))
            mysql.connection.commit() 
            cursor1 = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor1.execute('DELETE FROM chat WHERE society_code = %s AND msg_time < now() - interval 3 day', (session['Mcode'],))
            mysql.connection.commit()
        return redirect(url_for('chat'))
    elif session.get('member') is None:
        return login()
    else:
        return logout()
              
#
#   Admin Part
#
@app.route('/R-Portal/admin_home')
def admin_home():
    if 'admin' in session:
        return render_template('admin/admin_home.html', Ausername=session['Ausername'])
    elif session.get('admin') is None:
        return login()
    else:
        return logout()

@app.route('/R-Portal/asoc')
def asoc():
    if 'admin' in session:
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT  name, road, area, city, state, pin, Sname, Sflatno, Swing, Smobile, Semail, Scode, acname, acno, mmid, bankname, branch, ifsc, secretarty_status FROM secretary INNER JOIN society on secretary.Scode=society.code WHERE secretarty_status = %s;', ('active',))
        account = cursor.fetchall() 
        return render_template('admin/asoc.html', account=account)
    elif session.get('admin') is None:
        return login()
    else:
        return logout()
  
@app.route('/R-Portal/isoc')
def isoc():
    if 'admin' in session:
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT  name, road, area, city, state, pin, Sname, Sflatno, Swing, Smobile, Semail, Scode, acname, acno, mmid, bankname, branch, ifsc, secretarty_status FROM secretary INNER JOIN society on secretary.Scode=society.code WHERE secretarty_status = %s;', ('inactive',))
        account = cursor.fetchall() 
        return render_template('admin/isoc.html', account=account)
    elif session.get('admin') is None:
        return login()
    else:
        return logout()
    
@app.route('/R-Portal/admin_req/')
def admin_req():
    if 'admin' in session:
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT Sname, secretarty_status, Smobile, Semail, Scode, secretary_time, area, road, city, state, pin, name, kyc_file from secretary inner join society on secretary.Scode = society.code WHERE  secretarty_status = %s', ('request',))
        account = cursor.fetchall()           
        return render_template('admin/admin_req.html', account=account)
    elif session.get('admin') is None:
        return login()
    else:
        return logout()

@app.route('/R-Portal/a_sec/<string:Scode>')
def a_sec(Scode):
    if 'admin' in session:
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute("UPDATE secretary SET secretarty_status = %s WHERE Scode = %s" ,('active',Scode,)) 
        cursor.execute("UPDATE society SET society_status = %s WHERE code = %s" ,('active',Scode,)) 
        cursor.execute("UPDATE member SET member_status = %s WHERE Mcode = %s" ,('inactive',Scode,)) 
        cursor.execute("UPDATE security SET security_status = %s WHERE security_code = %s" ,('active',Scode,)) 
        cursor.execute("UPDATE staff SET staff_status = %s WHERE staff_code = %s" ,('active',Scode,)) 
        mysql.connection.commit()
        msg = 'Society Allowed'
        return admin_req()
    elif session.get('admin') is None:
        return login()
    else:
        return logout()

@app.route('/R-Portal/al_sec/<string:Scode>')
def al_sec(Scode):
    if 'admin' in session:
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute("UPDATE secretary SET secretarty_status = %s WHERE Scode = %s" ,('active',Scode,)) 
        cursor.execute("UPDATE society SET society_status = %s WHERE code = %s" ,('active',Scode,)) 
        cursor.execute("UPDATE member SET member_status = %s WHERE Mcode = %s" ,('inactive',Scode,)) 
        cursor.execute("UPDATE security SET security_status = %s WHERE security_code = %s" ,('active',Scode,)) 
        cursor.execute("UPDATE staff SET staff_status = %s WHERE staff_code = %s" ,('active',Scode,)) 
        mysql.connection.commit()
        msg = 'Society Allowed'
        return isoc()
    elif session.get('admin') is None:
        return login()
    else:
        return logout()

@app.route('/R-Portal/c_sec/<string:Scode>')
def c_sec(Scode):
    if 'admin' in session:
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute("UPDATE secretary SET secretarty_status = %s WHERE Scode = %s" ,('inactive',Scode,)) 
        cursor.execute("UPDATE society SET society_status = %s WHERE code = %s" ,('inactive',Scode,)) 
        cursor.execute("UPDATE member SET member_status = %s WHERE Mcode = %s" ,('inactive',Scode,)) 
        cursor.execute("UPDATE security SET security_status = %s WHERE security_code = %s" ,('active',Scode,)) 
        cursor.execute("UPDATE staff SET staff_status = %s WHERE staff_code = %s" ,('active',Scode,)) 
        mysql.connection.commit()
        msg = 'Society Disbanded'
        return asoc()
    elif session.get('admin') is None:
        return login()
    else:
        return logout()

@app.route('/R-Portal/r_sec' , methods=['GET', 'POST'])
def r_sec():
    if 'admin' in session:
        if request.method == 'POST' and 'email' in request.form and 'message'  in request.form and 'Scode' :
            email = request.form['email']
            message = request.form['message']
            Scode = request.form['Scode']
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute('DELETE FROM secretary WHERE Scode = %s',[Scode]) 
            cursor.execute('DELETE FROM society WHERE code = %s',[Scode]) 
            cursor.execute('DELETE FROM member WHERE Mcode = %s',[Scode]) 
            cursor.execute('DELETE FROM security WHERE security_code = %s',[Scode]) 
            cursor.execute('DELETE FROM staff WHERE staff_code = %s',[Scode]) 
            mysql.connection.commit()
            msg = Message('Society Rejected' ,sender ='Rportal<me@Rportal.com', recipients = [email])
            msg.body ="Hi \n"+ message
            mail.send(msg)  
            msg = 'Society Rejected/Deleted'
        return render_template('admin/admin_req.html', msg=msg)
    elif session.get('admin') is None:
        return login()
    else:
        return logout()

@app.route('/R-Portal/contactdata')
def contactdata():
    if 'admin' in session:
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT  * from contactus') 
        account = cursor.fetchall() 
        return render_template('admin/contactdata.html', account=account)
    elif session.get('admin') is None:
        return login()
    else:
        return logout()
   
#
#   Security Part
#
@app.route('/R-Portal/security_home')
def security_home():
    if 'security' in session:
        return render_template('security/security_home.html', security_username=session['security_username'])
    elif session.get('security') is None:
        return login()
    else:
        return logout()

@app.route('/R-Portal/security_profile')
def security_profile():
    if 'security' in session:
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT security_username, security_name, security_mobile, security_code FROM security WHERE security_id = %s;', (session['security_id'],))
        account = cursor.fetchone()
        return render_template('security/security_profile.html', account=account)
    elif session.get('security') is None:
        return login()
    else:
        return logout()

@app.route('/R-Portal/security_complaint',methods=['GET','POST'])
def security_complaint():
    if 'security' in session:
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM complaint WHERE complaint_against = %s AND complaint_status = %s AND complaint_code = %s', ('Security', 'active', session['security_code']))
        account = cursor.fetchall()
        cursor1 = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor1.execute('SELECT * FROM complaint WHERE complaint_against = %s AND complaint_status = %s AND complaint_code = %s', ('Security', 'review', session['security_code']))
        account1 = cursor1.fetchall()
        cursor2 = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor2.execute('SELECT * FROM complaint WHERE complaint_against = %s AND complaint_status = %s AND complaint_code = %s', ('Security', 'closed', session['security_code']))
        account2 = cursor2.fetchall()
        if request.method == 'POST' and 'cid' in request.form and 'reply' in request.form:
            complaint_id = request.form['cid']
            complaint_reply = request.form['reply']
            cursor3 = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor3.execute('UPDATE complaint SET complaint_reply = %s, complaint_status = %s  WHERE complaint_id = %s', (complaint_reply, 'review', complaint_id ))
            mysql.connection.commit()
            security_complaint()
        return render_template('security/security_complaint.html', account=account, account1=account1, account2=account2)
    elif session.get('security') is None:
        return login()
    else:
        return logout()

@app.route('/R-Portal/view_contacts')
def view_contacts():
    if 'security' in session:
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT *  from contact WHERE  society_code = %s', (session['security_code'],) ) 
        account = cursor.fetchall() 
        return render_template('security/view_contact.html', account=account)
    elif session.get('security') is None:
        return login()
    else:
        return logout()
    
#
#   Staff Part

@app.route('/R-Portal/staff_home')
def staff_home():
    if 'staff' in session:
        return render_template('staff/staff_home.html', staff_username=session['staff_username'])
    elif session.get('staff') is None:
        return login()
    else:
        return logout()

@app.route('/R-Portal/staff_profile')
def staff_profile():
    if 'staff' in session:
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT staff_username, staff_name, staff_mobile, staff_code FROM staff WHERE staff_id = %s;', (session['staff_id'],))
        account = cursor.fetchone()
        return render_template('staff/staff_profile.html', account=account)
    elif session.get('staff') is None:
        return login()
    else:
        return logout()

@app.route('/R-Portal/staff_complaint',methods=['GET','POST'])
def staff_complaint():
    if 'staff' in session:
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM complaint WHERE complaint_against = %s AND complaint_status = %s AND complaint_code = %s', (session['staff_post'], 'active', session['staff_code']))
        account = cursor.fetchall()
        cursor1 = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor1.execute('SELECT * FROM complaint WHERE complaint_against = %s AND complaint_status = %s AND complaint_code = %s', (session['staff_post'], 'review', session['staff_code']))
        account1 = cursor1.fetchall()
        cursor2 = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor2.execute('SELECT * FROM complaint WHERE complaint_against = %s AND complaint_status = %s AND complaint_code = %s', (session['staff_post'], 'closed', session['staff_code']))
        account2 = cursor2.fetchall()
        if request.method == 'POST' and 'cid' in request.form and 'reply' in request.form:
            complaint_id = request.form['cid']
            complaint_reply = request.form['reply']
            cursor3 = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor3.execute('UPDATE complaint SET complaint_reply = %s, complaint_status = %s  WHERE complaint_id = %s', (complaint_reply, 'review', complaint_id ))
            mysql.connection.commit()
            staff_complaint()
        return render_template('staff/staff_complaint.html', account=account, account1=account1, account2=account2)
    elif session.get('staff') is None:
        return login()
    else:
        return logout()

@app.route('/R-Portal/view_contactst')
def view_contactst():
    if 'staff' in session:
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT *  from contact WHERE  society_code = %s', (session['staff_code'],) ) 
        account = cursor.fetchall() 
        return render_template('staff/view_contact.html', account=account)
    elif session.get('staff') is None:
        return login()
    else:
        return logout()

#   Contact Us
@app.route('/R-Portal/contactus', methods=['GET', 'POST'] )
def contactus():
    if request.method == 'POST' and 'name' in request.form and 'email' in request.form and 'message' in request.form :
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('INSERT INTO contactus VALUES (NULL, %s, %s, %s)', (name , email , message))
        mysql.connection.commit()
        return render_template('rportal.html')

#
#   Runner Code
#
if __name__ == '__main__':
   app.run(debug=True)