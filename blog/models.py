import uuid

from django.db import models
from django.utils.text import slugify
from mptt.models import MPTTModel, TreeForeignKey


class Category(MPTTModel):
    """Category model which represents a category for article"""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True, null=True, blank=True)
    parent = TreeForeignKey(
        "self", null=True, blank=True, related_name="children", on_delete=models.PROTECT
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"<Category name: {self.name}, parent: {self.parent.name})"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)

        return super().save(*args, **kwargs)


class Article(models.Model):
    """Blog's article model"""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255, unique=True)
    content = models.TextField()
    slug = models.SlugField(max_length=255, unique=True, null=True, blank=True)
    author = models.ForeignKey(
        "user.User",
        on_delete=models.PROTECT,
        related_name="articles",
        limit_choices_to={"is_admin": True},
    )
    votes = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(
        "Category", on_delete=models.PROTECT, related_name="articles"
    )
    reading_time = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Article title: {self.title}, author: {self.author}, category: {self.category.name}"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        self.reading_time = (len(str(self.content)) / 200) * 100

        return super().save(*args, **kwargs)


class Tag(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True, null=True, blank=True)
    article = models.ForeignKey(
        "Article", related_name="tags", on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"<Article:  title: {self.name}, author: {self.article.title}>"
