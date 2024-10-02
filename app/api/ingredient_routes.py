from flask import Blueprint, request
from app.models import db, Recipe, RecipeIngredients, Ingredient
from app.forms.ingredient_form import IngredientForm
from flask_login import current_user, login_required
# from ..forms import RecipeForm

ingredient_routes = Blueprint("ingredients", __name__)


@ingredient_routes.route("/")
@login_required
def get_user_ingredients():
    """
    Get all ingredients made by the logged in user
    """
    user = current_user.to_dict()
    ingredients = Ingredient.query.filter(Ingredient.userId == user["id"]).all()
    return {"Ingredients": [ingredient.to_dict_simple() for ingredient in ingredients]}


@ingredient_routes.route("/<int:ingredient_id>")
@login_required
def get_ingredient_by_id(ingredient_id):
    """
    Get details of a specific ingredient by its ID
    """
    ingredient = Ingredient.query.get(ingredient_id)
    return ingredient.to_dict()


@ingredient_routes.route("/<int:ingredient_id>", methods=["DELETE"])
@login_required
def delete_ingredient(ingredient_id):
    """
    Delete a ingredient by ID
    """
    ingredient = Ingredient.query.get(ingredient_id)
    if not ingredient:
        return {"errors": {"message": "Ingredient not found"}}, 404
    if not ingredient.user_id == current_user.id:
        return {"errors": {"message": "Unauthorized"}}, 401

    temp = ingredient.to_dict()
    db.session.delete(ingredient)
    db.session.commit()
    return {"message": "Ingredient successfully deleted", "Ingredient": temp}


@ingredient_routes.route("/", methods=["POST"])
@login_required
def post_new_ingredient():
    """
    Create a new Ingredient
    """
    form = IngredientForm()
    form["csrf_token"].data = request.cookies["csrf_token"]

    if form.validate_on_submit():
        new_ingredient = Ingredient()

        form.populate_obj(new_ingredient)
        new_ingredient.user_id = current_user.to_dict()["id"]

        db.session.add(new_ingredient)
        db.session.commit()

        return new_ingredient.to_dict_simple(), 201

    if form.errors:
        return {"errors": form.errors}, 400

    return
