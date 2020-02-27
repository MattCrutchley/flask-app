from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import Required, Length, Email, EqualTo, ValidationError
from application.models import Users, Posts
from flask_login import current_user

def Unique_title():    #attempt to colaspe to singel unique function    message = 'value must be unique'
    def _Unique_title(form, feild):
        if str(Posts.query.filter_by(title = feild.data).all()) != '[]':
            raise ValidationError("Value entered not unique.")
            print('failed validation test for uniqueness')
    return _Unique_title


def Unique_content():
    message = 'value must be unique'
    def _Unique_content(form, feild):
        if str(Posts.query.filter_by(content = feild.data).all()) != '[]':
            raise ValidationError("Value entered not unique.")
            print('failed validation test for uniqueness')
    return _Unique_content









class PostForm(FlaskForm):
    title = StringField('Title',
        validators = [
            Required(),
            Unique_title(),
            Length(min=2, max=100)
        ]
    )
    content = StringField('Content',
        validators = [
            Required(),
            Unique_content(),
            Length(min=2, max=1000)
        ]
    )
    submit = SubmitField('Post!')   

class RegistrationForm(FlaskForm):

    first_name = StringField('First Name',
        validators = [
            Required(),
            Length(min=2, max=30)
        ]
    )
    last_name = StringField('last Name',
        validators = [
            Required(),
            Length(min=2, max=30)
        ]
    )

    email = StringField('Email',
        validators = [
           Required(),
            Email()
        ]
    )
    password = PasswordField('Password',
        validators = [
           Required(),
        ]
    )
    confirm_password = PasswordField('Confirm Password',
        validators = [
           Required(),
            EqualTo('password')
        ]
    )
    submit = SubmitField('Sign Up')

    def validate_email(self, email):
        user = Users.query.filter_by(email=email.data).first()

        if user:
            raise ValidationError('Email already in use')

class LoginForm(FlaskForm):
    email = StringField('Email',
        validators=[
            Required(),
            Email()
        ]
    )

    password = PasswordField('Password',
        validators=[
            Required()
        ]
    )

    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class UpdateAccountForm(FlaskForm):
    first_name = StringField('First Name',
        validators=[
            Required(),
            Length(min=4, max=30)
        ])
    last_name = StringField('Last Name',
        validators=[
            Required(),
            Length(min=4, max=30)
        ])
    email = StringField('Email',
        validators=[
            Required(),
            Email()
        ])
    submit = SubmitField('Update')

    def validate_email(self,email):
        if email.data != current_user.email:
            user = Users.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('Email already in use')












