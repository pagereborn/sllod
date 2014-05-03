from django import forms
from django.forms.widgets import Widget, Textarea
from django.utils.html import mark_safe
class PollWidget(forms.widgets.Textarea):
    def render(self, name, value, attrs=None):
        html = super(PollWidget, self).render(name, value, attrs)
        print(html)
        return mark_safe(html);