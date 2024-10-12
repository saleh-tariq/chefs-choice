from .db import db, environment, SCHEMA, add_prefix_for_prod


class Step(db.Model):
    __tablename__ = "steps"

    if environment == "production":
        __table_args__ = {"schema": SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(4000), nullable=False)
    seconds = db.Column(db.Integer)
    img = db.Column(db.String(400))
    next_step_id = db.Column(
        db.ForeignKey(add_prefix_for_prod("steps.id")), nullable=True
    )
    is_head = db.Column(db.Integer, nullable=True)
    recipe_id = db.Column(
        db.ForeignKey(add_prefix_for_prod("recipes.id")),
    )

    ingredients = db.relationship("StepIngredients", back_populates="step")
    recipe = db.relationship("Recipe", back_populates="steps")
    next_step = db.relationship("Step", back_populates="prev_step", remote_side=[id])
    prev_step = db.relationship("Step", back_populates="next_step")

    def can_make(self):
        for ingredient in self.ingredients:
            if ingredient.amount_needed > ingredient.ingredient.amount_available:
                return False

        return True

    def to_dict(self):
        return {
            "id": self.id,
            "description": self.description,
            "seconds": self.seconds,
            "img": self.img,
            "next_step_id": self.next_step_id,
            "Ingredients": [
                {
                    **ingredient.ingredient.to_dict_simple(),
                    "amount_needed": ingredient.amount_needed,
                }
                for ingredient in self.ingredients
            ],
            "has_ingredients": self.can_make(),
        }
