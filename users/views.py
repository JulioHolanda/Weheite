from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render

from .forms import CreateInForum, SignupForm
from .models import Forum


def home(request):
    discussao=Forum.objects.all() # Collect all records from table 
    return render(request, 'users/home.html', {'discussao': discussao})


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.profile.birth_date = form.cleaned_data.get('birth_date')
            user.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignupForm()

    context = {'form': form}
    return render(request, 'users/signup.html', context)



def criarForum(request):
    if request.method == 'POST':
        form = CreateInForum(request.POST)
        if form.is_valid():
            forum = form.save()
            forum.refresh_from_db()
            forum.autor = request.user
            forum.title = form.cleaned_data.get('title')
            forum.body = form.cleaned_data.get('body')
            forum.save()
            return redirect('forum')
    else:
        form = CreateInForum()

    context = {'form': form}
    return render(request, 'users/formulario.html', context)
