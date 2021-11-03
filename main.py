from flask import Flask, render_template, request, redirect, url_for, session
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
import sys
sys.path.insert(0, 'Rportal/config')
#from config import credentials as cred


UPLOAD_FOLDER = '/path/to/the/uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.secret_key = '65142'
app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '1234'
app.config['MYSQL_DB'] = 'rportal'
app.config['charset'] ='utf8'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
mysql = MySQL(app)
 
mail = Mail(app)
app.config["MAIL_SERVER"]='smtp.gmail.com'  
app.config["MAIL_PORT"] =465 #465 or 587 
app.config["MAIL_USERNAME"] = 'ajinfotics@gmail.com'  
app.config['MAIL_PASSWORD'] = 'JAIS@65142'  
#app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
part2 ="Your One Time Password for logging into R-Portal is\n\n" 
part3="""\n\nIf you did not Initiated this request,please ignore this mail.

If you have more queries, feel free to contact us at ajinfotics@gmail.com. 

We will love to help and assist you at any movement.

Automated mail sent by R-Portal. Please do not reply.
Regards! """
mail = Mail(app)
otp = random.randint(000000,999999)  

@app.route('/')
def index():
    return rportal()

@app.route('/R-Portal/')
def rportal():
    return render_template('rportal.html')

@app.route('/R-Portal/login', methods=['GET', 'POST'])
def login():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM secretary WHERE Susername = %s AND Spassword = %s AND secretarty_status=%s', (username, password,'active'))
        account = cursor.fetchone()
        if account:
            session['loggedin'] = True
            session['id'] = account['Sid']
            session['username'] = account['Susername']
            return sotp() 
        elif request.method == 'POST' and 'username' in request.form and 'password' in request.form:
            username = request.form['username']
            password = request.form['password']
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute('SELECT * FROM member WHERE Musername = %s AND Mpassword = %s AND member_status=%s', (username, password,'active'))
            account = cursor.fetchone()
            if account:
                session['loggedin'] = True
                session['id'] = account['Mid']
                session['username'] = account['Musername']
                return motp()       
            elif request.method == 'POST' and 'username' in request.form and 'password' in request.form:
                username = request.form['username']
                password = request.form['password']
                cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
                cursor.execute('SELECT * FROM admin WHERE Ausername = %s AND Apassword = %s', (username, password,))
                account = cursor.fetchone()
                if account:
                    session['loggedin'] = True
                    session['id'] = account['Aid']
                    session['username'] = account['Ausername']
                    return render_template("admin/admin.html")       
                elif request.method == 'POST' and 'username' in request.form and 'password' in request.form:
                    username = request.form['username']
                    password = request.form['password']
                    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
                    cursor.execute('SELECT * FROM security WHERE security_username = %s AND security_password = %s AND security_status=%s', (username, password,'active'))
                    account = cursor.fetchone()
                    if account:
                        session['loggedin'] = True
                        session['id'] = account['security_id']
                        session['username'] = account['security_username']
                        return render_template("security/security_home.html")       
                    elif request.method == 'POST' and 'username' in request.form and 'password' in request.form:
                        username = request.form['username']
                        password = request.form['password']
                        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
                        cursor.execute('SELECT * FROM staff WHERE staff_username = %s AND staff_password = %s AND staff_status=%s', (username, password,'active'))
                        account = cursor.fetchone()
                        if account:
                            session['loggedin'] = True
                            session['id'] = account['staff_id']
                            session['username'] = account['staff_username']
                            return render_template("staff/staff_home.html") 
                        elif request.method == 'POST' and 'username' in request.form and 'password' in request.form:
                            username = request.form['username']
                            password = request.form['password']
                            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
                            cursor.execute('SELECT * FROM secretary WHERE Susername = %s AND Spassword = %s AND secretarty_status=%s', (username, password,'request'))
                            account = cursor.fetchone()
                            if account:
                                msg = 'Your account is not activated yet or under verification process! Please come back once your account get verified!!'
                            elif request.method == 'POST' and 'username' in request.form and 'password' in request.form:
                                username = request.form['username']
                                password = request.form['password']
                                cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
                                cursor.execute('SELECT * FROM member WHERE Musername = %s AND Mpassword = %s AND member_status=%s', (username, password,'request'))
                                account = cursor.fetchone()
                                if account:
                                    msg = 'Your account is not activated yet or under verification process! Please come back once your account get verified!!'
                                elif request.method == 'POST' and 'username' in request.form and 'password' in request.form:
                                    username = request.form['username']
                                    password = request.form['password']
                                    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
                                    cursor.execute('SELECT * FROM security WHERE security_username = %s AND security_password = %s AND security_status=%s', (username, password,'request'))
                                    account = cursor.fetchone()
                                    if account:
                                        msg = 'Your account is not activated yet or under verification process! Please come back once your account get verified!!'
                                    elif request.method == 'POST' and 'username' in request.form and 'password' in request.form:
                                        username = request.form['username']
                                        password = request.form['password']
                                        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
                                        cursor.execute('SELECT * FROM staff WHERE staff_username = %s AND staff_password = %s AND staff_status=%s', (username, password,'request'))
                                        account = cursor.fetchone()
                                        if account:
                                            msg = 'Your account is not activated yet or under verification process! Please come back once your account get verified!!'
                                        elif request.method == 'POST' and 'username' in request.form and 'password' in request.form:
                                            username = request.form['username']
                                            password = request.form['password']
                                            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
                                            cursor.execute('SELECT * FROM secretary WHERE Susername = %s AND Spassword = %s AND secretarty_status=%s', (username, password,'inactive'))
                                            account = cursor.fetchone()
                                            if account:
                                                msg = 'Your account is temparorily disbanded! Contact Secretary of your society to learn more.'
                                            elif request.method == 'POST' and 'username' in request.form and 'password' in request.form:
                                                username = request.form['username']
                                                password = request.form['password']
                                                cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
                                                cursor.execute('SELECT * FROM member WHERE Musername = %s AND Mpassword = %s AND member_status=%s', (username, password,'inactive'))
                                                account = cursor.fetchone()
                                                if account:
                                                    msg = 'Your account is temparorily disbanded! Contact Secretary of your society to learn more.'
                                                elif request.method == 'POST' and 'username' in request.form and 'password' in request.form:
                                                    username = request.form['username']
                                                    password = request.form['password']
                                                    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
                                                    cursor.execute('SELECT * FROM security WHERE security_username = %s AND security_password = %s AND security_status=%s', (username, password,'inactive'))
                                                    account = cursor.fetchone()
                                                    if account:
                                                        msg = 'Your account is temparorily disbanded! Contact Secretary of your society to learn more.'
                                                    elif request.method == 'POST' and 'username' in request.form and 'password' in request.form:
                                                        username = request.form['username']
                                                        password = request.form['password']
                                                        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
                                                        cursor.execute('SELECT * FROM staff WHERE staff_username = %s AND staff_password = %s AND staff_status=%s', (username, password,'inactive'))
                                                        account = cursor.fetchone()
                                                        if account:
                                                            msg = 'Your account is temparorily disbanded! Contact Secretary of your society to learn more.'
                                                        else:
                                                            msg = 'Incorrect username/password! Please check Username/Password and try again!'
    return render_template('login.html', msg=msg)

def sotp(): 
    if 'loggedin' in session:
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM secretary WHERE Sid = %s', (session['id'],))
        account = cursor.fetchone()
        if account:
            email = account['Semail']
            msg = Message('OTP confirmation for RPortal' ,sender ='Rportal<me@Rportal.com', recipients = [email])
            msg.body = part2 + str(otp)+ part3 
            mail.send(msg) 
            msg1 = 'OTP: ',otp
            return render_template('secretary/sotp.html', msg1=msg1)
        else:
            msg = 'Something went wrong:( Please try again!'
    else:
        return render_template("rportal.html")
    
def motp():
    if 'loggedin' in session:
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM member WHERE Mid = %s ', (session['id'],))
        account = cursor.fetchone()
        if account:
            email = account['Memail']
            msg = Message('OTP confirmation for RPortal' ,sender ='Rportal<me@Rportal.com', recipients = [email]) 
            msg.body = part2 + str(otp) + part3 
            mail.send(msg)  
            msg1 = 'OTP: ',otp
            return render_template('member/Motp.html', msg1=msg1)
        else:
            msg = 'Something went wrong:( Please try again!'
    else:
        return render_template("rportal.html")

@app.route('/svalidate',methods=["POST"])
def svalidate():  
    user_otp = request.form['otp']  
    if otp == int(user_otp):  
        return redirect(url_for('shome')) 
    else: 
        return render_template("rportal.html")

@app.route('/mvalidate',methods=["POST"])
def mvalidate():  
    user_otp = request.form['otp']  
    if otp == int(user_otp):  
        return redirect(url_for('mhome')) 
    else: 
        return render_template("rportal.html")  

@app.route('/R-Portal/logout')
def logout():
   session.pop('loggedin', None)
   session.pop('id', None)
   session.pop('username', None)
   return redirect(url_for('rportal'))

@app.route('/R-Portal/add_security', methods=['GET','POST'])
def security():
    msg = ''
    if request.method == 'POST' and 'security_name' in request.form and 'security_username' in request.form and 'security_password' in request.form:
        
        security_username = request.form['security_username']
        security_mobile = request.form['security_mobile']
        security_password = request.form['security_password']
        security_name = request.form['security_name']
        security_code = request.form['security_code']
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
            cursor.execute('INSERT INTO security VALUES (NULL, %s, %s, %s, %s, %s, DEFAULT)', (security_username , security_password , security_name , security_mobile, security_code))
            mysql.connection.commit()
            msg = 'You have successfully registered!'
    elif request.method == 'POST':
        msg = 'elif code!' 
    return render_template('secretary/add_security.html', msg=msg)

@app.route('/R-Portal/security_home')
def security_home():
    if 'loggedin' in session:
        return render_template('security/security_home.html', security_username=session['username'])
    return redirect(url_for('login'))

@app.route('/R-Portal/security_profile')
def security_profile():
    if 'loggedin' in session:
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT security_username, security_password, security_name, security_mobile, security_code FROM security WHERE security_id = %s;', (session['id'],))
        account = cursor.fetchone()
        return render_template('security/security_profile.html', account=account)
    return redirect(url_for('login'))

@app.route('/R-Portal/add_staff', methods=['GET','POST'])
def staff():
    msg = ''
    if request.method == 'POST' and 'staff_name' in request.form and 'staff_username' in request.form and 'staff_password' in request.form:
        
        staff_username = request.form['staff_username']
        staff_mobile = request.form['staff_mobile']
        staff_password = request.form['staff_password']
        staff_name = request.form['staff_name']
        staff_code = request.form['staff_code']
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
            cursor.execute('INSERT INTO staff VALUES (NULL, %s, %s, %s, %s, %s, NULL)', (staff_username , staff_password , staff_name , staff_mobile, staff_code))
            mysql.connection.commit()
            msg = 'You have successfully registered!'
    elif request.method == 'POST':
        msg = 'elif code!' 
    return render_template('secretary/add_staff.html', msg=msg)

@app.route('/R-Portal/staff_home')
def staff_home():
    if 'loggedin' in session:
        return render_template('staff/staff_home.html', staff_username=session['username'])
    return redirect(url_for('login'))

@app.route('/R-Portal/staff_profile')
def staff_profile():
    if 'loggedin' in session:
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT staff_username, staff_password, staff_name, staff_mobile, staff_code FROM staff WHERE staff_id = %s;', (session['id'],))
        account = cursor.fetchone()
        return render_template('staff/staff_profile.html', account=account)
    return redirect(url_for('login'))

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
    msg = ''
    target = os.path.join( '/Rportal/static/upload/')
    if not os.path.isdir(target):
        os.makedirs(target)
    if request.method == 'POST' and 'Sname' in request.form and 'Susername' in request.form and 'Semail' in request.form:
        
        username = request.form['Susername']
        email = request.form['Semail']
        password = request.form['Spassword']
        Aname = request.form['Sname']
        flatno = request.form['Sflatno']
        wing = request.form['Swing']
        mobile = request.form['Smobile'] 
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
        kyc_file  = file_name;
        ...
        
        code = ""
        code =invitation()
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM member WHERE Musername = %s AND Memail = %s', (username, email))
        account = cursor.fetchone()
        cursor1 = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor1.execute('SELECT * FROM secretary WHERE Susername = %s AND Semail = %s', (username, email))
        account1 = cursor1.fetchone()
        cursor2 = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor2.execute('SELECT * FROM society WHERE code = %s', (code,))
        account2 = cursor2.fetchone()
        if account:
            msg = 'Warning! Account already exists!!'
        elif account1:
            msg = 'Warning! Account already exists!!'
        elif account2:
            msg = 'Something went wrong:( Please try again!'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Invalid email address!'
        elif not re.match(r'[A-Za-z0-9]+', username):
            msg = 'Username must contain only characters and numbers!'
        elif not username or not password or not email:
            msg = 'Please fill out the form!'
        else:
            cursor1.execute('INSERT INTO secretary VALUES (NULL, %s, %s, %s, %s, %s, %s, %s,%s)', (username , password , code ,  email , Aname , flatno , wing , mobile))
            cursor2.execute('INSERT INTO society VALUES (NULL, %s, %s, %s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, NULL, NULL,%s)', (code , name , city , road , area , state , pin , acname, acno, mmid, bankname, branch, ifsc, kyc_file))
            mysql.connection.commit()
            msg = 'You have successfully registered!'
    elif request.method == 'POST':
        msg = 'elif code!' 
    return render_template('secretary/sregister.html', msg=msg)

@app.route('/R-Portal/society_details')
def people():
    if 'loggedin' in session:
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT Mname, member_status, Mmobile from secretary inner join member on secretary.Scode = member.Mcode WHERE Sid = %s AND member_status=%s', (session['id'],'active'))
        account = cursor.fetchall()     
        cursor1 = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor1.execute('SELECT Sname,secretarty_status, Smobile from secretary WHERE Sid = %s AND secretarty_status=%s', (session['id'],'active'))
        account1 = cursor1.fetchone()  
        cursor2 = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor2.execute('SELECT security_name, security_status, security_mobile from secretary inner join security on secretary.Scode = security.security_code WHERE Sid = %s AND security_status=%s', (session['id'],'active'))
        account2 = cursor2.fetchall()     
        cursor3 = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor3.execute('SELECT staff_name, staff_status, staff_mobile from secretary inner join staff on secretary.Scode = staff.staff_code WHERE Sid = %s AND staff_status=%s', (session['id'],'active'))
        account3 = cursor3.fetchall()        
        return render_template('secretary/people.html', account=account, account1=account1, account2=account2, account3=account3)
    return redirect(url_for('login'))

@app.route('/R-Portal/allow_members/')
def allow_members():
    if 'loggedin' in session:
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT Mid, Mname, member_status, Mmobile, Mwing, Mflatno from secretary inner join member on secretary.Scode = member.Mcode WHERE Sid = %s AND member_status=%s', (session['id'],'inactive'))
        account = cursor.fetchall()           
        return render_template('secretary/allow_members.html', account=account)
    return redirect(url_for('login'))

@app.route('/R-Portal/a_members/<int:Mid>')
def a_members(Mid):

    if 'loggedin' in session: 

        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute("UPDATE member SET member_status = %s WHERE Mid = %s" ,('active',Mid,)) 
        mysql.connection.commit()
        msg = 'Member Allowed'
        return render_template('secretary/allow_members.html', msg=msg)
    return redirect(url_for('login'))

@app.route('/R-Portal/r_members/<int:Mid>')
def r_members(Mid):
    if 'loggedin' in session: 
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('DELETE FROM member WHERE Mid = %s',[Mid]) 
        mysql.connection.commit()
        msg = 'Member Delete'
        return render_template('secretary/allow_members.html', msg=msg)
    return redirect(url_for('login'))

@app.route('/R-Portal/shome')
def shome():
    if 'loggedin' in session:
        return render_template('secretary/shome.html')
    return redirect(url_for('login'))

@app.route('/R-Portal/sprofile')
def sprofile():
    if 'loggedin' in session:
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM secretary INNER JOIN society ON secretary.Scode = society.code WHERE Sid = %s', (session['id'],))
        account = cursor.fetchone()
        return render_template('secretary/sprofile.html', account=account)
    return redirect(url_for('login'))

@app.route('/R-Portal/mcode', methods=['GET', 'POST'])
def mcode():
    msg = ''
    if request.method == 'POST' and 'code' in request.form:
        code = request.form['code']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM society WHERE code = %s', (code,))
        account = cursor.fetchone()
        if account:
            cursor.execute('select name, city, road, area, state, pin from society WHERE code = %s', (code ,))
            account = cursor.fetchone()
            return render_template('member/mverify.html', account=account)
        else:
            mysql.connection.commit()
            msg='Invalid Society Code!'
    return render_template('member/mcode.html', msg=msg)

@app.route('/R-Portal/mregister', methods=['GET', 'POST'])
def mregister():
    msg = ''
    if request.method == 'POST' and 'Musername' in request.form and 'Mpassword' in request.form and 'Memail' in request.form and 'Mcode' in request.form and 'Mname' in request.form and 'Mflatno' in request.form and 'Mwing' in request.form and 'Mmobile' in request.form:
        username = request.form['Musername']
        password = request.form['Mpassword']
        code = request.form['Mcode']
        email = request.form['Memail']
        name = request.form['Mname']
        flatno = request.form['Mflatno']
        wing = request.form['Mwing']
        mobile = request.form['Mmobile']   
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM member WHERE Musername = %s AND Memail = %s', (username, email))
        account = cursor.fetchone()
        cursor1 = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor1.execute('SELECT * FROM secretary WHERE Susername = %s AND Semail = %s', (username, email))
        account1 = cursor1.fetchone()
        if account:
            msg = 'Warning! Account already exists!!'
        elif account1:
            msg = 'Warning! Account already exists!!'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Invalid email address!'
        elif not re.match(r'[A-Za-z0-9]+', username):
            msg = 'Username must contain only characters and numbers!'
        elif not username or not password or not email:
            msg = 'Please fill out the form!'
        else:
            cursor.execute('INSERT INTO member VALUES (NULL, %s, %s, %s, %s, %s, %s, %s,%s)', (username , password , code ,  email , name , flatno , wing , mobile))
            mysql.connection.commit()
            msg = 'You have successfully registered!'
    elif request.method == 'POST':
        msg = 'Please fill out the form!'
    return render_template('member/mregister.html', msg=msg)

@app.route('/R-Portal/mhome')
def mhome():
    if 'loggedin' in session:
        return render_template('member/mhome.html', Musername=session['username'])
    return redirect(url_for('login'))

@app.route('/R-Portal/mprofile')
def mprofile():
    if 'loggedin' in session:
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT Musername, Mpassword, Memail, Mname, Mflatno, Mwing, Mmobile, code, name, city, road, area, state, pin FROM member INNER JOIN society ON member.Mcode = society.code WHERE Mid = %s;', (session['id'],))
        account = cursor.fetchone()
        return render_template('member/mprofile.html', account=account)
    return redirect(url_for('login'))

@app.route('/R-Portal/asoc')
def asoc():
    if 'loggedin' in session:
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT  name, road, area, city, state, pin, Sname, Sflatno, Swing, Smobile, Semail, code, acname, acno, mmid, bankname, branch, ifsc, secretarty_status FROM secretary INNER JOIN society on secretary.Scode=society.code;')
        account = cursor.fetchall() 
        return render_template('admin/asoc.html', account=account)
    else:
        return redirect(url_for('login'))

    

if __name__ == '__main__':
   app.run(debug=True)