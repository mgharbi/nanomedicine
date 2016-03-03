from django.contrib import admin
from django.core.exceptions import ValidationError
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth.models import User
from django import forms
from models import (
    Event,
    News,
    Publication,
    UserProfile,
)

class EventAdmin(admin.ModelAdmin):
    pass

# Define an inline admin descriptor for Profile model
# which acts a bit like a singleton
class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'profiles'

# Define a new User admin
class NanoUserAdmin(UserAdmin):
    inlines = UserProfileInline,


# Register your models here.
admin.site.unregister(User)
admin.site.register(User, NanoUserAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(News)
admin.site.register(Publication)
