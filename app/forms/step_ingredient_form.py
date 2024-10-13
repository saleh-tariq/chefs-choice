from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FloatField
from wtforms.validators import DataRequired


class StepIngredientForm(FlaskForm):
    ingredient_id = IntegerField("ingredient_id", validators=[DataRequired()])
    amount_needed = FloatField("amount_needed", validators=[DataRequired()])
