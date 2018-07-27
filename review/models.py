from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=25, required=False)

    def __str__(self):
        return self.name

class Trait(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name

class Review(models.Model):
    reviewer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviewer_id')
    reviewee = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviewee_id')
    trait = models.ForeignKey(Trait, on_delete=models.CASCADE)
    trait_score = models.IntegerField()
