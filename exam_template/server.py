import imp
from flask import Flask, render_template
from exam_template import Exam
app = Flask(__name__)    
@app.route('/')          
def hello_world():
    return 'Hello World!'  
if __name__=="__main__":      
    app.run(debug=True)    