from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class CreateAuthor(FlaskForm):
    name = StringField("Author fullname", validators=[DataRequired()])
    submit = SubmitField("Add Author")