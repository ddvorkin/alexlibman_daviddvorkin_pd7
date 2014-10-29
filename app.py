#Alex Libman, David Dvorkin pd.7 Soft Dev
from flask import Flask
import pymongo import Connection

@app.route("/",methods = ["POST","GET"])
def home():
    pass

@app.route("/register",methods = ["POST","GET"])
def register():
    pass

if __name__=="__main__":
    app.debug = True
    app.run()
