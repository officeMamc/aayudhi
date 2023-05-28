from flask import Flask, render_template, redirect, request, session
from flask_session import Session
 
app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/", methods=['GET','POST'])
def hello_world():
    return render_template('index.html')

@app.route("/home", methods=['GET','POST'])
def home():
    if not session.get('uname'):
        if request.form.get('uname') == "vru" and request.form.get('pass') == "vru":
            session["name"] = "vru"
            session["pass"] = "vru"
            return render_template('home.html')
        else:
            return redirect('/')
    
app.run(debug=True)