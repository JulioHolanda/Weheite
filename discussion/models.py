from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Discussion(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=10000)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add = True)