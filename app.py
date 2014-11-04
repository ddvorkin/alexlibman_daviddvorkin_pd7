#Alex Libman, David Dvorkin pd.7 Soft Dev
from flask import Flask, render_template, request, redirect, url_for, session
import login

app = Flask(__name__)

@app.route("/",methods = ["POST","GET"])
@app.route("/home",methods = ["POST","GET"])
def home():
    if request.method == "POST":
        if request.form['b'] == "Register":
            return redirect(url_for("register"))
        user = request.form["username"]
        pword = request.form["password"]
        msg = login.login(user,pword)
        if msg == "Successfully logged in.":
            session["user"] = user
            return redirect(url_for("inform"))
            #redirect to info page
        else:
            return render_template("login.html",message=msg)
    else:
        return render_template("login.html")

@app.route("/register",methods = ["POST","GET"])
def register():
    if request.method == "POST":
        user = request.form["username"]
        pword = request.form["password"]
        pword2 = request.form["confirm_password"]
        name = request.form["name"]
        msg = login.register(user,pword,pword2,name)
        if msg == "Successfully registered.":
            return redirect(url_for("home"))
        else:
            return render_template("register.html",message=msg)
    else:
        return render_template("register.html")

@app.route("/mainpage")
def inform():
    if "user" in session:
        info = login.getinfo(session["user"])#dict which includes "user" and "name"
        return render_template("mainpage.html",info=info)
    else:
        return render_template("mainpage.html",msg="You must be logged in to view the contents of this page.") #???

if __name__=="__main__":
    app.debug = True
    app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
    app.run()

