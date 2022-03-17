from django.urls import path
from . import views

'''definition de l'ensemble des liens vers les vues'''
urlpatterns = [
    path('', views.post_list, name='post_list'),
]