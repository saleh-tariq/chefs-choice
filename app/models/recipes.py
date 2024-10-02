from .db import db, environment, SCHEMA, add_prefix_for_prod


class Recipe(db.Model):
    __tablename__ = "recipes"

    if environment == "production":
        __table_args__ = {"schema": SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), nullable=False)
    description = db.Column(db.String(4000), nullable=False)
    img = db.Column(db.String(40))
    user_id = db.Column(
        db.Integer, db.ForeignKey(add_prefix_for_prod("users.id")), nullable=False
    )

    user = db.relationship("User", back_populates="recipes")
    ingredients = db.relationship(
        "RecipeIngredients", back_populates="recipe", cascade="all, delete-orphan"
    )

    def to_dict_simple(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "img": self.img,
            "user_id": self.user_id,
        }

    def to_dict(self):
        ingredients = [
            {
                **ingredient.ingredient.to_dict_simple(),
                "amount_needed": ingredient.amount_needed,
            }
            for ingredient in self.ingredients
        ]

        return {
            **self.to_dict_simple(),
            "Ingredients": ingredients,
        }
