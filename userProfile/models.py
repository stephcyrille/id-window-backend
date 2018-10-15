from django.db import models
from django.contrib.auth.models import User


class UserAgent(models.Model):
    agent = models.ForeignKey(User, on_delete=True, null=True)
    reference = models.CharField(max_length=12)
    role = models.CharField(max_length=12)
    postOffice = models.CharField(max_length=150)
    language = models.CharField(max_length=12, default='fr')


    def __str__(self):
        return self.user.username

