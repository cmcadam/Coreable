from django.shortcuts import render, redirect
from review.forms import ReviewForm, FeedbackForm
from django.http import HttpResponse
from django.contrib.auth.models import User
from accounts.models import UserProfile
from review.models import Review, Feedback
from django.forms import formset_factory
from django import forms

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

            return redirect('/review/delivery')
    else:
        ReviewFormSet = formset_factory(ReviewForm, extra=len(users))
        formset = ReviewFormSet()
        UserForms = zip(users, formset)
        args = {'team_members': users, 'formset': formset, 'userforms': UserForms}
        return render(request, 'review/idea_sharing.html', args)

def delivery_review(request):
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
                    trait = 'delivery',
                    trait_score = int(request.POST.get('form-{}-trait_score'.format(i))),
                )
                i += 1

            return redirect('/review/complete')
    else:
        ReviewFormSet = formset_factory(ReviewForm, extra=len(users))
        formset = ReviewFormSet()
        UserForms = zip(users, formset)
        args = {'team_members': users, 'formset': formset, 'userforms': UserForms}
        return render(request, 'review/delivery.html', args)

def review_complete(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/home')
    else:
        form = FeedbackForm()
        args = {'form': form}
        return render(request, 'review/feedback.html', args)
