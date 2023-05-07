from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo




class RegistrationForm(FlaskForm):
    name = StringField(
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField(
                        validators=[DataRequired(), Email()])
    phone = StringField(
                        validators=[DataRequired(), Length(10)])
    startupname = StringField(
                        validators=[DataRequired(), Length(min=2, max=20)])
    teamnumber = StringField(
                        validators=[DataRequired(), Length(min=1, max=20)])
    submit = SubmitField('Register')

class AudienceForm(FlaskForm):
    name = StringField(
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField(
                        validators=[DataRequired(), Email()])
    phone = StringField(
                        validators=[DataRequired(), Length(10)])
    city = StringField(
                        validators=[DataRequired(), Length(min=2, max=20)])
    college = StringField(
                        validators=[Length(min=2, max=20)])
    submit = SubmitField('Submit')


