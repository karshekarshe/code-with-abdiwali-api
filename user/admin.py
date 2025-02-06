from django.contrib import admin
from django.contrib.admin import ModelAdmin

from user.models import User

class UserAdminModel(ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'password')


admin.site.register(User, UserAdminModel)
