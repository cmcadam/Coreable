from django import forms
from django.forms.widgets import NumberInput
from review.models import Team, Review, Feedback

class RangeInput(NumberInput):
    input_type = 'range'

class ReviewForm(forms.Form):
    pk = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'type': 'hidden',
            }
        ),
        label=''
    )
    trait_score = forms.IntegerField(
        widget=RangeInput(attrs={'value': '0'}),
        label='',
    )

class FeedbackForm(forms.ModelForm):

    class Meta:
        model = Feedback
        exclude = (
            'user',
        )

    def save(self, commit=True):
        feedback = super(FeedbackForm, self).save(commit=False)
        feedback.question1 = self.cleaned_data['question1']
        feedback.question2 = self.cleaned_data['question2']
        feedback.question3 = self.cleaned_data['question3']
        feedback.question4 = self.cleaned_data['question4']
        feedback.question5 = self.cleaned_data['question5']
        feedback.question6 = self.cleaned_data['question6']
        feedback.question7 = self.cleaned_data['question7']
        feedback.question8 = self.cleaned_data['question8']

        if commit:
            feedback.save()

        return feedback
