from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "counter"

@app.route('/')
def index():
    if "count" not in session:
        session["count"] = 0
    else:    
        session["count"] += 1
    
    return render_template("index.html")    

@app.route("/count", methods=["POST"])
def view_count():
    if request.form["button"]=="add":
        session["count"] += 1
    elif request.form["button"]=="reset":
        session["count"] = 0
    elif request.form["button"]=="3":
        session["count"] += 2
    elif request.form["button"]=="4":
        session["count"] += 3

    return redirect("/")

@app.route("/destroy_session")
def destroy():
    session.clear()
    session.pop("count")
    return redirect("/")
    
if __name__=="__main__":
    
    app.run(debug=True) 