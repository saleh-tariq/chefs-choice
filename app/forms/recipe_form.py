from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired


class RecipeForm(FlaskForm):
    name = StringField("name", validators=[DataRequired()])
    description = StringField("description")
    img = StringField("img")
