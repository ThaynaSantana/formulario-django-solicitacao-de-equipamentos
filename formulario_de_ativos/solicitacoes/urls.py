from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sucesso/', views.sucesso, name='sucesso'),  
]

