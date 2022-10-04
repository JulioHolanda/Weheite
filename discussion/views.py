from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Problem
from django.urls import reverse_lazy, reverse

# Create your views here.
def home(request):
    return render(request, 'discussion/home.html', context={
        'titulo': "repetições",
    })

#def create(request):

#   return render(request,'discussion/pages/createDiscussion.html')

def addInDiscussion(request):
    if request.method == 'POST':
        title = request.POST["titulo_post"]
        description = request.POST["corpo_post"]

    Problem = {
        "title"= title,
        "description" = description,
    } 

    return render(request,'discussion/createDiscussion.html')

def like(request, pk):
    post = get_object_or_404(Problem, id = request.POST.get('post_id'))
    post.likes.add(request.user)
    return HttpResponseRedirect(reverse(''))

def Discussion(request):
    return render





#def contato(request):
#    return HttpResponse('contato')