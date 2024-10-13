from flask import Blueprint, request
from app.models import db, Recipe, Ingredient, Step, StepIngredients
from app.forms.recipe_form import RecipeForm
from app.forms.recipe_step_form import RecipeStepForm
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
    recipes = Recipe.query.filter(Recipe.user_id == user["id"]).all()
    return {"Recipes": [recipe.to_dict() for recipe in recipes]}


@recipe_routes.route("/available")
@login_required
def get_available_recipes():
    """
    Get all recipes which the user has the ingredients to make
    """
    user = current_user.to_dict()
    recipes = Recipe.query.filter(Recipe.user_id == user["id"]).all()
    return {
        "Recipes": [recipe.to_dict() for recipe in recipes if recipe.is_available()]
    }


@recipe_routes.route("/unavailable")
@login_required
def get_unavailable_recipes():
    """
    Get all recipes which the user doesnt have the ingredients to make
    """
    user = current_user.to_dict()
    recipes = Recipe.query.filter(Recipe.user_id == user["id"]).all()
    return {
        "Recipes": [
            recipe.to_dict_simple() for recipe in recipes if not recipe.is_available()
        ]
    }


@recipe_routes.route("/<int:recipe_id>")
@login_required
def get_recipe_by_id(recipe_id):
    """
    Get details of a specific recipe by its ID
    """
    recipe = Recipe.query.get(recipe_id)
    # first_step = Step.query.filter(Step.is_head == 1, Step.recipe_id == recipe.id).first()
    # steps = [first_step]
    # while(True and steps[-1]):
    #     if steps[-1].next_step_id:
    #         steps.append(steps[-1].next_step)
    #     else:
    #         break
    return {**recipe.to_dict_advanced(), "steps": [step.to_dict() for step in recipe.steps]}


@recipe_routes.route("/<int:recipe_id>")
@login_required
def get_needed_ingredients(recipe_id):
    """
    Get details of a specific recipe by its ID
    """
    recipe = Recipe.query.get(recipe_id)
    return recipe.missing_ingredients()


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


@recipe_routes.route("/<int:recipe_id>/steps", methods=["POST"])
@login_required
def post_new_step_to_recipe(recipe_id):
    """
    Create a new step for a Recipe
    """

    recipe = Recipe.query.get(recipe_id)
    form = RecipeStepForm()
    form["csrf_token"].data = request.cookies["csrf_token"]
    if not recipe.user_id == current_user.id:
        return {"errors": {"message": "Unauthorized"}}, 401

    print('\n\n\n\n\n\n\n\n\n')
    if form.validate_on_submit():
        new_step = Step(
            # description=form.description.data,
            # img=form.img.data,
            # seconds=form.seconds.data,
        )

        form.populate_obj(new_step)

        print('form validated')
        print('')
        recipe.steps.append(new_step)

        new_step.user_id = current_user.to_dict()["id"]
        db.session.add(new_step)
        db.session.commit()

        return new_step.to_dict(), 201

    if form.errors:
        return {"errors": form.errors}, 400

    return


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
