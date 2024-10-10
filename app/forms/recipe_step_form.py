from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FloatField
from wtforms.validators import DataRequired


class RecipeStepForm(FlaskForm):
    description= StringField('description')
    img = StringField("img")