from django import forms
from django.forms.widgets import NumberInput
from review.models import Team, Review, Feedback

class RangeInput(NumberInput):
    input_type = 'range'

class ReviewForm(forms.Form):
    pk = forms.CharField(
        widget=forms.TextInput(
            attrs={
                 # 'type': 'hidden',
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
        widgets = {
            'question1': forms.Textarea(
                attrs={'placeholder': 'How did you feel completing the questions?'}
            ),
            'question2': forms.Textarea(
                attrs={'placeholder': 'Did you enjoy the experience, what could of been done better?'}
            ),
            'question3': forms.Textarea(
                attrs={'placeholder': 'Did you feel nervous or excited about the appraisal process?'}
            ),
            'question4': forms.Textarea(
                attrs={'placeholder': 'Did the bold words help the experience?'}
            ),
            'question5': forms.Textarea(
                attrs={'placeholder': 'Were there particular bands that you liked more than others?'}
            ),
            'question6': forms.Textarea(
                attrs={'placeholder': 'Did you have problems or disagree with any wording?'}
            ),
            'question7': forms.Textarea(
                attrs={'placeholder': 'How long did it take you?'}
            ),
            'question8': forms.Textarea(
                attrs={'placeholder': 'Is there anything we missed?'}
            ),
        }
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
