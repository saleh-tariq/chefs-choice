from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField
from wtforms.validators import DataRequired
from ..api.s3 import ALLOWED_EXTENSIONS


class RecipeForm(FlaskForm):
    name = StringField("name", validators=[DataRequired()])
    description = StringField("description")
    img = FileField("Image File", validators=[FileAllowed(list(ALLOWED_EXTENSIONS))])
