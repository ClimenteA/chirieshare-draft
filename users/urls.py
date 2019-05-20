from django.urls import path
from . import views


# autentificare + 

urlpatterns = [
    path('', views.autentificare, name='autentificare'),
    path('logare/', views.logare, name="logare"),
    path('inregistrare/', views.inregistrare, name="inregistrare"),
    path('delogare/', views.delogare, name="delogare"),
    path('resetare/', views.resetare, name="resetare"),
    path('utilizator/', views.utilizator, name="utilizator"),
    path('actualizare/', views.actualizare, name="actualizare")
]