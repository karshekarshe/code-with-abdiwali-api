from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from blog.models import Category


class CategoryAdminModel(MPTTModelAdmin):
    list_display = ('name', 'parent',"slug", "level")


admin.site.register(Category, CategoryAdminModel)
