from .db import db, environment, SCHEMA, add_prefix_for_prod


class Recipe(db.Model):
    __tablename__ = "recipes"

    if environment == "production":
        __table_args__ = {"schema": SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), nullable=False)
    description = db.Column(db.String(4000), nullable=False)
    img = db.Column(db.String(40))
    userId = db.Column(
        db.Integer, db.ForeignKey(add_prefix_for_prod("users.id")), nullable=False
    )

    user = db.relationship("User", back_populates="recipes")
    ingredients = db.relationship("RecipeIngredients", back_populates="recipe")

    def to_dict_simple(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "img": self.img,
            "userId": self.userId,
        }

    def to_dict(self):
        ingredients = {
            ingredient.id: ingredient.to_dict_simple()
            for ingredient in self.ingredients
        }

        # for amount in self.amounts:
        #     ingredients[amount.ingredient_id]["amount_needed"] = amount.amount_needed

        return {
            **self.to_dict_simple(),
            "Ingredients": ingredients,
        }
