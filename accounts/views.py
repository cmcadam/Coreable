from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.forms import UserCreationForm, UserChangeForm,  PasswordChangeForm
from accounts.forms import (
    RegistrationForm,
    ChangeTeamForm,
    CreateTeamForm,
    SelectTeamForm,
)
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from accounts.models import UserProfile


# Register page view
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            UserProfile.objects.create(
                user=user,
                # review_team=form.cleaned_data['review_team'],
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
            )
            return redirect('/home')
    else:
        form = RegistrationForm()
        args = {'form': form}
        return render(request, 'accounts/reg_form.html', args)

# Profile page view
def view_profile(request, pk=None):
    if pk:
        user = User.objects.get(pk=pk)
    else:
        user = request.user

    args = {'user': user}
    return render(request, 'accounts/profile.html', args)

# Edit profile page view
def change_team(request):
    if request.method == 'POST':
        form = ChangeTeamForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('/account/profile')

    else:
        form = ChangeTeamForm(instance=request.user)
        args = {'form': form}
        return render(request, 'accounts/edit_profile.html', args)

# Change password page view
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('/account/profile')
        else:
            return redirect('/account/change-password')

    else:
        form = PasswordChangeForm(user=request.user)
        args = {'form': form}
        return render(request, 'accounts/change_password.html', args)

def results(request):
    return render(request, 'accounts/results.html')

def team(request):
    if request.method == 'POST':
        form1 = CreateTeamForm(request.POST)
        form2 = SelectTeamForm(request.POST)
        if form1.is_valid() and form2.is_valid():
            form1.save()
            username = UserProfile.objects.filter(user=request.user).update(review_team=request.POST.get('name'))
        return redirect('/account/team')

    else:
        team_member = UserProfile.objects.get(user=request.user)
        form1 = CreateTeamForm()
        form2 = SelectTeamForm()
        args = {'form1': form1, 'form2': form2, 'team_member': team_member}
        return render(request, 'accounts/team.html', args)
