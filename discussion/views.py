from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *

# Create your views here.
def home(request):
    return render(request, 'discussion/pages/home.html', context={
        'titulo': "repetições",
    })

#def create(request):

 #   return render(request,'discussion/pages/createDiscussion.html')

def addInDiscussion(request):
    if request.method == "POST":
        Problem.title = request.POST["titulo_post"]
        Problem.description = request.POST["corpo_post"]

    return render(request,'discussion/pages/createDiscussion.html')


#def contato(request):
#    return HttpResponse('contato')