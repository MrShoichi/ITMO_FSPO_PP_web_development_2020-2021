from django.contrib import admin
from blog.models import *
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .forms import UserCreationForm, UserChangeForm


class CustomUserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = CarOwner


admin.site.register(CarOwner, CustomUserAdmin)
admin.site.register(DriverLicense)
admin.site.register(Car)
admin.site.register(Ownership)
