from django.urls import path
from . import views

urlpatterns = [
    path('adauga/', views.adauga, name='adauga'),
    path('mesaje/', views.mesaje, name='mesaje'),
]