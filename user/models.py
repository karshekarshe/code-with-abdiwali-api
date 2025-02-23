from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid
from user.manager import UserManager


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name", "password"]

    objects = UserManager()

    def __str__(self):
        return f"<User first_name: {self.first_name}, lastname: {self.last_name}>"
