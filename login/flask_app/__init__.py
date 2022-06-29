from flask import Flask
from flask import Bcrypt

app = Flask(__name__)
app.secret_key = "password"