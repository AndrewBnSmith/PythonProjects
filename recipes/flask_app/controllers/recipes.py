
from flask_app import app
from flask import render_template, request, redirect, session, flash

from flask_app.models.recipe import Recipe
from flask_app.models.user import User

@app.route('/recipes/new')
def recipes_new():
    return render_template('new.html')

@app.route('/recipe/create', methods=['POST'])
def create_recipe():
    print(request.form)
    if not Recipe.validate_recipe(request.form):
        return redirect('/recipes/new')
    recipe = Recipe.save(request.form) 
    print(recipe)
    return redirect(f"/dashboard")

# -----------------------------------------------------------------------------------------------

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html', recipes = Recipe.get_all())


@app.route('/recipes/show_card/<int:id>')
def show_recipe(id):
    data = {'id': id}
    return render_template('show_card.html', recipe = Recipe.get_one(data))
# --------------------------------------------------------------------------------------------------


@app.route('/recipes/edit/<int:id>')
def edit_recipe(id):
    data = {'id': id}
    recipe = Recipe.get_one(data)
    return render_template('edit.html', recipe = recipe)

@app.route('/edit/recipes', methods=['POST'])
def update_recipe():
    print(request.form)
    if not Recipe.validate_recipe(request.form):
        return redirect('/dashboard')
    recipe = Recipe.update(request.form)
    print(recipe)
    return redirect('/dashboard')


@app.route('/delete/<int:id>')
def destroy_recipe(id):
    data = {'id':id}
    Recipe.destroy(data)
    return redirect('/dashboard')
