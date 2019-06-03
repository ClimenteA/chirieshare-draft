from django.urls import path
from . import views

urlpatterns = [
    path('adauga/', views.adauga, name='adauga'),
    path('sheriasi/<int:id_anunt>', views.sheriasi, name='sheriasi'),
    path('join-sheriasi/<int:id_anunt>', views.join_sheriasi, name='join_sheriasi'),
    path('chirias/', views.chirias, name='chirias'),

]