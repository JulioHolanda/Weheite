from django.urls import path

from . import views


urlpatterns = [
    path('', views.home),
    #path('<int:problem_id>/', views.discussion),
    #path('createDisccusion/', views.create ),
    #path('<int:problem_id>/awnserDiscussion/', views.answer),
]
