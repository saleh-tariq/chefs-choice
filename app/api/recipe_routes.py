from flask import Blueprint, request
from app.models import db, Recipe, RecipeIngredients, Ingredient
from app.forms.recipe_form import RecipeForm
from flask_login import current_user, login_required
# from ..forms import RecipeForm

recipe_routes = Blueprint("recipes", __name__)


@recipe_routes.route("/")
@login_required
def get_user_recipes():
    """
    Get all recipes made by the logged in user
    """
    user = current_user.to_dict()
    recipes = Recipe.query.filter(Recipe.userId == user["id"]).all()
    return {"Recipes": [recipe.to_dict_simple() for recipe in recipes]}


@recipe_routes.route("/<int:recipe_id>")
@login_required
def get_recipe_by_id(recipe_id):
    """
    Get details of a specific recipe by its ID
    """
    recipe = Recipe.query.get(recipe_id)
    return recipe.to_dict()


@recipe_routes.route("/<int:recipe_id>", methods=["DELETE"])
@login_required
def delete_recipe(recipe_id):
    """
    Delete a recipe by ID
    """
    recipe = Recipe.query.get(recipe_id)
    if not recipe:
        return {"errors": {"message": "Recipe not found"}}, 404
    if not recipe.user_id == current_user.id:
        return {"errors": {"message": "Unauthorized"}}, 401

    temp = recipe.to_dict()
    db.session.delete(recipe)
    db.session.commit()
    return {"message": "Recipe successfully deleted", "Recipe": temp}


@recipe_routes.route("/", methods=["POST"])
@login_required
def post_new_recipe():
    """
    Create a new Recipe
    """
    form = RecipeForm()
    form["csrf_token"].data = request.cookies["csrf_token"]

    if form.validate_on_submit():
        new_recipe = Recipe()

        form.populate_obj(new_recipe)
        new_recipe.user_id = current_user.to_dict()["id"]

        db.session.add(new_recipe)
        db.session.commit()

        return new_recipe.to_dict_simple(), 201

    if form.errors:
        return {"errors": form.errors}, 400

    return
