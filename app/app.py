from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_PASSWORD'] = 'admin123'
app.config['MYSQL_USER'] = 'testuser'
app.config['MYSQL_DB'] = 'backend'

app.config['MYSQL_HOST'] = 'database'

db  = MySQL(app)


### Temporary database
### We will replace this dictionary

@app.route('/', methods=['POST', 'GET'])
def login():

    cursor = db.connection.cursor()


    if request.method == 'GET':
        return render_template('form.html', title='Sign In')
    else:
        username = request.form.get("username")
        password = request.form.get("password")


        status = cursor.execute('''SELECT username FROM `users` WHERE `username`="{0}" and `password`="{1}"'''.format(username,password))

        if status:


            return "<h1>Hi {0}, You are successfully logged in.</h1>".format(username)
        else:
            

            return " <h2>Wrong Credentials! Please <a href=\'/\'>try again</a></h2>"