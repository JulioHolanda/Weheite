from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic.edit import CreateView
from django.urls import reverse

from .forms import CreateInForum, SignupForm  # , CreateInReply,
from .models import Forum, Reply


def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''

    discussao = Forum.objects.filter(title__icontains=q).order_by("-id")

    # discussao = Forum.objects.all().order_by(
    #     '-id')  # Collect all records from table


    context = {'discussao': discussao}
    return render(request, 'users/home.html', context )


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
            return redirect('home')
    else:
        form = CreateInForum()

    context = {'form': form}
    return render(request, 'users/formulario.html', context)


def detailForum(request, forum_id):
    forum = get_object_or_404(Forum, pk=forum_id)
    replys = Reply.objects.filter(forum=forum_id).order_by('-id')  # Collect all records from table

    return render(request, "users/detailForum.html", {'forum': forum, 'replys': replys})


class replyForum(CreateView):
    model = Reply
    fields = ['body']
    template_name = 'users/reply_form.html'

    def form_valid(self, form):
        form.instance.autor = self.request.user
        form.instance.forum = Forum.objects.get(pk=self.kwargs['forum_id'])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('detail', kwargs={'forum_id': self.kwargs['forum_id']})

# class replyForum(CreateView):
#     model = Reply
#     fields = ['body']

#     def form_valid(self, form):
#         form.instance.forum_id = self.kwargs.get("forum_id")
#         return super().form_valid(form)

# def replyForum(request, forum_id):
#     if request.method == 'POST':
#         form = CreateInReply(request.POST)
#         if form.is_valid():
#             reply = form.save()
#             reply.refresh_from_db()
#             reply.autor = request.user
#             reply.body = form.cleaned_data.get('body')
#             print(forum_id)
#             reply.forum = forum_id
#             reply.save()

#             forum = get_object_or_404(Forum, pk = forum_id)
#             return render(request, "users/detailForum.html", {'forum':forum})

#     else:
#         form = CreateInReply()

#     context = {'form': form}
#     return render(request, 'users/replyForum.html', context)