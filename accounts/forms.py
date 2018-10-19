from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from review.models import Team
from accounts.models import UserProfile

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    # review_team = forms.ModelChoiceField(queryset=Team.objects.all())

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        )

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user

class ChangeTeamForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields  = (
            'review_team',
            )

class CreateTeamForm(forms.ModelForm):

    class Meta:
        model = Team
        fields = (
            'name',
        )

    def save(self, commit=True):
        team = super(CreateTeamForm, self).save(commit=False)
        team.name = self.cleaned_data['name']

        if commit:
            team.save()

        return team

class SelectTeamForm(forms.ModelForm):
    review_team = forms.ModelChoiceField(queryset=Team.objects.all())

    class Meta:
        model = UserProfile
        fields = (
            'review_team',
        )

    def save(self, commit=True):
        user = super(SelectTeamForm, self).save(commit=False)
        user.review_team = self.cleaned_data['review_team']

        if commit:
            user.save()

        return user
