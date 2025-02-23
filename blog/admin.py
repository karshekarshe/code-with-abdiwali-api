from django.contrib import admin
from django.contrib.admin import ModelAdmin
from mptt.admin import MPTTModelAdmin

from blog.models import Category, Article, Tag


class CategoryAdminModel(MPTTModelAdmin):
    list_display = ("name", "parent", "slug", "level")


class ArticleAdminModel(ModelAdmin):
    list_display = (
        "title",
        "slug",
        "category",
        "author",
        "votes",
        "reading_time",
    )

class TagAdminModel(ModelAdmin):
    list_display = ("name", "slug","article")


admin.site.register(Category, CategoryAdminModel)
admin.site.register(Article, ArticleAdminModel)
admin.site.register(Tag, TagAdminModel)
