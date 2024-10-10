from .db import db, add_prefix_for_prod, environment, SCHEMA


class StepIngredients(db.Model):
    __tablename__ = "step_ingredients"

    if environment == "production":
        __table_args__ = {"schema": SCHEMA}

    # left id
    ingredient_id = db.Column(
        db.ForeignKey(add_prefix_for_prod("ingredients.id")),
        primary_key=True,
    )
    # right id
    step_id = db.Column(
        db.ForeignKey(add_prefix_for_prod("steps.id")),
        primary_key=True,
    )
    # extra data
    amount_needed = db.Column("amount_needed", db.Float)
    # child parent relations
    ingredient = db.relationship("Ingredient", back_populates="steps")
    step = db.relationship("Step", back_populates="ingredients")
