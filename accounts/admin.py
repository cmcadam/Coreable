from django.contrib import admin
from accounts.models import UserProfile

# Register your models here.
# admin.site.register(Team)
# admin.site.unregister(Team)
admin.site.register(UserProfile)

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user',)

    def user_info(self, obj):
        return obj.description

    def get_queryset(self, request):
        queryset = super(UserProfileAdmin, self).get_queryset(request)
        queryset = queryset.order_by('user')
        return queryset

    user_info.short_description = 'Info'

admin.site.unregister(UserProfile)
admin.site.register(UserProfile, UserProfileAdmin)
