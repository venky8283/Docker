from flask import Flask, render_template, request, redirect

app = Flask(__name__)


### Temporary database
### We will replace this dictionary
database= {
    'users': {"username": "venky",
    "password": "admin123"}
}
logged_in=False

@app.route('/', methods=['POST', 'GET'])
def login():
    if request.method == 'GET':
        return render_template('form.html', title='Sign In')
    else:
        username = request.form.get("username")
        password = request.form.get("password")


        if username == database.get("users").get('username') and password == database.get('users').get('password'):


            logged_in = True


            return "<h1>Hi {0}, You are successfully logged in.</h1>".format(username)
        else:
            

            return " <h2>Wrong Credentials! Please <a href=\'/\'>try again</a></h2>"