import socket
import dns.resolver;
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
import base64
from PIL import Image
from io import BytesIO


#sys.path.insert(0, 'Rportal/config')
#from config import credentials as cred

API_KEY = 'DVKW9UngTg2lI1FnqrQVWA'
API_SEC = 'ZIN4AsaniiKYBBA0cQHLSupJOIZwMEdbcRm2'

UPLOAD_FOLDER = '/path/to/the/uploads'
UPLOAD_DOCS = '/path/to/the/uploads/docs'
UPLOAD_VPIC = '/path/to/the/uploads/vpic'
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
app.config['UPLOAD_VPIC'] = UPLOAD_VPIC
mysql = MySQL(app)
 
mail = Mail(app)
app.config["MAIL_SERVER"]='smtp.gmail.com'  
app.config["MAIL_PORT"] =465 #465 or 587 
app.config["MAIL_USERNAME"] = 'noreply.rportal@gmail.com'  
app.config['MAIL_PASSWORD'] = 'Ajinfo@1234'  
#app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

part2 ="Your One Time Password for logging into rportal is\n\n" 
part3="""\n\nIf you did not Initiated this request,please ignore this mail.

If you have more queries, feel free to contact us at ajinfotics@gmail.com. 

We will love to help and assist you at any movement.

Automated mail sent by rportal. Please do not reply.
Regards! """
part4 ="""\nIf you have any queries, feel free to contact us at ajinfotics@gmail.com. 
We will love to help and assist you at any movement.
Automated mail sent by RPortal. Please do not reply.
Regards! """
mail = Mail(app)

#   Index Page - rportal
@app.route('/')
def index():
    return rportal()
    
@app.route('/rportal/')
def rportal():
    count1=''
    count2=''
    count3=''
    count4=''

    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('select count(uid) from userdetails')
    count1 =  [v for v in cursor.fetchone().values()][0]

    cursor1 = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor1.execute('select count(Sid) from secretary')
    count2 =  [v for v in cursor1.fetchone().values()][0]

    cursor2 = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor2.execute('select count(Mid) from member')
    count3 =  [v for v in cursor2.fetchone().values()][0]

    cursor3 = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor3.execute('select count(id) from society')
    count4 =  [v for v in cursor3.fetchone().values()][0]

    return render_template('rportal.html', count1=count1, count2=count2, count3=count3, count4=count4)

#
#   Registrations
#
#   User Registration
@app.route('/rportal/register', methods=['GET','POST'])
def  register():
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
            email_address = email
            addressToVerify = email_address
            domain_name = email_address.split('@')[1]
            try:
                records = dns.resolver.query(domain_name, 'MX')
                mxRecord = records[0].exchange
                mxRecord = str(mxRecord)
                host = socket.gethostname()
                server = smtplib.SMTP()
                server.set_debuglevel(0)
                server.connect(mxRecord)
                server.helo(host)
                server.mail('me@domain.com')
                code, message = server.rcpt(str(addressToVerify))
                server.quit()
                if code == 250:
                    email = email
                    register.otp = random.randint(111111,999999)
                    msg = Message('OTP confirmation for RPortal' ,sender ='Residents Portal<me@Rportal.com', recipients = [email])
                    msg.body = part2 + str(register.otp)+ part3 
                    mail.send(msg)
                    msg1 = 'OTP: ',register.otp
                    return render_template('register_otp.html', msg1=msg1, name=name, mobile=mobile, email=email, username=username, password=password)
                else:
                    msg ='Mail adderss not found! Change the address and try again'
                    return render_template('register.html',msg=msg)
            except:
                msg ='Invalid Email address, change address and try again'
                return render_template('register.html',msg=msg)
        return render_template('register.html',msg=msg)
    return render_template('register.html',msg=msg)

@app.route('/rvalidate',methods=["POST"])
def rvalidate(): 
    form_otp = request.form['otp']  
    username = request.form['username']
    password = request.form['password']
    name = request.form['name']
    email = request.form['email']
    mobile = request.form['mobile']
    if register.otp == int(form_otp):  
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('INSERT INTO userdetails VALUES (NULL, %s, %s, %s, %s, %s, DEFAULT)', (username , name ,  password , mobile ,  email ,))
        mysql.connection.commit()
        msg = 'You have successfully registered!'
        return render_template('register.html',msg=msg)
    else: 
        msg = 'OTP Does not match! Try Again!!'
        return render_template('register_otp.html', msg=msg)

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
    
@app.route('/rportal/sregister', methods=['GET','POST'])
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
            cursor1.execute('SELECT * FROM secretary WHERE username = %s AND Scode = %s AND Sflatno = %s AND Swing = %s', (username, code, flatno, wing,))
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
@app.route('/rportal/mcode', methods=['GET', 'POST'])
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

@app.route('/rportal/mcode1/<string:code>', methods=['GET', 'POST'])
def mcode1(code):
    if 'user' in session:
        msg = ''
        code = code
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM society WHERE code = %s', (code,))
        account = cursor.fetchone()
        if account:
            cursor.execute('select name, city, road, area, state, pin, code , Semail from society inner join secretary WHERE code = %s', (code ,))
            account = cursor.fetchone()
            return render_template('member/mverify.html', account=account, name=session['user_name'],username=session['username'], email=session['user_email'], mobile=session['user_mobile'])
        else:
            msg='Invalid Society Code!'
        return render_template('member/Mcode.html', msg=msg)
    elif session.get('user') is None:
            return login()
    else:
        return logout()

@app.route('/rportal/mregister', methods=['GET', 'POST'])
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
                msg = Message('New Member Request' ,sender ='Residents Portal<me@Rportal.com', recipients = [Semail]) 
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
@app.route('/rportal/add_security', methods=['GET','POST'])
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
            cursor.execute('INSERT INTO security VALUES (NULL, %s, %s, %s, %s, %s, DEFAULT)', (security_username , security_password , security_name , security_mobile, session['Scode']))
            mysql.connection.commit()
            msg = 'You have successfully registered!'
    elif request.method == 'POST':
        msg = 'elif code!' 
    return people()

#   Staff Member Registaration
@app.route('/rportal/add_staff', methods=['GET','POST'])
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
            cursor.execute('INSERT INTO staff VALUES (NULL, %s, %s, %s, %s, %s, %s, DEFAULT)',(staff_username, staff_password, staff_name, staff_mobile, post, session['Scode'],))
            mysql.connection.commit()
            msg = 'You have successfully registered!'
    elif request.method == 'POST':
        msg = 'elif code!'
    return people()

#
#   Login Page
#

@app.route('/rportal/login', methods=['GET', 'POST'])
def login():
    msg = ''
    msg1 = ''
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
            cursor.execute('SELECT * FROM userdetails WHERE email = %s AND password = %s ', (username, password,))
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
                    return redirect(url_for('admin_home'))      
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
                                            msg1= 'If you are Security or Staff member, please use username only instead of email and try again'
    return render_template('login.html', msg=msg, msg1=msg1)

#   User OTP Validators
def uotp(): 
    if 'user' in session:
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM  userdetails WHERE uid = %s', (session['uid'],))
        account = cursor.fetchone()
        if account: 
            email = account['email']
            uotp.otp = random.randint(111111,999999)
            msg = Message('OTP confirmation for RPortal' ,sender ='Residents Portal<me@Rportal.com', recipients = [email])
            msg.body = part2 + str(uotp.otp)+ part3 
            mail.send(msg)
            msg1 = 'OTP: ',uotp.otp
            return render_template('otp.html', msg1=msg1)
        else:
            msg = 'Something went wrong:( Please try again!'
    elif session.get('user') is None:
        return login()
    else: 
        return logout()
 
@app.route('/validate',methods=["POST"])
def validate(): 
    if 'user' in session:     
        user_otp = request.form['otp']  
        if uotp.otp == int(user_otp):  
            return redirect(url_for('mainhome')) 
        else: 
            msg = 'OTP Does not match! Try Again!!'
            return render_template('otp.html', msg=msg)
    elif session.get('user') is None:
            return login()
    else:
        return logout()

#   Forgot Password
@app.route('/rportal/forgot_password', methods=['GET', 'POST'])
def forgot_password():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'email' in request.form and 'password' in request.form:
        username = request.form['username']
        email = request.form['email']
        passtext = request.form['password']
        password = hashlib.sha256((passtext).encode('utf-8')).hexdigest()
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM userdetails WHERE username = %s AND email = %s', (username, email,))
        account = cursor.fetchone()
        if account:
            email_address = email
            addressToVerify = email_address
            domain_name = email_address.split('@')[1]
            try:
                records = dns.resolver.query(domain_name, 'MX')
                mxRecord = records[0].exchange
                mxRecord = str(mxRecord)
                host = socket.gethostname()
                server = smtplib.SMTP()
                server.set_debuglevel(0)
                server.connect(mxRecord)
                server.helo(host)
                server.mail('me@domain.com')
                code, message = server.rcpt(str(addressToVerify))
                server.quit()
                if code == 250:
                    email = email
                    forgot_password.otp = random.randint(111111,999999)
                    msg = Message('OTP confirmation for RPortal' ,sender ='Residents Portal<me@Rportal.com', recipients = [email])
                    msg.body = part2 + str(forgot_password.otp)+ part3 
                    mail.send(msg)
                    msg1 = 'OTP: ',forgot_password.otp
                    return render_template('forgot_otp.html', msg1=msg1, username=username, password=password)
                else:
                    msg ='Mail adderss not found! Change the address and try again'
                    return render_template('forgot_password.html',msg=msg)   
            except:
                msg ='Invalid Email address, change address and try again'  
                return render_template('forgot_password.html',msg=msg)   
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
        return render_template('forgot_password.html', msg=msg)
    return render_template('forgot_password.html', msg=msg)

@app.route('/fvalidate',methods=["POST"])
def fvalidate(): 
    form_otp = request.form['otp']  
    username = request.form['username']
    passtext = request.form['password']
    if forgot_password.otp == int(form_otp):  
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('UPDATE userdetails SET password = %s WHERE username = %s', (passtext,username))  
        mysql.connection.commit()
        msg = 'Password Changed Sucsessfully'
        return render_template('forgot_password.html', msg=msg)
    else: 
        msg = 'OTP Does not match! Try Again!!'
        return render_template('forgot_otp.html', msg=msg)


#   Logout 
@app.route('/rportal/logout')
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
        session.pop('Mflatno',None)
        session.pop('Mwing',None)
        return redirect(url_for('rportal'))
    elif 'member' in session:
        session.pop('member', None)
        session.pop('Mid', None)
        session.pop('Mname', None)
        session.pop('Musername', None)
        session.pop('Mcode', None)
        session.pop('Memail',None)
        session.pop('Mflatno',None)
        session.pop('Mwing',None)
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
        session.pop('Mflatno',None)
        session.pop('Mwing',None)
        return redirect(url_for('rportal'))

#
#   User Part (MainHomePage)
#
@app.route('/rportal/mainhome')
def mainhome():
    session.pop('member', None)
    session.pop('Mid', None)
    session.pop('Mname', None)
    session.pop('Musername', None)
    session.pop('Mcode', None)
    session.pop('Memail', None)
    session.pop('Mflatno', None)
    session.pop('Mwing', None)
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
@app.route('/rportal/society_details')
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

@app.route('/rportal/inactive_people')
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

@app.route('/rportal/allow_members/')
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
    
@app.route('/rportal/a_members/<int:Mid>' , methods=['GET', 'POST'])
def a_members(Mid):
    if 'secretary' in session:
        if request.method == 'POST' and 'Memail' in request.form and 'Mname':
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute("UPDATE member SET member_status = %s WHERE Mid = %s" ,('active',Mid,)) 
            mysql.connection.commit()
            email = request.form['Memail']
            Mname = request.form['Mname']
            msg = Message('Your Joining Request is accepted' ,sender ='Residents Portal<me@Rportal.com', recipients = [email])
            msg.body ="Hello!" + Mname + " \n your account activate for login please login on rportal ." + part4
            mail.send(msg) 
        return allow_members()
    elif session.get('secretary') is None:
        return login()
    else:
        return logout()

@app.route('/rportal/i_members/<int:Mid>', methods=['GET', 'POST'])
def i_members(Mid):
    if 'secretary' in session:
        if request.method == 'POST' and 'Memail' in request.form and 'Mname':
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute("UPDATE member SET member_status = %s WHERE Mid = %s" ,('inactive',Mid,)) 
            mysql.connection.commit()
            email = request.form['Memail']
            Mname = request.form['Mname']
            msg = Message('Account Inactive' ,sender ='Residents Portal<me@Rportal.com', recipients = [email])
            msg.body ="Hello!" + Mname + " \n You have Temporary Inactive from secreatry please contact with your secretary." + part4
            mail.send(msg)  
            return people()
    elif session.get('secretary') is None:
        return login()
    else:
        return logout()

@app.route('/rportal/ac_members/<int:Mid>', methods=['GET', 'POST'])
def ac_members(Mid):
    if 'secretary' in session:
        if request.method == 'POST' and 'Memail' in request.form and 'Mname':
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute("UPDATE member SET member_status = %s WHERE Mid = %s" ,('active',Mid,)) 
            mysql.connection.commit()
            email = request.form['Memail']
            Mname = request.form['Mname']
            msg = Message('Account activated' ,sender ='Residents Portal<me@Rportal.com', recipients = [email])
            msg.body ="Hello!" + Mname + " \n You have active from secreatry any query please contact with your secretary." + part4
            mail.send(msg)  
        return inpeople()
    elif session.get('secretary') is None:
        return login()
    else:
        return logout()

@app.route('/rportal/r_members', methods=['GET', 'POST'])
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
            msg = Message('Member Request Rejected' ,sender ='Residents Portal<me@Rportal.com', recipients = [email])
            msg.body ="Hello! \n Your member request for the "+ name + " is rejected by "+ Sname + "!\n Reason: " + message +"\n\n Thank you for using rportal!\n" +part4
            mail.send(msg)  
            msg = 'Member Rejected/Deleted'
        return allow_members()
    elif session.get('secretary') is None:
        return login()
    else:
        return logout()

@app.route('/rportal/d_members/<int:Mid>' , methods=['GET', 'POST'])
def d_members(Mid):
    if 'secretary' in session:
        if request.method == 'POST' and 'Memail' in request.form and 'Mname':
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute('DELETE FROM member WHERE Mid = %s',[Mid]) 
            mysql.connection.commit()
            email = request.form['Memail']
            Mname = request.form['Mname']
            msg = Message('Account Delete' ,sender ='Residents Portal<me@Rportal.com', recipients = [email])
            msg.body ="Hello!" + Mname + " \n Your account has deleted from secreatry please contact with your secretary.\n" + part4
            mail.send(msg)  
        return people()
    elif session.get('secretary') is None:
        return login()
    else:
        return logout()

@app.route('/rportal/din_members/<int:Mid>')
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

@app.route('/rportal/i_security/<int:security_id>', methods=['GET', 'POST'])
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
        
@app.route('/rportal/a_security/<int:security_id>', methods=['GET', 'POST'])
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

@app.route('/rportal/d_security/<int:security_id>')
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

@app.route('/rportal/din_security/<int:security_id>')
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

@app.route('/rportal/i_staff/<int:staff_id>', methods=['GET', 'POST'])
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
        
@app.route('/rportal/a_staff/<int:staff_id>', methods=['GET', 'POST'])
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

@app.route('/rportal/d_staff/<int:staff_id>')
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

@app.route('/rportal/din_staff/<int:staff_id>')
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

@app.route('/rportal/shome', methods=['GET','POST'])
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
            session['Scode']= Scode
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

@app.route('/rportal/sprofile')
def sprofile():
    if 'secretary' in session:
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM secretary INNER JOIN society ON secretary.Scode = society.code WHERE Sid = %s', (session['Sid'],))
        account = cursor.fetchone()

        cursor1 = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor1.execute('SELECT username FROM  member where member_status=%s AND Mcode=%s', ('active', session['Scode'], ) )
        account1 = cursor1.fetchall()

        return render_template('secretary/sprofile.html', account=account, account1=account1)
    elif session.get('secretary') is None:
        return login()
    else:
        return logout()

@app.route('/rportal/sprofile/<string:msg>')
def sprofile1(msg):
    if 'secretary' in session:
        msg = msg
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM secretary INNER JOIN society ON secretary.Scode = society.code WHERE Sid = %s', (session['Sid'],))
        account = cursor.fetchone()

        cursor1 = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor1.execute('SELECT username FROM  member where member_status=%s AND Mcode=%s', ('active', session['Scode'], ) )
        account1 = cursor1.fetchall()

        return render_template('secretary/sprofile.html', msg=msg, account=account, account1=account1)
    elif session.get('secretary') is None:
        return login()
    else:
        return logout()

@app.route('/rportal/supdate', methods=['GET', 'POST'] )
def supdate():
    if 'secretary' in session:
        msg=''
        if request.method == 'POST' and 'email' in request.form and 'mobile' in request.form:
            email = request.form['email']
            Aname = request.form['name']
            mobile = request.form['mobile']
            cursor2 = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor2.execute('UPDATE secretary SET Sname=%s, Semail=%s, Smobile=%s WHERE Sid=%s', (Aname, email, mobile, session['Sid'],))
            mysql.connection.commit()
            msg ='Profile updated!'
            return sprofile1(msg)
        return sprofile()
    elif session.get('secretary') is None:
        return login()
    else:
        return logout()

@app.route('/rportal/schange', methods=['GET', 'POST'] )
def schange():
    if 'secretary' in session:
        if request.method == 'POST' and 'flatno' in request.form and 'wing' in request.form:
            email = request.form['email']
            username = request.form['username']
            Aname = request.form['name']
            flatno = request.form['flatno']
            wing = request.form['wing']
            mobile = request.form['mobile']
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute('SELECT username FROM member WHERE Mcode = %s AND Mflatno = %s AND Mwing = %s', (session['Scode'], flatno, wing,))
            account = cursor.fetchone()
            cursor1 = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor1.execute('SELECT username FROM secretary WHERE Scode = %s AND Sflatno = %s AND Swing = %s', (session['Scode'], flatno, wing,))
            account1 = cursor1.fetchone()
            if account:
                if account['username'] == username:
                    cursor2 = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
                    cursor2.execute('UPDATE secretary SET Sname=%s, Sflatno=%s, Swing=%s, Semail=%s, Smobile=%s WHERE Sid=%s', (Aname , flatno , wing , email, mobile, session['Sid'],))
                    mysql.connection.commit()
                    msg ='Secretary Changed!'
                    return sprofile1(msg)
                else:
                    msg= 'Please enter valid flat number or wing and try again!'
                    return sprofile1(msg)
            elif account1:
                if account1['username'] == username:
                    cursor2 = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
                    cursor2.execute('UPDATE secretary SET Sname=%s, Sflatno=%s, Swing=%s, Semail=%s, Smobile=%s WHERE Sid=%s', (Aname , flatno , wing , email, mobile, session['Sid'],))
                    mysql.connection.commit()
                    msg ='Secretary Changed!'
                    return sprofile1(msg)
                else:
                    msg= 'Please enter valid flat number or wing and try again!'
                    return sprofile1(msg)
        msg= 'Please enter valid flat number or wing and try again!'
        return sprofile1(msg)
    elif session.get('secretary') is None:
        return login()
    else:
        return logout()
        
@app.route('/rportal/createnotice', methods=['GET', 'POST'] )
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
    
@app.route('/rportal/manage_complaint', methods=['GET','POST'])
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


    #meeting added
@app.route('/rportal/meeting')
def meeting():
    if 'secretary' in session:
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT *  from meetings WHERE society_code = %s  ', (session['Scode'],) ) 
        account = cursor.fetchall()
        return render_template('secretary/createmeeting.html', account= account)
    elif session.get('secretary') is None:
        return login()
    else:
        return logout() 

@app.route('/rportal/createmeeting', methods=['GET', 'POST'] )
def createmeeting():
    if 'secretary' in session:
        msg = ''
        msg1 = ''
        msg2 = ''
        if request.method == 'POST' and 'topic' in request.form and 'start_time' in request.form and 'duration' in request.form and 'agenda' in request.form  :
            topic = request.form['topic']
            start_time = request.form['start_time']
            duration = request.form['duration']
            agenda = request.form['agenda']
            date = request.form['date']
            meetingdetails = {
                "topic":  topic,
                "type": 2,
                "start_time":  start_time,
                "duration":  duration,
                "timezone": "India/Mumbai",
                "agenda":  agenda,
               
                "recurrence": {"type": 1,
                            "repeat_interval": 1
                            },
                "settings": {"host_video": "true",
                               "participant_video": "true",
                               "join_before_host": "true",
                               "mute_upon_entry": "False",
                               "watermark": "true",
                               "audio": "voip",
                               "auto_recording": "cloud"
                            }
                }
            headers = {'authorization': 'Bearer %s' % generateToken(),
               'content-type': 'application/json'}
            r = requests.post(
            f'https://api.zoom.us/v2/users/me/meetings/', 
            headers=headers, data=json.dumps(meetingdetails))
            result = json.loads(r.text)
            link = result['join_url']
            msg = link 
            msg1 = "\n Host Key : 528614"
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute('INSERT INTO meetings values (NULL , %s,%s ,%s ,%s, %s, %s, %s,  DEFAULT)', (topic, date, start_time, duration, link, agenda, session['Scode']))
            mysql.connection.commit() 
            msg2 = 'Meeting Scheduled'
            return redirect(url_for('meeting'))
    elif session.get('secretary') is None:
        return login()
    else:
        return logout()

@app.route('/rportal/contact')
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

@app.route('/rportal/add_contact', methods=['GET', 'POST'] )
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
        
@app.route('/rportal/d_contact/<int:contact_id>' , methods=['GET', 'POST'])
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

@app.route('/rportal/add_docs', methods=['GET', 'POST'] )
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

@app.route('/rportal/docs')
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
        
@app.route('/rportal/d_docs/<int:doc_id>' , methods=['GET', 'POST'])
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

@app.route('/rportal/invite')
def invite():
    if 'secretary' in session:
        account = session['Scode']
        return render_template('secretary/invite.html', account=account)
    elif session.get('secretary') is None:
        return login()
    else:
        return logout() 

@app.route('/rportal/chats')
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

@app.route('/rportal/add_chats', methods=['GET', 'POST'] )
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

@app.route('/rportal/permissions')
def permissions():
    if 'secretary' in session:
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT *  from permission WHERE pstatus = %s AND society_code = %s', ('request',session['Scode'],) ) 
        account = cursor.fetchall() 

        cursor1 = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor1.execute('SELECT *  from permission WHERE pstatus = %s AND society_code = %s', ('granted',session['Scode'],) ) 
        account1 = cursor1.fetchall() 

        cursor2 = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor2.execute('SELECT *  from permission WHERE pstatus = %s AND society_code = %s', ('denied',session['Scode'],) ) 
        account2 = cursor2.fetchall() 

        return render_template('secretary/permissions.html', account=account, account1=account1, account2=account2)
    elif session.get('secretary') is None:
        return login()
    else:
        return logout() 

@app.route('/rportal/grantpermission',methods=['GET','POST'])
def grantpermission():
    if 'secretary' in session:
        if request.method == 'POST' and 'pid' in request.form:
            pid = request.form['pid']
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute('UPDATE permission SET pstatus = %s WHERE pid = %s', ('granted', pid,))
            mysql.connection.commit()
        return  permissions()
    elif session.get('secretary') is None:
        return login()
    else:
        return logout()  

@app.route('/rportal/denypermission',methods=['GET','POST'])
def  denypermission():
    if 'secretary' in session:
        if request.method == 'POST' and 'pid' in request.form:
            pid = request.form['pid']
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute('UPDATE permission SET pstatus = %s  WHERE  pid = %s', ('denied', pid,))
            mysql.connection.commit()
        return  permissions()
    elif session.get('secretary') is None:
        return login()
    else:
        return logout()  

@app.route('/rportal/maintenance_add',methods=['GET','POST'])
def maintenance_add():
    if 'secretary' in session:
        if request.method == 'POST' and 'balance' in request.form:
            balance = request.form['balance']
            amount = request.form['amount']

            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute('UPDATE society SET soc_bal = %s  WHERE  code = %s', (balance, session['Scode'],))
            mysql.connection.commit()
        
            cursor1 = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor1.execute('INSERT INTO maintenance (Musername, Mname, code, amount, pending_amount) SELECT username, Mname, Mcode, %s, %s FROM member WHERE Mcode = %s and member_status=%s', (amount, amount,session['Scode'],'active',))
            mysql.connection.commit()
            
        return Smaintenance()
    elif session.get('secretary') is None:
        return login()
    else:
        return logout()

@app.route('/rportal/secretary_maintenance',methods=['GET','POST'])
def Smaintenance():
    if 'secretary' in session:
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM maintenance WHERE code = %s GROUP BY due_date',(session['Scode'],))
        account = cursor.fetchall()
        cursor1 = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor1.execute('SELECT * FROM maintenance WHERE code = %s and payment_status=%s',(session['Scode'],'paid',))
        account1 = cursor1.fetchall()
        cursor2 = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor2.execute('SELECT * FROM maintenance WHERE code = %s and payment_status=%s',(session['Scode'],'unpaid',))
        account2 = cursor2.fetchall()
        cursor3 = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor3.execute('SELECT soc_bal FROM society WHERE code = %s',(session['Scode'],))
        account3 = cursor3.fetchone()

        return render_template('secretary/Smaintenance.html', account=account,account1=account1,account2=account2, account3=account3)
    elif session.get('secretary') is None:
        return login()
    else:
        return logout()  

#
#   Member Part
#
@app.route('/rportal/mhome' , methods=['GET','POST'])
def mhome():
    if 'user' in session:
        if request.method == 'POST' and 'Mname' in request.form and 'Mcode' in request.form and 'Memail'  in request.form and 'username'  in request.form and 'Mid':
            Mname= request.form['Mname']
            Mcode = request.form['Mcode']
            Memail = request.form['Memail']
            username = request.form['username']
            Mid = request.form['Mid']
            Mflatno = request.form['Mflatno']
            Mwing = request.form['Mwing']
     
            session['member'] = True
            session['Mid'] = Mid
            session['Musername'] = username
            session['Mcode'] = Mcode
            session['Memail'] = Memail
            session['Mname'] = Mname
            session['Mflatno'] = Mflatno
            session['Mwing'] = Mwing
     
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

@app.route('/rportal/mprofile')
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

@app.route('/rportal/mprofile/<string:msg>')
def mprofile1(msg):
    if 'member' in session:
        msg = msg
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT username, Memail, Mname, Mflatno, Mwing, Mmobile, code, name, city, road, area, state, pin FROM member INNER JOIN society ON member.Mcode = society.code WHERE Mid = %s;', (session['Mid'],))
        account = cursor.fetchone()
        return render_template('member/mprofile.html', msg=msg,account=account)
    elif session.get('member') is None:
        return login()
    else:
        return logout()

@app.route('/rportal/mupdate', methods=['GET', 'POST'] )
def mupdate():
    if 'member' in session:
        if request.method == 'POST' and 'email' in request.form and 'name' in request.form:
            email = request.form['email']
            Aname = request.form['name']
            # flatno = request.form['flatno']
            # wing = request.form['wing']
            mobile = request.form['mobile']
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute('SELECT username FROM member WHERE Mcode = %s AND Memail = %s AND Mmobile = %s', (session['Mcode'], email, mobile,))
            account = cursor.fetchone()
            cursor1 = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor1.execute('SELECT username FROM secretary WHERE Scode = %s AND Semail = %s AND Smobile = %s', (session['Mcode'], email, mobile,))
            account1 = cursor1.fetchone()
            if account:
                if account['username'] == session['Musername']:
                    cursor2 = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
                    cursor2.execute('UPDATE member SET Mname=%s, Memail=%s, Mmobile=%s WHERE Mid=%s', (Aname , email, mobile, session['Mid'],))
                    mysql.connection.commit()
                    msg ='Profile updated!'
                    return mprofile1(msg)
                else:
                    msg = 'Warning! User already exists on specified flat no!!'
                    return mprofile1(msg)
            elif account1:
                if account1['username'] == session['Musername']:
                    cursor2 = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
                    cursor2.execute('UPDATE member SET Mname=%s, Memail=%s, Mmobile=%s WHERE Mid=%s', (Aname , email, mobile, session['Mid'],))
                    mysql.connection.commit()
                    msg ='Profile updated!'
                    return mprofile1(msg)
                else:
                    msg = 'Warning! User already exists on specified flat no!!'
                    return mprofile1(msg)
            else:
                cursor2 = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
                cursor2.execute('UPDATE member SET Mname=%s, Memail=%s, Mmobile=%s WHERE Mid=%s', (Aname , email, mobile, session['Mid'],))
                mysql.connection.commit()
                msg ='Profile updated!'
                return mprofile1(msg)
        return mprofile()
    elif session.get('member') is None:
        return login()
    else:
        return logout()

@app.route('/rportal/viewnotice')
def mviewnotice():
    if 'member' in session:
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT *  from notice WHERE notice_code = %s', (session['Mcode'],) ) 
        account = cursor.fetchall() 
        return render_template('member/viewnotice.html', account=account)
    elif session.get('member') is None:
        return login()
    else:
        return logout()
    
@app.route('/rportal/docsm')
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

@app.route('/rportal/meetings')
def meetings():
    if 'member' in session:
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT *  from meetings WHERE society_code = %s  ', (session['Mcode'],) ) 
        account = cursor.fetchall() 
        return render_template('member/meetings.html', account=account)
    elif session.get('member') is None:
        return login()
    else:
        return logout()

@app.route('/rportal/complaint', methods=['GET','POST'])
def member_complaint():
    if 'member' in session:
        msg = ''
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT post from staff WHERE staff_code= %s AND staff_status=%s', (session['Mcode'],'active',))
        account = cursor.fetchall() 
        cursor1 = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor1.execute('SELECT * from complaint WHERE complaint_username= %s AND complaint_status = %s', (session['Musername'], 'active'))
        account1 = cursor1.fetchall()
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
            cursor4 = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor4.execute('INSERT INTO complaint VALUES (NULL, %s, %s, %s, %s, %s, %s, DEFAULT, NULL, NULL, DEFAULT)', (session['Musername'] , session['Mname'] , compaint_subject, complaint_message, session['Mcode'], complaint_against,))
            mysql.connection.commit()
            msg = 'Complaint Added Succsesfully!'
        elif request.method == 'POST':
            msg = 'Please fill out the form!'
        return render_template('member/member_complaint.html', msg=msg , account=account,account2= account2, account3=account3, account1=account1)
    elif session.get('member') is None:
        return login()
    else:
        return logout()

@app.route('/rportal/view_contact')
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

@app.route('/rportal/chat')
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

@app.route('/rportal/add_chat', methods=['GET', 'POST'] )
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

#guest added
@app.route('/rportal/guest')
def guest():
    if 'member' in session:
        cursor1 = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor1.execute('SELECT *  from visitor WHERE  society_code = %s AND vstatus = %s AND Mflatno = %s AND Mwing = %s', (session['Mcode'],'upcoming', session['Mflatno'], session['Mwing'],) ) 
        account = cursor1.fetchall()
        return render_template('member/addguest.html', account=account)
    elif session.get('member') is None:
        return login()
    else:
        return logout() 

@app.route('/rportal/addguest', methods=['GET', 'POST'] )
def addguest():
    if 'member' in session:
        msg = ''
        target2 = os.path.join('/Rportal/static/upload/vpic/')
        if not os.path.isdir(target2):
            os.makedirs(target2)
        if request.method == 'POST' and 'vname' in request.form  and 'vmobile' in request.form:
            vname = request.form['vname']
            vmobile = request.form['vmobile'] 
            vehical_no = request.form['vehical_no'] 
            in_time = request.form['in_time']
            in_date = request.form['in_date']
                        
            ...
            file = request.files['vpic']
            file_name = file.filename or ''
            destination = ''.join([target2, file_name])
            file.save(destination)
            vpic  = file_name
            ...
            
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute('INSERT INTO visitor VALUES (NULL, %s, %s, %s, %s, %s, NULL, NULL, %s, %s, %s, %s, %s, %s, %s, DEFAULT )',(vname, vmobile, vehical_no, in_time, in_date, vpic, session['Mname'], session['Mflatno'], session['Mwing'], 'upcoming', session['Mcode'], session['Musername']))
            mysql.connection.commit() 
            msg = "Guest Add successfully!"
            #calling geust function
        return redirect(url_for('guest'))
    elif session.get('member') is None:
        return login()
    else:
        return logout()

@app.route('/rportal/alvisitor',methods=['GET','POST'])
def alvisitor():
    if 'member' in session:
        if request.method == 'POST' and 'vid' in request.form:
            vid = request.form['vid']
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute('UPDATE visitor SET out_time = DEFAULT, out_date = DEFAULT, vstatus = %s  WHERE  vid = %s', ('allowed', vid,))
            mysql.connection.commit()
        return manage_visitor() 
    elif session.get('member') is None:
        return login()
    else:
        return logout()
              
@app.route('/rportal/decvisitor',methods=['GET','POST'])
def decvisitor():
    if 'member' in session:
        if request.method == 'POST' and 'vid' in request.form:
            vid = request.form['vid']
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute('UPDATE visitor SET out_time = DEFAULT, out_date = DEFAULT, vstatus = %s  WHERE  vid = %s', ('declined', vid,))
            mysql.connection.commit()
        return manage_visitor() 
    elif session.get('member') is None:
        return login()
    else:
        return logout()
        
@app.route('/rportal/manage_visitor')
def manage_visitor():
    if 'member' in session:
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT *  from visitor WHERE  society_code = %s AND vstatus = %s AND Mflatno = %s AND Mwing = %s', (session['Mcode'],'request', session['Mflatno'], session['Mwing'],) ) 
        account = cursor.fetchall() 
        cursor1 = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor1.execute('SELECT *  from visitor WHERE  society_code = %s AND vstatus = %s AND Mflatno = %s AND Mwing = %s', (session['Mcode'],'allowed', session['Mflatno'], session['Mwing'],) ) 
        account1 = cursor1.fetchall() 
        cursor2 = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor2.execute('SELECT *  from visitor WHERE  society_code = %s AND vstatus = %s AND Mflatno = %s AND Mwing = %s', (session['Mcode'],'declined', session['Mflatno'], session['Mwing'],) ) 
        account2 = cursor2.fetchall() 
        return render_template('member/manage_visitor.html', account=account, account1=account1, account2=account2)
    elif session.get('member') is None:
        return login()
    else:
        return logout()
# added new permission route
@app.route('/rportal/mpermission')
def mpermission():
    if 'member' in session:
        msg = ''
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT *  from permission WHERE pstatus = %s AND society_code = %s', ('request',session['Mcode'],) ) 
        account = cursor.fetchall() 

        cursor1 = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor1.execute('SELECT *  from permission WHERE pstatus = %s AND society_code = %s', ('granted',session['Mcode'],) ) 
        account1 = cursor1.fetchall() 

        cursor2 = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor2.execute('SELECT *  from permission WHERE pstatus = %s AND society_code = %s', ('denied',session['Mcode'],) ) 
        account2 = cursor2.fetchall() 

        return render_template('member/askpermission.html',account=account, account1=account1,account2=account2)
    elif session.get('member') is None:
        return login()
    else:
        return logout()

@app.route('/rportal/askpermission', methods=['GET', 'POST'] )
def askpermission():
    if 'member' in session:
        msg = ''
        if request.method == 'POST'and 'subject' in request.form :
            subject = request.form['subject']
            text = request.form['text']
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute('INSERT INTO permission values (NULL , %s, %s,%s, %s, %s, DEFAULT )', (session['Mname'],subject, text ,'request', session['Mcode']))
            mysql.connection.commit() 
            msg="successfully request submit"
        return redirect(url_for('mpermission'))
    elif session.get('member') is None:
        return login()
    else:
        return logout()

@app.route('/rportal/maintenance_pay',methods=['GET','POST'])
def maintenance_pay():
    if 'member' in session:
        msg = ''
        new_bal = ''
        paid_date =''
        if request.method == 'POST' and 'id' in request.form:
            main_id = request.form['id']
            soc_bal = request.form['soc_bal']
            amount = request.form['amount']
            print( soc_bal ,amount)
            new_bal = float(soc_bal) + float(amount)
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute('UPDATE society SET soc_bal = %s  WHERE  code = %s', (new_bal, session['Mcode'],))
            mysql.connection.commit()

            cursor1 = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor1.execute('select CURRENT_TIMESTAMP as time')
            account1 = cursor1.fetchone()
            paid_date = account1['time']
            cursor2 = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor2.execute('update maintenance set pending_amount=%s, paid_date=%s, payment_status=%s where main_id = %s', ('0', paid_date, 'paid',main_id,))
            mysql.connection.commit()

            msg = 'Payment Sucsessful!'
        return Mmaintenance1(msg)
    elif session.get('member') is None:
        return login()
    else:
        return logout()

@app.route('/rportal/member_maintenance')
def Mmaintenance():
    if 'member' in session:
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM maintenance WHERE code = %s and Musername=%s GROUP BY due_date',(session['Mcode'],session['Musername'],))
        account = cursor.fetchall()
        cursor1 = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor1.execute('SELECT * FROM maintenance WHERE code = %s and payment_status=%s and Musername=%s',(session['Mcode'],'paid',session['Musername'],))
        account1 = cursor1.fetchall()
        cursor2 = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor2.execute('SELECT * FROM maintenance WHERE code = %s and payment_status=%s and Musername=%s',(session['Mcode'],'unpaid',session['Musername'],))
        account2 = cursor2.fetchall()
        cursor3 = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor3.execute('SELECT soc_bal FROM society WHERE code = %s',(session['Mcode'],))
        account3 = cursor3.fetchone()
        print(account3)
        return render_template('member/Mmaintenance.html', account=account,account1=account1,account2=account2, account3 =account3)
    elif session.get('member') is None:
        return login()
    else:
        return logout() 

@app.route('/rportal/member_maintenance/<string:msg>')
def Mmaintenance1(msg):
    if 'member' in session:
        msg=msg
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM maintenance WHERE code = %s and Musername=%s GROUP BY due_date',(session['Mcode'],session['Musername'],))
        account = cursor.fetchall()
        cursor1 = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor1.execute('SELECT * FROM maintenance WHERE code = %s and payment_status=%s and Musername=%s',(session['Mcode'],'paid',session['Musername'],))
        account1 = cursor1.fetchall()
        cursor2 = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor2.execute('SELECT * FROM maintenance WHERE code = %s and payment_status=%s and Musername=%s',(session['Mcode'],'unpaid',session['Musername'],))
        account2 = cursor2.fetchall()
        cursor3 = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor3.execute('SELECT soc_bal FROM society WHERE code = %s',(session['Mcode'],))
        account3 = cursor3.fetchall()

        return render_template('member/Mmaintenance.html', msg=msg, account=account,account1=account1,account2=account2, account3 =account3)
    elif session.get('member') is None:
        return login()
    else:
        return logout() 

#
#   Admin Part
#
@app.route('/rportal/admin_home')
def admin_home():
    if 'admin' in session:
        c1=''
        c2=''
        c3=''
        c4=''
        c5=''
        c6=''
        c7=''
        c8=''
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('select count(uid) from userdetails')
        c1 =  [v for v in cursor.fetchone().values()][0]
    
        cursor1 = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor1.execute('select count(Sid) from secretary where secretarty_status=%s',('active',))
        c2 =  [v for v in cursor1.fetchone().values()][0]

        cursor2 = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor2.execute('select count(Mid) from member where member_status=%s',('active',))
        c3 =  [v for v in cursor2.fetchone().values()][0]

        cursor3 = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor3.execute('select count(id) from society where society_status=%s',('active',))
        c4 =  [v for v in cursor3.fetchone().values()][0]
    
        cursor4 = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor4.execute('select count(Sid) from secretary where secretarty_status=%s',('inactive',))
        c5 =  [v for v in cursor4.fetchone().values()][0]
        
        cursor5 = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor5.execute('select count(Mid) from member where member_status=%s',('inactive',))
        c6 =  [v for v in cursor5.fetchone().values()][0]

        cursor6 = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor6.execute('select count(id) from society where society_status=%s',('inactive',))
        c7 =  [v for v in cursor6.fetchone().values()][0]

        cursor7 = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor7.execute('select count(id) from society where society_status=%s',('request',))
        c8 =  [v for v in cursor7.fetchone().values()][0]

        return render_template('admin/admin_home.html', Ausername=session['Ausername'],c1=c1,c2=c2,c3=c3,c4=c4,c5=c5,c6=c6,c7=c7,c8=c8)
    elif session.get('admin') is None:
        return login(),
    else:
        return logout()

@app.route('/rportal/asoc')
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
  
@app.route('/rportal/isoc')
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
    
@app.route('/rportal/admin_req/')
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

@app.route('/rportal/a_sec/<string:Scode>')
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

@app.route('/rportal/al_sec/<string:Scode>')
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

@app.route('/rportal/c_sec/<string:Scode>')
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

@app.route('/rportal/r_sec' , methods=['GET', 'POST'])
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
            msg = Message('Society Rejected' ,sender ='Residents Portal<me@Rportal.com', recipients = [email])
            msg.body ="Hi \n"+ message
            mail.send(msg)  
            msg = 'Society Rejected/Deleted'
        return render_template('admin/admin_req.html', msg=msg)
    elif session.get('admin') is None:
        return login()
    else:
        return logout()

@app.route('/rportal/contactdata')
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
@app.route('/rportal/security_home')
def security_home():
    if 'security' in session:
        return render_template('security/security_home.html', security_username=session['security_username'])
    elif session.get('security') is None:
        return login()
    else:
        return logout()

@app.route('/rportal/security_profile')
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

@app.route('/rportal/security_update', methods=['GET', 'POST'] )
def security_update():
    if 'security' in session:
        if request.method == 'POST' and 'name' in request.form and 'mobile' in request.form:
            Aname = request.form['name']
            mobile = request.form['mobile']
            cursor1 = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor1.execute('UPDATE security SET security_name=%s, security_mobile=%s, security_status=%s WHERE security_id=%s', (Aname, mobile, 'inactive', session['security_id'],))
            mysql.connection.commit()
        return security_profile()
    elif session.get('security') is None:
        return login()
    else:
        return logout()

@app.route('/rportal/security_complaint',methods=['GET','POST'])
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

@app.route('/rportal/view_contacts')
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

@app.route('/rportal/visitorlog')
def visitorlog():
    if 'security' in session:
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT *  from visitor WHERE  society_code = %s AND vstatus = %s', (session['security_code'], 'exit',) ) 
        account = cursor.fetchall() 
        return render_template('security/visitorlog.html', account=account)
    elif session.get('security') is None:
        return login()
    else:
        return logout()

@app.route('/rportal/recentvisitor')
def recentvisitor():
    if 'security' in session:
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT *  from visitor WHERE  society_code = %s AND vstatus = %s', (session['security_code'],'request') ) 
        account = cursor.fetchall() 
        cursor1 = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor1.execute('SELECT *  from visitor WHERE  society_code = %s AND vstatus = %s', (session['security_code'],'allowed') ) 
        account1 = cursor1.fetchall() 
        cursor2 = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor2.execute('SELECT *  from visitor WHERE  society_code = %s AND vstatus = %s', (session['security_code'],'declined') ) 
        account2 = cursor2.fetchall() 
        return render_template('security/recentvisitor.html', account=account, account1=account1, account2=account2)
    elif session.get('security') is None:
        return login()
    else:
        return logout()

@app.route('/rportal/visitorexit',methods=['GET','POST'])
def visitorexit():
    if 'security' in session:
        if request.method == 'POST' and 'vid' in request.form and 'out_time' in request.form:
            vid = request.form['vid']
            out_date = request.form['out_date']
            out_time = request.form['out_time']
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute('UPDATE visitor SET out_time = %s, out_date = %s, vstatus = %s  WHERE  vid = %s', (out_time, out_date, 'exit', vid,))
            mysql.connection.commit()
        return recentvisitor() 
    elif session.get('security') is None:
        return login()
    else:
        return logout()

@app.route('/rportal/upvisitor',methods=['GET','POST'])
def upvisitor():
    if 'security' in session:
        if request.method == 'POST' and 'vid' in request.form:
            vid = request.form['vid']
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute('UPDATE visitor SET out_time = DEFAULT, out_date = DEFAULT, vstatus = %s  WHERE  vid = %s', ('allowed', vid,))
            mysql.connection.commit()
        return addvisitor() 
    elif session.get('security') is None:
        return login()
    else:
        return logout()

@app.route('/rportal/addvisitor', methods=['GET', 'POST'] )
def addvisitor():
    if 'security' in session:
        msg = ''
        target2 = os.path.join('/Rportal/static/upload/vpic/')
        cursor1 = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor1.execute('SELECT *  from visitor WHERE  society_code = %s AND vstatus = %s', (session['security_code'],'upcoming') ) 
        account1 = cursor1.fetchall() 
        if not os.path.isdir(target2):
            os.makedirs(target2)
        if request.method == 'POST' and 'vname' in request.form  and 'vmobile' in request.form:
            vname = request.form['vname']
            vmobile = request.form['vmobile'] 
            vehical_no = request.form['vehical_no'] 
            username = request.form['username']   
            Mflatno = request.form['Mflatno']   
            Mwing = request.form['Mwing']  
            vpicText=request.form['vpicText']
            if  len(vpicText) != 0:
                data=vpicText.replace("data:image/png;base64,","")
                im = Image.open(BytesIO(base64.b64decode(data)))
                file_name =  vname+"image.png"
                destination = ''.join([target2, file_name])
                im.save(destination)
                vpic  = file_name
            else:
                ...
                file = request.files['vpic']
                file_name = file.filename or ''
                destination = ''.join([target2, file_name])
                file.save(destination)
                vpic  = file_name
                ...

            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute('SELECT * FROM member WHERE Mflatno = %s AND Mwing = %s AND Mcode=%s', (Mflatno, Mwing,session['security_code'],))
            account = cursor.fetchone()
            if account:
                cursor1 = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
                cursor1.execute('INSERT INTO visitor VALUES (NULL, %s, %s, %s, DEFAULT, DEFAULT, NULL, NULL, %s, %s, %s, %s, %s, %s, %s, DEFAULT )',(vname, vmobile, vehical_no, vpic, username, Mflatno, Mwing, 'request', session['security_code'], session['security_username'],))
                mysql.connection.commit() 
                msg = "visitor Add successfully!"
            else:
                msg = "Member not found! Please check detils and try again."
        return render_template('security/addvisitor.html',msg=msg, account=account1)
    elif session.get('security') is None:
        return login()
    else:
        return logout()
              
    
#
#   Staff Part

@app.route('/rportal/staff_home')
def staff_home():
    if 'staff' in session:
        return render_template('staff/staff_home.html', staff_username=session['staff_username'])
    elif session.get('staff') is None:
        return login()
    else:
        return logout()

@app.route('/rportal/staff_profile')
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

@app.route('/rportal/staff_update', methods=['GET', 'POST'] )
def staff_update():
    if 'staff' in session:
        if request.method == 'POST' and 'name' in request.form and 'mobile' in request.form:
            Aname = request.form['name']
            mobile = request.form['mobile']
            cursor1 = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor1.execute('UPDATE staff SET staff_name=%s, staff_mobile=%s, staff_status=%s WHERE staff_id=%s', (Aname, mobile, 'inactive', session['staff_id'],))
            mysql.connection.commit()
        return staff_profile()
    elif session.get('staff') is None:
        return login()
    else:
        return logout()

@app.route('/rportal/staff_complaint',methods=['GET','POST'])
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
        return render_template('staff/staff_complaint.html', account=account, account1=account1, account2=account2)
    elif session.get('staff') is None:
        return login()
    else:
        return logout()

@app.route('/rportal/view_contactst')
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
@app.route('/rportal/contactus', methods=['GET', 'POST'] )
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