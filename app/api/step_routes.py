from flask import Blueprint, request
from app.models import db, Recipe, Ingredient, Step, StepIngredients
from app.forms.recipe_form import RecipeForm
from app.forms.recipe_step_form import RecipeStepForm
from app.forms.step_form import StepForm
from app.forms.step_ingredient_form import StepIngredientForm

from flask_login import current_user, login_required
# from ..forms import RecipeForm

step_routes = Blueprint("steps", __name__)


@step_routes.route("/<int:step_id>", methods=["DELETE"])
@login_required
def delete_step(step_id):
    """
    Delete a step by ID
    """
    step = Step.query.get(step_id)
    if not step:
        return {"errors": {"message": "Step not found"}}, 404
    if not step.user_id == current_user.id:
        return {"errors": {"message": "Unauthorized"}}, 401

    temp = step.to_dict()
    db.session.delete(step)
    db.session.commit()
    return {"message": "Recipe successfully deleted", "data": temp}


@step_routes.route("/<int:step_id>/ingredients", methods=["POST"])
@login_required
def post_new_ingredient_to_step(step_id):
    """
    Create a new Ingredient for a Recipe
    """

    step = Step.query.get(step_id)
    form = StepIngredientForm()
    form["csrf_token"].data = request.cookies["csrf_token"]
    if not step.recipe.user_id == current_user.id:
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

        step_ingredient = StepIngredients(amount_needed=form.amount_needed.data)
        step_ingredient.ingredient = new_ingredient
        step.ingredients.append(step_ingredient)

        db.session.add(new_ingredient)
        db.session.commit()

        return new_ingredient.to_dict_simple(), 201

    if form.errors:
        return {"errors": form.errors}, 400

    return


@step_routes.route("/<int:step_id>/ingredients/<int:ingredient_id>", methods=["DELETE"])
@login_required
def delete_ingredient_from_a_step(step_id, ingredient_id):
    """
    Delete an Ingredient from a Recipe
    """
    ingredient = Ingredient.query.get(ingredient_id)
    step_ingredient = StepIngredients.query.filter(
        StepIngredients.step_id == step_id
        and StepIngredients.ingredient_id == ingredient_id
    ).first()
    if not step_ingredient:
        return {"errors": {"message": "Ingredient not found for this step"}}, 404
    if not ingredient.user_id == current_user.id:
        return {"errors": {"message": "Unauthorized"}}, 401

    temp = ingredient.to_dict_simple()
    db.session.delete(step_ingredient)
    db.session.commit()
    return {"message": "Ingredient successfully deleted from step", "Recipe": temp}


@step_routes.route("/<int:step_id>", methods=["PUT"])
@login_required
def put_step(step_id):
    """
    Edits an existing step
    """
    step = Step.query.get(step_id)
    if not step:
        return {"errors": {"message": "Step not found"}}, 404

    if not step.recipe.user_id == current_user.id:
        return {"errors": {"message": "Unauthorized"}}, 401

    form = StepForm()
    form["csrf_token"].data = request.cookies["csrf_token"]

    if form.validate_on_submit():
        form.populate_obj(step)

        db.session.add(step)
        db.session.commit()

        return step.to_dict_simple(), 201

    return
