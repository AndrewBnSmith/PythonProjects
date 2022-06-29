from flask_app import app
from flask import render_template, request, redirect

from flask_app.models.recipe import Recipe
from flask_app.models.user import User

@app.route('/recipes')
def ninjas():
    return render_template('recipes.html', recipes = User.get_all())


@app.route('/create/recipe', methods = ["POST"])
def create_recipe():
    Recipe.save(request.form)

    return redirect('/recpes')
