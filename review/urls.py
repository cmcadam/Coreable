from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^positivity/', views.positivity_review, name='positivity_review'),
    url(r'^relationships/', views.relationships_review, name='relationships_review'),
    url(r'^contribution/', views.contribution_review, name='contribution_review'),
    url(r'^diplomacy/', views.diplomacy_review, name='diplomacy_review'),
    url(r'^openness/', views.openness_review, name='openness_review'),
    url(r'^drive/', views.drive_review, name='drive_review'),
    url(r'^tone/', views.tone_review, name='tone_review'),
    url(r'^communication/', views.communication_review, name='communication_review'),
    url(r'^listening/', views.listening_review, name='listening_review'),
    url(r'^idea-sharing/', views.idea_sharing_review, name='idea_sharing_review'),
    url(r'^delivery/', views.delivery_review, name='delivery_review'),
    url(r'^complete/', views.review_complete, name='review_complete'),
]
