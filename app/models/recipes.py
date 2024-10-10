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
    steps = db.relationship(
        "Step", back_populates="recipe", cascade="all, delete-orphan"
    )

    def to_dict_simple(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "img": self.img,
            "user_id": self.user_id,
        }

    def total_seconds(self):
        seconds = 0
        for step in self.steps:
            seconds = seconds + step.seconds

        return seconds

    def total_ingredients(self):
        res = []
        for step in self.steps:
            for ingredient in step.to_dict()["Ingredients"]:
                res.append(ingredient)

        return res

    def is_available(self):
        for step in self.steps:
            if not step.can_make():
                return False
        return True

    def missing_ingredients(self):
        return [
            ingredient
            for ingredient in self.total_ingredients()
            if ingredient.amount_needed > ingredient.amount_available
        ]

    def to_dict(self):
        return {
            **self.to_dict_simple(),
            "steps": [step.to_dict() for step in self.steps],
            "total_seconds": self.total_seconds(),
            "is_available": self.is_available(),
            "missing_ingredients": self.missing_ingredients(),
        }
