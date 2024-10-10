from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FloatField
from wtforms.validators import DataRequired


class StepIngredientForm(FlaskForm):
    name = StringField("name", validators=DataRequired())
    price_per_unit = IntegerField("price_per_unit")
    amount_available = FloatField("amount_available", validators=DataRequired())
    unit_of_measurement = StringField("unit_of_measurement", validators=DataRequired())
    img = StringField("img")
    amount_needed = FloatField("amount_needed", validators=DataRequired())
