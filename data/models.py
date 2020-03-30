from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()


class Data(models.Model):
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=128)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
