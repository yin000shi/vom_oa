from django.contrib import admin
from .models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['name', 'birthday', 'gender', 'mobile', 'email', 'post','city']


admin.site.register(UserProfile,UserProfileAdmin)
