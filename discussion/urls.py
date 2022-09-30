from django.urls import path

from discussion.views import home


urlpatterns = [
    path('', home),
    #path('contato/', contato),
]
