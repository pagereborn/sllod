from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import BaseValidator
class PollField(forms.Field):
    default_error_messages = {
        'not_an_a': _(u'you can only input A here! damn!'),
    }

    def to_python(self, value):
        if value in value.EMPTY_VALUES:
            return None
        return value

    def validate(self, value):
        if value != 'A':
            raise ValidationError(self.error_messages['not_an_a'])