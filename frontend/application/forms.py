from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class TaskForm(FlaskForm):
    description = StringField("Task Description", validators=[DataRequired()])
    submit = SubmitField("Add Task")