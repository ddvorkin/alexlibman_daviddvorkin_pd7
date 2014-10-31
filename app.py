#Alex Libman, David Dvorkin pd.7 Soft Dev
from flask import Flask, render_template, request, redirect, url_for
from pymongo import Connection

app = Flask(__name__)

@app.route("/",methods = ["POST","GET"])
def home():
    if request.form['b'] == "Register":
        return redirect(url_for("register"))
    if request.method == "POST":
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
        list = [{user:pword}]
        db.users.insert(list)
        return render_template("register.html")
    else:
        return render_template("register.html")

if __name__=="__main__":
    app.debug = True
    app.run()

