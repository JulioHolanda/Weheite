"""we-heite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from xml.etree.ElementInclude import include

from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from users import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', user_views.home, name='home'),
    path('signup/', user_views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name="users/login.html"), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name="users/home.html"), name='logout'),
    path('criarForum/', user_views.criarForum, name='forum'),
    path('<int:forum_id>/detailForum/', user_views.detailForum, name="detail"),
    path('<int:forum_id>/detailForum/reply_form/', user_views.replyForum.as_view(), name="reply"),
    path('<int:forum_id>/detailForum/like/', user_views.like_reply, name="like"),
    path('<int:forum_id>/detailForum/done/', user_views.done_forum, name="done"),
    path('profile/', user_views.profile, name="profile"),
    path('myDiscussions/', user_views.myDisc, name='myDiscs'),
    
]
