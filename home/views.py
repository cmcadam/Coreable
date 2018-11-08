from django.shortcuts import render

# Create your views here.
def home_page(request):
    return render(request, 'home/home.html')

def features_page(request):
    return render(request, 'home/features.html')

def contact_page(request):
    return render(request, 'home/contact.html')

def landing_page(request):
    return render(request, 'home/landing.html')
