from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'discussion/pages/home.html', context={
        'titulo': "repetições",
    })

#def contato(request):
#    return HttpResponse('contato')