from flask_app import app
from flask import render_template, request, redirect

from flask_app.models.model import Model

##!CREATE
## TODO Show the new model form
@app.route('/models/new')
def new_model():
    return render_template('new_model.html')

## TODO handle new model form
@app.route('/create/model', methods=['POST'])
def create_model():
    print(request.form)
    model = Model.save(request.form) #! class method in model class, find it in ../controllers/model.py
    print(model)
    return redirect(f"/models/{model}")


##! READ
@app.route('/dashboard')
def dashboard():
    return render_template('models.html', models = Model.get_all())

@app.route('/models/<int:id>')
def show_model(id):
    data = {'id': id}
    return render_template('show_model.html', model = Model.get_one(data))


#! UPDATE
## TODO route to edit model form
@app.route('/models/<int:id>/edit')
def edit_model(id):
    data = {'id': id}
    model = Model.get_one(data)
    return render_template('edit_model.html', model = model)

## TODO handle model edit
@app.route('/edit/model', methods=['POST'])
def update_model():
    print(request.form)
    model = Model.update(request.form)
    print(model)
    return redirect(f"/models/{request.form['id']}")
