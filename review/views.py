from django.shortcuts import render, redirect
from review.forms import ReviewForm
from django.http import HttpResponse

# Create your views here.
def positivity_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/review/relationships')
    else:
        form = ReviewForm()

        args = {'form': form}
        return render(request, 'review/positivity.html', args)

def relationships_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/review/contribution')
    else:
        form = ReviewForm()

        args = {'form': form}
        return render(request, 'review/relationships.html', args)

def contribution_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/review/diplomacy')
    else:
        form = ReviewForm()

        args = {'form': form}
        return render(request, 'review/contribution.html', args)

def diplomacy_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/review/openness')
    else:
        form = ReviewForm()

        args = {'form': form}
        return render(request, 'review/diplomacy.html', args)

def openness_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/review/drive')
    else:
        form = ReviewForm()

        args = {'form': form}
        return render(request, 'review/openness.html', args)

def drive_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/review/tone')
    else:
        form = ReviewForm()

        args = {'form': form}
        return render(request, 'review/drive.html', args)

def tone_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/review/communication')
    else:
        form = ReviewForm()

        args = {'form': form}
        return render(request, 'review/tone.html', args)

def communication_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/review/listening')
    else:
        form = ReviewForm()

        args = {'form': form}
        return render(request, 'review/communication.html', args)

def listening_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/review/idea-sharing')
    else:
        form = ReviewForm()

        args = {'form': form}
        return render(request, 'review/listening.html', args)

def idea_sharing_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/review/delivery')
    else:
        form = ReviewForm()

        args = {'form': form}
        return render(request, 'review/idea_sharing.html', args)

def delivery_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/review/complete')
    else:
        form = ReviewForm()

        args = {'form': form}
        return render(request, 'review/delivery.html', args)

def review_complete(request):
    return render(request, 'review/complete.html')
