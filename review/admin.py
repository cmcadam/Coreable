from django.contrib import admin
from review.models import Team, Trait, Review

# Register your models here.
admin.site.register(Team)

admin.site.register(Trait)

admin.site.register(Review)
