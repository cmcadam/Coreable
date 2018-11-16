import random
from django.shortcuts import render, redirect
from review.forms import ReviewForm, FeedbackForm
from django.http import HttpResponse
from django.contrib.auth.models import User
from accounts.models import UserProfile
from review.models import Review, Feedback
from django.forms import formset_factory
from django import forms

##################
#TEAMWORK REVIEWS#
##################

def positivity_review(request):
    users = UserProfile.objects.filter(review_team=request.user.userprofile.review_team)
    if request.method == 'POST':
        ReviewFormSet = formset_factory(ReviewForm, extra=len(users))
        formset = ReviewFormSet(request.POST)
        if formset.is_valid():
            i = 0
            while i < len(users):
                Review.objects.create(
                    reviewer = request.user,
                    reviewee = User.objects.get(pk=int(request.POST.get('form-{}-pk'.format(i)))),
                    trait = 'positivity',
                    trait_score = int(request.POST.get('form-{}-trait_score'.format(i))),
                )
                i += 1

            return redirect('/review/relationships')
    else:
        ReviewFormSet = formset_factory(ReviewForm, extra=len(users))
        formset = ReviewFormSet()
        UserForms = zip(users, formset)
        args = {'team_members': users, 'formset': formset, 'userforms': UserForms}
        return render(request, 'review/positivity.html', args)

def relationships_review(request):
    users = UserProfile.objects.filter(review_team=request.user.userprofile.review_team)
    if request.method == 'POST':
        ReviewFormSet = formset_factory(ReviewForm, extra=len(users))
        formset = ReviewFormSet(request.POST)
        if formset.is_valid():
            i = 0
            while i < len(users):
                Review.objects.create(
                    reviewer = request.user,
                    reviewee = User.objects.get(pk=int(request.POST.get('form-{}-pk'.format(i)))),
                    trait = 'relationships',
                    trait_score = int(request.POST.get('form-{}-trait_score'.format(i))),
                )
                i += 1

            return redirect('/review/contribution')
    else:
        ReviewFormSet = formset_factory(ReviewForm, extra=len(users))
        formset = ReviewFormSet()
        UserForms = zip(users, formset)
        args = {'team_members': users, 'formset': formset, 'userforms': UserForms}
        return render(request, 'review/relationships.html', args)

def contribution_review(request):
    users = UserProfile.objects.filter(review_team=request.user.userprofile.review_team)
    if request.method == 'POST':
        ReviewFormSet = formset_factory(ReviewForm, extra=len(users))
        formset = ReviewFormSet(request.POST)
        if formset.is_valid():
            i = 0
            while i < len(users):
                Review.objects.create(
                    reviewer = request.user,
                    reviewee = User.objects.get(pk=int(request.POST.get('form-{}-pk'.format(i)))),
                    trait = 'contribution',
                    trait_score = int(request.POST.get('form-{}-trait_score'.format(i))),
                )
                i += 1

            return redirect('/review/diplomacy')
    else:
        ReviewFormSet = formset_factory(ReviewForm, extra=len(users))
        formset = ReviewFormSet()
        UserForms = zip(users, formset)
        args = {'team_members': users, 'formset': formset, 'userforms': UserForms}
        return render(request, 'review/contribution.html', args)

def diplomacy_review(request):
    users = UserProfile.objects.filter(review_team=request.user.userprofile.review_team)
    if request.method == 'POST':
        ReviewFormSet = formset_factory(ReviewForm, extra=len(users))
        formset = ReviewFormSet(request.POST)
        if formset.is_valid():
            i = 0
            while i < len(users):
                Review.objects.create(
                    reviewer = request.user,
                    reviewee = User.objects.get(pk=int(request.POST.get('form-{}-pk'.format(i)))),
                    trait = 'diplomacy',
                    trait_score = int(request.POST.get('form-{}-trait_score'.format(i))),
                )
                i += 1

            return redirect('/review/openness')
    else:
        ReviewFormSet = formset_factory(ReviewForm, extra=len(users))
        formset = ReviewFormSet()
        UserForms = zip(users, formset)
        args = {'team_members': users, 'formset': formset, 'userforms': UserForms}
        return render(request, 'review/diplomacy.html', args)

def openness_review(request):
    users = UserProfile.objects.filter(review_team=request.user.userprofile.review_team)
    if request.method == 'POST':
        ReviewFormSet = formset_factory(ReviewForm, extra=len(users))
        formset = ReviewFormSet(request.POST)
        if formset.is_valid():
            i = 0
            while i < len(users):
                Review.objects.create(
                    reviewer = request.user,
                    reviewee = User.objects.get(pk=int(request.POST.get('form-{}-pk'.format(i)))),
                    trait = 'openness',
                    trait_score = int(request.POST.get('form-{}-trait_score'.format(i))),
                )
                i += 1

            return redirect('/review/drive')
    else:
        ReviewFormSet = formset_factory(ReviewForm, extra=len(users))
        formset = ReviewFormSet()
        UserForms = zip(users, formset)
        args = {'team_members': users, 'formset': formset, 'userforms': UserForms}
        return render(request, 'review/openness.html', args)

def drive_review(request):
    users = UserProfile.objects.filter(review_team=request.user.userprofile.review_team)
    if request.method == 'POST':
        ReviewFormSet = formset_factory(ReviewForm, extra=len(users))
        formset = ReviewFormSet(request.POST)
        if formset.is_valid():
            i = 0
            while i < len(users):
                Review.objects.create(
                    reviewer = request.user,
                    reviewee = User.objects.get(pk=int(request.POST.get('form-{}-pk'.format(i)))),
                    trait = 'drive',
                    trait_score = int(request.POST.get('form-{}-trait_score'.format(i))),
                )
                i += 1

            return redirect('/review/tone')
    else:
        ReviewFormSet = formset_factory(ReviewForm, extra=len(users))
        formset = ReviewFormSet()
        UserForms = zip(users, formset)
        args = {'team_members': users, 'formset': formset, 'userforms': UserForms}
        return render(request, 'review/drive.html', args)

def tone_review(request):
    users = UserProfile.objects.filter(review_team=request.user.userprofile.review_team)
    if request.method == 'POST':
        ReviewFormSet = formset_factory(ReviewForm, extra=len(users))
        formset = ReviewFormSet(request.POST)
        if formset.is_valid():
            i = 0
            while i < len(users):
                Review.objects.create(
                    reviewer = request.user,
                    reviewee = User.objects.get(pk=int(request.POST.get('form-{}-pk'.format(i)))),
                    trait = 'tone',
                    trait_score = int(request.POST.get('form-{}-trait_score'.format(i))),
                )
                i += 1

            return redirect('/review/communication')
    else:
        ReviewFormSet = formset_factory(ReviewForm, extra=len(users))
        formset = ReviewFormSet()
        UserForms = zip(users, formset)
        args = {'team_members': users, 'formset': formset, 'userforms': UserForms}
        return render(request, 'review/tone.html', args)

def communication_review(request):
    users = UserProfile.objects.filter(review_team=request.user.userprofile.review_team)
    if request.method == 'POST':
        ReviewFormSet = formset_factory(ReviewForm, extra=len(users))
        formset = ReviewFormSet(request.POST)
        if formset.is_valid():
            i = 0
            while i < len(users):
                Review.objects.create(
                    reviewer = request.user,
                    reviewee = User.objects.get(pk=int(request.POST.get('form-{}-pk'.format(i)))),
                    trait = 'communication',
                    trait_score = int(request.POST.get('form-{}-trait_score'.format(i))),
                )
                i += 1

            return redirect('/review/listening')
    else:
        ReviewFormSet = formset_factory(ReviewForm, extra=len(users))
        formset = ReviewFormSet()
        UserForms = zip(users, formset)
        args = {'team_members': users, 'formset': formset, 'userforms': UserForms}
        return render(request, 'review/communication.html', args)

def listening_review(request):
    users = UserProfile.objects.filter(review_team=request.user.userprofile.review_team)
    if request.method == 'POST':
        ReviewFormSet = formset_factory(ReviewForm, extra=len(users))
        formset = ReviewFormSet(request.POST)
        if formset.is_valid():
            i = 0
            while i < len(users):
                Review.objects.create(
                    reviewer = request.user,
                    reviewee = User.objects.get(pk=int(request.POST.get('form-{}-pk'.format(i)))),
                    trait = 'listening',
                    trait_score = int(request.POST.get('form-{}-trait_score'.format(i))),
                )
                i += 1

            return redirect('/review/idea-sharing')
    else:
        ReviewFormSet = formset_factory(ReviewForm, extra=len(users))
        formset = ReviewFormSet()
        UserForms = zip(users, formset)
        args = {'team_members': users, 'formset': formset, 'userforms': UserForms}
        return render(request, 'review/listening.html', args)

def idea_sharing_review(request):
    users = UserProfile.objects.filter(review_team=request.user.userprofile.review_team)
    if request.method == 'POST':
        ReviewFormSet = formset_factory(ReviewForm, extra=len(users))
        formset = ReviewFormSet(request.POST)
        if formset.is_valid():
            i = 0
            while i < len(users):
                Review.objects.create(
                    reviewer = request.user,
                    reviewee = User.objects.get(pk=int(request.POST.get('form-{}-pk'.format(i)))),
                    trait = 'idea sharing',
                    trait_score = int(request.POST.get('form-{}-trait_score'.format(i))),
                )
                i += 1

            return redirect('/review/feedback')
    else:
        ReviewFormSet = formset_factory(ReviewForm, extra=len(users))
        formset = ReviewFormSet()
        UserForms = zip(users, formset)
        args = {'team_members': users, 'formset': formset, 'userforms': UserForms}
        return render(request, 'review/idea_sharing.html', args)

# def delivery_review(request):
#     users = UserProfile.objects.filter(review_team=request.user.userprofile.review_team)
#     if request.method == 'POST':
#         ReviewFormSet = formset_factory(ReviewForm, extra=len(users))
#         formset = ReviewFormSet(request.POST)
#         if formset.is_valid():
#             i = 0
#             while i < len(users):
#                 Review.objects.create(
#                     reviewer = request.user,
#                     reviewee = User.objects.get(pk=int(request.POST.get('form-{}-pk'.format(i)))),
#                     trait = 'delivery',
#                     trait_score = int(request.POST.get('form-{}-trait_score'.format(i))),
#                 )
#                 i += 1
#
#             return redirect('/review/complete')
#     else:
#         ReviewFormSet = formset_factory(ReviewForm, extra=len(users))
#         formset = ReviewFormSet()
#         UserForms = zip(users, formset)
#         args = {'team_members': users, 'formset': formset, 'userforms': UserForms}
#         return render(request, 'review/delivery.html', args)

def feedback(request):
    users = UserProfile.objects.filter(review_team=request.user.userprofile.review_team)
    traits = [
        'emotional intelligence',
        'moral trust',
        'resilience',
        'flexibility',
        'initiative',
        'empowering others',
        'clarity',
        'culture',
        'non verbal conversation',
        'verbal attention',
    ]
    random_user = random.choice(users)
    random_trait = random.choice(traits)
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/home')
    else:
        form = FeedbackForm()
        args = {'form': form, 'random_user': random_user, 'random_trait': random_trait}
        return render(request, 'review/feedback.html', args)

def review_options(request):
    return render(request, 'review/review_options.html')

#########################
#PROBLEM SOLVING REVIEWS#
#########################
def observe_review(request):
    users = UserProfile.objects.filter(review_team=request.user.userprofile.review_team)
    if request.method == 'POST':
        ReviewFormSet = formset_factory(ReviewForm, extra=len(users))
        formset = ReviewFormSet(request.POST)
        if formset.is_valid():
            i = 0
            while i < len(users):
                Review.objects.create(
                    reviewer = request.user,
                    reviewee = User.objects.get(pk=int(request.POST.get('form-{}-pk'.format(i)))),
                    trait = 'observe',
                    trait_score = int(request.POST.get('form-{}-trait_score'.format(i))),
                )
                i += 1

            return redirect('/review/analyse')
    else:
        ReviewFormSet = formset_factory(ReviewForm, extra=len(users))
        formset = ReviewFormSet()
        UserForms = zip(users, formset)
        args = {'team_members': users, 'formset': formset, 'userforms': UserForms}
        return render(request, 'review/observe2.html', args)

def analyse_review(request):
    users = UserProfile.objects.filter(review_team=request.user.userprofile.review_team)
    if request.method == 'POST':
        ReviewFormSet = formset_factory(ReviewForm, extra=len(users))
        formset = ReviewFormSet(request.POST)
        if formset.is_valid():
            i = 0
            while i < len(users):
                Review.objects.create(
                    reviewer = request.user,
                    reviewee = User.objects.get(pk=int(request.POST.get('form-{}-pk'.format(i)))),
                    trait = 'analyse',
                    trait_score = int(request.POST.get('form-{}-trait_score'.format(i))),
                )
                i += 1

            return redirect('/review/evaluate')
    else:
        ReviewFormSet = formset_factory(ReviewForm, extra=len(users))
        formset = ReviewFormSet()
        UserForms = zip(users, formset)
        args = {'team_members': users, 'formset': formset, 'userforms': UserForms}
        return render(request, 'review/analyse2.html', args)

def evaluate_review(request):
    users = UserProfile.objects.filter(review_team=request.user.userprofile.review_team)
    if request.method == 'POST':
        ReviewFormSet = formset_factory(ReviewForm, extra=len(users))
        formset = ReviewFormSet(request.POST)
        if formset.is_valid():
            i = 0
            while i < len(users):
                Review.objects.create(
                    reviewer = request.user,
                    reviewee = User.objects.get(pk=int(request.POST.get('form-{}-pk'.format(i)))),
                    trait = 'evaluate',
                    trait_score = int(request.POST.get('form-{}-trait_score'.format(i))),
                )
                i += 1

            return redirect('/review/question')
    else:
        ReviewFormSet = formset_factory(ReviewForm, extra=len(users))
        formset = ReviewFormSet()
        UserForms = zip(users, formset)
        args = {'team_members': users, 'formset': formset, 'userforms': UserForms}
        return render(request, 'review/evaluate2.html', args)

def question_review(request):
    users = UserProfile.objects.filter(review_team=request.user.userprofile.review_team)
    if request.method == 'POST':
        ReviewFormSet = formset_factory(ReviewForm, extra=len(users))
        formset = ReviewFormSet(request.POST)
        if formset.is_valid():
            i = 0
            while i < len(users):
                Review.objects.create(
                    reviewer = request.user,
                    reviewee = User.objects.get(pk=int(request.POST.get('form-{}-pk'.format(i)))),
                    trait = 'question',
                    trait_score = int(request.POST.get('form-{}-trait_score'.format(i))),
                )
                i += 1

            return redirect('/review/justify')
    else:
        ReviewFormSet = formset_factory(ReviewForm, extra=len(users))
        formset = ReviewFormSet()
        UserForms = zip(users, formset)
        args = {'team_members': users, 'formset': formset, 'userforms': UserForms}
        return render(request, 'review/question2.html', args)

def justify_review(request):
    users = UserProfile.objects.filter(review_team=request.user.userprofile.review_team)
    if request.method == 'POST':
        ReviewFormSet = formset_factory(ReviewForm, extra=len(users))
        formset = ReviewFormSet(request.POST)
        if formset.is_valid():
            i = 0
            while i < len(users):
                Review.objects.create(
                    reviewer = request.user,
                    reviewee = User.objects.get(pk=int(request.POST.get('form-{}-pk'.format(i)))),
                    trait = 'justify',
                    trait_score = int(request.POST.get('form-{}-trait_score'.format(i))),
                )
                i += 1

            return redirect('/review/contextualise')
    else:
        ReviewFormSet = formset_factory(ReviewForm, extra=len(users))
        formset = ReviewFormSet()
        UserForms = zip(users, formset)
        args = {'team_members': users, 'formset': formset, 'userforms': UserForms}
        return render(request, 'review/justify2.html', args)

def contextualise_review(request):
    users = UserProfile.objects.filter(review_team=request.user.userprofile.review_team)
    if request.method == 'POST':
        ReviewFormSet = formset_factory(ReviewForm, extra=len(users))
        formset = ReviewFormSet(request.POST)
        if formset.is_valid():
            i = 0
            while i < len(users):
                Review.objects.create(
                    reviewer = request.user,
                    reviewee = User.objects.get(pk=int(request.POST.get('form-{}-pk'.format(i)))),
                    trait = 'contextualise',
                    trait_score = int(request.POST.get('form-{}-trait_score'.format(i))),
                )
                i += 1

            return redirect('/review/innovative')
    else:
        ReviewFormSet = formset_factory(ReviewForm, extra=len(users))
        formset = ReviewFormSet()
        UserForms = zip(users, formset)
        args = {'team_members': users, 'formset': formset, 'userforms': UserForms}
        return render(request, 'review/contextualise2.html', args)

def innovative_review(request):
    users = UserProfile.objects.filter(review_team=request.user.userprofile.review_team)
    if request.method == 'POST':
        ReviewFormSet = formset_factory(ReviewForm, extra=len(users))
        formset = ReviewFormSet(request.POST)
        if formset.is_valid():
            i = 0
            while i < len(users):
                Review.objects.create(
                    reviewer = request.user,
                    reviewee = User.objects.get(pk=int(request.POST.get('form-{}-pk'.format(i)))),
                    trait = 'innovative',
                    trait_score = int(request.POST.get('form-{}-trait_score'.format(i))),
                )
                i += 1

            return redirect('/review/connectivity')
    else:
        ReviewFormSet = formset_factory(ReviewForm, extra=len(users))
        formset = ReviewFormSet()
        UserForms = zip(users, formset)
        args = {'team_members': users, 'formset': formset, 'userforms': UserForms}
        return render(request, 'review/innovative2.html', args)

def connectivity_review(request):
    users = UserProfile.objects.filter(review_team=request.user.userprofile.review_team)
    if request.method == 'POST':
        ReviewFormSet = formset_factory(ReviewForm, extra=len(users))
        formset = ReviewFormSet(request.POST)
        if formset.is_valid():
            i = 0
            while i < len(users):
                Review.objects.create(
                    reviewer = request.user,
                    reviewee = User.objects.get(pk=int(request.POST.get('form-{}-pk'.format(i)))),
                    trait = 'connectivity',
                    trait_score = int(request.POST.get('form-{}-trait_score'.format(i))),
                )
                i += 1

            return redirect('/review/problem-solving-openness')
    else:
        ReviewFormSet = formset_factory(ReviewForm, extra=len(users))
        formset = ReviewFormSet()
        UserForms = zip(users, formset)
        args = {'team_members': users, 'formset': formset, 'userforms': UserForms}
        return render(request, 'review/connectivity2.html', args)

def problem_solving_openness_review(request):
    users = UserProfile.objects.filter(review_team=request.user.userprofile.review_team)
    if request.method == 'POST':
        ReviewFormSet = formset_factory(ReviewForm, extra=len(users))
        formset = ReviewFormSet(request.POST)
        if formset.is_valid():
            i = 0
            while i < len(users):
                Review.objects.create(
                    reviewer = request.user,
                    reviewee = User.objects.get(pk=int(request.POST.get('form-{}-pk'.format(i)))),
                    trait = 'problem solving openness',
                    trait_score = int(request.POST.get('form-{}-trait_score'.format(i))),
                )
                i += 1

            return redirect('/review/question-making')
    else:
        ReviewFormSet = formset_factory(ReviewForm, extra=len(users))
        formset = ReviewFormSet()
        UserForms = zip(users, formset)
        args = {'team_members': users, 'formset': formset, 'userforms': UserForms}
        return render(request, 'review/openness2.html', args)

def question_making_review(request):
    users = UserProfile.objects.filter(review_team=request.user.userprofile.review_team)
    if request.method == 'POST':
        ReviewFormSet = formset_factory(ReviewForm, extra=len(users))
        formset = ReviewFormSet(request.POST)
        if formset.is_valid():
            i = 0
            while i < len(users):
                Review.objects.create(
                    reviewer = request.user,
                    reviewee = User.objects.get(pk=int(request.POST.get('form-{}-pk'.format(i)))),
                    trait = 'question making',
                    trait_score = int(request.POST.get('form-{}-trait_score'.format(i))),
                )
                i += 1

            return redirect('/review/complexity')
    else:
        ReviewFormSet = formset_factory(ReviewForm, extra=len(users))
        formset = ReviewFormSet()
        UserForms = zip(users, formset)
        args = {'team_members': users, 'formset': formset, 'userforms': UserForms}
        return render(request, 'review/question_making2.html', args)

def complexity_review(request):
    users = UserProfile.objects.filter(review_team=request.user.userprofile.review_team)
    if request.method == 'POST':
        ReviewFormSet = formset_factory(ReviewForm, extra=len(users))
        formset = ReviewFormSet(request.POST)
        if formset.is_valid():
            i = 0
            while i < len(users):
                Review.objects.create(
                    reviewer = request.user,
                    reviewee = User.objects.get(pk=int(request.POST.get('form-{}-pk'.format(i)))),
                    trait = 'complexity',
                    trait_score = int(request.POST.get('form-{}-trait_score'.format(i))),
                )
                i += 1

            return redirect('/review/knowledge')
    else:
        ReviewFormSet = formset_factory(ReviewForm, extra=len(users))
        formset = ReviewFormSet()
        UserForms = zip(users, formset)
        args = {'team_members': users, 'formset': formset, 'userforms': UserForms}
        return render(request, 'review/complexity2.html', args)

def knowledge_review(request):
    users = UserProfile.objects.filter(review_team=request.user.userprofile.review_team)
    if request.method == 'POST':
        ReviewFormSet = formset_factory(ReviewForm, extra=len(users))
        formset = ReviewFormSet(request.POST)
        if formset.is_valid():
            i = 0
            while i < len(users):
                Review.objects.create(
                    reviewer = request.user,
                    reviewee = User.objects.get(pk=int(request.POST.get('form-{}-pk'.format(i)))),
                    trait = 'knowledge',
                    trait_score = int(request.POST.get('form-{}-trait_score'.format(i))),
                )
                i += 1

            return redirect('/review/complete')
    else:
        ReviewFormSet = formset_factory(ReviewForm, extra=len(users))
        formset = ReviewFormSet()
        UserForms = zip(users, formset)
        args = {'team_members': users, 'formset': formset, 'userforms': UserForms}
        return render(request, 'review/knowledge2.html', args)
