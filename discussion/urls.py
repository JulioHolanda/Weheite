from django.urls import path

from . import views


urlpatterns = [
    path('', views.home),
    #path('<int:problem_id>/', views.discussion),
    path('createDiscussion/', views.create ),
    #path('<int:problem_id>/awnserDiscussion/', views.answer),
    path('like/<int:pk>/', views.create, name = 'like_post'),
]
