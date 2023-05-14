from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

# Register your models here.
class CustomUserAdmin(UserAdmin):
    list_display=('username', 'email', 'first_name', 'last_name', 'mobile_no', 'address')

# admin.site.register(User,CustomUserAdmin)