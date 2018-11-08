from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home_page, name='home_page'),
    url(r'^landing/', views.landing_page, name='landing_page'),
    url(r'^features/', views.features_page, name='features_page'),
    url(r'^contact/', views.contact_page, name='contact_page'),
]
