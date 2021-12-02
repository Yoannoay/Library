from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired

class CreateAuthor(FlaskForm):
    name = StringField("Author fullname: ", validators=[DataRequired()])
    submit = SubmitField("Add Author")

class NewBook(FlaskForm):
    name = StringField("Book title: ", validators=[DataRequired()])
    submit = SubmitField("Add Book")

class NewReview(FlaskForm):
    rating = SelectField("Rating: ", choices=[('1', '1'),('2', '2'),('3', '3'),('4', '4'),
    ('5', '5'),('6', '6'),('7', '7'),('8', '8'),('9', '9'),('10', '10')], validators=[DataRequired()])

    thoughts = StringField("Review: ", maxlength=1000, validators=[DataRequired()])
    
    submit = SubmitField("Submit review")