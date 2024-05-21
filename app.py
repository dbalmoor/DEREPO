from flask import Flask, request, render_template,session,flash,redirect,url_for
import pandas as pd
from werkzeug.utils import secure_filename
import mysql.connector
from datetime import datetime
import os
import random
from datetime import datetime

from flask_mail import *
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import secrets

UPLOAD_FOLDER = '/path/to/the/uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.secret_key='Lakshmi'
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="derepo",
    charset='utf8'
)
mycursor = mydb.cursor()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/csp')
def csp():
    return render_template('csp.html')

@app.route('/cspback',methods=['POST', 'GET'])
def cspback():
    if request.method=="POST":
        username = request.form['email']
        password1 = request.form['pwd']
        if username == 'csp@gmail.com' and password1 == 'csp' :
            flash("Welcome Server", "primary")
            return render_template('csphome.html')
        elif username== 'attacker@gmail.com' and password1== 'attacker':
            return render_template('attack.html')
        else:
            flash("Invalid credentials", "warning")
            return render_template('csp.html')
        return render_template('csp.html')
    
@app.route('/csphome')
def csphome():
    return render_template('csphome.html')

@app.route("/vusers")
def vusers():
    print("Reading BLOB data from python_employee table")
    sql = "select * from user "
    '''mycursor.execute(sql)
    x=mycursor.fetchall()'''
    x = pd.read_sql_query(sql, mydb)
    print(type(x))
    print(x)
    x = x.drop(['pwd'], axis=1)
    return render_template("vusers.html", col_name=x.columns.values, row_val=x.values.tolist())

@app.route('/user')
def user():
    return render_template('user.html')

@app.route('/ureg')
def ureg():
    return render_template('ureg.html')

@app.route('/uregback',methods=['POST','GET'])
def uregback():
    if request.method=='POST':
        print("gekjhiuth")
        name=request.form['name']
        email=request.form['email']
        pwd=request.form['pwd']
        addr=request.form['addr']
        cpwd=request.form['cpwd']
        sql="select * from user"
        result=pd.read_sql_query(sql,mydb)
        email1=result['email'].values
        print(email1)
        if email in email1:
            flash("email already existed","success")
            return render_template('ureg.html')
        if(pwd==cpwd):
            sql = "INSERT INTO user (name,email,pwd,addr) VALUES (%s,%s,%s,%s)"
            val = (name,email,pwd,addr)
            mycursor.execute(sql, val)
            mydb.commit()
            flash("Successfully Registered","warning")
            return render_template('user.html')
        else:
            flash("Password and Confirm Password not same")
    return render_template('ureg.html')

@app.route('/userback',methods=['POST', 'GET'])
def userback():
    if request.method == "POST":
        email = request.form['email']
        password1 = request.form['pwd']
        print('p')
        sql = "select * from user where email='%s' and pwd='%s' and status='Activated' " % (email, password1)
        print('q')
        x = mycursor.execute(sql)
        print(x)
        results = mycursor.fetchall()
        print(results)
        global name
        name=results[0][1]
        print('name is:', name)
        session['email'] = email
        session['name'] = name
        if len(results) > 0:
            flash("Welcome ", "primary")
            return render_template('userhome.html', msg=results[0][1])
        else:
            return render_template('user.html', msg="invalid value")
    return render_template('user.html')

@app.route('/userhome')
def userhome():
    return render_template("userhome.html")

@app.route('/upload')
def upload():
    return render_template("upload.html")

@app.route("/upback",methods=["POST","GET"])
def upback():
    if request.method=="POST":
        fname = request.form['fname']
        server = request.form['server']
        file = request.form['file']
        dd = "text_files/" + file
        f = open(dd, "r")
        data = f.read()
        otp = random.randint(000000, 999999)
        print(otp)
        skey = secrets.token_hex(4)
        print(skey)

        if server=='Amazon':
            sql = "select * from amezon where fname='%s'" % (fname)
            result = pd.read_sql_query(sql, mydb)
            fname1 = result['fname'].values
            if fname in fname1:
                flash("File with this name already exists", "danger")
                return render_template('upload.html')
            else:
                now = datetime.now()
                t = now.strftime("%H:%M:%S")
                current_date = datetime.now().date()
                print(current_date)
                print(t)
                email = session.get('email')
                name = session.get('name')
                print(name)
                sql = "INSERT INTO amezon(email,name,fname,files,time,skey) VALUES(%s,%s,%s,AES_ENCRYPT(%s,'lakshmi'),%s,%s)"
                val = (email, name, fname, data, t, skey)
                mycursor.execute(sql, val)
                mydb.commit()
            flash("file uploaded successfully", "success")
            return render_template('upload.html')
        elif server=='BigRocks':
            sql = "select * from bigrock where fname='%s'" % (fname)
            result = pd.read_sql_query(sql, mydb)
            fname1 = result['fname'].values
            if fname in fname1:
                flash("File with this name already exists", "danger")
                return render_template('upload.html')
            else:
                now = datetime.now()
                t = now.strftime("%H:%M:%S")
                current_date = datetime.now().date()
                print(current_date)
                print(t)
                email = session.get('email')
                name = session.get('name')
                sql = "INSERT INTO bigrock (email,name,fname,files,time,skey) VALUES (%s,%s,%s,AES_ENCRYPT(%s,'lakshmi'),%s,%s)"
                val = (email, name, fname, data, t, skey)
                mycursor.execute(sql, val)
                mydb.commit()
            flash("file uploaded successfully", "success")
            return render_template('upload.html')
        else:
            sql = "select * from icloud where fname='%s'" % (fname)
            result = pd.read_sql_query(sql, mydb)
            fname1 = result['fname'].values
            if fname in fname1:
                flash("File with this name already exists", "danger")
                return render_template('upload.html')
            else:
                now = datetime.now()
                t = now.strftime("%H:%M:%S")
                current_date = datetime.now().date()
                print(current_date)
                print(t)
                email = session.get('email')
                name = session.get('name')
                sql = "INSERT INTO icloud (email,name,fname,files,time,skey) VALUES (%s,%s,%s,AES_ENCRYPT(%s,'lakshmi'),%s,%s)"
                val = (email, name, fname, data, t, skey)
                mycursor.execute(sql, val)
                mydb.commit()
            flash("file uploaded successfully", "success")
            return render_template('upload.html')
    return render_template('upback.html')

@app.route('/vfiles')
def vfiles():
    return render_template("vfiles.html")

@app.route("/amazon")
def amazon():
    print("Reading BLOB data from python_employee table")
    email = session.get('email')
    sql = "select * from amezon where email='%s' " %(email)
    x = pd.read_sql_query(sql, mydb)
    print(type(x))
    print(x)
    x = x.drop(['files'], axis=1)
    x = x.drop(['email'], axis=1)
    x = x.drop(['name'], axis=1)
    x = x.drop(['status'], axis=1)
    x = x.drop(['share'], axis=1)
    x = x.drop(['request'], axis=1)
    x = x.drop(['adate'], axis=1)
    return render_template("amazon.html", col_name=x.columns.values, row_val=x.values.tolist())

@app.route("/bigrock")
def bigrock():
    print("Reading BLOB data from python_employee table")
    email = session.get('email')
    sql = "select * from bigrock where email='%s' " %(email)
    x = pd.read_sql_query(sql, mydb)
    print(type(x))
    print(x)
    x = x.drop(['files'], axis=1)
    x = x.drop(['email'], axis=1)
    x = x.drop(['name'], axis=1)
    x = x.drop(['status'], axis=1)
    x = x.drop(['share'], axis=1)
    x = x.drop(['request'], axis=1)
    x = x.drop(['adate'], axis=1)
    return render_template("bigrock.html", col_name=x.columns.values, row_val=x.values.tolist())

@app.route("/icloud")
def icloud():
    print("Reading BLOB data from python_employee table")
    email = session.get('email')
    sql = "select * from icloud where email='%s' " %(email)
    x = pd.read_sql_query(sql, mydb)
    print(type(x))
    print(x)
    x = x.drop(['files'], axis=1)
    x = x.drop(['email'], axis=1)
    x = x.drop(['name'], axis=1)
    x = x.drop(['status'], axis=1)
    x = x.drop(['share'], axis=1)
    x = x.drop(['request'], axis=1)
    x = x.drop(['adate'], axis=1)
    return render_template("icloud.html", col_name=x.columns.values, row_val=x.values.tolist())


@app.route("/vdata1/<s1>")
def vdata1(s1=0):
    print("dfhlksokhso")
    print("Reading BLOB data from python_employee table")
    sql = "select * from bigrock where id='%s' "%(s1)
    x = pd.read_sql_query(sql, mydb)
    print(type(x))
    print(x)
    x = x.drop(['fname'], axis=1)
    x = x.drop(['email'], axis=1)
    x = x.drop(['name'], axis=1)
    x = x.drop(['time'], axis=1)
    x = x.drop(['status'], axis=1)
    x = x.drop(['skey'], axis=1)
    x = x.drop(['id'], axis=1)
    x = x.drop(['request'], axis=1)
    x = x.drop(['share'], axis=1)
    return render_template("vdata1.html", col_name=x.columns.values, row_val=x.values.tolist())

@app.route("/vdata2/<s1>")
def vdata2(s1=0):
    print("dfhlksokhso")
    print("Reading BLOB data from python_employee table")
    sql = "select * from amezon where id='%s' "%(s1)
    x = pd.read_sql_query(sql, mydb)
    print(type(x))
    print(x)
    x = x.drop(['fname'], axis=1)
    x = x.drop(['email'], axis=1)
    x = x.drop(['name'], axis=1)
    x = x.drop(['time'], axis=1)
    x = x.drop(['status'], axis=1)
    x = x.drop(['skey'], axis=1)
    x = x.drop(['id'], axis=1)
    x = x.drop(['request'], axis=1)
    x = x.drop(['share'], axis=1)
    return render_template("vdata2.html", col_name=x.columns.values, row_val=x.values.tolist())

@app.route("/share/<s1>")
def share(s1=0):
    email = session.get('email')
    sql="select * from amezon where email='%s' "%(email)
    x = mycursor.execute(sql)
    print(x)
    results = mycursor.fetchall()
    print(results)
    global name
    name=results[0][2]
    print(name)
    return render_template("share.html", s1=s1,s2=name)


@app.route("/vdata/<s1>")
def vdata(s1=0):
    print("dfhlksokhso")
    print("Reading BLOB data from python_employee table")
    sql = "select * from icloud where id='%s' "%(s1)
    x = pd.read_sql_query(sql, mydb)
    print(type(x))
    print(x)
    x = x.drop(['fname'], axis=1)
    x = x.drop(['email'], axis=1)
    x = x.drop(['name'], axis=1)
    x = x.drop(['time'], axis=1)
    x = x.drop(['status'], axis=1)
    x = x.drop(['skey'], axis=1)
    x = x.drop(['id'], axis=1)
    x = x.drop(['request'], axis=1)
    x = x.drop(['share'], axis=1)
    return render_template("vdata.html", col_name=x.columns.values, row_val=x.values.tolist())

@app.route('/sback',methods=["POST","GET"])
def sback():
    if request.method == "POST":
        name = request.form['name']
        id = request.form['id']
        share = request.form['share']
        if share=='Share to all':
            sql = "update amezon set share='%s' where id='%s' "%(share,id)
            mycursor.execute(sql)
            mydb.commit()
        else:
            sql = "update amezon set share='%s' where id='%s' and name='%s' " % (share, id,name)
            mycursor.execute(sql)
            mydb.commit()
        flash("File shared successfully","primary")
        return render_template("amazon.html")

@app.route("/share1/<s1>")
def share1(s1=0):
    email = session.get('email')
    sql = "select * from amezon where email='%s' " % (email)
    x = mycursor.execute(sql)
    print(x)
    results = mycursor.fetchall()
    print(results)
    global name
    name = results[0][2]
    print(name)
    return render_template("share1.html", s1=s1,name=name)

@app.route('/sback1',methods=["POST","GET"])
def sback1():
    if request.method == "POST":
        name = request.form['name']
        id = request.form['id']
        share = request.form['share']
        if share=='Share to all':
            sql = "update bigrock set share='%s' where id='%s' and name='%s' "%(share,id,name)
            mycursor.execute(sql)
            mydb.commit()
        else:
            sql = "update bigrock set share='%s' where id='%s' " % (share, id)
            mycursor.execute(sql)
            mydb.commit()
        flash("File shared successfully", "primary")
        return render_template("bigrock.html")

@app.route("/share2/<s1>")
def share2(s1=0):
    email = session.get('email')
    sql = "select * from amezon where email='%s' " % (email)
    x = mycursor.execute(sql)
    print(x)
    results = mycursor.fetchall()
    print(results)
    global name
    name = results[0][2]
    print(name)
    return render_template("share2.html", s1=s1,name=name)

@app.route('/sback2',methods=["POST","GET"])
def sback2():
    if request.method == "POST":
        name = request.form['name']
        id = request.form['id']
        share = request.form['share']
        if share=='Share to all':
            sql = "update icloud set share='%s' where id='%s' and name='%s' "%(share,id,name)
            mycursor.execute(sql)
            mydb.commit()
        else:
            sql = "update icloud set share='%s' where id='%s' " % (share, id)
            mycursor.execute(sql)
            mydb.commit()
        flash("File shared successfully", "primary")
        return render_template("icloud.html")

@app.route('/sfiles')
def sfiles():
    return render_template("sfiles.html")

@app.route("/a1")
def a1():
    print("Reading BLOB data from python_employee table")
    email = session.get('email')
    sql = "select * from amezon where email='%s' and share='Name hide on share' or share='Share to all' " %(email)
    x = pd.read_sql_query(sql, mydb)
    print(type(x))
    print(x)
    x = x.drop(['files'], axis=1)
    x = x.drop(['email'], axis=1)
    x = x.drop(['status'], axis=1)
    x = x.drop(['share'], axis=1)
    x = x.drop(['time'], axis=1)
    x = x.drop(['skey'], axis=1)
    x = x.drop(['request'], axis=1)
    x = x.drop(['adate'], axis=1)
    return render_template("a1.html", col_name=x.columns.values, row_val=x.values.tolist())

@app.route('/cancel/<s1>')
def cancel(s1=0):
    status='Cancel'
    sql = "update amezon set share='%s' where id='%s' "%(status,s1)
    mycursor.execute(sql)
    mydb.commit()
    flash("File Cancelled","primary")
    return render_template("sfiles.html")

@app.route("/b1")
def b1():
    print("Reading BLOB data from python_employee table")
    email = session.get('email')
    sql = "select * from bigrock where email='%s' and share='Name hide on share' or share='Share to all' " %(email)
    x = pd.read_sql_query(sql, mydb)
    print(type(x))
    print(x)
    x = x.drop(['files'], axis=1)
    x = x.drop(['email'], axis=1)
    x = x.drop(['status'], axis=1)
    x = x.drop(['share'], axis=1)
    x = x.drop(['time'], axis=1)
    x = x.drop(['skey'], axis=1)
    x = x.drop(['request'], axis=1)
    x = x.drop(['adate'], axis=1)
    return render_template("b1.html", col_name=x.columns.values, row_val=x.values.tolist())

@app.route('/cancel1/<s1>')
def cancel1(s1=0):
    status='Cancel'
    sql = "update bigrock set share='%s' where id='%s' "%(status,s1)
    mycursor.execute(sql)
    mydb.commit()
    flash("File Cancelled","primary")
    return render_template("sfiles.html")

@app.route("/c1")
def c1():
    print("Reading BLOB data from python_employee table")
    email = session.get('email')
    sql = "select * from icloud where email='%s' and share='Name hide on share' or share='Share to all' " %(email)
    x = pd.read_sql_query(sql, mydb)
    print(type(x))
    print(x)
    x = x.drop(['files'], axis=1)
    x = x.drop(['email'], axis=1)
    x = x.drop(['adate'], axis=1)
    x = x.drop(['status'], axis=1)
    x = x.drop(['share'], axis=1)
    x = x.drop(['time'], axis=1)
    x = x.drop(['skey'], axis=1)
    x = x.drop(['request'], axis=1)
    return render_template("c1.html", col_name=x.columns.values, row_val=x.values.tolist())

@app.route('/cancel2/<s1>')
def cancel2(s1=0):
    status='Cancel'
    sql = "update icloud set share='%s' where id='%s' "%(status,s1)
    mycursor.execute(sql)
    mydb.commit()
    flash("File Cancelled","primary")
    return render_template("sfiles.html")

@app.route('/datafiles')
def datafiles():
    return render_template("datafiles.html")

@app.route("/d1")
def d1():
    print("Reading BLOB data from python_employee table")
    email = session.get('email')
    sql = "select * from amezon where email!='%s' and request='waiting' " %(email)
    x = pd.read_sql_query(sql, mydb)
    print(type(x))
    print(x)
    x = x.drop(['files'], axis=1)
    x = x.drop(['email'], axis=1)
    x = x.drop(['status'], axis=1)
    x = x.drop(['share'], axis=1)
    x = x.drop(['time'], axis=1)
    x = x.drop(['skey'], axis=1)
    x = x.drop(['request'], axis=1)
    x = x.drop(['adate'], axis=1)
    return render_template("d1.html", col_name=x.columns.values, row_val=x.values.tolist())

@app.route('/requestn/<s1>/<s2>/<s3>')
def requestn(s1=0,s2='',s3=''):
    email=session.get('email')
    name=session.get('name')
    sql = "insert into amazon_requests(fid,oname,uname,demail,fname) values(%s,%s,%s,%s,%s)"
    val=(s1,s2,name,email,s3)
    mycursor.execute(sql,val)
    mydb.commit()
    flash("Request Sended to Data Consumer","primary")
    return redirect(url_for('d1'))

@app.route("/d2")
def d2():
    print("Reading BLOB data from python_employee table")
    email = session.get('email')
    sql = "select * from bigrock where email!='%s' and request='waiting'" %(email)
    x = pd.read_sql_query(sql, mydb)
    print(type(x))
    print(x)
    x = x.drop(['files'], axis=1)
    x = x.drop(['email'], axis=1)
    x = x.drop(['adate'], axis=1)
    x = x.drop(['status'], axis=1)
    x = x.drop(['share'], axis=1)
    x = x.drop(['time'], axis=1)
    x = x.drop(['skey'], axis=1)
    x = x.drop(['request'], axis=1)


    return render_template("d2.html", col_name=x.columns.values, row_val=x.values.tolist())

@app.route('/request1/<s1>/<s2>/<s3>')
def request1(s1=0,s2='',s3=''):
    email = session.get('email')
    name = session.get('name')
    sql = "insert into bigrock_requests(fid,oname,uname,demail,fname) values(%s,%s,%s,%s,%s)"
    val = (s1, s2,name, email, s3)
    mycursor.execute(sql, val)
    mydb.commit()
    flash("Request Sended to Data Consumer", "primary")
    return redirect(url_for('d2'))

@app.route("/d3")
def d3():
    print("Reading BLOB data from python_employee table")
    email = session.get('email')
    sql = "select * from icloud where email!='%s' and request='waiting' " %(email)
    x = pd.read_sql_query(sql, mydb)
    print(type(x))
    print(x)
    x = x.drop(['files'], axis=1)
    x = x.drop(['email'], axis=1)
    x = x.drop(['adate'], axis=1)
    x = x.drop(['status'], axis=1)
    x = x.drop(['share'], axis=1)
    x = x.drop(['time'], axis=1)
    x = x.drop(['skey'], axis=1)
    x = x.drop(['request'], axis=1)
    return render_template("d3.html", col_name=x.columns.values, row_val=x.values.tolist())

@app.route('/request2/<s1>/<s2>/<s3>')
def request2(s1=0,s2='',s3=''):
    email = session.get('email')
    name = session.get('name')
    sql = "insert into icloud_requests(fid,oname,uname,demail,fname) values(%s,%s,%s,%s,%s)"
    val = (s1, s2,name, email, s3)
    mycursor.execute(sql, val)
    mydb.commit()
    flash("Request Sended to Data Consumer", "primary")
    return redirect(url_for('d3'))

@app.route('/active/<s1>')
def active(s1=0):
    status='Activated'
    sql = "update user set status='%s' where id='%s' "%(status,s1)
    data= mycursor.execute(sql)
    mydb.commit()
    print(data)
    flash("Registration accepted","primary")
    return render_template("active.html")


@app.route('/consumer')
def consumer():
    return render_template("consumer.html")

@app.route('/creg')
def creg():
    return render_template("creg.html")

@app.route('/cregback',methods=['POST','GET'])
def cregback():
    if request.method=='POST':
        print("gekjhiuth")
        name=request.form['name']
        email=request.form['email']
        pwd=request.form['pwd']
        addr=request.form['addr']
        cpwd=request.form['cpwd']
        sql="select * from user"
        result=pd.read_sql_query(sql,mydb)
        email1=result['email'].values
        print(email1)
        if email in email1:
            flash("email already existed","success")
            return render_template('ureg.html')
        if(pwd==cpwd):
            sql = "INSERT INTO consumer (name,email,pwd,addr) VALUES (%s,%s,%s,%s)"
            val = (name,email,pwd,addr)
            mycursor.execute(sql, val)
            mydb.commit()
            flash("Successfully Registered","warning")
            return render_template('consumer.html')
        else:
            flash("Password and Confirm Password not same")
    return render_template('creg.html')

@app.route('/cback',methods=['POST', 'GET'])
def cback():
    if request.method == "POST":
        email = request.form['email']
        password1 = request.form['pwd']
        print('p')
        if email=='consumer@gmail.com' and password1=='consumer':
            flash("Welcome to Data Consumer page", "primary")
            return render_template('chome.html')
        else:
            flash("Email or Password invalid ", "primary")
            return render_template('consumer.html')
    flash("Something wrong ", "primary")
    return render_template('consumer.html')

@app.route("/req")
def req():

    hists = ['AMAZON SERVER', 'BIGROCK SERVER', 'ICLOUD SERVER']

    return render_template('req.html', hists=hists)

@app.route("/req1")
def req1():
    print("Reading BLOB data from python_employee table")
    email = session.get('email')
    sql = "select * from amazon_requests where status='pending' "

    x = pd.read_sql_query(sql, mydb)
    print("^^^^^^^^^^^^^")
    print(type(x))
    print(x)
    x = x.drop(['status'], axis=1)
    x = x.drop(['pkey'], axis=1)
    return render_template("req1.html", col_name=x.columns.values, row_val=x.values.tolist())

@app.route('/req1back/<s1>/<s2>')
def req1back(s1=0,s2=''):
    status = 'Accepted'
    otp1 = random.randint(000000, 999999)
    # skey = secrets.token_hex(4)
    # print(skey)
    otp = "Your Master key is:"
    mail_content = otp + ' ' + str(otp1)
    sender_address = 'deepanabalmoor7@gmail.com'
    sender_pass = 'vndhkjqdtiihalpq'
    receiver_address = s2
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = 'Derepo: A Distributed Privacy-Preserving Data Repository with Decentralized Access Control for Smart Health'

    message.attach(MIMEText(mail_content, 'plain'))
    session = smtplib.SMTP('smtp.gmail.com', 587)
    session.starttls()
    session.login(sender_address, sender_pass)
    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    session.quit()
    action = "Completed"
    sql = "update amazon_requests set status='%s',pkey='%s' where id='%s' " % (status, otp1, s1)
    mycursor.execute(sql)
    mydb.commit()
    flash("Request accepted and Master Key Sended to User Mail", "primary")
    return redirect(url_for('req1'))

@app.route("/req2")
def req2():
    email = session.get('email')
    sql = "select * from bigrock_requests where status='pending' "

    x = pd.read_sql_query(sql, mydb)
    print("^^^^^^^^^^^^^")
    print(type(x))
    print(x)
    x = x.drop(['status'], axis=1)
    x = x.drop(['pkey'], axis=1)

    return render_template("req2.html", col_name=x.columns.values, row_val=x.values.tolist())

@app.route('/req2back/<s1>/<s2>')
def req2back(s1=0,s2=''):
    status = 'Accepted'
    otp1 = random.randint(000000, 999999)
    # skey = secrets.token_hex(4)
    # print(skey)
    otp = "Your Master key is:"
    mail_content = otp + ' ' + str(otp1)
    sender_address = 'deepanabalmoor7@gmail.com'
    sender_pass = 'vndhkjqdtiihalpq'
    receiver_address = s2
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = 'Derepo: A Distributed Privacy-Preserving Data Repository with Decentralized Access Control for Smart Health'

    message.attach(MIMEText(mail_content, 'plain'))
    session = smtplib.SMTP('smtp.gmail.com', 587)
    session.starttls()
    session.login(sender_address, sender_pass)
    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    session.quit()
    action = "Completed"
    sql = "update bigrock_requests set status='%s',pkey='%s' where id='%s' " % (status, otp1, s1)
    mycursor.execute(sql)
    mydb.commit()
    flash("Request accepted and Master Key Sended to User Mail", "primary")
    return redirect(url_for('req2'))

@app.route("/req3")
def req3():
    email = session.get('email')
    sql = "select * from icloud_requests where status='pending' "

    x = pd.read_sql_query(sql, mydb)
    print("^^^^^^^^^^^^^")
    print(type(x))
    print(x)
    x = x.drop(['status'], axis=1)
    x = x.drop(['pkey'], axis=1)


    return render_template("req3.html", col_name=x.columns.values, row_val=x.values.tolist())

@app.route('/req3back/<s1>/<s2>')
def req3back(s1=0,s2=''):
    status = 'Accepted'
    otp1 = random.randint(000000, 999999)
    # skey = secrets.token_hex(4)
    # print(skey)
    otp = "Your Master key is:"
    mail_content = otp + ' ' + str(otp1)
    sender_address = 'deepanabalmoor7@gmail.com'
    sender_pass = 'vndhkjqdtiihalpq'
    receiver_address = s2
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = 'Derepo: A Distributed Privacy-Preserving Data Repository with Decentralized Access Control for Smart Health'

    message.attach(MIMEText(mail_content, 'plain'))
    session = smtplib.SMTP('smtp.gmail.com', 587)
    session.starttls()
    session.login(sender_address, sender_pass)
    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    session.quit()
    action = "Completed"
    sql = "update icloud_requests set status='%s',pkey='%s' where id='%s' " % (status,otp1, s1)
    mycursor.execute(sql)
    mydb.commit()
    flash("Request accepted and Master Key Sended to User Mail", "primary")
    return redirect(url_for('req3'))

@app.route('/down')
def down():
    email=session.get('email')
    sql = "select * from amazon_requests where status ='Accepted' and demail='%s' "%(email)
    x = pd.read_sql_query(sql, mydb)
    print("^^^^^^^^^^^^^")
    print(type(x))
    print(x)
    x = x.drop(['pkey'], axis=1)
    x = x.drop(['status'], axis=1)
    x = x.drop(['uname'], axis=1)
    x = x.drop(['demail'], axis=1)
    sql1 = "select * from bigrock_requests where status ='Accepted' and demail='%s' "%(email)
    y = pd.read_sql_query(sql1, mydb)
    print("^^^^^^^^^^^^^")
    print(type(y))
    print(y)
    # x = x.drop(['pwd'], axis=1)
    y = y.drop(['status'], axis=1)
    y = y.drop(['uname'], axis=1)
    y = y.drop(['pkey'], axis=1)
    y = y.drop(['demail'], axis=1)

    sql2 = "select * from icloud_requests where status ='Accepted' and demail='%s' " % (email)
    z = pd.read_sql_query(sql2, mydb)
    print("^^^^^^^^^^^^^")
    print(type(z))
    print(z)
    # x = x.drop(['pwd'], axis=1)
    z = z.drop(['status'], axis=1)
    z = z.drop(['uname'], axis=1)
    z = z.drop(['pkey'], axis=1)
    z = z.drop(['demail'], axis=1)


    return render_template('down.html',col_name=x.columns.values, row_val=x.values.tolist(), col=y.columns.values,row_main=y.values.tolist(),cols=z.columns.values,rows=z.values.tolist())

@app.route('/down1/<s1>/<s2>/<s3>')
def down1(s1=0,s2='',s3=''):
    a = random.randrange(10000, 999999)
    return render_template('down1.html',a=a,s1=s1,s2=s2,s3=s3)

@app.route('/down1back', methods=["POST","GET"])
def down1back():
    if request.method=='POST':
        pkey=request.form['pkey']
        id = request.form['id']
        fid=request.form['fid']
        fname=request.form['fname']

        sql = "select count(*),aes_decrypt(files,'lakshmi') from amezon,amazon_requests where amezon.id='"+fid+"' and amazon_requests.fid='"+fid+"' and amazon_requests.pkey='"+pkey+"'"
        x = pd.read_sql_query(sql, mydb)
        count=x.values[0][0]
        print(count)
        asss=x.values[0][1]
        asss=asss.decode('utf-8')
        #as=asss.decode('base64','strict')
        print(asss)
        if count==0:
            flash("Invalid Key","danger")
            return render_template("down1.html")
        print("^^^^^^^^^^^^^")
        if count==1:
            return render_template("hdfs.html", msg=asss)
    return render_template("down2.html")


@app.route('/down2/<s1>/<s2>/<s3>')
def down2(s1=0,s2='',s3=''):
    a = random.randrange(10000, 999999)
    print(a)
    return render_template('down2.html',a=a,s1=s1,s2=s2,s3=s3)

@app.route('/down2back', methods=["POST","GET"])
def down2back():
    if request.method=='POST':
        pkey=request.form['pkey']
        id = request.form['id']
        fid=request.form['fid']
        fname=request.form['fname']
        print(fid)
        print(pkey)

        sql = "select count(*),aes_decrypt(files,'lakshmi') from bigrock,bigrock_requests where bigrock.id='"+fid+"' and bigrock_requests.fid='"+fid+"' and bigrock_requests.pkey='"+pkey+"' "
        x = pd.read_sql_query(sql, mydb)
        count=x.values[0][0]
        print(count)
        asss=x.values[0][1]
        asss=asss.decode('utf-8')
        #as=asss.decode('base64','strict')
        print(asss)
        if count==0:
            flash("Invalid Key","danger")
            return render_template("down2.html")
        print("^^^^^^^^^^^^^")
        if count==1:
            return render_template("hdfs.html", msg=asss)
    return render_template("down2.html")

@app.route('/down3/<s1>/<s2>/<s3>')
def down3(s1=0,s2='',s3=''):
    a = random.randrange(10000, 999999)
    print(a)
    return render_template('down3.html',a=a,s1=s1,s2=s2,s3=s3)

@app.route('/down3back', methods=["POST","GET"])
def down3back():
    if request.method=='POST':
        pkey=request.form['pkey']
        id = request.form['id']
        fid=request.form['fid']
        fname=request.form['fname']
        print(pkey)

        sql = "select count(*),aes_decrypt(files,'lakshmi') from icloud,icloud_requests where icloud.id='"+fid+"' and icloud_requests.fid='"+fid+"' and icloud_requests.pkey='"+pkey+"' "
        x = pd.read_sql_query(sql, mydb)
        count=x.values[0][0]
        print(count)
        asss=x.values[0][1]
        asss=asss.decode('utf-8')
        #as=asss.decode('base64','strict')
        print(asss)
        if count==0:
            flash("Invalid Key","danger")
            return render_template("down3.html")
        print("^^^^^^^^^^^^^")
        if count==1:
            return render_template("hdfs.html", msg=asss)
    return render_template("down3.html")

@app.route('/viewfiles')
def viewfiles():
    sql = "select * from amezon"
    x = pd.read_sql_query(sql, mydb)
    print("^^^^^^^^^^^^^")
    print(type(x))
    print(x)
    x = x.drop(['skey'], axis=1)
    x = x.drop(['status'], axis=1)
    x = x.drop(['files'], axis=1)
    x = x.drop(['share'], axis=1)
    x = x.drop(['request'], axis=1)
    x = x.drop(['adate'], axis=1)
    sql1 = "select * from bigrock"
    y = pd.read_sql_query(sql1, mydb)
    print("^^^^^^^^^^^^^")
    print(type(y))
    print(y)
    # x = x.drop(['pwd'], axis=1)
    y = y.drop(['status'], axis=1)
    y = y.drop(['skey'], axis=1)
    y = y.drop(['files'], axis=1)
    y = y.drop(['share'], axis=1)
    y = y.drop(['request'], axis=1)
    y = y.drop(['adate'], axis=1)

    sql2 = "select * from icloud"
    z = pd.read_sql_query(sql2, mydb)
    print("^^^^^^^^^^^^^")
    print(type(z))
    print(z)
    # x = x.drop(['pwd'], axis=1)
    z = z.drop(['status'], axis=1)
    z = z.drop(['skey'], axis=1)
    z = z.drop(['files'], axis=1)
    z = z.drop(['share'], axis=1)
    z = z.drop(['request'], axis=1)
    z = z.drop(['adate'], axis=1)

    return render_template('viewfiles.html', col_name=x.columns.values, row_val=x.values.tolist(), col=y.columns.values,
                           row_main=y.values.tolist(), cols=z.columns.values, rows=z.values.tolist())
@app.route('/attackfile')
def attackfile():
    return render_template('attackfile.html')

@app.route('/attackback', methods=["POST","GET"])
def attackback():
    if request.method=='POST':
        fname=request.form['fname']
        print(fname)
        status='Unsafe'
        sql="select count(*) from amezon where fname='%s' and status='safe' "%(fname)
        x = pd.read_sql_query(sql, mydb)
        count = x.values[0][0]
        global name, name1, name2
        a = datetime.now()
        t = a.strftime("%Y/%m/%d,%H:%M:%S")
        if count==1:
            count = x.values[0][0]
            # if name in fname:
            sql1="update amezon set status='%s',adate='%s' where fname='%s'" %(status,t,fname)
            mycursor.execute(sql1)
            mydb.commit()
            flash("File attacked","success")
            return render_template('attackfile.html')
        if count==0:
            sqln = "select count(*) from bigrock where fname='%s' and status='safe'" % (fname)
            x = pd.read_sql_query(sqln, mydb)
            count = x.values[0][0]
            if count==1:
                sql2 = "update bigrock set status='%s',adate='%s' where fname='%s'" %(status,t,fname)
                mycursor.execute(sql2)
                mydb.commit()
                flash("File attacked", "success")
                return render_template('attackfile.html')
            if count==0:
                    sqln = "select count(*) from icloud where fname='%s' and status='safe' " % (fname)
                    x = pd.read_sql_query(sqln, mydb)
                    count = x.values[0][0]
                    if count == 1:
                        sql2 = "update icloud set status='%s',adate='%s' where fname='%s'" %(status,t,fname)
                        mycursor.execute(sql2)
                        mydb.commit()
                        flash("File attacked", "success")
                        return render_template('attackfile.html')
                    else:
                        flash("No files are found", "danger")
                        return render_template('attackfile.html')
            flash("No files are found", "danger")
            return render_template('attackfile.html')

@app.route('/viewattack')
def viewattack():
    sql = "select * from amezon where status='Unsafe'"
    x = pd.read_sql_query(sql, mydb)
    print("^^^^^^^^^^^^^")
    print(type(x))
    print(x)
    x = x.drop(['skey'], axis=1)
    x = x.drop(['status'], axis=1)
    x = x.drop(['files'], axis=1)
    x = x.drop(['share'], axis=1)
    x = x.drop(['request'], axis=1)
    x = x.drop(['time'], axis=1)
    sql1 = "select * from bigrock  where status='Unsafe'"
    y = pd.read_sql_query(sql1, mydb)
    print("^^^^^^^^^^^^^")
    print(type(y))
    print(y)
    y = y.drop(['status'], axis=1)
    y = y.drop(['skey'], axis=1)
    y = y.drop(['files'], axis=1)
    y = y.drop(['share'], axis=1)
    y = y.drop(['request'], axis=1)
    y = y.drop(['time'], axis=1)

    sql2 = "select * from icloud  where status='Unsafe'"
    z = pd.read_sql_query(sql2, mydb)
    print("^^^^^^^^^^^^^")
    print(type(z))
    print(z)
    # x = x.drop(['pwd'], axis=1)
    z = z.drop(['status'], axis=1)
    z = z.drop(['skey'], axis=1)
    z = z.drop(['files'], axis=1)
    z = z.drop(['share'], axis=1)
    z = z.drop(['request'], axis=1)
    z = z.drop(['time'], axis=1)

    return render_template('viewattack.html', col_name=x.columns.values, row_val=x.values.tolist(), col=y.columns.values,
                           row_main=y.values.tolist(), cols=z.columns.values, rows=z.values.tolist())

@app.route('/protect/<s1>')
def protect(s1=0):
    sql="update amezon set status='Protected' where id='%s'"%(s1)
    mycursor.execute(sql)
    mydb.commit()
    flash("File is Protected","success")
    return redirect(url_for('viewattack'))

@app.route('/protect1/<s1>')
def protect1(s1=0):
    sql="update bigrock set status='Protected' where id='%s'"%(s1)
    mycursor.execute(sql)
    mydb.commit()
    flash("File is Protected","success")
    return redirect(url_for('viewattack'))

@app.route('/protect2/<s1>')
def protect2(s1=0):
    sql="update icloud set status='Protected' where id='%s'"%(s1)
    mycursor.execute(sql)
    mydb.commit()
    flash("File is Protected","success")
    return redirect(url_for('viewattack'))


if __name__=="__main__":
    app.run(debug=True)
