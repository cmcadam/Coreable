from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.landing_page, name='landing_page'),
    url(r'^login/', views.login_page, name='login_page'),
    url(r'^about/', views.about_page, name='about_page'),
    url(r'^features/', views.features_page, name='features_page'),
    url(r'^contact/', views.contact_page, name='contact_page'),

    # url(r'^$', views.landing_page, name='landing_page'),
    # url(r'^members/', views.home_page, name='home_page'),
    # url(r'^features/', views.features_page, name='features_page'),
    # url(r'^contact/', views.contact_page, name='contact_page'),
]
