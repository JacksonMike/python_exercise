from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser


class UserInfo(AbstractUser):
    phone = models.CharField(max_length=32)
    gender = models.IntegerField(choices=((1, "男"), (2, "女")), default=1)