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
    url(r'^review-options/', views.review_options, name='review_options'),

    url(r'^observe/', views.observe_review, name='observe_review'),
    url(r'^analyse/', views.analyse_review, name='analyse_review'),
    url(r'^evalute/', views.evaluate_review, name='evaluate_review'),
    url(r'^question/', views.question_review, name='question_review'),
    url(r'^justify/', views.justify_review, name='justify_review'),
    url(r'^contextualise/', views.contextualise_review, name='contextualise_review'),
    url(r'^innovative/', views.innovative_review, name='innovative_review'),
    url(r'^connectivity/', views.connectvity_review, name='connectivity_review'),
    url(r'^problem-solving-openness/', views.problem_solving_openness_review, name='problem_solving_opennes_review'),
    url(r'^question-making/', views.question_making_review, name='quesiton_making_review'),
    url(r'^complexity/', views.complexity_review, name='complexity_review'),
    url(r'^knowledge/', views.knowledge_review, name='knowledge_review'),
]
