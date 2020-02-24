from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Required, Length

class PostForm(FlaskForm):
    first_name = StringField('First Name',
        validators = [
            Required(),
            Length(min=2, max=30)
        ]
    )
    last_name = StringField('First Name',
        validators = [
            Required(),
            Length(min=2, max=30)
        ]
    )
    title = StringField('First Name',
        validators = [
            Required(),
            Length(min=2, max=100)
        ]
    )
    content = StringField('First Name',
        validators = [
            Required(),
            Length(min=2, max=1000)
        ]
    )
    submit = SubmitField('Post!')    