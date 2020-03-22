#! python
#
# ~/app/formsubmit/forms.py
# The forms available to the formsubmit application within the
# example flask application
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired
from wtforms.validators import Length


class AddressForm(FlaskForm):
    addr1 = StringField('Address 1', validators=[DataRequired()])
    addr2 = StringField('Address 2')
    city = StringField('City', validators=[DataRequired()])
    state = StringField(
        'State',
        validators=[
            DataRequired(),
            Length(min=2, max=2)
        ]
    )
