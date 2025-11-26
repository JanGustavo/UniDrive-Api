from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length

class ItemForm(FlaskForm):
    title = StringField('Título', validators=[DataRequired(), Length(max=120)])
    description = TextAreaField('Descrição')
    submit = SubmitField('Salvar')
