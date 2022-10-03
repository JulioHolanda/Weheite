from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Problem(models.Model):
   title = models.CharField(max_length=200)
   description = models.CharField(max_length=10000)
   author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
   created_at = models.DateTimeField(auto_now_add = True)

   def __str__(self):
      return self.title

class Answer(models.Model):
   owner = models.ForeignKey(Problem,blank=True,on_delete=models.CASCADE)
   description = models.CharField(max_length=10000)
   author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
   created_at = models.DateTimeField(auto_now_add = True)
   vote = models.IntegerField(null=True)