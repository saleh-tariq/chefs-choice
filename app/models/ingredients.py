from .db import db, environment, SCHEMA, add_prefix_for_prod


class Ingredient(db.Model):
    __tablename__ = "ingredients"

    if environment == "production":
        __table_args__ = {"schema": SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), nullable=False)
    price_per_unit = db.Column(db.Integer, nullable=False)
    amount_available = db.Column(db.Float, nullable=False)
    unit_of_measurement = db.Column(db.String(40), nullable=False)
    img = db.Column(db.String(40))
    user_id = db.Column(
        db.Integer, db.ForeignKey(add_prefix_for_prod("users.id")), nullable=False
    )

    user = db.relationship("User", back_populates="ingredients")
    recipes = db.relationship("RecipeIngredients", back_populates="ingredient")
    # amounts = db.relationship(add_prefix_for_prod("RecipeIngredients"))

    def to_dict_simple(self):
        return {
            "id": self.id,
            "name": self.name,
            "price": self.price_per_unit,
            "amount_available": self.amount_available,
            "unit_of_measurement": self.unit_of_measurement,
            "img": self.img,
            "user_id": self.user_id,
        }

    def to_dict(self):
        recipes = [
            {**recipe.recipe.to_dict_simple(), "amount_needed": recipe.amount_needed}
            for recipe in self.recipes
        ]

        return {
            **self.to_dict_simple(),
            "Recipes": recipes,
        }
