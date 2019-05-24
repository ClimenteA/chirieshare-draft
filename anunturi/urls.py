from django.urls import path
from . import views

urlpatterns = [
    path('adauga/', views.adauga, name='adauga'),
    path('chirias/', views.chirias, name='chirias'),
]