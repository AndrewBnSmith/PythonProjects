
from flask import Flask, render_template, request, redirect, session 
app = Flask(__name__)
app.secret_key = 'survey'


@app.route('/')          
def index():
    return render_template("index.html")

# @app.route('/process', methods=['POST'])          
# def process():
#     print(request.form)
#     return redirect("/")

@app.route('/result', methods =['POST'])
def user_result():
    session['name'] = request.form['your_name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']
    return render_template("result.html", name=request.form['your_name'], location=request.form['location'], language = request.form['language'], comment = request.form['comment'])

    return redirect("/")

if __name__=="__main__":  
    app.run(debug=True)   