from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from accounts.forms import RegistrationForm
from accounts.models import UserProfile

# Create your views here.
def login_page(request):
    if request.method == 'POST':
        registration_form = RegistrationForm(request.POST, prefix='register')
        authentication_form = AuthenticationForm(request.POST, prefix='authenticate')
        if 'register-username' in request.POST:
            if registration_form.is_valid():
                user = registration_form.save()
                UserProfile.objects.create(
                    user=user,
                    first_name=registration_form.cleaned_data['first_name'],
                    last_name=registration_form.cleaned_data['last_name'],
                    )
                return redirect('/home')
        elif 'authenticate-username' in request.POST:
            username = request.POST['authenticate-username']
            password = request.POST['authenticate-password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('/account/profile')
            else:
                return redirect('/home')
    else:
        register_form = RegistrationForm(prefix='register')
        authentication_form = AuthenticationForm(prefix='authenticate')
        args = {'register_form': register_form, 'authentication_form': authentication_form}
        return render(request, 'home/login-or-signup.html', args)

def features_page(request):
    return render(request, 'home/features.html')

def contact_page(request):
    return render(request, 'home/contact.html')

def landing_page(request):
    return render(request, 'home/landing.html')
