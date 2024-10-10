from .db import db, environment, SCHEMA, add_prefix_for_prod


class Step(db.Model):
    __tablename__ = "steps"

    if environment == "production":
        __table_args__ = {"schema": SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(4000), nullable=False)
    seconds = db.Column(db.Integer)
    img = db.Column(db.String(400))
    recipe_id = db.Column(
        db.ForeignKey(add_prefix_for_prod("recipes.id")),
    )

    ingredients = db.relationship("StepIngredients", back_populates="step")
    recipe = db.relationship("Recipe", back_populates="steps")