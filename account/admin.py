from django.contrib import admin

# Register your models here.
from .models import UserProfile
@admin.register(UserProfile)
class UserProfile(admin.ModelAdmin):
    list_display = ["id","user", "avatar"]