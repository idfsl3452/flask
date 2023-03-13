from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from market.models import User, Item

class RegisterForm(FlaskForm):
    
    def validate_username(self, username_to_check):
        user = User.query.filter_by(username=username_to_check.data).first()
        if user :
            raise ValidationError('Username already exists! Please try a different username')
    
    def validate_email_address(self, email_address_to_check):
        email_address = User.query.filter_by(email_address=email_address_to_check.data).first()
        if email_address:
            raise ValidationError('Email Address already exists! Please try a different email address')
    
    username = StringField(label='User Name:', validators=[Length(min=2, max=30), DataRequired()])
    email_address = StringField(label='Email Address:', validators=[Email(), DataRequired()])
    password1 = PasswordField(label='Password:', validators=[Length(min=6), DataRequired()])
    password2 = PasswordField(label='Confirm Password:', validators=[EqualTo('password1'), DataRequired()])
    submit = SubmitField(label='Create Account')
    
class LoginForm(FlaskForm):
    username = StringField(label='User Name:', validators=[DataRequired()])
    password = PasswordField(label='Password:', validators=[DataRequired()])
    submit = SubmitField(label='Sign in')
    
class PurchaseItemForm(FlaskForm):
    submit = SubmitField(label='Purchase Item!')

class SellItemForm(FlaskForm):
    submit = SubmitField(label='Sell Item!')
    
class DeleteItemForm(FlaskForm):
    submit = SubmitField(label='Delete Item !')

class CreateItemForm(FlaskForm):
    
    def validate_name(self, name_to_check):
        name = Item.query.filter_by(name=name_to_check.data).first()
        if name :
            raise ValidationError('Item name already exists! Please try a different item name')
    
    def validate_name(self, barcode_to_check):
        barcode = Item.query.filter_by(barcode=barcode_to_check.data).first()
        if barcode :
            raise ValidationError('barcode already exists! Please try a different barcode')
    
    name = StringField(lable='Item name',validators=[Length(max=30),DataRequired()])
    price = IntegerField(label='price')
    barcode = StringField(lable='barcode',validators=[Length(max=12),DataRequired()])
    description = StringField(lable='description',validators=[Length(max=1024),DataRequired()])
    submit = SubmitField(label='Create Item')
    