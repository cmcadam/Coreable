from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from review.models import Team, Organisation

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    organisation = models.ForeignKey(Organisation, on_delete=models.CASCADE, blank=True, null=True)
    review_team = models.ForeignKey(Team, on_delete=models.CASCADE, blank=True, null=True)
    first_name = models.CharField(max_length=25, blank=True, null=True)
    last_name = models.CharField(max_length=25, blank=True, null=True)

    def __str__(self):
        return self.user.username

# def create_profile(sender, **kwargs):
#     if kwargs['created']:
#         user_profile = UserProfile.objects.create(user=kwargs['instance'])
#
# post_save.connect(create_profile, sender=User)

#HELLO
