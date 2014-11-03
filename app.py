#Alex Libman, David Dvorkin pd.7 Soft Dev
from flask import Flask, render_template, request, redirect, url_for
from pymongo import Connection

app = Flask(__name__)

@app.route("/",methods = ["POST","GET"])
def home():
    if request.method == "POST":
        if request.form['b'] == "Register":
            return redirect(url_for("register"))
        conn = Connection()
        db = conn['login']
        user = request.form["username"]
        pword = request.form["password"]
        list = [{user:pword}]
        db.users.insert(list)
        #validate info from text boxes
        for a in db.users.find():
            print a
        return render_template("login.html")
    else:
        return render_template("login.html")

@app.route("/register",methods = ["POST","GET"])
def register():
    if request.method == "POST":
        conn = Connection()
        db = conn['login']
        user = request.form["username"]
        pword = request.form["password"]
        pword2 = request.form["confirm_password"]
        name = request.form["name"]
        if user == "":
            msg = "Please enter a username."
            pword2 = request.form["confirm_password"]
        if pword == "" or pword2 == "":
            msg = "No password entered in one or more of the fields."
            return render_template("register.html",message=msg)
        if pword != pword2:
            msg = "Passwords entered do not match."
            return render_template("register.html",message=msg)
        if name == "":
            msg = "Please enter your name."
            return render_template("register.html",message=msg)
        list = [{user:pword}]
        db.users.insert(list)
        return redirect(url_for("/"))
    else:
        return render_template("register.html")

@app.route("/mainpage", methods = ["POST", "GET"])
def information():
    pass

if __name__=="__main__":
    app.debug = True
    app.run()

