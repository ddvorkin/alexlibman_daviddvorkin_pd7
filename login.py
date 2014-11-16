from pymongo import Connection

conn = Connection()
db = conn['login']

def has_user(user):
    return next(db.users.find({"user":user}),None) != None

def user_pass_match(user,pword):
    return next(db.users.find({"user":user,"password":pword}),None) != None

def enter_into_db(user,pword,name):
    list = [{"user":user,"password":pword,"name":name}]
    db.users.insert(list)    

def register(user,pword,pword2,name):
    if user == "":
        return (False,"Please enter a username.")
    elif has_user(user):
        return (False,"The username entered is already registered.")
    elif pword == "" or pword2 == "":
        return (False,"No password entered in one or more of the fields.")
    elif pword != pword2:
        return (False,"The passwords entered do not match.")
    elif name == "":
        return (False,"No name entered.")
    else:
        enter_into_db(user,pword,name)
        return (True,"Successfully registered.")

def login(user,pword):
    if user == "":
        return (False,"Please enter your username.")
    elif pword == "":
        return (False,"Please enter your password.")
    elif not has_user(user):
        return (False,"No such username is registered.")
    elif not user_pass_match(user,pword):
        return (False,"Incorrect password.")
    else:
        return (True,"Successfully logged in.")

def getinfo(user):
    return next(db.users.find({"user":user},{'_id':False,'password':False}),None);

if __name__ == "__main__":
    print "Clearing the users database"
    db.users.drop()
