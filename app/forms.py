from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, SubmitField, SelectField
from wtforms.validators import InputRequired

class AddStudentForm(FlaskForm):
    name = StringField('Student name', validators=[InputRequired()])
    grade_id = SelectField('Grade', coerce=int)
    house_id = SelectField('House', coerce=int)
    # TODO: Add a field to select the house_id once a House model has been defined
    english_mark = IntegerField('English', validators=[InputRequired()])
    science_mark = IntegerField('Science', validators=[InputRequired()])
    mathematics_mark = IntegerField('Maths', validators=[InputRequired()])
    # TODO: Add a field for the mathematics mark (should be an integer)
    does_homework = BooleanField('Does homework?')
    # TODO: Add a field for the stays_on_task field (should be a boolean)
    stays_on_task = BooleanField('Stays on Task?')
    
    submit = SubmitField('Add student')
