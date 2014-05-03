from django.forms import ModelForm
from .models import Poll, Option
from django.forms.widgets import Widget, Textarea
from sllod.widgets import PollWidget
class PollForm(ModelForm):
    
    class Meta:
        model = Poll
        fields = ['message']
        widgets = {
                  'message': PollWidget,
                  }
