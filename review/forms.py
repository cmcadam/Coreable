from django import forms
from django.forms.widgets import NumberInput
from review.models import Team

class RangeInput(NumberInput):
    input_type = 'range'


class ReviewForm(forms.ModelForm):
    num_of_members = forms.IntegerField(widget=RangeInput, min_value=0, max_value=100, label='')
    # num_of_members.widget.attrs.update(size='100')

    class Meta:
        model = Team
        fields = ('num_of_members',)
