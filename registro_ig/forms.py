from flask_wtf import FlaskForm
from wtforms import DateField, StringField, FloatField, SubmitField
from wtforms.validators import DataRequired, Length


class MovementForm(FlaskForm):
    date = DateField("Fecha", validators=[DataRequired()])
    concept = StringField("Concepto", validators=[DataRequired(), Length(min=4, message="Tiene que contener mas de 4 caracteres")])
    quantity = FloatField("Cantidad", validators=[DataRequired()])

    submit = SubmitField("Aceptar")