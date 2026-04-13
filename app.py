from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login", methods = ["GET","POST"])
def login():
    username = None
    password = None
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        
    return render_template("login.html", username=username, password=password)

@app.route("/register")
def register():
    username = None
    password = None
    name = None
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        name = request.form.get("name")
    return render_template("register.html", username=username, password=password, name=name)

if(__name__ == "__main__"):
    app.run(debug=True)