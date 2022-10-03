from django.shortcuts import render
from django.http import HttpResponse
from .models import Problem

# Create your views here.
def home(request):
    return render(request, 'discussion/pages/home.html', context={
        'titulo': "repetições",
    })

def create(request):
    return render(request,'discussion/pages/createDiscussion.html')





#def contato(request):
#    return HttpResponse('contato')