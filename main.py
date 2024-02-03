from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///login.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login", methods=['GET','POST'])
def LogIn():
    if request.method == "POST":
        email = request.form['email']
        print(email)
    return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True)
