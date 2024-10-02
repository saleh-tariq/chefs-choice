from .db import db, add_prefix_for_prod, environment, SCHEMA


class RecipeIngredients(db.Model):
    __tablename__ = "recipe_ingredients"

    if environment == "production":
        __table_args__ = {"schema": SCHEMA}

    # left id
    ingredient_id = db.Column(
        db.ForeignKey(add_prefix_for_prod("ingredients.id")),
        primary_key=True,
    )
    # right id
    recipe_id = db.Column(
        db.ForeignKey(add_prefix_for_prod("recipes.id")),
        primary_key=True,
    )
    # extra data
    amount_needed = db.Column("amount_needed", db.Float)
    # child parent relations
    ingredient = db.relationship("Ingredient", back_populates="recipes")
    recipe = db.relationship("Recipe", back_populates="ingredients")
