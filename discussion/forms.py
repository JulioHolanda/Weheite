from django.forms import ModelForm
from .models import *
 
class CreateAnswer(ModelForm):
    class Meta:
        model = Answer
        fields = "__all__"
 
class CreateDiscussion(ModelForm):
    class Meta:
        model= Problem
        fields = "__all__"