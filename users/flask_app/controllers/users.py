from flask_app import app 
from flask import render_template,redirect,request,session,flash
from flask_app.models.user import User

@app.route('/')
@app.route('/users')
def index():
    users = User.get_all() 
    return render_template('index.html', users = users)

@app.route('/users/new')
def new_user():
    return render_template('new_user.html')

@app.route('/create/user', methods=['POST'])
def create_user():
    print(request.form)
    user = User.save(request.form)
    print(user)
    return redirect(f"/users/{user}")

@app.route('/users/<int:id>')
def show_user(id):
    data = {'id':id}
    user = User.get_one(data)
    return render_template('show_user.html', user = user)

@app.route('/users/<int:id>/edit')
def edit_user(id):
    data = {'id': id}
    user = User.get_one(data)
    return render_template('edit_user.html', user = user)

@app.route('/edit/user', methods=['POST'])
def update_user():
    print(request.form)
    user = User.update(request.form)
    print(user)
    return redirect(f"/users/{request.form['id']}")

@app.route('/delete/<int:id>')
def destroy_user(id):
    data = {'id':id}
    User.destroy(data)  
    return redirect('/')
