from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired


class StepForm(FlaskForm):
    description = StringField("description")
    img = StringField("img")
    seconds = IntegerField("seconds")
