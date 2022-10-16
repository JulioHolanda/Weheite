from django.shortcuts import redirect, render
from django.http import Http404
from django.contrib import messages

from .forms import RegisterForm

def register_view(request):

    ##quantas vezes a pessoa entrou na sessao (coockie)
    '''request.session['number'] = request.session.get('number') or 0
    request.session['number'] += 1'''
    register_form_data = request.session.get('register_form_data', None)

    form = RegisterForm(register_form_data)        
    return render(request,'authors/register_view.html',{
        'form':form,
    })

def register_create(request):
    if not request.POST:
        raise Http404()

    POST = request.POST

    request.session['register_form_data'] = POST
    form = RegisterForm(POST)

    if form.is_valid():
        form.save() ##salva no banco de dados
        messages.success(request, "Usuário criado, faça o login")

        del(request.session['register_form_data'])

    return redirect('authors:register')


