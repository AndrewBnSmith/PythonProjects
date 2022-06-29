
from flask_app import app
from flask import render_template, request, redirect, session, flash

from flask_app.models.painting import Painting
from flask_app.models.user import User

@app.route('/paintings/new')
def paintings_new():
    if 'user_id' not in session:
        return redirect('/logout')
    return render_template('new.html')

@app.route('/painting/create', methods=['POST'])
def create_painting():
    print(request.form)
   
    data = { 
        "name": request.form['name'],
        "description": request.form['description'],
        # "price": request.form [int(input('price'))]
        "price" : int(request.form['price'])
        }
    if not Painting.validate_painting(data):
        return redirect('/paintings/new')

    painting = Painting.save(request.form) 
    print(painting)
    return redirect(f"/dashboard")

# -----------------------------------------------------------------------------------------------

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect('/logout')
    return render_template('dashboard.html', paintings = Painting.get_all())

# @app.route('/dashboard')
# def dashboard():
#     return render_template('dashboard.html', users = User.get_user_with_paintings())
    


@app.route('/paintings/show_card/<int:id>')
def show_painting(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {'id': id}
    return render_template('show_card.html', painting = Painting.get_one(data))
# --------------------------------------------------------------------------------------------------


@app.route('/paintings/edit/<int:id>')
def edit_painting(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {'id': id}
    painting = Painting.get_one(data)
    return render_template('edit.html', painting = painting)

@app.route('/edit/paintings', methods=['POST'])
def update_painting():
    print(request.form)
    data = { 
        "name": request.form['name'],
        "description": request.form['description'],
        # "price": request.form [int(input('price'))]
        "price" : int(request.form['price'])
        }
    if not Painting.validate_painting(data):
        return redirect('/dashboard')
    painting = Painting.update(request.form)
    print(painting)
    return redirect('/dashboard')


@app.route('/delete/<int:id>')
def destroy_painting(id):
    data = {'id':id}
    Painting.destroy(data)
    return redirect('/dashboard')
