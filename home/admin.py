from django.contrib import admin
from .models import SubscribedUser

class SubscribedUsersAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'created_date')

admin.site.register(SubscribedUser, SubscribedUsersAdmin)
