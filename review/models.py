from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Organisation(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Team(models.Model):
    organisation = models.ForeignKey(Organisation, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name


class Trait(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name

class Review(models.Model):
    reviewer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviewer_id')
    reviewee = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviewee_id')
    trait = models.CharField(max_length=20)
    trait_score = models.IntegerField()

class Feedback(models.Model):
    question1 = models.TextField()
    question2 = models.TextField()
    question3 = models.TextField()
    question4 = models.TextField()
    question5 = models.TextField()
    question6 = models.TextField()
    question7 = models.TextField()
    question8 = models.TextField()
