from flask import Blueprint, request
from app.models import db, Recipe, RecipeIngredients, Ingredient
from app.forms.recipe_form import RecipeForm
from app.forms.recipe_ingredient_form import RecipeIngredientForm
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


@recipe_routes.route("/<int:recipe_id>/ingredients", methods=["POST"])
@login_required
def post_new_ingredient_to_recipe(recipe_id):
    """
    Create a new Ingredient for a Recipe
    """

    recipe = Recipe.query.get(recipe_id)
    form = RecipeIngredientForm()
    form["csrf_token"].data = request.cookies["csrf_token"]
    if not recipe.user_id == current_user.id:
        return {"errors": {"message": "Unauthorized"}}, 401

    if form.validate_on_submit():
        new_ingredient = Ingredient(
            name=form.name.data,
            price_per_unit=form.price_per_unit.data,
            amount_available=form.amount_available.data,
            unit_of_measurement=form.unit_of_measurement.data,
            img=form.img.data,
        )

        new_ingredient.user_id = current_user.to_dict()["id"]

        recipe_ingredient = RecipeIngredients(amount_needed=form.amount_needed.data)
        recipe_ingredient.ingredient = new_ingredient
        recipe.ingredients.append(recipe_ingredient)

        db.session.add(new_ingredient)
        db.session.commit()

        return new_ingredient.to_dict(), 201

    if form.errors:
        return {"errors": form.errors}, 400

    return


@recipe_routes.route(
    "/<int:recipe_id>/ingredients/<int:ingredient_id>", methods=["DELETE"]
)
@login_required
def delete_ingredient_from_a_recipe(recipe_id, ingredient_id):
    """
    Delete an Ingredient from a Recipe
    """
    ingredient = Ingredient.query.get(ingredient_id)
    recipe_ingredient = RecipeIngredients.query.filter(
        RecipeIngredients.recipe_id == recipe_id
        and RecipeIngredients.ingredient_id == ingredient_id
    ).first()
    if not recipe_ingredient:
        return {"errors": {"message": "Ingredient not found for this recipe"}}, 404
    if not ingredient.user_id == current_user.id:
        return {"errors": {"message": "Unauthorized"}}, 401

    temp = ingredient.to_dict()
    db.session.delete(recipe_ingredient)
    db.session.commit()
    return {"message": "Ingredient successfully deleted from recipe", "Recipe": temp}


@recipe_routes.route("/<int:recipe_id>", methods=["PUT"])
@login_required
def put_template(recipe_id):
    """
    Edits an existing recipe
    """
    recipe = Recipe.query.get(recipe_id)
    if not recipe:
        return {"errors": {"message": "Recipe not found"}}, 404

    if not recipe.user_id == current_user.id:
        return {"errors": {"message": "Unauthorized"}}, 401

    form = RecipeForm()
    form["csrf_token"].data = request.cookies["csrf_token"]

    if form.validate_on_submit():
        form.populate_obj(recipe)
        recipe.user_id = current_user.to_dict()["id"]

        db.session.add(recipe)
        db.session.commit()

        return recipe.to_dict_simple(), 201

    return
