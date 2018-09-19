from django.contrib import admin
from review.models import Team, Trait, Review, Organisation, Feedback

# Register your models here.
admin.site.register(Team)

admin.site.register(Organisation)

admin.site.register(Trait)

admin.site.register(Review)

admin.site.register(Feedback)
