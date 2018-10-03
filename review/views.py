from django.shortcuts import render, redirect
from review.forms import ReviewForm, FeedbackForm
from django.http import HttpResponse
from django.contrib.auth.models import User
from accounts.models import UserProfile
from review.models import Review, Feedback

def positivity_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            # print(request.POST)
            reviewee_id = request.POST.get('pk')
            trait_score = request.POST.get('trait_score')
            reviewee = User.objects.get(pk=reviewee_id)
            Review.objects.create(
                 reviewer = request.user,
                 reviewee = reviewee,
                 trait = 'positivity',
                 trait_score = trait_score,
            )
            return redirect('/review/positivity')
    else:
        form = ReviewForm()
        users = UserProfile.objects.filter(review_team=request.user.userprofile.review_team)
        # args = {'form': form, 'team_members': users}
        args = {'team_members': users}
        for x in range(len(users)):
            name = 'form' + str(x + 1)
            args[name] = form

        # print(args)

        # return render(request, 'review/positivity.html', args)
        return render(request, 'review/test.html', args)

def relationships_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            reviewee_id = request.POST.get('pk')
            trait_score = request.POST.get('trait_score')
            reviewee = User.objects.get(pk=reviewee_id)
            Review.objects.create(
                 reviewer = request.user,
                 reviewee = reviewee,
                 trait = 'relationships',
                 trait_score = trait_score,
            )
            return redirect('/review/relationships')
    else:
        form = ReviewForm()
        users = UserProfile.objects.filter(review_team=request.user.userprofile.review_team)
        args = {'form': form, 'team_members': users}
        return render(request, 'review/relationships.html', args)

def contribution_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            reviewee_id = request.POST.get('pk')
            trait_score = request.POST.get('trait_score')
            reviewee = User.objects.get(pk=reviewee_id)
            Review.objects.create(
                 reviewer = request.user,
                 reviewee = reviewee,
                 trait = 'contribution',
                 trait_score = trait_score,
            )
            return redirect('/review/contribution')
    else:
        form = ReviewForm()
        users = UserProfile.objects.filter(review_team=request.user.userprofile.review_team)
        args = {'form': form, 'team_members': users}
        return render(request, 'review/contribution.html', args)

def diplomacy_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            reviewee_id = request.POST.get('pk')
            trait_score = request.POST.get('trait_score')
            reviewee = User.objects.get(pk=reviewee_id)
            Review.objects.create(
                 reviewer = request.user,
                 reviewee = reviewee,
                 trait = 'diplomacy',
                 trait_score = trait_score,
            )
            return redirect('/review/diplomacy')
    else:
        form = ReviewForm()
        users = UserProfile.objects.filter(review_team=request.user.userprofile.review_team)
        args = {'form': form, 'team_members': users}
        return render(request, 'review/diplomacy.html', args)

def openness_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            reviewee_id = request.POST.get('pk')
            trait_score = request.POST.get('trait_score')
            reviewee = User.objects.get(pk=reviewee_id)
            Review.objects.create(
                 reviewer = request.user,
                 reviewee = reviewee,
                 trait = 'openness',
                 trait_score = trait_score,
            )
            return redirect('/review/openness')
    else:
        form = ReviewForm()
        users = UserProfile.objects.filter(review_team=request.user.userprofile.review_team)
        args = {'form': form, 'team_members': users}
        return render(request, 'review/openness.html', args)

def drive_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            reviewee_id = request.POST.get('pk')
            trait_score = request.POST.get('trait_score')
            reviewee = User.objects.get(pk=reviewee_id)
            Review.objects.create(
                 reviewer = request.user,
                 reviewee = reviewee,
                 trait = 'drive',
                 trait_score = trait_score,
            )
            return redirect('/review/drive')
    else:
        form = ReviewForm()
        users = UserProfile.objects.filter(review_team=request.user.userprofile.review_team)
        args = {'form': form, 'team_members': users}
        return render(request, 'review/drive.html', args)

def tone_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            reviewee_id = request.POST.get('pk')
            trait_score = request.POST.get('trait_score')
            reviewee = User.objects.get(pk=reviewee_id)
            Review.objects.create(
                 reviewer = request.user,
                 reviewee = reviewee,
                 trait = 'tone',
                 trait_score = trait_score,
            )
            return redirect('/review/tone')
    else:
        form = ReviewForm()
        users = UserProfile.objects.filter(review_team=request.user.userprofile.review_team)
        args = {'form': form, 'team_members': users}
        return render(request, 'review/tone.html', args)

def communication_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            reviewee_id = request.POST.get('pk')
            trait_score = request.POST.get('trait_score')
            reviewee = User.objects.get(pk=reviewee_id)
            Review.objects.create(
                 reviewer = request.user,
                 reviewee = reviewee,
                 trait = 'communication',
                 trait_score = trait_score,
            )
            return redirect('/review/communication')
    else:
        form = ReviewForm()
        users = UserProfile.objects.filter(review_team=request.user.userprofile.review_team)
        args = {'form': form, 'team_members': users}
        return render(request, 'review/communication.html', args)

def listening_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            reviewee_id = request.POST.get('pk')
            trait_score = request.POST.get('trait_score')
            reviewee = User.objects.get(pk=reviewee_id)
            Review.objects.create(
                 reviewer = request.user,
                 reviewee = reviewee,
                 trait = 'listening',
                 trait_score = trait_score,
            )
            return redirect('/review/listening')
    else:
        form = ReviewForm()
        users = UserProfile.objects.filter(review_team=request.user.userprofile.review_team)
        args = {'form': form, 'team_members': users}
        return render(request, 'review/listening.html', args)

def idea_sharing_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            reviewee_id = request.POST.get('pk')
            trait_score = request.POST.get('trait_score')
            reviewee = User.objects.get(pk=reviewee_id)
            Review.objects.create(
                 reviewer = request.user,
                 reviewee = reviewee,
                 trait = 'idea sharing',
                 trait_score = trait_score,
            )
            return redirect('/review/idea-sharing')
    else:
        form = ReviewForm()
        users = UserProfile.objects.filter(review_team=request.user.userprofile.review_team)
        args = {'form': form, 'team_members': users}
        return render(request, 'review/idea_sharing.html', args)

def delivery_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            reviewee_id = request.POST.get('pk')
            trait_score = request.POST.get('trait_score')
            reviewee = User.objects.get(pk=reviewee_id)
            Review.objects.create(
                 reviewer = request.user,
                 reviewee = reviewee,
                 trait = 'delivery',
                 trait_score = trait_score,
            )
            return redirect('/review/delivery')
    else:
        form = ReviewForm()
        users = UserProfile.objects.filter(review_team=request.user.userprofile.review_team)
        args = {'form': form, 'team_members': users}
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
